#! /usr/bin/python3

from socket import *
from termcolor import *
import optparse
from  threading import *

#thost--> host ip
#tports-->portnumbers
def getbanner(thost,tport):
	try:
		sock = socket()
		sock.connect((thost,tport))
		banner=sock.recv(10000)
		sock.close()
		return banner
	except:
		sock.close()
		return

def connscan(thost,tport):
	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.connect((thost,tport))
		banner=getbanner(thost,tport)
		#print(banner)
		if banner :
			print(colored(f"[+] {tport} is open   :{banner}",'green'))
		else:
			print(colored(f"[+] {tport} is open   :Unknown ",'green'))
	except:
		 print(colored(f"[-] {tport} is closed ",'red'))
	finally:
		sock.close()


def portscan(thost,tports,prange):
	try:
		#get_hostip_name
		tip=gethostbyname(thost)
		
	except:
		print(colored(f"[!] Unable to resolve name : {thost}",red))
		#print("Trying with another settings ......")

	try:
		#passing ip 
		tname=gethostbyaddr()
		print('[+] Scan Result For '+ tname[0])
		
	except:
		print('[+] Scan Result For '+ tip)
		
	#setdefaulttime(1)

	if prange:
		l=int(prange[0])
		u=int(prange[1])
		for tport in range(l,u):
			t=Thread(target=connscan,args=(thost,int(tport)))
			t.start()
    	

	else:
		for tport in tports:
			t=Thread(target=connscan,args=(thost,int(tport)))
			t.start()

	

def main():
	prange=[]
	parser =optparse.OptionParser('Usage:'+'pmap.py -H <Target host ip/hostname>  -p/--pr <target ports>')
	parser.add_option('-H',dest='thost',type='string',help='specify  target host ')
	parser.add_option('-p',dest='tports',type='string',help='specify  target ports seprated by comma')
	parser.add_option('--pr',dest='prange',type='string',help='specify  target ports range seprated by "-"')
	(options,args)=parser.parse_args()
	thost=options.thost
	tports=str(options.tports).split(",")
	if options.prange:
		try:
			prange=str(options.prange).split("-")
			if not  prange[1]:
				print(parser.usage)
				exit(0)

		except:
			print(parser.usage)
			exit(0)


		if (thost==None)|((prange[0]==None)&(prange[1]==None)):
			print(parser.usage)
			exit(0)
		else:
			portscan(thost,tports,prange)

	if (thost==None)|(tports[0]==None):
		print(parser.usage)
		exit(0)
	else:
		portscan(thost,tports,prange)		
		

if __name__=='__main__':
	main()