from django.contrib import admin
from .models import User_Profile, Student, Staff
# Register your models here.

"SELECT id, first_name, NIM status FROM user NATURAL JOIN student"
class StudentTable(admin.ModelAdmin):
    list_display = ["id", "nama_mahasiswa", "NIM"]
    def nama_mahasiswa(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

"SELECT id, nama_staff, NIM, jabatan status FROM user NATURAL JOIN staff"
class StaffTable(admin.ModelAdmin):
    list_display = ["id", "nama_staff", "NIP","Jabatan"]

    def nama_staff(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

"SELECT id, nama, alamat, no_telp, prodi status FROM user NATURAL JOIN user_profile"
class UserProfileTable(admin.ModelAdmin):
    list_display = ["id", "nama", "alamat","no_telp", 'prodi']
    def nama(self, obj):
        return obj.account.first_name + ' ' + obj.account.last_name
    
    def prodi(self, obj):
        return obj.prodi.nama_prodi
    
admin.site.register(User_Profile, UserProfileTable)
admin.site.register(Student, StudentTable)
admin.site.register(Staff, StaffTable)
