from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Model Barang
KATEGORI = (
    ('Elektronik', 'Elektronik'),
    ('Alat Tulis', 'Alat Tulis'),
    ('Buku', 'Buku'),
    ('Kunci Kendaraan', 'Kunci Kendaraan'),
    ('KATEGORI 5', 'KATEGORI 5'),
    ('KATEGORI 6', 'KATEGORI 6'),
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
PRODI = (
    (1, 'Teknik Informatika'),
    (2, 'Teknik Elektro'),
    (3, 'Teknologi Pangan'),
    (4, 'Teknik Geofisika'),
    (5, 'Teknik Sipil'),
    (6, 'Teknik Arsitektur'),
    (7, 'Teknik Mesin'),
    (8, 'Biologi'),
    (9, 'Farmasi'),
    (10, 'Perencanaan Wilayah dan Kota'),
)

class Barang(models.Model):
    class Meta:
        db_table = 'barang'  # nama tabel
        verbose_name_plural = 'Daftar Barang'

    nama_barang = models.CharField(max_length=20, null=True)
    jenis_barang = models.CharField(max_length=25, choices=KATEGORI, null=True)

    def __str__(self):
        return f'{self.nama_barang} - {self.id}'
    # ------------------------- punya laporan---------------------------

class Laporan(models.Model):
    class Meta:
        db_table = 'laporan'  # nama tabel
        verbose_name_plural = 'Daftar Laporan'

    status = models.CharField(max_length=10, choices=STATUS, null=True)
    isSolved = models.BooleanField(default=False)
    deskripsi_barang = models.TextField(null=True)
    tgl_laporan = models.DateField(auto_now_add=True, null=True)
    lokasi = models.CharField(max_length=10, choices=LOCATION, null=True)
    
    barang_id = models.ForeignKey(Barang, on_delete=models.CASCADE, related_name='laporan', null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='laporan', null=True)

    def __str__(self):
        return f'{self.barang_id.nama_barang} - {self.tgl_laporan} - {self.lokasi}'
    #userid -belom
    #adminid -belom
    # ------------------------- punya laporan---------------------------

    #id_admin = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_admin', default='')
    #id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='barang', null=True, default=None)

class Prodi(models.Model):
    class Meta:
        db_table = 'Program-studi'  # nama tabel
        verbose_name_plural = 'Daftar Program Studi'

    nama_prodi = models.CharField(max_length=50)
    #userid -belom
    #adminid -belom


