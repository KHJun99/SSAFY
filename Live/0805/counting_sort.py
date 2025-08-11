def counting_sort(DATA, TEMP, k):
    COUNTS = [0] * (k + 1)

    for i in range(len(DATA)):
        COUNTS[DATA[i]] += 1
    
    for i in range(1, len(COUNTS)):
        COUNTS[i] += COUNTS[i-1]

    for i in range(len(DATA) -1 , -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]
    
    return TEMP

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
k = 4
TEMP = [ 0 for i in range(len(DATA))]

print(counting_sort(DATA, TEMP, k))