import socket

def service_client(new_socket):
    """
    给客户端返回数据
    """
    request = new_socket.recv(1024)
    print(request)

    response = 'HTTP/1.1 200 OK\r\n'
    response += "\r\n"
    response += "hahaha"
    new_socket.send(response.encode("utf-8"))
    new_socket.close()

def main():
    tcp_server_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定
    tcp_server_scoket.bind(("", 7890))

    # 变为监听套接字
    tcp_server_scoket.listen(128)

    while True:
        new_socket, client_addr = tcp_server_scoket.accept()
        service_client(new_socket)

    # 关闭套接字
    tcp_server_scoket.close()


if __name__ == "__main__":
    main()
