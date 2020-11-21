from rest_framework import serializers
from .models import Ms_Pegawai, Ms_tugas_harian, Absensi


class PegawaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ms_Pegawai
        fields = ('nip', 'nip_pimpinan', 'nama', 'pangkat', 'nm_jabatan', 'unit_kerja', 'unor')

class TugasHarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ms_tugas_harian
        fields = ('__all__')
        depth = 1

class AbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absensi
        fields = ('__all__')