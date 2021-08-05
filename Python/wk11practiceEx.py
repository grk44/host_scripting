d1 = {'sourceip':'127.1.0.1','sourceport':'8820', 'destip':'192.111.232.1', 'destport':'8122'}
d2 = {'sourceip':'127.3.0.1','sourceport':'8233', 'destip':'192.15.235.2', 'destport':'3322'}
d3 = {'sourceip':'127.4.0.1','sourceport':'8130', 'destip':'123.111.55.66', 'destport':'4521'}

print(d2['sourceport'],d2['destport'])

arr = [d1,d2,d3]
print(arr[1]['sourceip'],arr[1]['destip'])

class wk11ex:
	def __init__(self, sourceip, sourceport, destip, destport):
		self.sourceip = sourceip
		self.sourceport = sourceport
		self.destip = destip
		self.destport = destport

c1 = wk11ex('127.1.0.1','8820','192.111.232.1','8122')
c2 = wk11ex('127.3.0.1','8233','192.15.235.2','3322')
c3 = wk11ex('127.4.0.1','8130','123.111.55.66','4521')

print("class called")
print(c2.sourceport,c2.destport)

