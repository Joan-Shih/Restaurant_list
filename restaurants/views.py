from django.shortcuts import render,render_to_response
import datetime
from django.http import HttpResponse
from restaurants.models import Restaurant,Food,Comment
from django.utils import timezone
from django.template import RequestContext
from restaurants.forms import CommentForm
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required,permission_required

@login_required
def menu(request,id):
	if id:
		r = Restaurant.objects.get(id = id)
		path = request.path
		return render_to_response('menu.html',locals())
	else:
		return HttpResponseRedirect('/restaurants_list/')

def meta(request):
	values = request.META.items()
	html = []
	for k,v in values:
		html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k,v))
	return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))


@login_required
def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	request.session['restaurant'] = restaurants
	return render(request,'restaurants_list.html',locals())

@permission_required('restaurants.see_comment')
def comment(request,id):
	if id:
		r = Restaurant.objects.get(id = id)
	else:
		return HttpResponseRedirect('/restaurants_list/')
	if request.POST:
		f = CommentForm(request.POST)

		if f.is_valid():
			visitor = f.cleaned_data['visitor']
			email  = f.cleaned_data['email']
			content = f.cleaned_data['content']
			date_time = datetime.datetime.now()
			Comment.objects.create(
					visitor = visitor,
					email = email,
					content = content,
					date_time = date_time,
					restaurant = r
				)
			f = CommentForm(initial = {'visitor':'我是丁丁'})
	else:
		f = CommentForm(initial ={'content':'好吃阿!'})
	c=locals()
	return render(request,'comments.html',c)
#	return render_to_response('comments.html',RequestContext(request,locals()))

def set_c(request):
	response = HttpResponse('設定幸運數字為八')
	response.set_cookie('lunky_number',8)
#	response.set_cookie('try',4)
	return response


def get_c(request):
	if 'lunky_number' in request.COOKIES:
		return HttpResponse('Your lunky_number is {0}'.format(request.COOKIES.get('lunky_number','error')))

	else:
		return HttpResponse('No cookie')

def use_session(request):
	request.session['lucky'] = 10
	if 'lucky' in request.session:
		lucky = request.session['lucky']
		response = HttpResponse('Your lucky is {0}'.format(lucky))
#	del request.session['lucky']
	return response
def test_session(request):
	sid = request.COOKIES['sessionid']
	s = Session.objects.get(pk = sid)
	s_infro = 'ID:' + sid + '<br>Expire date:' + str(s.expire_date)+ '<br>Data:' + str(s.get_decoded())
	return HttpResponse(s_infro)


