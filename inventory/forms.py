from django import forms
from .models import *

# class DeviceForm(forms.ModelForm):
# 	class Meta:
# 		model = Device
# 		fields = ('item','price','status','issues')

# class LaptopForm(DeviceForm):
# 	pass

# class DesktopForm(DeviceForm):
# 	pass

# class MobileForm(DeviceForm):
# 	pass


class LaptopForm(forms.ModelForm):
	class Meta:
		model = Laptop
		fields = ('item','price','status','issues')


class DesktopForm(forms.ModelForm):
	class Meta:
		model = Desktop
		fields = ('item','price','status','issues')


class MobileForm(forms.ModelForm):
	class Meta:
		model = Mobile
		fields = ('item','price','status','issues')