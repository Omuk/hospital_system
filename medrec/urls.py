from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('doc_reg/', views.doc_reg, name='docreg'),
    path('coder_reg/', views.coder_reg, name='coderreg'),
    path('pat_reg/', views.pat_reg, name='patreg'),
    path('doc_login/', views.doc_login, name='doclogin'),
    path('coder_login/', views.coder_login, name='coderlogin'),
    path('pat_rec/', views.pat_rec, name='patrec'),
    path('user_logout/', views.user_logout, name='logout'),
    path('patsearch/', views.patient_search, name='patsearch'),
]