from django.urls import path
from .views import *

urlpatterns = [
    path('pertanian/', PertanianListCreate.as_view()),
    path('pertanian/<str:zone_id>/', PertanianDetailUpdate.as_view()),
    
    path('peternakan/', PeternakanListCreate.as_view()),
    path('peternakan/<str:pen_id>/', PeternakanDetailUpdate.as_view()),
    
    path('perikanan/', PerikananListCreate.as_view()),
    path('perikanan/<str:pond_id>/', PerikananDetailUpdate.as_view()),
    
    path('penerangan/', PeneranganListCreate.as_view()),
    path('penerangan/<str:light_id>/', PeneranganDetailUpdate.as_view()),
    
    path('irigasi/', IrigasiListCreate.as_view()),
    path('irigasi/<str:valve_id>/', IrigasiDetailUpdate.as_view()),
    
    path('cctv/', CCTVListCreate.as_view()),

    # Mesjid
    path('mesjid/', MesjidListCreate.as_view(), name='mesjid-list'),
    path('mesjid/<str:mesjid_id>/', MesjidDetailUpdate.as_view(), name='mesjid-detail'),
    
    # Pos Ronda
    path('posronda/', PosRondaListCreate.as_view(), name='posronda-list'),
    path('posronda/<str:pos_id>/', PosRondaDetailUpdate.as_view(), name='posronda-detail'),
]