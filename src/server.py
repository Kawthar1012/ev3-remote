"""
server.py

the server class

to be run on a computer, lauches the ip camera

usage: pass an object in front of the cam, wait at least 3 seconds 
and press space, then put the object in the sorter.

"""
import socket


class Server(object):
    def __init__(self, cam_url, port=12345):
        self.socket = socket.socket()
        self.port = port
        self.hostname = socket.gethostname() 
        self.ipv4 = socket.gethostbyname(self.hostname) 

        print('[LOG] socket created')
        print('[LOG] hostname : {}'.format(self.hostname))
        print('[LOG] addr : {}:{}'.format(self.ipv4, self.port))

    def start(self):
        self.socket.bind(('', self.port))

        self.socket.listen(5)
        print('[LOG] listening')
        c, addr = self.socket.accept()
        print('[CLIENT] connection from', addr)
        return c


    def send_msg(self,msg,client):
        client.send(msg.encode())


