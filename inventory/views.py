from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *


# Create your views here.

def index(request):
	return render(request,'index.html')

def display_laptop(request):
	items = Laptop.objects.all()
	product = request.GET.get('q')
	if product:
		items = Laptop.objects.filter(item__icontains=product)
	context = {
	'items':items,
	'header':'Laptop',
	}
	return render(request,'index.html',context)



def display_desktop(request):
	items = Desktop.objects.all()
	product = request.GET.get('q')
	if product:
		items = Desktop.objects.filter(item__icontains=product)
	context = {
	'items':items,
	'header':'Desktops',
	}
	return render(request,'index.html',context)

def display_mobile(request):
	items = Mobile.objects.all()
	product = request.GET.get('q')
	if product:
		items = Mobile.objects.filter(item__icontains=product)
	context = {
	'items':items,
	'header':'Mobiles',
	}
	return render(request,'index.html',context)

def add_laptop(request):
	if request.method == 'POST':
		form = LaptopForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('display_laptop')
	else:
		form = LaptopForm()
		return render(request,'add_new.html',{'form':form,'header':'latop'})

def add_desktop(request):
	if request.method == 'POST':
		form = DesktopForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('display_desktop')
	else:
		form = DesktopForm()
		return render(request,'add_new.html',{'form':form,'header':'desktop'})

def add_mobile(request):
	if request.method == 'POST':
		form = MobileForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('display_mobile')
	else:
		form = MobileForm()
		return render(request,'add_new.html',{'form':form,'header':'mobile'})


def edit_device(request,pk,model,cls):
	items = get_object_or_404(model,pk=pk)

	if request.method == 'POST':
		form = cls(request.POST,instance=items)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = cls(instance=items)
		return render(request,'edit_item.html',{'form':form})

def edit_laptop(request,pk):
	return edit_device(request,pk,Laptop,LaptopForm)

def edit_desktop(request,pk):
	return edit_device(request,pk,Desktop,DesktopForm)

def edit_mobile(request,pk):
	return edit_device(request,pk,Mobile,MobileForm)

def delete_device(request,pk):
	Device.objects.filter(pk=pk).delete()
	items = Device.objects.all()
	return render(request,'index.html',{'items':items})


def delete_laptop(request,pk):
	Laptop.objects.filter(pk=pk).delete()
	items = Laptop.objects.all()
	return render(request,'index.html',{'items':items})

def delete_desktop(request,pk):
	Desktop.objects.filter(pk=pk).delete()
	items = Desktop.objects.all()
	return render(request,'index.html',{'items':items})

def delete_mobile(request,pk):
	Mobile.objects.filter(pk=pk).delete()
	items = Mobile.objects.all()
	return render(request,'index.html',{'items':items})

