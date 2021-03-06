from django.shortcuts import render, HttpResponse, redirect
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.schemas.openapi import SchemaGenerator
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.schemas.openapi import AutoSchema

import coreapi
import coreschema

from .models import Ms_Pegawai, Absensi, ijin_pindah_lokasi, Ms_tugas_harian, Hukuman
# from django.utils.six import BytesIO
from .serializers import PegawaiSerializer
import requests
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
import io
import json
from . import apitest
from .forms import TugasharianForm, AbsensiForm, HukumanForm
from django.contrib import messages
from .serializers import PegawaiSerializer, TugasHarianSerializer, AbsensiSerializer

import datetime



def home(request):
    #34.199.13.26/api/pegawai
    is_caches = ('data_peg' in request.session)
    if request.method=='POST':
        # data = request.POST.get('is_approve', False)
        post_pegawai = request.POST.getlist('nm_peg')
        id_absensi = request.POST.getlist('id_absensi')
        tugas_harian = Ms_tugas_harian.objects.all()
        pimpinan = Ms_Pegawai.objects.get(nama__startswith='Muhammad')
        is_approve = request.POST.getlist('is_approve')
        id_tugas_harian = request.POST.getlist('id')
        # presensi = Absensi.objects.
        selisih = len(id_tugas_harian) - len(is_approve)

        # for id in range(len(id_tugas_harian)):
        #     if len(is_approve)!=len(id_tugas_harian):
        #         if(is_approve[id]=='on'):
        #             is_approve[id]==True
        #         elif(is_approve[id]==''):
        #             is_approve[id]==False
        print("ini id tugas")
        print(request.POST.get('id_tugas'))


        # if len(is_approve)==0 and id_tugas_harian != 0:
        #     for i in id_tugas_harian:
        #         is_approve.append('False')
        # print(is_approve)
        count=0
        # print(id_tugas_harian)
        print(request.POST)
        for person, id in zip(post_pegawai, id_absensi):
            try:
                pegawai = Absensi.objects.get(id=int(id), nip__nama__startswith=person)
            except pegawai.DoesNotExist:
                continue
            
            # kehadiran = Absensi.objects.get()
            # print(person)
            # print(type(int(id)), id)
            # print(type(pegawai.id), id)
            # print(is_approve)
            
            for id_tgs, apr in zip(id_tugas_harian, is_approve):
                print(id_tgs)
                try:
                    new_tugas = Ms_tugas_harian.objects.get(id=int(id_tgs), id_absensi=pegawai.id)
                except new_tugas.DoesNotExist:
                    continue
                if apr=='on':
                    apr=True
                else:
                    apr=False
                print(id_tgs, apr)
                # new_tugas = Ms_tugas_harian(id=1,
                #                         id_absensi=Absensi.objects.get(id=1),
                #                         is_approved=is_approve1,
                #                         ket_tugas=request.POST.get('tambah_tugas1'),
                #                         # status=request.POST.get()
                #                         nip_pimpinan='1995012314')
            
            # tugas1 = request.POST.get('tambah_tugas{}'.format(person), False)
            # approved = request.POST.get('id_absensi.id', False)
            # tugas2 = request.POST.get('tambah_tugas2', False)
            # print(tugas1, approved)
        # print(  tugas_id)
        # new_tugas.save(update_fields=['id_absensi', 'is_approved', 'ket_tugas', 'nip_pimpinan'])
            count+=1
    #cache API agar lebih cepat saat load data
    # if not is_caches:
    #     ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    #     response = requests.get('http://localhost:8080/api/pegawai/')
    #     request.session['data_peg'] = response.json()
    
    # data_peg = request.session['data_peg']
    list_pegawai = []
    # for pegawai in data_peg:
    #     if pegawai['nip_pimpinan'] not None:
    #         if pegawai['nip_pimpinan']['id'] == 2:
    #             list_pegawai = pegawai['nip_pimpinan']
    pegawai = Ms_Pegawai.objects.all()
    kelima = 432000
    list_org_bermasalah = []
    for orang in pegawai:
        telat = Absensi.objects.filter(
           nip__nama = orang.nama,
           tgl__year = 2020, 
        ).values_list('selisih', flat=True)
        
        jml_telat=sum(telat)
        # jml_telat = datetime.timedelta(seconds=jml_telat)
        # jml_telat = jml_telat - datetime.timedelta(microseconds=jml_telat.microseconds)
        print(jml_telat)
        if jml_telat > kelima:
            list_org_bermasalah.append(orang)
    messages.warning(request, "Ada pegawai yang melanggar aturan!")
    print(list_org_bermasalah)

    pimpinan = Ms_Pegawai.objects.get(nip='199510102010121001')
    presensi = Absensi.objects.all()
    tugas_harian = Ms_tugas_harian.objects.all()
    pegawai = Ms_Pegawai.objects.filter(nip_pimpinan__nip='199510102010121001')
    print(list_pegawai)

    return render(request, 'core/home.html', {
        'data_peg': pegawai,
        'presensi': presensi,
        'tugas_harian': tugas_harian,
        'pimpinan': pimpinan,
        'is_caches': is_caches,
        
    })

