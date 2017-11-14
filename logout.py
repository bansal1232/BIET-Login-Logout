import requests,time
from bs4 import BeautifulSoup

def biet_logout(username,password):
	try:
		r=requests.post('http://172.16.40.5:8090/httpclient.html',data={'mode':'193','username':username,'password':password})
		
		soup=BeautifulSoup(r.content,'lxml-xml')
		print(soup.find('message').text,flush=True)

	except:
		print("Something might wrong! Please check your internet connection",flush=True)
	time.sleep(0.3)
if __name__ == '__main__':
	
	#Type registered username and password 
	username = ""
	password = ""
	biet_logout(username, password)
