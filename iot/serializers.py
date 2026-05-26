from rest_framework import serializers
from .models import *

class PertanianSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonePertanian
        fields = '__all__'

class PeternakanSerializer(serializers.ModelSerializer):
    class Meta:
        model = KandangSapi
        fields = '__all__'

class PerikananSerializer(serializers.ModelSerializer):
    class Meta:
        model = KolamBioflok
        fields = '__all__'

class PeneranganSerializer(serializers.ModelSerializer):
    class Meta:
        model = LampuJalan
        fields = '__all__'

class IrigasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeranIrigasi
        fields = '__all__'

class CCTVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCTV
        fields = '__all__'

class MesjidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesjid
        fields = '__all__'

class PosRondaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosRonda
        fields = '__all__'        