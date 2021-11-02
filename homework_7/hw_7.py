import socket
import threading
from time import sleep


def server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        conn, addr = sock.accept()

        with conn:
            print('Server start. Connected by', addr)

            while True:
                data = conn.recv(1024).decode()

                if not data:
                    conn.send(f'Client sent no more data.'.encode())
                    break
                elif data in ('stop', 'break', 'end', 'exit', '.'):
                    conn.send(f'Client sent {data} to break connection.'.encode())
                    break
                
                print(f'Received from client: {data}')    
                conn.sendall(input('Enter your message: ').encode())


def client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sleep(1)
        print('Client start')

        while True:
            sock.sendall(input('Enter your message: ').encode())
            data = sock.recv(1024).decode()

            if data in ('stop', 'break', 'end', 'exit' '.'):
                break

            print(f'Received from server: {data}')


if __name__ == '__main__':
    host = 'localhost'
    port = 8080

    server = threading.Thread(target=server, args=(host, port))
    client = threading.Thread(target=client, args=(host, port))

    server.start()
    client.start()

    server.join()
    client.join()
    print('Exit chat!')
