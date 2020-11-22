from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save_peg/', views.save_pegawai, name='save_peg'),
    path('tugas/', views.tugas, name='tugas'),
    path('update_task/<int:pk>/', views.update_task, name='update_task'),
    path('api/absensi/<int:pk>/tugas_harian/', views.Tugasharian_list.as_view(), name="tugas_harian"),
    path('api/absensi/', views.Absensi_list.as_view(), name="absensi"),
    path('hukuman/', views.hukuman_list, name='hukuman'),
    path('hukuman/buat/', views.buat_hukuman, name="buat-hukuman"),
]
