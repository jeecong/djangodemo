#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns=[
	#首页
	url(r"select",views.publisher_select),
	#用户注册
	url(r'pubregister',views.publisher_register),
	#修改信息
	url(r'alterinfo',views.alter),
	#用户登录
	url(r'publogin',views.publisher_login),
	#发布帖子
	url(r"publishnote", views.publish_note),
	#判断用户名是否存在数据库里面
	url(r'ajaxhaddle',views.ajax_response),
	#个人删帖
	url(r'delete',views.delete_notes),
	#帖子详情
	url(r'detail',views.detail),
	#进入大厅
	url(r'host',views.host),
]