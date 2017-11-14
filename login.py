import requests,time
from bs4 import BeautifulSoup
def biet_login(username,password):
	try:
		r=requests.post('http://172.16.40.5:8090/httpclient.html',data={'mode':'191','username':username,'password':password,'a':'1510598306463','producttype':'1'})
		
		soup=BeautifulSoup(r.content,'lxml-xml')

		if soup.find('status').text == 'LIVE':
			print(soup.find('message').text,flush=True)
		else:
			print(soup.find('message').text,flush=True)


	except:
		print("Something might wrong! Please check your internet connection",flush=True)
	time.sleep(0.3)
	
if __name__ == '__main__':
	#Write down the registered username and password 
	username = ""
	password = ""
	biet_login(username, password)