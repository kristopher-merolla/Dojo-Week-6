# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PostManager(models.Manager):
	def add_post(self,postData):
		if postData['post'] == "":
			message = "<p style='color:red;'>Please enter in a valid post!</p>"
			return (False,message)
		else:
			new_post = Post.objects.create(post=postData['post'])
			return (True,new_post)

class Post(models.Model):
	post = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = PostManager()