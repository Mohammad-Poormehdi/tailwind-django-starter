from django import forms
from main.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'name': 'نام',
            'email':'ایمیل (اختیاری)',
            'phone_number':'تلفن همراه',
            'project_name':'نام پروژه',
            'project_description':'توضیحات پروژه',
        }
        error_messages = {
            'email':
                {'invalid':'یک ایمیل معتبر وارد کنید'},
            'phone_number':
                {'invalid':'یک شماره همراه معتبر وارد کنید'},
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'نام و نام خانوادگی خود را وارد کنید'}),
            'email': forms.TextInput(attrs={'placeholder':'ایمیل خود را وارد کنید'}),
            'phone_number': forms.TextInput(attrs={'placeholder':'شماره تلفن همراه خود را وارد کنید', 'dir':'rtl'}),
            'project_name': forms.TextInput(attrs={'placeholder':'نام پروژه خود را وارد کنید'}),
            'project_description': forms.Textarea(attrs={'placeholder':'توضیحاتی در مورد پروژه خود بنویسید'}),
        }