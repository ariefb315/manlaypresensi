import json
import requests

id_list = []
nip_list = []
nama_list = []
nip_pimpinan_list = []
unit_kerja_list = []
unor_list = []
pangkat_list = []
nm_jabatan_list = []
resp = requests.get('http://localhost:8080/api/pegawai/')
data = resp.json()

for i in range(3):
    if data[i]['nip_pimpinan']==None:
        id = data[i]['id']
        nip = data[i]['nip']
        nama = data[i]['nama']
        # nip_pimpinan = data[i]['nip_pimpinan']
        unit_kerja = data[i]['id_unker']['nm_unker']
        unor = data[i]['id_unor']['nm_unor']
        pangkat = data[i]['pangkat']
        nm_jabatan = data[i]['id_jabatan']['nm_jabatan']
        id_list.append(id)
        nip_list.append(nip)
        nama_list.append(nama)
        # nip_pimpinan_list.append(nip_pimpinan)
        unit_kerja_list.append(unit_kerja)
        unor_list.append(unor)
        pangkat_list.append(pangkat)
        nm_jabatan_list.append(nm_jabatan)
    else:
        id = data[i]['id']
        nip = data[i]['nip']
        nama = data[i]['nama']
        nip_pimpinan = data[i]['nip_pimpinan']['nip']
        unit_kerja = data[i]['id_unker']['nm_unker']
        unor = data[i]['id_unor']['nm_unor']
        pangkat = data[i]['pangkat']
        nm_jabatan = data[i]['id_jabatan']['nm_jabatan']
        id_list.append(id)
        nip_list.append(nip)
        nama_list.append(nama)
        nip_pimpinan_list.append(nip_pimpinan)
        unit_kerja_list.append(unit_kerja)
        unor_list.append(unor)
        pangkat_list.append(pangkat)
        nm_jabatan_list.append(nm_jabatan)

    # print(nama_list, nip_pimpinan_list)
# for i in range(4):
