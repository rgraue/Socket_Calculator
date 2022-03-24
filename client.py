import socket

MAX_SIZE = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# initialize client port on OS
s.sendto('init'.encode('ascii'), ('127.0.0.1', 3000))
print('Client running at {}\n\n'.format(s.getsockname()))

while True:
    # Input and prepare message to send
    message = input('Input message to send: ')
    
    # if message is not init case
    if (message != 'init'):
        print('preparing and sending data...\n')
        payload = message.encode('ascii')

        # sends data to server 127.0.0.1:3000
        s.sendto(payload, ('127.0.0.1', 3000))

        # Waits for response and prints to console
        data, address = s.recvfrom(MAX_SIZE)
        print(data.decode('ascii') + '\n')
    else :
        print("\nMessage cannot be 'init'\n")