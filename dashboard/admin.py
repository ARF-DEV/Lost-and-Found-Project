from django.contrib import admin
from .models import Barang, Laporan, Prodi

admin.site.site_header = 'Lost-Found Admin Dashboard'


"SELECT nama_barang,jenis_baran FROM barang"
class BarangTable(admin.ModelAdmin):
    list_display = ["nama_barang", "jenis_barang",]
    list_filter = ["jenis_barang"]

"SELECT nama_barang,jenis_barang,tgl_laporan,lokasi,isSolved,status FROM laporan NATURAL JOIN barang"
class LaporanTable(admin.ModelAdmin):
    list_display = ["nama_barang", "jenis_barang","tgl_laporan", "lokasi", "isSolved", "status"]
    list_filter = [ "lokasi", "tgl_laporan", "isSolved", "status","barang_id__jenis_barang"]

    def nama_barang(self, obj):
        return obj.barang_id.nama_barang

    def jenis_barang(self, obj):
        return obj.barang_id.jenis_barang

# Register your models here.
admin.site.register(Barang, BarangTable)

admin.site.register(Laporan, LaporanTable)

admin.site.register(Prodi)