from django.db import models

# Create your models here.

# Model Barang
KATEGORI = (
    ('Elektronik', 'Elektronik'),
    ('KATEGORI 2', 'KATEGORI 2'),
    ('KATEGORI 3', 'KATEGORI 3'),
    ('KATEGORI 4', 'KATEGORI 4'),
    ('KATEGORI 5', 'KATEGORI 5'),
    ('KATEGORI 6', 'KATEGORI 6'),
)
STATUS = (
    ('FOUND', 'FOUND'),
    ('LOST', 'LOST'),
)

LOCATION = (
    ('FOUND', 'FOUND'),
    ('LOST', 'LOST'),
)


class Barang(models.Model):
    class Meta:
        db_table = 'barang'  # nama tabel

    nama_barang = models.CharField(max_length=20, null=True)
    jenis_barang = models.CharField(max_length=10, choices=KATEGORI, null=True)

    # ------------------------- punya laporan---------------------------
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    isSolved = models.BooleanField(default=False)
    deskripsi_barang = models.TextField(null=True)
    tgl_laporan = models.DateField(auto_now_add=True, null=True)

    #userid -belom
    #adminid -belom
    # ------------------------- punya laporan---------------------------

    #id_admin = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_admin', default='')
    #id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='barang', null=True, default=None)

    def __str__(self):
        return f'{self.nama_barang} - {self.id}'
