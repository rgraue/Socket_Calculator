import socket
from calculator import Calculator

MAX_SIZE = 65535

# Parses through payload and prepares equation for calculation
def parsePayload (payload):
    eq = payload.split()
    if (len(eq) == 1):
        if (eq[0] == '-help'):
            return helpHandler()
        else :
            return handleError('Unkown argument. try "-help" for help')
    if (len(eq) != 3):
        return handleError('Only accepts 3 arguments')
    else:
        try:
            # convert arguments to numbers
            lhs = float(eq[0])
            rhs = float(eq[2])
            # create and perform calculation
            calc = Calculator(eq[1], lhs, rhs)
            return str(calc.perform())
        except:
            return handleError('Variables must be numbers')

# General Error handeler
def handleError(error):
    return 'Error Thrown: {}'.format(error)

def helpHandler():
    return (
        "Welcome to Ryan's simple calculator\n\n" + 
        "This calculator accepts 2 argument simple equations\n" + 
        "Equations are input as following\n" +
        "x <operator> y\n\n" + 
        "Supports:\n"+
        "Addition (+)\n" +
        "Subtraction (-)\n"+
        "Multiplication (*, X)\n"+
        "Division (/)\n"+
        "Exponentials (^)\n" + 
        "Modulo (%)\n"+
        "Scientific Notaion (e, E)\n\n"
    )

def main ():
    # socket listening config
    port = 3000
    hostname = '127.0.0.1'

    # Create and bind socket to listening config
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((hostname, port))

    print('Listening at {}'.format(s.getsockname()))

    # socket functionality
    while True:
        data, clientIP = s.recvfrom(MAX_SIZE)
        message = data.decode('ascii')
        # if initial connection
        # OS establishes port for client on first send
        if (message == 'init'):
            print('Connection established with {}'.format(clientIP))
        else :
            payload = parsePayload(message)
            s.sendto(payload.encode('ascii'), clientIP)

if __name__ == '__main__':
    main()