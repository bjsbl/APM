import socket
import logging

def setup_logging(level,logfile):
	log_format = "[%(asctime)s] {0}/%(levelname)s/%(name)s: %(message)s".format(host)
	logging.basicConfig(level=level, filename=logfile, format=log_format)
