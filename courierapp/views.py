from django.shortcuts import render
from courierapp.models import *;

# Create your views here.
def homepage(request):
	return render(request,"home.html")

def trackpage(request):
	return render(request,"tracking.html")

def insepage(request):
	return render(request,"inse.html")

def aboutpage(request):
	return render(request,"about.html")

def contactpage(request):
	return render(request,"contus.html")

def memberpage(request):
	return render(request,"member.html")

def workpage(request):
	if 'workuser' in request.session:
		return render(request,"backend.html")
	return render(request,"login.html")

def logcheck(request):
	mEmail = request.GET.get('cem')
	mpass =request.GET.get('cpass')
	data=Member.objects.all()
	for d in data:
		if d.Email==mEmail and d.Password==mpass:
			request.session['username']=d.FirstName
			return render(request,'home.html')
	return render(request,'member.html')

def regpage(request):
	return render(request,"reg.html")

def member_save_View(request):
	mFirstname = request.GET.get('fn')
	mLastname = request.GET.get('ln')
	mPhone = request.GET.get('pno')
	mEmail = request.GET.get('cem')
	mpass =request.GET.get('cpass')
	m = Member()
	m.FirstName = mFirstname
	m.LastName = mLastname
	m.PhoneNumber = mPhone
	m.Email = mEmail
	m.Password= mpass
	m.save()
	request.session['username']=mFirstname
	return render(request,'home.html')

def tdisp(request):
	note=request.GET.get('cnote')
	data1=BackendModel.objects.all()
	for d in data1:
		if d.noteno==note:
			data=BackendModel.objects.get(noteno=note)
			return render(request,'trckdisp.html',{"disp":data})
	return render(request,'tracking.html')

def logpage(request):
	return render(request,"login.html")

def logc(request):
	name=request.GET.get('un')
	pwd=request.GET.get('pw')
	data=RegModels.objects.all()
	for d in data:
		if d.Username==name and d.Password==pwd:
			request.session['workuser']=d.Username
			return render(request,"backend.html")
	return render(request,"login.html")

def shipment(request):
	if 'workuser' in request.session:
		Origin=request.GET.get('origin')
		Date=request.GET.get('date')
		Company=request.GET.get('company')
		Time=request.GET.get('time')
		Destination=request.GET.get('destination')
		Noteno=request.GET.get('noteno')
		data=BackendModel()
		data.origin=Origin
		data.date=Date
		data.companyname=Company
		data.time=Time
		data.destination=Destination
		data.noteno=Noteno
		data.save()
		return render(request,'backend.html')
	return render(request,"login.html")

def cmpsave(request):
	if 'username' in request.session:
		info=request.GET.get('comp')
		phone=request.GET.get('pno')
		email=request.GET.get('em')
		d=cmpModel()
		d.Context=info
		d.PhoneNumber=phone
		d.Email=email
		d.save()
		return render(request,"contus.html")
	return render(request,"member.html")

def findview(request):
	if 'workuser' in request.session:
		ws=request.GET.get('worksearch')
		data=BackendModel.objects.all()
		for d in data:
			if d.date==ws:
				data2=BackendModel.objects.filter(date=ws)
				return render(request,"display.html",{"info":data2})
			if d.destination==ws:
				data2=BackendModel.objects.filter(destination=ws)
				return render(request,"display.html",{"info":data2})
		return render(request,"backend.html")
	return render(request,"login.html")

def deleteview(request):
	if 'workuser' in request.session:
		did=request.GET.get('id')
		del_obj=BackendModel.objects.get(id=did)
		del_obj.delete()
		data2=BackendModel.objects.all()
		return render(request,"display.html",{"info":data2})
	return render(request,"login.html")

def dispall(request):
	if 'workuser' in request.session:
		data2=BackendModel.objects.all()
		return render(request,"display.html",{"info":data2})
	return render(request,"login.html")

def logoutview(request):
	del request.session['workuser']
	return render(request,"login.html")