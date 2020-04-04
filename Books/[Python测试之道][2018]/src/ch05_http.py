import requests
# test_url = "http://www.163.com"
# h = {"User-Agent": "Android/H60-L01/4.4.2/"}
# response = requests.get(test_url, headers=h)

# test_url = "https://mail.163.com/js6/main.jsp"
# p = {"sid": "sBLwabSkKYKYITUiBckkNUFCgRlAYAtR",
#      "df": "mail163_letter#module=welcome.WelcomeModule%7C%7B%7D"}
# c = "JSESSIONID=ACB09DC3461B791B76ACBC5038CF0B30"
# response = requests.get(test_url, headers={"cookies":c}, params=p)

# 搜歌
test_url = "https://music.163.com/weapi/search/suggest/web?csrf_token="
form = {"params": "O3WQvvRDz7K6uOUnQfxTG0x/turzk7pPMvIXl8teTsLxo4l61u4qx9uQ1NJSsqUMzkYLyKGF1Bo+CRttRxPsIhyS3+KT+5kocvNPT593ZOYlFGxpuvPVNbImMb01e0uR",
        "encSecKey": "47145f3182d7c6b46330db6a573ca9d8a61283376e42fc0e004f729111ddfef3ebd25858de158f205173c560d448d9ab33dd94543159ba63c3ea5e49ae52b340fbfe8cad4348c2f126505e80d54e0e858d61cb8f2a7c93a1697164022267401618d07b5bf0979793913d90061a9379a2c505396d045ebc03ef5f4106cc043109"}
response = requests.post(test_url, data=form)

print(response.status_code)
print('-'*40)
print(response.headers)
print('-'*40)
print(response.text)
