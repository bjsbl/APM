import socket
import zmq.green as zmq
import msgpack

class Message(object):
    def __init__(self, message_type, data, node_id):
        self.type = message_type
        self.data = data
        self.node_id = node_id

    def serialize(self):
        return msgpack.dumps((self.type, self.data, self.node_id))

class BaseSocket(object):

    def send(self, msg):
        self.sender.send(msg.serialize())


class Client(BaseSocket):
    def __init__(self, host, port):
        context = zmq.Context()
        self.sender = context.socket(zmq.PUSH)
        self.sender.connect("tcp://%s:%i" % (host, port))