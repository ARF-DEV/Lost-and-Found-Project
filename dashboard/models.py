from django.db import models

# Create your models here.

# Model Barang
KATEGORI = (
    ('KATEGORI 1', 'KATEGORI 1'),
    ('KATEGORI 2', 'KATEGORI 2'),
    ('KATEGORI 3', 'KATEGORI 3'),
    ('KATEGORI 4', 'KATEGORI 4'),
    ('KATEGORI 5', 'KATEGORI 5'),
    ('KATEGORI 6', 'KATEGORI 6'),
)


class Barang(models.Model):
    nama_barang = models.CharField(max_length=20, null=True)
    jenis_barang = models.CharField(max_length=10, choices=KATEGORI, null=True)
    isFound = models.BooleanField(default=False)
    isSolved = models.BooleanField(default=False)
    deskripsi_barang = models.TextField(null=True)
    #id_admin = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_admin', default='')
    #id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='barang', null=True, default=None)

    def __str__(self):
        return f'{self.nama_barang} - {self.id}'

    class Meta:
        #managed = False
        db_table = 'barang'
