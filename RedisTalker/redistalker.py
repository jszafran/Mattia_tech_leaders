"""
Basic client for Redis implementing GET & SET methods
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
    
    def _send_data_to_socket(self, msg_type, **kwargs):
        if not all(k in kwargs for k in ("lval","val")):
            kwargs["lval"], kwargs["val"] = "", ""

        msg_templates = {
            "get": f"*2\r\n$3\r\nGET\r\n${kwargs['lkey']}\r\n{kwargs['key']}\r\n",
            "set": f"*3\r\n$3\r\nSET\r\n${kwargs['lkey']}\r\n{kwargs['key']}\r\n${kwargs['lval']}\r\n{kwargs['val']}\r\n"
        }
        self.sckt.sendall(bytes(msg_templates[msg_type], encoding="ascii"))
        
    def _parse_socket_response(self, rsp):
        rsp_parsed = rsp.split(bytes('\r\n', encoding="ascii"))
        return rsp_parsed

    def set(self, key, val):
        if not self.is_connected:
            print("There's no connection established!")
            return

        self._send_data_to_socket("set", lkey=len(key),
                                         key=key,
                                         lval=len(val),
                                         val=val)
        ans = self._parse_socket_response(self.sckt.recv(1024))
        print(f"Redis response: {ans[0]}")

    def get(self, key):
        if not self.is_connected:
            print("There's no connection established!")
            return 
        
        self._send_data_to_socket("get", lkey=len(key),
                                         key=key)
        ans = self._parse_socket_response(self.sckt.recv(1024))
        print(f"Redis response: {ans[1]}")
