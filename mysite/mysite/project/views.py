#coding=utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from project import models
# Create your views here.

@csrf_exempt
def home(request):
	titles = models.Attention.objects.all().values('title')

	if request.method == 'POST':
		#获取用户登录名密码
		username = request.POST['username']
		pw = request.POST['pw']
		#匹配数据库的用户名密码
		try:
			isTel = models.Newuser.objects.get(tel=username)
			isPassword = models.Newuser.objects.get(password=pw)
			if (isTel and isPassword):
				return render_to_response('show.html')
		except:
			return HttpResponse('<h3>sorry!用户名或密码错误</h3><a href="/home/" style="color:red">点击返回</a>')
	return render_to_response('home.html',{'titles':titles})

def produces(request):
	produces = models.Attention.objects.all()

	return render_to_response('produces_center.html',{'produces':produces})

def aboutus(request):
	return render_to_response('about_us.html')

def find(request):
	return render_to_response('about_us.html')

def chatus(request):
	return render_to_response('chat_us.html')

@csrf_exempt
def zhuce(request):
	
	if request.method == 'POST':
	 	name = request.POST['person']
	 	tel = request.POST['Tel']
	 	email = request.POST['Email']
	 	password = request.POST['Password']
	 	models.Newuser.objects.create(name=name,tel=tel,email=email,password=password)
	 	return render_to_response('show.html',{'name':name})

	users = models.Newuser.objects.all()
	return render_to_response('zhuce.html',{
		'users':users
		})
	
def show(request):
	return render_to_response('show.html')

