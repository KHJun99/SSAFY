import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'Player1'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

# --- 샷 계산 유틸 ---
BALL_DIAMETER = 2.3
BLOCK_TOL = BALL_DIAMETER
CONTACT_OFFSET = BALL_DIAMETER

def distance(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def line_point_distance(px, py, ax, ay, bx, by):
    apx, apy = px - ax, py - ay
    abx, aby = bx - ax, by - ay
    ab2 = abx*abx + aby*aby
    if ab2 == 0:
        return math.hypot(apx, apy)
    t = (apx*abx + apy*aby) / ab2
    t = clamp(t, 0.0, 1.0)
    cx, cy = ax + t*abx, ay + t*aby
    return math.hypot(px - cx, py - cy)

def is_line_clear(ax, ay, bx, by, balls, ignore_indices):
    for i, (x, y) in enumerate(balls):
        if i in ignore_indices:
            continue
        if x < 0 or y < 0:
            continue
        if line_point_distance(x, y, ax, ay, bx, by) < BLOCK_TOL:
            return False
    return True

def aim_contact_point(tx, ty, hx, hy):
    vx, vy = hx - tx, hy - ty
    d = math.hypot(vx, vy) or 1.0
    cx = tx - (vx/d) * CONTACT_OFFSET
    cy = ty - (vy/d) * CONTACT_OFFSET
    cx = clamp(cx, 0.0, TABLE_WIDTH)
    cy = clamp(cy, 0.0, TABLE_HEIGHT)
    return cx, cy

def calc_angle_and_power(wx, wy, cx, cy, tx, ty, hx, hy):
    # 각도 규격: 위=0°, 시계방향 증가 → atan2(ax, ay)
    ax, ay = (cx - wx), (cy - wy)
    angle = math.degrees(math.atan2(ax, ay))
    if angle < 0:
        angle += 360.0

    d_wc = distance(wx, wy, cx, cy)
    d_th = distance(tx, ty, hx, hy)
    raw = d_wc * 0.9 + d_th * 0.6
    power = max(10.0, min(raw, 100.0))
    return angle, power

def choose_targets_player1(balls):
    # 선공: 1, 3, 5
    cand = [1, 3, 5]
    return [i for i in cand if balls[i][0] >= 0 and balls[i][1] >= 0]

def pick_best_shot_player1(balls):
    wx, wy = balls[0]
    if wx < 0 or wy < 0:
        return 0.0, 0.0

    targets = choose_targets_player1(balls)
    if not targets:
        return 0.0, 0.0

    best = None
    best_score = float('inf')

    for t in targets:
        tx, ty = balls[t]
        for hx, hy in HOLES:
            cx, cy = aim_contact_point(tx, ty, hx, hy)

            clear_wc = is_line_clear(wx, wy, cx, cy, balls, ignore_indices={0, t})
            clear_th = is_line_clear(tx, ty, hx, hy, balls, ignore_indices={0, t})
            if not (clear_wc and clear_th):
                continue

            d_wc = distance(wx, wy, cx, cy)
            d_th = distance(tx, ty, hx, hy)

            v1x, v1y = cx - wx, cy - wy
            v2x, v2y = hx - tx, hy - ty
            n1 = math.hypot(v1x, v1y) or 1.0
            n2 = math.hypot(v2x, v2y) or 1.0
            cos_sim = (v1x*v2x + v1y*v2y) / (n1*n2)
            angle_penalty = (1.0 - cos_sim) * 20.0

            score = d_wc + d_th + angle_penalty
            if score < best_score:
                best_score = score
                best = calc_angle_and_power(wx, wy, cx, cy, tx, ty, hx, hy)

    if best is None:
        # 세이프티 대용: 가장 가까운 목적구로 살짝
        t = min(targets, key=lambda k: distance(wx, wy, balls[k][0], balls[k][1]))
        tx, ty = balls[t]
        ax, ay = tx - wx, ty - wy
        angle = math.degrees(math.atan2(ax, ay))
        if angle < 0:
            angle += 360.0
        power = min(distance(wx, wy, tx, ty) * 0.7, 40.0)
        return angle, power

    return best
# --- 유틸 끝 ---

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 여기서부터 코드를 작성하세요.
    angle, power = pick_best_shot_player1(balls)
    if not (0.0 <= power <= 100.0): power = 0.0
    if not (0.0 <= angle < 360.0): angle = 0.0
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
