import datetime
import time
import random
import string

class Provider(object):

  def random_string(self,length):
    _str = [random.choice(string.digits+string.ascii_letters) for i in range(length)]
    ran_str = ''.join(_str)
    return ran_str

  def random_num(self,length):
    _str = [random.choice(string.digits) for i in range(length)]
    ran_str = ''.join(_str)
    return ran_str

  def random_date(self):
    return datetime.datetime.now()
  
  def random_time(self):
    return time.time()

  def random_sign(self,length):
    salt = '!@#$%^&*()><?'
    _str = [random.choice(salt) for i in range(length)]
    ran_str = ''.join(_str)
    return ran_str


if __name__ == '__main__':
  t = Provider()
  print(t.random_string(13))
  print(t.random_num(13))
  print(t.random_time())
  print(t.random_sign(20))
  print(t.random_date())