def save_pegawai(request):
    pegawai = Ms_Pegawai.objects.all()
    id = apitest.id_list
    nip = apitest.nip_list
    nama = apitest.nama_list
    nip_pimpinan = apitest.nip_pimpinan_list
    unit_kerja = apitest.unit_kerja_list
    unor = apitest.unor_list
    pangkat = apitest.pangkat_list
    nm_jabatan = apitest.nm_jabatan_list
    
    hitung_pegawai = Ms_Pegawai.objects.all().count()
    print(len(id), hitung_pegawai)
    count_save = 0

    for i in range(len(id)):
        pegawai_exist = Ms_Pegawai.objects.filter(nip=nip[i]).count()
        if pegawai_exist == 0:
            value = Ms_Pegawai(
                                id = id[i],
                                nip = nip[i],
                                nama = nama[i],
                                unit_kerja = unit_kerja[i],
                                pangkat = pangkat[i],
                                unor = unor[i],
                                nm_jabatan=nm_jabatan[i],
                                # nip_pimpinan = Ms_Pegawai.objects.get(nip=nip_pimpinan[i])
                            )
            value.save()
            msg = '{} Data berhasil disimpan'.format(i+1)
        else:
            msg = 'Tidak ada data baru.'
    
    
    return render(request, 'core/savepeg.html', {'msg': msg})


def tugas(request):
    pegawai = Ms_Pegawai.objects.all()
    kelima = 432000
    list_org_bermasalah = []
    for orang in pegawai:
        telat = Absensi.objects.filter(
           nip__nama = orang.nama,
           tgl__year = 2020, 
        ).values_list('selisih', flat=True)
        
        jml_telat=sum(telat)
        # jml_telat = datetime.timedelta(seconds=jml_telat)
        # jml_telat = jml_telat - datetime.timedelta(microseconds=jml_telat.microseconds)
        print(jml_telat)
        if jml_telat > kelima:
            list_org_bermasalah.append(orang)
    messages.warning(request, "Ada pegawai yang melanggar aturan!")
    print(list_org_bermasalah)
    context = {
       
    }
    return render(request, 'core/tugas.html', context)

def update_task(request, pk):
    if request.method=='POST':
        tgs_harian = Ms_tugas_harian.objects.get(id=pk)
        is_approve = False
        
        print(tgs_harian.id)
        print(request.POST.get('is_approve'))
        if request.POST.get('is_approve') == "true":
            is_approve = True
        else:
            is_approve = False

        new_tugas = Ms_tugas_harian(id=pk,
                                     ket_tugas=request.POST.get('tambah_tugas'),
                                     is_approved=is_approve)
        new_tugas.save(update_fields=['ket_tugas', 'is_approved'])
        messages.success(request, "data disimpan")
    # return redirect(request, )
    
    #penambahan instance untuk dapat melakukan pengisian otomatis pada html
    tgs_harian = Ms_tugas_harian.objects.get(id=pk)
    tugasform = TugasharianForm(instance=tgs_harian)
    return render(request, 'core/update_task.html', {'tugasform':tugasform})
# Create your views here.
## return redirect('/') ini akan mengembalikan nilai ke halaman yang sama


class Tugasharian_list(generics.ListCreateAPIView):
    queryset = Ms_tugas_harian.objects.all()
    serializer_class = TugasHarianSerializer
    schema = AutoSchema(
        tags=['API Tugas Harian'],
        component_name='tgs_harian',
        operation_id_base='tgs_harian',
    )
    
class Tugasharian_Detail(generics.RetrieveUpdateAPIView):
    queryset = Ms_tugas_harian.objects.all()
    serializer_class = TugasHarianSerializer
    schema = AutoSchema(
        tags=['API Tugas Harian Detail'],
        component_name='tgs_harian_dtl',
        operation_id_base='tgs_harian_dtl',
    )
    
# @api_view(['GET', 'POST'])
# def tugasharian_list(request):
#     if request.method == 'GET':
#         tgs_harian = Ms_tugas_harian.objects.all()
#         tgs_serializer = TugasHarianSerializer(tgs_harian, many=True)
#         return Response(tgs_serializer.data)

#     elif request.method == 'POST':
#         tgs_serializer = TugasHarianSerializer(data=request.data)
#         if tgs_serializer.is_valid():
#             tgs_serializer.save()
#             return Response(tgs_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(tgs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Absensi_list(generics.ListCreateAPIView):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer
    name="Daftar Absensi"
    schema = AutoSchema(
        tags=['API Daftar Absensi Pegawai'],
        component_name='absensi_list',
        operation_id_base='absensi_list',
    )

class Absensi_Detail(generics.RetrieveUpdateAPIView):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer
    schema = AutoSchema(
        tags=['API Daftar Absensi Pegawai Detail'],
        component_name='absensi_dtl',
        operation_id_base='absensi_dtl',
    )

def hukuman_list(request):
    hukuman = Hukuman.objects.all()
    return render(request, 'core/hukuman.html', {'hukuman':hukuman})


def buat_hukuman(request):
    data = dict()

    if request.method == 'POST':
        form = HukumanForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            hukuman = Hukuman.objects.all()
            data['html_daftar_hukuman'] = render_to_string('core/partial_daftar_hukuman.html',{
                'hukuman':hukuman,
            })
        else:
            data['form_is_valid'] = False
    else:
        form = HukumanForm()
    
    context = {'form': form}
    data['html_form'] = render_to_string('core/partial_buat_hukuman.html',
        context,
        request=request,
    )
    return JsonResponse(data)