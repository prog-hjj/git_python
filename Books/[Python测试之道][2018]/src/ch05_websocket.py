import websocket
url = "ws://www.xxxx.com/xxxx"
# 连接聊天室
ws = websocket.create_connection(url)
# 登录
ws.send('{"request":1111,"service":1001,"name":"xxxx"}')
new_msg = ws.recv()
print(new_msg)
print('-'*40)
# 发送聊天内容
ws.send('{"request":1111,"service":1003,"name":"x","message":"1111111"}')
new_msg1 = ws.recv()
print(new_msg1)
