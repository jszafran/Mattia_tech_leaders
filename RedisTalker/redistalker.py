"""
Basic client for Redis implementing GET & SET methods

TODO:
1. Implement Redis responses parsing.
2. Apply some refactoring:
    *implement generic method for pushing data to socket
     with dict containg type of message (get/set) and appropriate string template

"""

import socket

class RedisTalker():


    def __init__(self, host="localhost", port=6379):
        self.host = host
        self.port = port
        self.is_connected = False
        self.sckt = None


    def connect(self):
        try:
            self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sckt.connect((self.host, self.port))
            print(f"Connected to Redis on {self.host}:{self.port}")
            self.is_connected = True
        except:
            print("Connection to Redis failed.")
    
        
    def set(self, key, val):
        if not self.is_connected:
            print("There's no connection established!")
            return

        lkey, lval = len(key), len(val)
        set_template = f"*3\r\n$3\r\nSET\r\n${lkey}\r\n{key}\r\n${lval}\r\n{val}\r\n"
        self.sckt.sendall(bytes(set_template, encoding="ascii"))
        ans = self.sckt.recv(1024)
        print(f"Redis response: {ans}")


    def get(self, key):
        if not self.is_connected:
            print("There's no connection established!")
            return 
        
        lkey = len(key)
        get_template = f"*2\r\n$3\r\nGET\r\n${lkey}\r\n{key}\r\n"
        self.sckt.sendall(bytes(get_template, encoding="ascii"))
        ans = self.sckt.recv(1024)
        print(f"Redis response: {ans}")


# just to check if this is working
# on my local machine
r = RedisTalker()
r.connect()
r.set("first_name", "kuba")
r.get("first_name")