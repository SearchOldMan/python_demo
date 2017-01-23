#coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib import admin


# Create your models here.

#save user's message
class Newuser(models.Model):
	name = models.CharField(max_length=30)
	tel = models.IntegerField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=30)

class Attention(models.Model):
	number = models.CharField(max_length=30)
	href = models.CharField(max_length=30)
	title = models.CharField(max_length=50)
	content = models.TextField()
	author = models.CharField(max_length=40)
	time = models.CharField(max_length=30)

class ATitle(models.Model):
	a_title = models.ForeignKey(Attention)

#定义表单模型
class UserForm(models.Model):
 	username = models.CharField(max_length=100)
 	pw = models.CharField(max_length=30)

