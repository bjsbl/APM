import socket
import threading
import requests
import json
import time
from Server import Message

class Worker(object):

  def __init__(self,client,greenlet):
    file = './api.json'
    self.client = client
    self.greenlet = greenlet
    self.load_api_json_file(file)

  def request_run(self,name,method,url,**args):
    request_meta = {}
    request_meta['method'] = method
    request_meta["start_time"] = time.time()
    response = requests.request(method,url,**args)
    request_meta["response_time"] = (time.time() - request_meta["start_time"]) * 1000
    request_meta["name"] = name or response.request.path_url
    if args.get("stream", False):
      request_meta["content_size"] = int(response.headers.get("content-length") or 0)
    else:
      request_meta["content_size"] = len(response.content or "")
    request_meta['status_code'] = response.status_code
    self.client.send(Message('slave_stats',request_meta,socket.gethostname()))

  def load_api_json_file(self,file):
    with open(file, 'r',encoding='utf8') as json_file:
      json_api = json.loads(json_file.read())
      name = json_api['name']
      create_time = json_api['create_time']
      total = json_api['total']
      api_list = json_api['api_list']
      frequency = json_api['frequency']
      self.normal_run(name,api_list,frequency)
     
  def run(self,name,api_list):
    for url in api_list:
      sleep_time = url['sleep']
      for x in range(url['frequency']):
        _url = url['url']
        _name = url['name']
        _method = url['method']
        _data = url['data']
        _header = url['headers']
        self.request_run(_name,_method,_url,data=json.dumps(_data),headers = _header[0])
        time.sleep(sleep_time)

  def normal_run(self,name,api_list,frequency):
    for x in range(frequency):
      self.run(name, api_list)

  def gevent_run(self,name,api_list,frequency):
    for x in range(frequency):
      self.greenlet.spawn(self.run,name,api_list)
    


  def thread_run(self,name,api_list,frequency):
    thread_list = []
    for x in range(frequency):
      t = threading.Thread(target=self.run,args=(name,api_list))
      t.setDaemon(True)
      t.start()
      thread_list.append(t)
    for x in thread_list:
      x.join()
    self.client.send(Message('slave_complete',None,socket.gethostname()))