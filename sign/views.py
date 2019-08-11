from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event
# Create your views here.
def index(request):
	return render(request,"index.html")

#登录动作
def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		# if username == 'admin' and password == 'admin123':
		# 	return HttpResponseRedirect('/event_manage/')
		# 	#response.set_cookie('user',username,3600) #添加浏览器cookie
		# 	#request.session['user'] = username #将session记录到浏览器
		# 	return response
		# else:
		# 	return render(request,'index.html',{'error':'user or pwd error!'})
		user = auth.authenticate(username=username,password=password)
		if user is not None: #用户认证通过
			auth.login(request,user) #登录
			request.session['user'] = username #将session记录到浏览器
			response = HttpResponseRedirect('/event_manage/')
			return response
	else:
		return render(request,'index.html',{'error':'user or pwd error!'})
#发布会管理
@login_required
def event_manage(request):
	#username = request.COOKIES.get('user','')#读取浏览器cookie
	event_list = Event.objects.all()
	username = request.session.get('user','')#读取浏览器session
	#return render(request,"event_manage.html",{"user":username,"events""event_list})
	return render(request,"event_manage.html",{"user":username})