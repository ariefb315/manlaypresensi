from django.contrib import admin
from .models import Ms_Pegawai, Ms_tugas_harian, ijin_pindah_lokasi, Absensi, Hukuman

class PegawaiAdmin(admin.ModelAdmin):
    list_display = ('nip', 'nama', 'nip_pimpinan', 'pangkat', 'nm_jabatan', 'unit_kerja', 'unor' )

class TugasharianAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_absensi', 'nm_tugas_harian', 'is_approved', 'nip_pimpinan')

class AbsensiAdmin(admin.ModelAdmin):
    list_display = ('nip', 'tgl', 'jam_masuk', 'jam_keluar', 'nm_lokasi')

class IjinAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_absensi', 'alasan', 'lokasi_awal', 'lokasi_baru')


admin.site.register(Ms_Pegawai, PegawaiAdmin)
admin.site.register(Ms_tugas_harian, TugasharianAdmin)
admin.site.register(Absensi, AbsensiAdmin)
admin.site.register(ijin_pindah_lokasi, IjinAdmin)
admin.site.register(Hukuman)

