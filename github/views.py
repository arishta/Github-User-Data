from django.shortcuts import render
import requests

def get(request):
	return render(request,'github/user.html')

def submit(request):
	posts={}
	query=request.GET['GithubUserName']
	r=requests.get("https://api.github.com/search/users",params={'q':query})
	data=(r.json())
	try:
		data=data['items'][0]
		posts['login']=data['login']
		posts['score']=data['score']
		posts['html_url']=data['html_url']
		posts['query_data']=query
		context={'posts':posts}
		return render(request,'github/user_data.html',context)
	except:
		posts['login']="NA"
		posts['score']="NA"
		posts['html_url']="NA"
		return render(request,'github/user_data.html',{'posts':posts})
	