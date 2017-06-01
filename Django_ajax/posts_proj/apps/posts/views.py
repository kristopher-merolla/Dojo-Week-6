# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Post

# Create your views here.
def index(request):
	return render(request, 'posts/index.html')

def post(request):
	postData = {
		"post":request.POST['post']
	}
	model_resp = Post.objects.add_post(postData)
	if model_resp[0]: # model_resp[0] will return a True or False boolean depending on if the post passed our model validations
		context = {
			"posts":Post.objects.all()
		}
		return render(request, 'posts/index.html', context)
	else:
		context = {
			"message":model_resp[1] # model_resp[1] will return the error message (if, for example, a user tries an empty post)
		}
		return render(request, 'posts/index.html', context)