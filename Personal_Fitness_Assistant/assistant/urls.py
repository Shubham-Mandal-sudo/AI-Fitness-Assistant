from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:assessment_id>/', views.result, name='result'),
    path('download-pdf/<int:assessment_id>/', views.download_pdf, name='download_pdf'),
]