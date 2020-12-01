#Simple script to port scan a host
from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
	target = input('Please enter the host IP to scan: ')
	t_IP = gethostbyname(target)
	print ('Starting scan on host: ' , t_IP)

	for i in range(50, 500):
		s = socket(AF_INET, SOCK_STREAM)

		conn = s.connect_ex((t_IP, i))
		if(conn == 0) :
			print ('Port %d: OPEN' % (i,))
		s.close()
		
print('Time taken: ', time.time() - startTime)
