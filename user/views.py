from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm, StudentForm, StaffForm, User_profileForm, UserUpdateForm, User_profileUpdateForm
from .models import Student, User_Profile, Staff
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    
    return render(request, 'user/register_selector.html')


def register_student(request):

    if request.user.is_authenticated:
        return redirect('/profile')

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
            messages.success(request, 'User berhasil terdaftar' )
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


def register_staff(request):
    if request.user.is_autenticated():
        return redirect('/profile')

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = User_profileForm(request.POST)
        specialization_form = StaffForm(request.POST)

        if form.is_valid() and specialization_form.is_valid() and profile_form.is_valid():
            user = form.save()

            new_profile = User_Profile(
                account=user,
                alamat=profile_form.cleaned_data['alamat'],
                no_telp=profile_form.cleaned_data['no_telp'],
                prodi=profile_form.cleaned_data['prodi']
            )
            new_profile.save()

            new_staff = Staff(
                NIP=specialization_form.cleaned_data['NIP'],
                # Jabatan=specialization_form.cleaned_data['Jabatan'],
                user=user
            )
            new_staff.save()
            messages.success(request, 'User berhasil terdaftar')
            return redirect('user-login')
    else:
        form = CreateUserForm()
        profile_form = User_profileForm()
        specialization_form = StaffForm()
    context = {
        'form': form,
        'pForm': profile_form,
        'sForm': specialization_form
    }
    return render(request, 'user/register.html', context)

@login_required()
def profile(request):
    return render(request, 'user/profile.html')

@login_required()
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = User_profileUpdateForm(
            request.POST, request.FILES, instance=request.user.account_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = User_profileUpdateForm(
            instance=request.user.account_profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)
