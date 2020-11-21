from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save_peg/', views.save_pegawai, name='save_peg'),
    path('tugas/', views.tugas, name='tugas'),
    path('update_task/<int:pk>/', views.update_task, name='update_task'),
    path('api/tugas_harian/', views.Tugasharian_list.as_view(), name="tugas_harian")
]
