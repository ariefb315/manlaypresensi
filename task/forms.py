from django.forms import ModelForm
from .models import Ms_tugas_harian, Absensi


class TugasharianForm(ModelForm):
    class Meta:
        model = Ms_tugas_harian
        fields = ['id', 'id_absensi', 'nm_tugas_harian', 'is_approved', 'ket_tugas', 'status', 'nip_pimpinan']

class AbsensiForm(ModelForm):
    class Meta:
        model = Absensi
        fields = '__all__'