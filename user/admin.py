from django.contrib import admin
from .models import User_Profile, Student, Staff
# Register your models here.

class StudentTable(admin.ModelAdmin):
    list_display = ["id", "nama_mahasiswa", "NIM"]
    def nama_mahasiswa(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

class StaffTable(admin.ModelAdmin):
    list_display = ["id", "nama_staff", "NIP","Jabatan"]

    def nama_staff(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

class UserProfileTable(admin.ModelAdmin):
    list_display = ["id", "nama", "alamat","no_telp", 'prodi']
    def nama(self, obj):
        return obj.account.first_name + ' ' + obj.account.last_name
    
    def prodi(self, obj):
        return obj.prodi.nama_prodi
    
admin.site.register(User_Profile, UserProfileTable)
admin.site.register(Student, StudentTable)
admin.site.register(Staff, StaffTable)
