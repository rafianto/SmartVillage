from rest_framework import generics
from .models import *
from .serializers import *

# GET semua data, POST data baru
class PertanianListCreate(generics.ListCreateAPIView):
    queryset = ZonePertanian.objects.all()
    serializer_class = PertanianSerializer

# GET detail, PUT/PATCH update (untuk toggle kontrol)
class PertanianDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = ZonePertanian.objects.all()
    serializer_class = PertanianSerializer
    lookup_field = 'zone_id'

class PeternakanListCreate(generics.ListCreateAPIView):
    queryset = KandangSapi.objects.all()
    serializer_class = PeternakanSerializer

class PeternakanDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = KandangSapi.objects.all()
    serializer_class = PeternakanSerializer
    lookup_field = 'pen_id'

class PerikananListCreate(generics.ListCreateAPIView):
    queryset = KolamBioflok.objects.all()
    serializer_class = PerikananSerializer

class PerikananDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = KolamBioflok.objects.all()
    serializer_class = PerikananSerializer
    lookup_field = 'pond_id'

class PeneranganListCreate(generics.ListCreateAPIView):
    queryset = LampuJalan.objects.all()
    serializer_class = PeneranganSerializer

class PeneranganDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = LampuJalan.objects.all()
    serializer_class = PeneranganSerializer
    lookup_field = 'light_id'

class IrigasiListCreate(generics.ListCreateAPIView):
    queryset = KeranIrigasi.objects.all()
    serializer_class = IrigasiSerializer

class IrigasiDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = KeranIrigasi.objects.all()
    serializer_class = IrigasiSerializer
    lookup_field = 'valve_id'

class CCTVListCreate(generics.ListCreateAPIView):
    queryset = CCTV.objects.all()
    serializer_class = CCTVSerializer

class MesjidListCreate(generics.ListCreateAPIView):
    queryset = Mesjid.objects.all()
    serializer_class = MesjidSerializer

class MesjidDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Mesjid.objects.all()
    serializer_class = MesjidSerializer
    lookup_field = 'mesjid_id'

class PosRondaListCreate(generics.ListCreateAPIView):
    queryset = PosRonda.objects.all()
    serializer_class = PosRondaSerializer

class PosRondaDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = PosRonda.objects.all()
    serializer_class = PosRondaSerializer
    lookup_field = 'pos_id'    