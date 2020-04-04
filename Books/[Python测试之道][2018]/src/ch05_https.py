import requests
test_url = "https://www.zhihu.com"
h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
response = requests.get(test_url, headers=h)

print(response.status_code)
print('-'*40)
print(response.headers)
print('-'*40)
print(response.text)
