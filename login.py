import requests,time
from bs4 import BeautifulSoup
def biet_login():
	with open('biet.txt', 'r') as ptr:
		info=ptr.read()
	username, password=info.split('\n')	

	try:
		r=requests.post('http://172.16.40.5:8090/httpclient.html',data={'mode':'191','username':username,'password':password,'a':'1510598306463','producttype':'1'})
		
		soup=BeautifulSoup(r.content,'lxml-xml')

		if soup.find('status').text == 'LIVE':
			print(soup.find('message').text,flush=True)
		else:
			print(soup.find('message').text,flush=True)

	except:
		print("Something might wrong! Please check your internet connection",flush=True)
	time.sleep(0.7)
	
if __name__ == '__main__':
	#Enter your registered username and password in command prompt 
	try: 
		op=open("biet.txt",'r')
		op.close()
		biet_login()
	except IOError:
		user=input("Enter your username: ").strip(' ')
		password=input("Enter your password: ")
		f=open('biet.txt','w')
		f.write(user+'\n'+password)
		f.close()
		biet_login()
