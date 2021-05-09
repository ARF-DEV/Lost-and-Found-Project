from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, StudentForm, StaffForm, User_profileForm, UserUpdateForm, User_profileUpdateForm
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
                account=user,
                alamat=profile_form.cleaned_data['alamat'],
                no_telp=profile_form.cleaned_data['no_telp'],
                prodi=profile_form.cleaned_data['prodi']
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
    context = {
        'form': form,
        'pForm': profile_form,
        'sForm': specialization_form
    }
    return render(request, 'user/register.html', context)


def profile(request):
    return render(request, 'user/profile.html')


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = User_profileUpdateForm(
            request.POST, request.FILES, instance=request.user.user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = User_profileUpdateForm(
            instance=request.user.user_profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)
