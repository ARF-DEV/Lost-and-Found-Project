from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, StudentForm, User_profileForm
from .models import Student, User_Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = User_profileForm(request.POST)
        specialization_form = StudentForm(request.POST)
        
        if form.is_valid() and specialization_form.is_valid() and profile_form.is_valid():
            user = form.save()
            
            new_profile = User_Profile(
                account = user,
                alamat = profile_form.cleaned_data['alamat'],
                no_telp = profile_form.cleaned_data['no_telp'],
                prodi = profile_form.cleaned_data['prodi']
            )
            new_profile.save()

            new_student = Student(
                NIM=specialization_form.cleaned_data['NIM'],
                user=user
            )
            new_student.save()

            return redirect('user-login')
    else:
        form = CreateUserForm()
        profile_form = User_profileForm()
        specialization_form = StudentForm()
    context={
        'form':form,
        'pForm': profile_form,
        'sForm': specialization_form
    }
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')