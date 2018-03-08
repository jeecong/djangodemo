#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


#######【发布者】##########
class Publisher(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(unique=True,max_length=20)
	password = models.CharField(max_length=20)
	nickname = models.CharField(max_length=20)
	sex = models.CharField(max_length=4)
	signature = models.CharField(max_length=80)

	url = models.FileField(upload_to='pubheader')

	class Meta:
		db_table = 'publisher'

	def __unicode__(self):
		return self.username

#2.管理者
class Admin(models.Model):
	id = models.CharField(primary_key=True,max_length=20)
	password = models.CharField(max_length=20)

	class Meta:
		db_table = 'admin'

#3.帖子
class Note(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=80)
	time = models.DateTimeField()
	content = models.TextField()


	#外键
	publisher = models.ForeignKey(
		Publisher,
		on_delete=models.CASCADE)

	class Meta:
		db_table = 'note'

	def __unicode__(self):
		return self.title

#4.关系表
class Browse(models.Model):

	reader = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	note = models.ForeignKey(Note, on_delete=models.CASCADE)

	attitude = models.IntegerField()
	class Meta:
		db_table = 'browse'



