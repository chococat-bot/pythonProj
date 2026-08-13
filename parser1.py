import requests

url1 = "https://www.google.com/"
url2= "https://www.google.com/search?q=2330"
url3= "https://www.momoshop.com.tw/"
url4= "https://tw.yahoo.com/"

headers_s = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}

response = requests.get(url4,headers=headers_s) 

print(response.status_code)

print("呼叫的結果(網頁內容):", response.text)

with open("c://news/yahoo_news.html", "w", encoding="utf-8") as f:
    f.write(response.text)