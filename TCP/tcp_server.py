import socket

def main():
    #  创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定信息
    tcp_server_socket.bind(("", 7890))

    # 使用socket创建的套接字默认的属性是主动的， 使用listen将其变为被动的， 这样就可以接收别人的链接了
    tcp_server_socket.listen(128)

    while True:   #  等待多个客户端
        new_client_socket, client_addr = tcp_server_socket.accept()

        while True:   # 为同一个客户端，服务。
            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode("utf-8"))

            # 当客户端调用close()， recv_data = None
            if recv_data:
                new_client_socket.send("hello world".encode('utf-8'))
            else:
                break
        # 关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
    