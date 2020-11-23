from rest_framework import serializers
from .models import Ms_Pegawai, Ms_tugas_harian, Absensi, Hukuman


class PegawaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ms_Pegawai
        fields = ('nip', 'nip_pimpinan', 'nama', 'pangkat', 'nm_jabatan', 'unit_kerja', 'unor')

class TugasHarianSerializer(serializers.ModelSerializer):
    id_absensi = serializers.PrimaryKeyRelatedField(queryset=Absensi.objects.all())
    nip_pimpinan = serializers.PrimaryKeyRelatedField(queryset=Ms_Pegawai.objects.all())
    class Meta:
        model = Ms_tugas_harian
        fields = ('id', 'id_absensi', 'nm_tugas_harian', 'is_approved', 'ket_tugas', 'status', 'nip_pimpinan')
        depth = 1

class AbsensiSerializer(serializers.ModelSerializer):
    # tgs_harian = TugasHarianSerializer(many = True, read_only=False)
    class Meta:
        model = Absensi
        fields = ('id', 'nip', 'tgl', 'ket', 'jam_masuk', 'jam_keluar','selisih', 'latitude', 'longitude', 'nm_lokasi')


class HukumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hukuman
        fields = ('nip', 'nip_pimpinan', 'jns_hukuman', 'teguran')