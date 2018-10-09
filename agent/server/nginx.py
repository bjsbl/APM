import re
from requests.auth import HTTPBasicAuth
import requests

class Nginx(object):

	def __init__(self,host=None,port=None,user=None,password=None,status_path=None,ssl=False):
		if host is None:
			self.host = '127.0.0.1'
		else:
			self.host = host
		if port is None:
			self.port = 80
		else:
			self.port = int(port)
		if ssl:
			self._proto = 'https'
			if port is not None:
				self.port = 443
		else:
			self._proto = 'http'
		if status_path is None:
			self.status_path = 'nginx_status'
		else:
			self.status_path = status_path
		if user is not None and password is not None:
			self.auth=HTTPBasicAuth(user,password)
		else:
			self.auth = None
		self._status = {}
		self.initStats()


	def initStats(self):
		# http://39.107.38.199/status
		url = "%s://%s:%d/%s" % (self._proto,self.host,self.port,self.status_path)
		res = requests.get(url,self.auth)
		res.encoding = 'utf-8'
		res = res.text
		for line in res.splitlines():
			for (key,val) in re.findall('(\w+):\s*(\d+)', line):
				self._status[key.lower()] = val

	def getStats(self):
		return self._status




if __name__ == '__main__':
	t = Nginx('39.107.38.199',None,None,None,'status',None)
	print(t.getStats())