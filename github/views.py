from django.shortcuts import render
import requests

def get(request):
	return render(request,'github/user.html')

def submit(request):
	print("inside function submit")
	r=requests.get("https://api.github.com/search/users",params={'q':"jainadit27"})
	data=(r.json())['items'][0]
	print(data)
	posts={}
	posts['username']=data['login']
	posts['score']=data['score']
	posts['blog_url']=data['html_url']
	context={'posts':posts}
	return render(request,'github/user_data.html',context)