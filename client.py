import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
client.sendall(b"Hello server!")
data = client.recv(1024)
print("Server says:", data.decode())
client.close()