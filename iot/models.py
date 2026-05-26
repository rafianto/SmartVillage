from django.db import models

class ZonePertanian(models.Model):
    zone_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    moisture = models.FloatField(default=0)
    temp = models.FloatField(default=0)
    ph = models.FloatField(default=0)
    npk_status = models.CharField(max_length=50, default='Normal')
    irrig_on = models.BooleanField(default=False)

    def __str__(self): return f"{self.zone_id} - {self.name}"

class KandangSapi(models.Model):
    pen_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    population = models.IntegerField(default=0)
    healthy = models.IntegerField(default=0)
    sick = models.IntegerField(default=0)
    temp = models.FloatField(default=0)
    ammonia = models.FloatField(default=0)

    def __str__(self): return f"{self.pen_id} - {self.name}"

class KolamBioflok(models.Model):
    pond_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    ph = models.FloatField(default=7.0)
    do_level = models.FloatField(default=5.0)
    temp = models.FloatField(default=28.0)
    ammonia = models.FloatField(default=0.1)
    biofloc_status = models.CharField(max_length=20, default='Baik')
    aerator_on = models.BooleanField(default=True)

    def __str__(self): return f"{self.pond_id} - {self.name}"

class LampuJalan(models.Model):
    light_id = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100)
    is_on = models.BooleanField(default=False)
    brightness = models.IntegerField(default=0)
    watt = models.IntegerField(default=30)
    is_fault = models.BooleanField(default=False)

    def __str__(self): return f"{self.light_id} - {self.location}"

class KeranIrigasi(models.Model):
    valve_id = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100)
    is_open = models.BooleanField(default=False)
    flow_rate = models.FloatField(default=0)
    pressure = models.FloatField(default=0)
    def __str__(self): return f"{self.valve_id} - {self.location}"

class CCTV(models.Model):
    cam_id = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100)
    is_online = models.BooleanField(default=True)
    is_recording = models.BooleanField(default=True)
    stream_url = models.URLField(max_length=300, blank=True, null=True) # TAMBAHAN INI

    def __str__(self): return f"{self.cam_id} - {self.location}"

# class CCTV(models.Model):
#     cam_id = models.CharField(max_length=10, unique=True)
#     location = models.CharField(max_length=100)
#     is_online = models.BooleanField(default=True)
#     is_recording = models.BooleanField(default=True)
#     def __str__(self): return f"{self.cam_id} - {self.location}"

class Mesjid(models.Model):
    mesjid_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    is_speaker_on = models.BooleanField(default=False) # Pengeras suara
    is_ac_on = models.BooleanField(default=False)      # AC / Kipas Angin
    temp = models.FloatField(default=28.0)              # Suhu dalam mesjid
    power_usage = models.FloatField(default=0)          # Konsumsi listrik (Watt)

    def __str__(self): return f"{self.mesjid_id} - {self.name}"

class PosRonda(models.Model):
    pos_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    is_online = models.BooleanField(default=True)       # Status koneksi pos
    is_sorot_on = models.BooleanField(default=False)    # Lampu sorot halaman
    is_alarm_active = models.BooleanField(default=False)# Tombol alarm darurat
    last_patrol = models.CharField(max_length=20, default='-') # Jam patroli terakhir

    def __str__(self): return f"{self.pos_id} - {self.name}"