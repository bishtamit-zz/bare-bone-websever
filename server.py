import builtins
import socket
import sys


class Mylist(builtins.list):
    def get(self, idx):
        try:
            return self[idx]
        except IndexError:
            return None


builtins.list = Mylist

HOST, PORT = '', list(sys.argv).get(1) or 8001
PORT = int(PORT)
HTTP_RESPONSE = """HTTP/1.1 200 OK

Hello World!
"""
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(listen_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1))
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print(f'Serving on port {PORT}')

try:
    while True:
        print(f"{'=' * 50}")
        client_connection, client_address = listen_socket.accept()
        print(f"client: {client_address}")
        request_data = client_connection.recv(1024)
        print(f'Raw:   {request_data}')
        print(request_data.decode('utf-8'))

        http_response = HTTP_RESPONSE.encode('ascii')
        client_connection.sendall(http_response)
        client_connection.close()
        print(f"{'=-' * 50}")

        print(f'{http_response}')
except (KeyboardInterrupt, SystemExit):
    listen_socket.close()
except:
    listen_socket.close()
    client_connection.close()
