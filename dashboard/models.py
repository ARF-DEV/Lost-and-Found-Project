from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Model Barang
KATEGORI = (
    ('Elektronik', 'Elektronik'),
    ('Alat Tulis', 'Alat Tulis'),
    ('Buku', 'Buku'),
    ('Kunci Kendaraan', 'Kunci Kendaraan'),
    ('Lainnya', 'Lainnya'),
)


STATUS = (
    ('FOUND', 'FOUND'),
    ('LOST', 'LOST'),
)

LOCATION = (
    ('GEDUNG A', 'GEDUNG A'),
    ('GEDUNG B', 'GEDUNG B'),
    ('GEDUNG C', 'GEDUNG C'),
    ('GEDUNG D', 'GEDUNG D'),
    ('GEDUNG E', 'GEDUNG E'),
    ('GEDUNG F', 'GEDUNG F'),
    ('LABTEK 1', 'LABTEK 1'),
    ('LABTEK 2', 'LABTEK 2'),
    ('LABTEK 3', 'LABTEK 3'),
    ('GKU 1', 'GKU 1'),
    ('LAINNYA', 'LAINNYA'),
)


class Barang(models.Model):
    class Meta:
        db_table = 'barang'  # nama tabel
        verbose_name_plural = 'Daftar Barang'

    nama_barang = models.CharField(max_length=20, null=True)
    jenis_barang = models.CharField(max_length=25, choices=KATEGORI, null=True)

    def __str__(self):
        return f'{self.nama_barang} - {self.id}'


class Laporan(models.Model):
    class Meta:
        db_table = 'laporan'  # nama tabel
        verbose_name_plural = 'Daftar Laporan'

    status = models.CharField(max_length=5, choices=STATUS, null=True)
    isSolved = models.BooleanField(default=False)
    deskripsi_barang = models.TextField(null=True)
    tgl_laporan = models.DateField(auto_now_add=True, null=True)
    lokasi = models.CharField(max_length=10, choices=LOCATION, null=True)
    image = models.ImageField(
        default=f"/item/default.png", upload_to='item')
    barang_id = models.ForeignKey(
        Barang, on_delete=models.CASCADE, related_name='laporan', null=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='laporan', null=True)

    def __str__(self):
        return f'{self.barang_id.nama_barang} - {self.tgl_laporan} - {self.lokasi}'


class Prodi(models.Model):
    class Meta:
        db_table = 'program-studi'  # nama tabel
        verbose_name_plural = 'Daftar Program Studi'

    nama_prodi = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} - {self.nama_prodi}'
    #userid -belom
    #adminid -belom
