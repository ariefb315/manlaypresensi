from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, nama, username, password=None):
        if not username:
            raise ValueError("Users must have an username!")

        user = self.model(
            nama=nama,
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, nama, username, password=None):
        user = self.create_user(
            nama=nama,
            password=password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Ms_Pegawai(models.Model):
    nip             = models.CharField(max_length=30)
    nip_pimpinan    = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    nama            = models.CharField(max_length=75)
    pangkat         = models.CharField(max_length=7)
    nm_jabatan      = models.CharField(max_length=50)
    unit_kerja      = models.CharField(max_length=50)
    unor            = models.CharField(max_length=50)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nama',]

    objects = MyAccountManager

    def __str__(self):
        return self.nama

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    # def __str__(self):
    #     return self.nama 

class Absensi(models.Model):
    nip             = models.ForeignKey(Ms_Pegawai, on_delete=models.CASCADE)
    tgl             = models.DateField()
    ket             = models.CharField(max_length=200, null=True)
    jam_masuk       = models.DateTimeField(null=True)
    jam_keluar      = models.DateTimeField(null=True)
    latitude        = models.FloatField(null=True)
    longitude       = models.FloatField(null=True)
    nm_lokasi       = models.CharField(max_length=75)

    def __str__(self):
        return str(self.nip)   


class Ms_tugas_harian(models.Model):
    id_absensi      = models.ForeignKey('Absensi', on_delete=models.CASCADE)
    nm_tugas_harian = models.CharField(max_length=100)
    is_approved     = models.BooleanField(default=False)
    ket_tugas       = models.CharField(max_length=100, blank=True, null=True)
    status          = models.CharField(max_length=100, blank=True, null=True)
    nip_pimpinan    = models.ForeignKey('Ms_Pegawai', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nm_tugas_harian
   


class ijin_pindah_lokasi(models.Model):
    id_absensi      = models.ForeignKey('Absensi', on_delete=models.CASCADE)
    alasan          = models.CharField(max_length=70)
    lat_awal        = models.FloatField(null=True)
    long_awal       = models.FloatField(null=True)
    lokasi_awal     = models.CharField(max_length=75)
    lat_baru        = models.FloatField(null=True)
    long_baru       = models.FloatField(null=True)
    lokasi_baru     = models.CharField(max_length=75)

    def __str__(self):
        return self.alasan


# Create your models here.
