r1 ={'ip': '127.0.0.1','mac':'AAAAAABBBBBB'}
r2={'ip':'127.0.0.2','mac':'111111222222'}

arr =[r1,r2]	#load two dictionary into array

print(arr)

print(arr[0]['ip'])
print(arr[1]['ip'])


class netinfo:
  def __init__(self,ip,mac):
    self.ip = ip
    self.mac = mac

p1 = netinfo('192.168.0.1','DDDDDD444444')
p2 = netinfo('192.168.100.50','EEEEEE666666')
print(p1.ip)
print(p1.mac)
print(p2.ip,p2.mac,sep=':') #sep is a separator