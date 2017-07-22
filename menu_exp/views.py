from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.contrib import auth
#from menu_exp.forms import LoginForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission,Group,User

from django.views.generic.base import View,TemplateView

def welcome(request):
	if ('user_name' in request.GET) and (request.GET.get('user_name','') != ''):
		return HttpResponse('Welcome!~'+request.GET.get('user_name'))
	else:
		return render_to_response('welcome.html',locals())
'''
def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')

		user = auth.authenticate(username = username ,password =password)
		if (user is not None) and (user.is_active):
			auth.login(request,user)
			return HttpResponseRedirect('/index/')
		else:
			f = LoginForm()
			c = locals()
			return render(request,'login.html',c)
	else:
			f = LoginForm()
			c = locals()
			return render(request,'login.html',c)
'''
def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/accounts/login/')
		else:
			form = UserCreationForm()
			return render(request,'register.html',locals())
	else:
		form = UserCreationForm()
		return render(request,'register.html',locals())
'''
class  Index(TemplateView):
	template_name =  'index.html'
	def get(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)
		context['request'] = request
		context['really'] = '真的假的'
		return self.render_to_response(context)
'''


'''

def index(request):
	if request.user.is_authenticated():
		g = Group.objects.get(name = 'see_comment_group')
	#	perm2 = Permission.objects.get(codename = 'add_comment')
		request.user.groups.add(g)
	return render(request,'index.html',locals())
'''
'''
def register(request):
	if (request.method == "POST") and (request.POST.get('username','') != '') and (request.POST.get('password','') != ''):
		un = request.POST['username']
		pw = request.POST['password']
		new_user = User.objects.create(username = un, password = pw)
		new_user.set_password(pw)
		new_user.save()
		return HttpResponseRedirect('/accounts/login/')
	else:
		f = RegisterForm(request.POST)
		return render(request,'register.html',locals())

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')
'''
