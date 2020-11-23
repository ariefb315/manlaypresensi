from .models import Ms_Pegawai, Absensi

def cek_hukuman():
    pegawai = Ms_Pegawai.objects.all()
    for orang in pegawai:
        print(orang)