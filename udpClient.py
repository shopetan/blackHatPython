import socket

target_host = "127.0.0.1"
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto("AABBCC",(target_host,target_port))

# reveave data
data, addr = client.recvfrom(4096)

print data
