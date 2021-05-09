from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, StudentForm
from .models import Student

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        studentForm = StudentForm(request.POST)
        if form.is_valid() and studentForm.is_valid():
            user = form.save()

            new_nim = studentForm.cleaned_data['NIM']
            new_student = Student(NIM=new_nim)
            new_student.user = user
            new_student.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
        SpecializationForm = StudentForm()
    context={
        'form':form,
        'sForm': SpecializationForm
    }
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')