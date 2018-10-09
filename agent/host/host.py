import netifaces
import platform
import os
import socket
import psutil
import time
import logging
# from client import Message,Client

logger = logging.getLogger(__name__)


class Host(object):
  def __init__(self):
    # self.client = Client(host,port)
    name = socket.getfqdn(socket.gethostname())
    self.client_id = socket.gethostbyname(name)

  def get_sysinfo(self):
    uptime = int(time.time() - psutil.boot_time())
    sysinfo = {
        'uptime': uptime,
        'hostname': socket.gethostname(),
        'os': platform.platform(),
        # 'load_avg': os.getloadavg(),
        'num_cpus': psutil.cpu_count()
    }
    return sysinfo
    # self.client.send(Message('sysinfo',sysinfo,self.client_id))

  def get_memory(self):
    memory = psutil.virtual_memory()._asdict()
    return memory
    # self.client.send(Message('memory',memory,self.client_id))

  def get_swap_space(self):
    sm = psutil.swap_memory()
    swap = {
        'total': sm.total,
        'free': sm.free,
        'used': sm.used,
        'percent': sm.percent,
        'swapped_in': sm.sin,
        'swapped_out': sm.sout
    }
    return swap
    # self.client.send(Message('swap',swap,self.client_id))

  def get_disks(self, all_partitions=False):
    disks = []
    for dp in psutil.disk_partitions(all_partitions):
        usage = psutil.disk_usage(dp.mountpoint)
        disk = {
            'device': dp.device,
            'mountpoint': dp.mountpoint,
            'type': dp.fstype,
            'options': dp.opts,
            'space_total': usage.total,
            'space_used': usage.used,
            'space_used_percent': usage.percent,
            'space_free': usage.free
        }
        disks.append(disk)
    return disks
    # self.client.send(Message('disks',disks,self.client_id))


  def get_users(self):
    users = [u._asdict() for u in psutil.users()]
    return users
    # self.client.send(Message('users',users,self.client_id))

  def get_cpu(self):
    cpu_percent = psutil.cpu_times_percent(0)._asdict()
    return cpu_percent
    # self.client.send(Message('cpu_percent',cpu_percent,self.client_id))

  def get_network_interfaces(self):
    netifs = []
    net = psutil.net_io_counters(pernic=True)
    for name,c in net.items():
        netifs.append({
            'name': name,
            'bytes_sent': c.bytes_sent,
            'bytes_recv': c.bytes_recv,
            'packets_sent': c.packets_sent,
            'packets_recv': c.packets_recv,
            'errors_in': c.errin,
            'errors_out': c.errout,
            'dropped_in': c.dropin,
            'dropped_out': c.dropout
        })
    return netifs
    # self.client.send(Message('interfaces',interfaces,self.client_id))

  def get_threads(self,pid):
    threads = []
    proc = psutil.Process(pid)
    for t in proc.threads():
      thread = {
          'id': t.id,
          'cpu_time_user': t.user_time,
          'cpu_time_system': t.system_time,
      }
      threads.append(thread)
    return threads
    # self.client.send(Message('threads',threads,self.client_id))

  def get_process_open_files(self, pid):
    proc = psutil.Process(pid)
    open_files = [f._asdict() for f in proc.open_files()]
    return open_files
    # self.client.send(Message('open_files',open_files,self.client_id))

  def get_process_connections(self, pid):
    proc = psutil.Process(pid)
    connections = []
    for c in proc.connections(kind='all'):
        conn = {
            'fd': c.fd,
            'family': socket_families[c.family],
            'type': socket_types[c.type],
            'local_addr_host': c.laddr[0] if c.laddr else None,
            'local_addr_port': c.laddr[1] if c.laddr else None,
            'remote_addr_host': c.raddr[0] if c.raddr else None,
            'remote_addr_port': c.raddr[1] if c.raddr else None,
            'state': c.status
        }
        connections.append(conn)
    return connections
    # self.client.send(Message('connections',connections,self.client_id))

  def get_process_list(self):
    process_list = []
    for p in psutil.process_iter():
      mem = p.memory_info()
      proc = {
          'pid': p.pid,
          'name': p.name(),
          # 'cmdline': ' '.join(p.cmdline()),
          'status': p.status(),
          'created': p.create_time(),
          'mem_rss': mem.rss,
          'mem_vms': mem.vms,
          'mem_percent': p.memory_percent(),
          'cpu_percent': p.cpu_percent(0)
      }
      process_list.append(proc)
    return process_list
    # self.client.send(Message('process_list',process_list,self.client_id))

  def get_process(self,pid):
    process = psutil.Process(pid)
    process.threads
    mem = process.memory_info()
    process = {
      'pid': process.pid,
      'ppid': process.ppid(),
      'name': process.name(),
      'created': process.create_time(),
      # 'terminal': process.terminal(),
      'mem_rss': mem.rss,
      'mem_vms': mem.vms,
      # 'mem_shared': mem.shared,
      # 'mem_text': mem.text,
      # 'mem_lib': mem.lib,
      # 'mem_data': mem.data,
      # 'mem_dirty': mem.dirty,
      'mem_percent': process.memory_percent(),
      'cwd': process.cwd(),
      'nice': process.nice(),
      # 'io_nice_class': process.ionice()[0],
      # 'io_nice_value': process.ionice()[1],
      'cpu_percent': process.cpu_percent(0),
      'num_threads': process.num_threads(),
      'num_files': len(process.open_files()),
      'num_children': len(process.children()),
      'num_ctx_switches_invol': process.num_ctx_switches().involuntary,
      'num_ctx_switches_vol': process.num_ctx_switches().voluntary,
      # 'cpu_times_user': cpu_times.user,
      # 'cpu_times_system': cpu_times.system,
      'cpu_affinity': process.cpu_affinity()
    }
    return process
    # self.client.send(Message('process',process,self.client_id))


if __name__ == '__main__':
  t = Host()
  # while True:
  print(t.get_cpu())
  time.sleep(1)