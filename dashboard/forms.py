from django import forms
from .models import Laporan, STATUS, LOCATION, KATEGORI



class LaporanForm(forms.Form):
    
    nama_barang = forms.CharField(max_length=20)
    jenis_barang = forms.ChoiceField(choices=KATEGORI)

    status = forms.ChoiceField(choices=STATUS)
    deskripsi = forms.CharField(widget=forms.Textarea(attrs={'rows' : 5, 'cols' : 20}))
    lokasi = forms.ChoiceField(choices=LOCATION)
    foto = forms.ImageField()

    #class Meta:
    #    model = Laporan
    #    fields = ['status', 'lokasi',
    #              'image']


#class BarangForm(forms.ModelForm):
#    class Meta:
#        model = Barang
#        fields = ['nama_barang', 'jenis_barang']
