from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Prodi
from lostandfoundweb.settings import MEDIA_ROOT
# Create your models here.


class User_Profile(models.Model):
    class Meta:
        db_table = 'user-profile'  # nama tabel
        verbose_name_plural = 'Daftar User Profile'
    account = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name='account_profile')

    alamat = models.CharField(max_length=200)
    no_telp = models.CharField(max_length=20, null=True)

    image = models.ImageField(
        default=f"/profile_images/avatar.png", upload_to='profile_images')

    prodi = models.ForeignKey(
        Prodi, on_delete=models.CASCADE, related_name='laporan', null=True)

    def __str__(self):
        return f'{self.account.username}-profile'


class Student(models.Model):
    class Meta:
        db_table = 'student'  # nama tabel
        verbose_name_plural = 'Daftar Mahasiswa'
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="student", null=True)
    NIM = models.CharField(max_length=20)


class Staff(models.Model):
    class Meta:
        db_table = 'staff'  # nama tabel
        verbose_name_plural = 'Daftar Staff & Dosen'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NIP = models.CharField(max_length=20)
    Jabatan = models.CharField(max_length=20)
