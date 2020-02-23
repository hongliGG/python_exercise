import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)

    new_tcp_socket, client_addr = tcp_server_socket.accept()
    
    file_name = new_tcp_socket.recv(1024).decode("utf-8")

    # 返回一部分数据给客户端
    new_tcp_socket.send("hahahha".encode('utf-8'))


if __name__ == "__main__":
    main()