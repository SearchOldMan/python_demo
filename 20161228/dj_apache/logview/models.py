from __future__ import unicode_literals

from django.db import models

# Create your models here.

class OperatingSystem(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.name

class Service(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.name

class HardwareComponent(models.Model):
	manufacturer = models.CharField(max_length=50)
	#types include video card,network card
	type = models.CharField(max_length=50)
	model = models.CharField(max_length=50,blank=True,null=True)
	vendor_part_number = models.CharField(max_length=50,blank=True,null=True)
	description = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.model

class Server(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True,null=True)
	os = models.ForeignKey(OperatingSystem)
	services = models.ManyToManyField(Service)
	hardware_component = models.ManyToManyField(HardwareComponent)

	def __str__(self):
		return self.name 

class IPAddress(models.Model):
	address = models.TextField(blank=True,null=True)
	server = models.ForeignKey(Server)

	def __str__(self):
		return self.address

class Computal(models.Model):
	hostname = models.CharField(max_length=50)
	comdescription = models.TextField(blank=True,null=True)