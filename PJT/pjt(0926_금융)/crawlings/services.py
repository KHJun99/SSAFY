# crawlings/services.py
import time
from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service          # ✅ 추가
from webdriver_manager.chrome import ChromeDriverManager

def _get_driver(headless: bool = True):
    opts = Options()
    if headless:
        # Chrome 109+ 권장. 구버전이면 "--headless"로 바꾸세요.
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    return driver

def fetch_toss_comments(company_name: str, limit: int = 20, max_scroll: int = 10) -> Tuple[str, List[str]]:
    driver = _get_driver(headless=True)
    try:
        driver.get("https://www.tossinvest.com/")
        time.sleep(0.8)

        driver.find_element(By.TAG_NAME, "body").send_keys("/")
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='검색어를 입력해주세요']"))
        )
        search_input.send_keys(company_name)
        search_input.send_keys(Keys.ENTER)

        WebDriverWait(driver, 15).until(EC.url_contains("/order"))
        cur = driver.current_url
        parts = cur.split("/")
        code = parts[parts.index("stocks") + 1]

        community_url = f"https://www.tossinvest.com/stocks/{code}/community"
        driver.get(community_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main article"))
        )

        comments, last_h = [], driver.execute_script("return document.body.scrollHeight")
        for _ in range(max_scroll):
            spans = driver.find_elements(By.CSS_SELECTOR, "article.comment span.tw-1r5dc8g0._60z0ev1")
            for sp in spans:
                t = sp.text.strip()
                if t and t not in comments:
                    comments.append(t)
                    if len(comments) >= limit:
                        return code, comments[:limit]
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            h = driver.execute_script("return document.body.scrollHeight")
            if h == last_h:
                break
            last_h = h
        return code, comments[:limit]
    finally:
        driver.quit()
