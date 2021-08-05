
#list can be modified
ips = ['172.217.7.132','74.6.143.25','136.142.34.104' ]
ips.append('136.142.156.16')
ips.remove('74.6.143.25')
for x in ips:
	print(x)

#tuples can't be changed	
ips_t = ('172.217.7.132','74.6.143.25','136.142.34.104')

#dictionary creation
ports = {'http':'80','https':'443','ssh':'22','telnet':'23','ftp':'21'}
print(ports['ssh'])