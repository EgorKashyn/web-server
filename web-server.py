import socket
sock = socket.socket()
sock.bind(('', 8080))
sock.listen(5)
page = open(f'index.html', mode='r', encoding='utf-8').read()
k=0
while True:
    k+=1
    resp = f"""HTTP/1.1 200 OK

    {page}\n
    Member {k}"""
    conn,addr=sock.accept()
    conn.send(resp.encode())
conn.close()
