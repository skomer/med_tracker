from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
from models import Medication, Event


# Create your views here.


def load_home(request):
	return render(request, 'med_tracker_app/main.html')


def load_registration_page(request):
	return render(request, 'med_tracker_app/main.html', {})


def login_auth(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user is not None:
	    # the password verified for the user
	    login(request, user)
	    return render(request, 'med_tracker_app/user_dash.html', {'good_login': "Welcome back!"})
	else:
	    # the authentication system was unable to verify the username and password
		return render(request, 'med_tracker_app/main.html', {'failed_login': "The username or password was incorrect."})


def create_user(request):
	username = request.POST.get('username')
	email  = request.POST.get('email')
	password = request.POST.get('password')
	user = User.objects.create_user(username,email,password)
	user.save()
	user_login = authenticate(username=username, password=password)
	login(request, user_login)
	return render(request, 'med_tracker_app/user_dash.html', {})


@login_required#(redirect_field_name='/register/')
def add_med(request):
	generic_name = request.POST.get('generic_name')
	units = request.POST.get('units')
	user = request.user.pk
	new_med_entry = Medication()	#.objects.create(generic_name=generic_name, units, user)
	new_med_entry.generic_name = generic_name
	new_med_entry.units = units
	new_med_entry.user = request.user
	new_med_entry.save()
	# use redirect here
	return HttpResponseRedirect(reverse('med_tracker_app:user_dash'))
	# return render(request, 'med_tracker_app/user_dash.html', { 'new_med' : "You added a new medication."})


@login_required
def add_event(request):
	date = request.POST.get('date')
	time = request.POST.get('time')
	event_type = request.POST.get('event_type')
	description = request.POST.get('description')
	dosage = request.POST.get('dosage')
	medication_id = int(request.POST.get('select_med'))
	user_id = request.user.pk
	datetime = str(date) + " " + time
	print "datetime", datetime
	new_event_entry = Event()
	new_event_entry.date = datetime
	new_event_entry.event_type = event_type
	new_event_entry.description = description
	new_event_entry.dosage = dosage
	new_event_entry.medication_id = medication_id
	new_event_entry.user_id = user_id
	new_event_entry.save()
	#return render(request, 'med_tracker_app/user_dash.html', { 'new_event' : "You added a new event." })
	return HttpResponseRedirect(reverse('med_tracker_app:user_dash'))


def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('med_tracker_app:load_home'))
	#return render(request, 'med_tracker_app/main.html', {'logout': "You have successfully logged out."})


@login_required
def user_account(request):
	user_id = request.user.pk
	# can I use a request/query thing here, like in user_dash() below, rather than a for loop?
	for item in User.objects.values_list('username', 'id', 'email'):
		if item[1] == user_id:
			username = item[0]
			user_email = item[2]
	return render(request, 'med_tracker_app/account.html', { 'username' : username, 'user_email' : user_email })


@login_required#(redirect_field_name='/register/')
def user_dash(request):
	user_id = request.user.pk
	# if the med's foreign key is the same as the user_id of the user currently logged in, then get that med
	# use the following syntax for one-to-many queries, rather than using a for loop
	your_meds = request.user.medication_set.all().order_by('generic_name')
	your_events = request.user.event_set.all().order_by('date')
	time_list = ["01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00 (midday)", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00 (midnight)"]
	return render(request, 'med_tracker_app/user_dash.html', { 'your_meds' : your_meds, 'your_events' : your_events, 'range' : time_list })



