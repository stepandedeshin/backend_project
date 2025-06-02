import asyncio
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from config import cnf


async def get_regions() -> list[int] | None:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver_path = 'core/driver/chromedriver-win64/chromedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url = cnf.app.REGIONS_URL

    try:
        driver.get(url=url)

        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.TableBlock__table-m5Tic')))

        page_html = driver.page_source

        soup = BeautifulSoup(page_html, 'html.parser')
        tables = soup.find_all('table', class_='TableBlock__table-m5Tic')

        if not tables:
            print("Таблицы не найдены.")
            return None

        for table in tables:
            text = table.get_text(strip=True).replace('\n', '')
            numbers = re.findall(r'\d+', text)
            print(numbers)
            return numbers
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return None
    finally:
        driver.quit()

asyncio.run(get_regions())
