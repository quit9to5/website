from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import information
from .forms import ContactForm, SignupForm
# Create your views here.

def index(request):
	title = 'Hello '
	#if request.user.is_authenticated():
	#	title = "My title %s" %(request.user)
	form = SignupForm(request.POST or None)
	context = {
		"Title": title,
		"form": form,
	}

	if form.is_valid():
		form.save()

	return render(request,'our_form/form.html',context)

def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}
	if form.is_valid():
		form.save()
	return render(request, "our_form/form.html", context)
