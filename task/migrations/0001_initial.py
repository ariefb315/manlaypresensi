# Generated by Django 3.1.2 on 2020-11-19 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absensi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField()),
                ('ket', models.CharField(max_length=200, null=True)),
                ('jam_masuk', models.DateTimeField(null=True)),
                ('jam_keluar', models.DateTimeField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('nm_lokasi', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Ms_Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=75)),
                ('pangkat', models.CharField(max_length=7)),
                ('nm_jabatan', models.CharField(max_length=50)),
                ('unit_kerja', models.CharField(max_length=50)),
                ('unor', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('nip_pimpinan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.ms_pegawai')),
            ],
        ),
        migrations.CreateModel(
            name='Ms_tugas_harian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_tugas_harian', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('ket_tugas', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('id_absensi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.absensi')),
                ('nip_pimpinan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.ms_pegawai')),
            ],
        ),
        migrations.CreateModel(
            name='ijin_pindah_lokasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alasan', models.CharField(max_length=70)),
                ('lat_awal', models.FloatField(null=True)),
                ('long_awal', models.FloatField(null=True)),
                ('lokasi_awal', models.CharField(max_length=75)),
                ('lat_baru', models.FloatField(null=True)),
                ('long_baru', models.FloatField(null=True)),
                ('lokasi_baru', models.CharField(max_length=75)),
                ('id_absensi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.absensi')),
            ],
        ),
        migrations.AddField(
            model_name='absensi',
            name='nip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.ms_pegawai'),
        ),
    ]
