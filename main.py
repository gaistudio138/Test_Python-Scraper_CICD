import requests
from bs4 import BeautifulSoup
import urllib3

# 關閉因安全性降低而產生的警告訊息
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def run_scraper():
    url = "https://example.com"
    try:
        # 加入 verify=False 略過憑證檢查
        response = requests.get(url, verify=False)
        # response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').text
        print(f"成功抓取網頁標題123: {title}")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    run_scraper()