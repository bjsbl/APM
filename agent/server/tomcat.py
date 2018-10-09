import xml.etree.ElementTree as ET
import re
from requests.auth import HTTPBasicAuth
import requests

class Tomcat(object):

	def __init__(self,host=None,port=None,user=None,password=None,ssl=False):
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
		if user is not None and password is not None:
			self.auth=HTTPBasicAuth(user,password)
		else:
			self.auth = None
		self._status = None
		self.initStats()


	def initStats(self):
		# http://39.107.38.199:8080/manager/status
		url = "%s://%s:%d/manager/status?XML=true" % (self._proto,self.host,self.port)
		res = requests.get(url,auth = self.auth)
		res.encoding = 'utf-8'
		self._status = ET.XML(res.text)


	def getMemoryStats(self):
		node = self._status.find('jvm/memory')
		memstats = {}
		if node is not None:
			for (key,val) in node.items():
				memstats[key] = val
		return memstats

	def getMemoryPoolStats(self):
		# memorypool 
		node = self._status.findall('jvm/memorypool')
		memstats = {}
		if node is not None:
			for pool in node:
				name = pool.get('name').lower()
				memstats[name] = pool.items()
		return memstats


	def getConnectorStats(self):
		node = self._status.findall('connector')
		connstats = {}
		if node:
			for _node in node:
				name = _node.get('name')
				if name is not None:
					connstats[name] = {'name':name}
					for tag in ('threadInfo', 'requestInfo'):
						cnode = _node.find(tag)
						if cnode is not None:
							connstats[name][tag] = cnode.items()
		return connstats

		


if __name__ == '__main__':
	t = Tomcat('39.107.38.199','8080','tomcat','BJwxkj^^88',None)
	print(t.getConnectorStats())
	print(t.getMemoryStats())
	print(t.getMemoryPoolStats())
