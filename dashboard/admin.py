from django.contrib import admin
from .models import Barang

admin.site.site_header = 'Lost-Found Admin Dashboard'


class BarangTable(admin.ModelAdmin):
    list_display = ["nama_barang", "jenis_barang", "status", "isSolved"]
    list_filter = ["jenis_barang"]


# Register your models here.
admin.site.register(Barang, BarangTable)
