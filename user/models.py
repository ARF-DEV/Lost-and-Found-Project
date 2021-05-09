from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Prodi
# Create your models here.

class User_Profile(models.Model):
    class Meta:
        db_table = 'user-profile'  # nama tabel
        verbose_name_plural = 'Daftar User Profile'
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    alamat = models.CharField(max_length=200)
    no_telp = models.CharField(max_length=20, null=True)
    
    image = models.ImageField(default='avatar.png', upload_to='Profile_images')
    
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE, related_name='laporan', null=True)

    def __str__(self):
        return f'{self.account.username}-profile'


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student", null=True)
    NIM = models.CharField(max_length=20 )

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NIP = models.CharField(max_length=20)
    Jabatan = models.CharField(max_length=20)