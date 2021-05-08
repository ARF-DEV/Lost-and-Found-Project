from django.contrib import admin
from .models import Barang, Laporan

admin.site.site_header = 'Lost-Found Admin Dashboard'


class BarangTable(admin.ModelAdmin):
    list_display = ["nama_barang", "jenis_barang",]
    list_filter = ["jenis_barang"]

class LaporanTable(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(LaporanTable, self).get_form(request, obj, **kwargs)
        form.fields['theme'].queryset = Theme.objects.filter(name__iexact='company')
        return form


# Register your models here.
admin.site.register(
    Barang, BarangTable
)

admin.site.register(
    Laporan, LaporanTable
)