from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dashboard.models import Prodi



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1','password2']
    
    email = forms.EmailField()

    #prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE, related_name='prodi', null=True)

class StudentForm(forms.Form):
    NIM = forms.CharField(max_length=20)

class StaffForm(forms.Form):
    NIP = forms.CharField(max_length=20)
    jabatan = forms.CharField(max_length=20)
