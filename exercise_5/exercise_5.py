import socket
import queue
import threading
import time
import sys


class Server(object):
    def __init__(self, address, port=1111):
        self.__address = address
        self.__buffer_size = 1024
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # self.server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        # 检测对方是否崩溃
        self.server.setblocking(0)  # 端口释放 端口复用
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.__address, port))
        self.server.listen(5)
        print('waiting...')

        # id : socket
        self.sockets_dict = {}
        # socket : id
        self.id_dict = {}
        # aim_id : message_queue
        self.message_queues = {}

    def get_ids_msg(self, data, split_string):
        print(data)
        string = data.split(split_string)
        print(string)
        src_id = string[0]
        aim_id = string[1]
        msg = string[2]
        return src_id, aim_id, msg

    def link(self, sock, addr):
        while True:
            try:
                sock_id = sock.recv(self.__buffer_size).decode()
            except:
                continue
            else:
                print(sock_id)
                break
        self.sockets_dict[sock_id] = sock
        self.id_dict[sock] = sock_id

        while True:
            time.sleep(0.1)

            try:
                data = sock.recv(self.__buffer_size).decode()
                print("Received:", data)
            except:
                continue
            else:
                print(data)
                src_id, aim_id, msg = self.get_ids_msg(data, "&")

                if not self.sockets_dict[aim_id]:
                    # 如果目的客户端没有连接
                    print("No %s Server" % aim_id)
                    continue
                else:
                    aim_sock = self.sockets_dict[aim_id]
                    aim_sock.send(str(msg).encode())

    def test_run(self):
        print("Listening")
        while True:
            try:
                conn, address = self.server.accept()
            except:
                continue
            th = threading.Thread(target=self.link, args=(conn, address))
            th.start()
            

class Client(object):

    def __init__(self, identity, address, port):
        self.buffer_size = 1024
        self.identity = identity
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client_socket.settimeout(2)

        # connect
        try:
            self.client_socket.connect((address, port))
            # 连接后必须发送该客户端的id建立索引
        except Exception as e:
            print("Unable to connect because %s" % e)
            sys.exit()
        else:
            self.client_socket.send(str(self.identity).encode())
            print(self.identity, "connected to server...")

    def send(self, des_id, msg):
        try:
            msg = self.identity + "&" + des_id + "&" + msg
            self.client_socket.send(str(msg).encode())
        except Exception as e:
            print("A can not send，cuz %s" % e)
            sys.exit()

    def receive(self):
        while True:
            time.sleep(0.1)
            try:
                data = self.client_socket.recv(self.buffer_size).decode()
            except:
                pass
            else:
                print(data)

    def test_run(self, aim_id, msg):
        print("Start")
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        send_thread = threading.Thread(target=self.send, args=(aim_id, msg))
        send_thread.start()
        send_thread.join()
        
        
if __name__ == '__main__':
    address = '127.0.0.1'
    port = 1111
    ser = Server(address, port)
    ser.test_run()
    
    
def exercise_5(inputs): # DO NOT CHANGE THIS LINE
    """
    This functions receives the input in the parameter 'inputs'. 
    Change the code, so that the output is sqaure of the given input.

    Output should be the name of the class.
    """
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
