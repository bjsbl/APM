import threading
from gevent.pool import Group
import time
import logging
import sys
import socket
import Server as rpc
from Server import Message
from Worker import Worker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SLAVE_REPORT_INTERVAL = 3.0

class Runner(object):
  def __init__(self,host,port):
    self.host = host
    self.port = port
    self.state = 'ready'

  def stop(self):
      self.greenlet.kill()

class MasterRunner(Runner):
  def __init__(self,host,port):
    super().__init__(host,port)
    self.server = rpc.Server(self.host, self.port)
    self.slave = {}
    self.greenlet = Group()
    self.greenlet.spawn(self.slave_listener)
    # self.slave_listener()

  def slave_listener(self):
    while True:
      msg = self.server.recv()
      if msg.type == 'slave_ready':
        id = msg.node_id
        self.slave[id] = id
        logger.info("Client %r reported as ready. Currently %i slaves ready to emit." % (id, len(self.slave)))
        self.server.send(Message('slave_stop',None,None))
      elif msg.type == 'slave_stats':
        logger.info(msg.data)
      elif msg.type == 'slave_complete':
        logger.info("=====================================")
        self.server.send(Message('slave_stop',None,None))
      elif msg.type == 'slave_start':
        pass
      elif msg.type == 'slave_stop':
        del self.slave[msg.node_id]
        logger.info("Removing %s from running slaves" % (msg.node_id))
        if len(self.slave)==0:
          self.state = 'stopped'


class SlaveRunner(Runner):

  def __init__(self,host,port):
    super().__init__(host,port)
    self.slave_id = socket.gethostname()
    self.client = rpc.Client(self.host, self.port)
    self.greenlet = Group()
    self.greenlet.spawn(self.work)
    self.client.send(rpc.Message('slave_ready',None,self.slave_id))

  def stats_reporter(self):
    while True:
        logger.info("starting....."+str(time.time()))
        # work = Worker(self.client,self.greenlet)
        time.sleep(SLAVE_REPORT_INTERVAL)
        self.client.send(Message('slave_complete',None,socket.gethostname()))

  def work(self):
    while True:
        print(">>>>>>>>>><<<<<<<<")
        msg = self.client.recv()
        logger.info(msg.type)
        if msg.type == 'slave_start':
          pass
        elif msg.type == 'slave_stop':
          # self.stop()
          self.client.send(Message("slave_stop", None, self.slave_id))
          self.client.send(Message("slave_ready", None, self.slave_id))
        elif msg.type == 'slave_quit':
          logger.info("Got quit message from master, shutting down...")
          self.stop()
          self.greenlet.kill()

       

            



