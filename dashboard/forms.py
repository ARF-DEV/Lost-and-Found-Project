from django import forms
from .models import Laporan

STATUS = (
    ('FOUND', 'FOUND'),
    ('LOST', 'LOST'),
)


class LaporanForm(forms.ModelForm):
    class Meta:
        model = Laporan
        fields = ['status', 'tgl_laporan', 'lokasi',
                  'image']


class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['nama_barang', 'jenis_barang']
