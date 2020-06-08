
import socket 
class Client:
    PORT = 4444
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = "192.168.64.1"
    # SERVER = socket.gethostname()
    ADDR = (SERVER, PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    get_msg = ""

    def __init__(self, PORT = PORT, f = FORMAT, dis = DISCONNECT_MESSAGE,sv =SERVER , ad= ADDR, cl= client):
        self.PORT = PORT
        self.FORMAT = f
        self.DISCONNECT_MESSAGE = dis
        self.SERVER = sv
        self.ADDR = ad
        self.client = cl   
        self.connect()

    def send(self,msg):
        msg = msg.encode('utf-8')
        self.client.send(msg)

    def recive(self):
        msg = self.client.recv(128).decode(self.FORMAT)
        print('da goi recive')
        return str(msg)


    def connect(self):
        self.client.connect(("192.168.64.1",4444))
        
    def close(self):
        self.client.close()
