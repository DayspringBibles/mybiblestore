# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import insides
from .models import leather

# Create your views here.
def index(request):

	#return HttpResponse('home')
	inside_options = insides.objects.all()
	return render(request, 'home/home.html',{	
		'inside_options' : inside_options,
		'page_title' : 'Home | My Bible',
		'page_heading' : 'Home'
		})


def store(request):
	#return HttpResponse('store')
	if request.method == 'POST':
	        item_name = request.POST.get('item_name')

	        return redirect('store_item',item_name = item_name.strip())

	inside_options = insides.objects.all()
	
	return render(request, 'home/store.html',{	
		'inside_options' : inside_options,
		'page_title' : 'Store | My Bible',
		'page_heading' : 'Store'
		})

def store_item(request,item_name):
	item = insides.objects.filter(name=item_name)[0]
	cover = leather.objects.all()
	return render(request, 'home/item.html',{	
		'item' : item,
		'page_title' : item.name + " | My Bible",
		'page_description' : item.short_description,
		'leather' : cover,
		'page_heading' : item.name
		})

	return HttpResponse(item_name)


def about(request):
	#return HttpResponse('about')
	return render(request, 'home/about.html',{
		'page_title' : 'About | My Bible',
		'page_heading' : 'About'
		})

def contact(request):
	#return HttpResponse('contact')
	return render(request, 'home/contact.html',{
		'site_description' : "test",
		'page_title' : "Contact | My Bible",
		'page_heading' : 'Contact'
		})