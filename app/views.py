#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import Publisher,Note,Browse,Admin
from django.conf import settings
from django.conf.urls.static import static
import os
import time

# Create your views here.

# def welcome(request):
# 	return render(request,"index.html")


#选择
def publisher_select(request):
	noteArr=Note.objects.all()
	infoArr=[]
	for note in noteArr:
		publisher=Publisher.objects.filter(id=note.publisher_id)[0]
		infoDict={'note':note,'publisher':publisher}
		infoArr.append(infoDict)
		pass
	context={'noteArr':infoArr}
	return render(request,'index.html',context)

#用户登录
def publisher_login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']

		#根据数据从数据库 中查找用户
		userArr = Publisher.objects.filter(username=username)
		if userArr:
			#说明用户名正确，进一步比较密码
			#从userArr取出列表元素
			user = userArr[0]


			if user.password==password:
				#说明密码正确
				#return HttpResponse("登录成功")
				notesArr = Note.objects.filter(publisher_id=user.id)
				userDict={"id":user.id,"username":user.username,"nickname":user.nickname,"sex":user.sex,"signature":user.signature,"url":user.url,"notesArr":notesArr}
				context = {}
				context['userinfo'] = userDict

				return render(request,"person.html",context)
			else:
				#密码不对
				return HttpResponse("密码错误")

		else:
			#说明用户名不对
			return HttpResponse('用户名不存在')


	#return HttpResponse('login')
	return render(request,"login.html")
	pass


#注册
def publisher_register(request):
	#模板中发生提交事件，在下面代码中处理
	if request.method=='POST':
		#一旦发生post事件，在这里处理

		username = request.POST['username']
		password = request.POST['password']
		nickname = request.POST['nickname']
		sex = request.POST['sex']
		signature = request.POST['signature']

		url = request.FILES['headerimg']

		#处理前端数据

		#建模
		pub = Publisher(username=username,password=password,nickname=nickname,sex=sex,signature=signature,url=url)
		pub.save()

		return HttpResponse("<script type = 'text/javascript'>alert('注册成功');window.history.go(-2);</script>")


	return render(request,"register.html")
	pass

#修改个人信息
def alter(request):
	if request.method=='POST':
		if request.POST['flag']=='index':
			#在这里安装修改模板
			userid=request.POST['userid']
			#根据userid查找出对象
			userArr = Publisher.objects.filter(id=userid)
			usr = userArr[0]

			#转成字典
			userDict = {'id':usr.id,'nickname':usr.nickname,'signature':usr.signature,'password':usr.password}
			context = {'userinfo':userDict}


			return render(request,'alter.html',context)
		else:
			#说明不是index页发出的请求，有可能是模板页，处理模板的post请求
			nickname = request.POST['nickname']
			signature = request.POST['signature']
			img = request.FILES['headerimg']

			id = request.POST['userid']
			userArr = Publisher.objects.filter(id=id)
			usr = userArr[0]

			usr.nickname = nickname
			usr.signature = signature

			usr.url = img

			usr.save()


			return HttpResponse("<script type = 'text/javascript'>alert('修改成功');window.history.go(-2);</script>")

	return HttpResponse("修改模板")




#发帖子
def publish_note(request):


	if request.POST['flag']=='index':

		id=request.POST['userid']
		pub=Publisher.objects.filter(id=id)[0]
		return render(request,'edit.html',{'pub':pub})
	else :

		username=request.POST['id']
		title=request.POST['title']
		content=request.POST['content']
		flag=request.POST['flag']
		timer=time.strftime("%Y-%m-%d %X",time.localtime())

		note=Note(title=title,time=timer,content=content,publisher_id=username)
		note.save()
		#待修改
		#增刷新个人主页帖子window.location.reload;
		return HttpResponse('<script type="text/javascript">alert("发布成功");window.history.go(-2);</script>')

#显示首页的所有帖子
# def note_index(request):
# 	noteArr=Note.objects.all()
# 	infoArr=[]
# 	for note in noteArr:
# 		publisher=Publisher.objects.filter(id=note.publisher_id)[0]
# 		infoDict={'note':note,'publisher':publisher}
# 		infoArr.append(infoDict)
# 		pass
# 	context={'noteArr':infoArr}
# 	return render(request,'index.html',context)


#大厅
def host(request):
	noteArr=Note.objects.all()
	infoArr=[]
	for note in noteArr:
		publisher=Publisher.objects.filter(id=note.publisher_id)[0]

		id=request.POST['userid']
		pub=Publisher.objects.filter(id=id)[0]

		infoDict={'note':note,'publisher':publisher,'pub':pub}
		infoArr.append(infoDict)
	context={'noteArr':infoArr}

	return render(request,'host.html',context)
	pass


# ajax请求的响应

def ajax_response(request):
	username = request.POST['username']
	#查询前端传过来的用户名是否在数据库中
	res = Publisher.objects.filter(username=username)
	#将查询结果作为响应体返回

	return HttpResponse(res)

def delete_notes(request):
	notesid = request.POST['notesid']
	Note.objects.filter(id=notesid).delete()
	return HttpResponse('ok')

isLogin=0
def detail(request):
	notesid=request.GET['notesid']
	notes=Note.objects.filter(id=notesid)[0]
	pubid=notes.publisher_id
	pub=Publisher.objects.filter(id=pubid)[0]


	global isLogin
	context={'notes':notes,'isLogin':isLogin,'publisher':pub}
	return render(request,'detail.html',context)
	pass




# def replays(req,post_id):
# 	userid=request.POST['userid']
# 	if req.is_ajax():
# 		content = req.POST.get('content',None)
# 		if content:
# 			item=Note.objects.get(id=post_id)
# 			Browse.objects.create(reader_id=userid,note_id=item,content=content,replay_time=datetime.datetime.today())#将评论写进数据库
# 			return  HttpResponse(json.dumps({"content":content}))
#         else:
#         	form = ReplayForm()
#         note_id=post_id
#         replays = Note.objects.get(id=note_id).replay_set.all()#一条帖子的所有评
#         title = Note.objects.get(id=note_id).title
#         content = Note.objects.get(id=post_id).content
#         username = Publisher.objects.get(id=userid)
#         return render_to_response('host.html',{

#                 'replays':replays,

#                 'form':form,
#                 },context_instance=RequestContext(req))