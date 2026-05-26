from django.core.management.base import BaseCommand
from iot.models import ZonePertanian, KandangSapi, KolamBioflok, LampuJalan, KeranIrigasi, CCTV, Mesjid, PosRonda   

class Command(BaseCommand):
    help = 'Mengisi database dengan data dummy awal untuk dashboard IoT Smart Village'

    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        # Hapus data lama agar tidak duplikat saat dijalankan ulang
        ZonePertanian.objects.all().delete()
        KandangSapi.objects.all().delete()
        KolamBioflok.objects.all().delete()
        LampuJalan.objects.all().delete()
        KeranIrigasi.objects.all().delete()
        CCTV.objects.all().delete()

        self.stdout.write("Memasukkan data baru...")

        # ==========================================
        # 1. DATA PERIKANAN BIOFLOK (FOCUS)
        # ==========================================
        perikanan_data = [
            {'pond_id':'KB-01', 'name':'Kolam Bioflok 1', 'ph':7.2, 'do_level':5.8, 'temp':28.5, 'ammonia':0.3, 'biofloc_status':'Baik', 'aerator_on':True},
            {'pond_id':'KB-02', 'name':'Kolam Bioflok 2', 'ph':6.9, 'do_level':4.2, 'temp':29.1, 'ammonia':0.8, 'biofloc_status':'Sedang', 'aerator_on':True},
            {'pond_id':'KB-03', 'name':'Kolam Pembesaran', 'ph':7.5, 'do_level':6.1, 'temp':27.8, 'ammonia':0.1, 'biofloc_status':'Baik', 'aerator_on':False},
            {'pond_id':'KB-04', 'name':'Kolam Pembenihan', 'ph':6.8, 'do_level':3.9, 'temp':30.2, 'ammonia':1.1, 'biofloc_status':'Buruk', 'aerator_on':True},
        ]
        for data in perikanan_data:
            KolamBioflok.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(perikanan_data)} data Perikanan berhasil ditambahkan!'))

        # ==========================================
        # 2. DATA PERTANIAN
        # ==========================================
        pertanian_data = [
            {'zone_id':'PA-01', 'name':'Zona A — Sawah Utara', 'moisture':78, 'temp':27.3, 'ph':6.5, 'npk_status':'Normal', 'irrig_on':False},
            {'zone_id':'PA-02', 'name':'Zona B — Sawah Selatan', 'moisture':65, 'temp':28.1, 'ph':6.8, 'npk_status':'Rendah N', 'irrig_on':True},
            {'zone_id':'PA-03', 'name':'Zona C — Ladang Timur', 'moisture':82, 'temp':26.8, 'ph':6.2, 'npk_status':'Normal', 'irrig_on':False},
            {'zone_id':'PA-04', 'name':'Zona D — Kebun Barat', 'moisture':54, 'temp':29.2, 'ph':7.1, 'npk_status':'Rendah P', 'irrig_on':True},
        ]
        for data in pertanian_data:
            ZonePertanian.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(pertanian_data)} data Pertanian berhasil ditambahkan!'))

        # ==========================================
        # 3. DATA PETERNAKAN
        # ==========================================
        peternakan_data = [
            {'pen_id':'KS-01', 'name':'Kandang A', 'population':48, 'healthy':45, 'sick':2, 'temp':28.5, 'ammonia':12},
            {'pen_id':'KS-02', 'name':'Kandang B', 'population':52, 'healthy':50, 'sick':1, 'temp':27.8, 'ammonia':8},
            {'pen_id':'KS-03', 'name':'Kandang C', 'population':42, 'healthy':40, 'sick':1, 'temp':29.1, 'ammonia':15},
        ]
        for data in peternakan_data:
            KandangSapi.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(peternakan_data)} data Peternakan berhasil ditambahkan!'))

        # ==========================================
        # 4. DATA PENERANGAN
        # ==========================================
        penerangan_data = [
            {'light_id':'LJ-01', 'location':'Jalan Utama 1', 'is_on':True, 'brightness':80, 'watt':30, 'is_fault':False},
            {'light_id':'LJ-02', 'location':'Jalan Utama 2', 'is_on':True, 'brightness':80, 'watt':30, 'is_fault':False},
            {'light_id':'LJ-03', 'location':'Jalan Utama 3', 'is_on':False, 'brightness':0, 'watt':30, 'is_fault':True},
            {'light_id':'LJ-04', 'location':'Pasar Desa', 'is_on':True, 'brightness':100, 'watt':50, 'is_fault':False},
            {'light_id':'LJ-05', 'location':'Lapangan Desa', 'is_on':True, 'brightness':60, 'watt':40, 'is_fault':False},
            {'light_id':'LJ-06', 'location':'Jalan Gang 1', 'is_on':True, 'brightness':70, 'watt':20, 'is_fault':False},
            {'light_id':'LJ-07', 'location':'Jalan Gang 2', 'is_on':True, 'brightness':70, 'watt':20, 'is_fault':False},
            {'light_id':'LJ-08', 'location':'Area Masjid', 'is_on':True, 'brightness':90, 'watt':40, 'is_fault':False},
            {'light_id':'LJ-09', 'location':'Jalan Sawah', 'is_on':False, 'brightness':0, 'watt':20, 'is_fault':False},
            {'light_id':'LJ-10', 'location':'Puskesmas', 'is_on':True, 'brightness':100, 'watt':50, 'is_fault':False},
        ]
        for data in penerangan_data:
            LampuJalan.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(penerangan_data)} data Penerangan berhasil ditambahkan!'))

        # ==========================================
        # 5. DATA IRIGASI
        # ==========================================
        irigasi_data = [
            {'valve_id':'KI-01', 'location':'Pintu Air Sawah Utara', 'is_open':True, 'flow_rate':45.2, 'pressure':2.1},
            {'valve_id':'KI-02', 'location':'Pintu Air Sawah Selatan', 'is_open':True, 'flow_rate':38.7, 'pressure':1.8},
            {'valve_id':'KI-03', 'location':'Saluran Ladang Timur', 'is_open':False, 'flow_rate':0, 'pressure':0},
            {'valve_id':'KI-04', 'location':'Saluran Kebun Barat', 'is_open':True, 'flow_rate':22.1, 'pressure':1.2},
            {'valve_id':'KI-05', 'location':'Pintu Air Cadangan', 'is_open':False, 'flow_rate':0, 'pressure':0.5},
            {'valve_id':'KI-06', 'location':'Saluran Drainase', 'is_open':True, 'flow_rate':15.6, 'pressure':0.8},
            {'valve_id':'KI-07', 'location':'Keran Kolam Bioflok', 'is_open':True, 'flow_rate':12.3, 'pressure':1.5},
            {'valve_id':'KI-08', 'location':'Keran Kebun Desa', 'is_open':False, 'flow_rate':0, 'pressure':0.3},
        ]
        for data in irigasi_data:
            KeranIrigasi.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(irigasi_data)} data Irigasi berhasil ditambahkan!'))

        # ==========================================
        # 6. DATA CCTV
        # ==========================================
        cctv_data = [
            {'cam_id':'CAM-01', 'location':'Gapura Desa', 'is_online':True, 'is_recording':True},
            {'cam_id':'CAM-02', 'location':'Pasar Desa', 'is_online':True, 'is_recording':True},
            {'cam_id':'CAM-03', 'location':'Lapangan Desa', 'is_online':True, 'is_recording':True},
            {'cam_id':'CAM-04', 'location':'Kantor Desa', 'is_online':True, 'is_recording':True},
            {'cam_id':'CAM-05', 'location':'Puskesmas', 'is_online':True, 'is_recording':True},
            {'cam_id':'CAM-06', 'location':'Jalan Utara', 'is_online':True, 'is_recording':True},
            {'cam_id':'CAM-07', 'location':'Area Kandang', 'is_online':True, 'is_recording':True},
            {'cam_id':'CAM-08', 'location':'Simpang Selatan', 'is_online':False, 'is_recording':False},
        ]
        for data in cctv_data:
            CCTV.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(cctv_data)} data CCTV berhasil ditambahkan!'))

        self.stdout.write(self.style.SUCCESS('\n🚀 SEMUA DATA DUMMY BERHASIL DIISI KE DATABASE!'))


        # ==========================================
        # 7. DATA MESJID / MUSHOLA
        # ==========================================
        mesjid_data = [
            {'mesjid_id':'MJ-01', 'name':'Mesjid Al-Ikhlas', 'is_speaker_on':False, 'is_ac_on':False, 'temp':28.5, 'power_usage':120},
            {'mesjid_id':'MJ-02', 'name':'Mushola Al-Falah', 'is_speaker_on':False, 'is_ac_on':True, 'temp':26.1, 'power_usage':350},
            {'mesjid_id':'MJ-03', 'name':'Mesjid Jami Nurul Imam', 'is_speaker_on':True, 'is_ac_on':True, 'temp':25.3, 'power_usage':850},
            {'mesjid_id':'MJ-04', 'name':'Mushola At-Taqwa', 'is_speaker_on':False, 'is_ac_on':False, 'temp':29.0, 'power_usage':15},
            {'mesjid_id':'MJ-05', 'name':'Mushola Baitul Makmur', 'is_speaker_on':False, 'is_ac_on':False, 'temp':27.8, 'power_usage':10},
        ]

        for data in mesjid_data:
            Mesjid.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(mesjid_data)} data Mesjid berhasil ditambahkan!'))

        # ==========================================
        # 8. DATA POS RONDA
        # ==========================================
        posronda_data = [
            {'pos_id':'PR-01', 'name':'Pos Ronda 1 - RT 01', 'is_online':True, 'is_sorot_on':False, 'is_alarm_active':False, 'last_patrol':'23:00'},
            {'pos_id':'PR-02', 'name':'Pos Ronda 2 - RT 02', 'is_online':True, 'is_sorot_on':True, 'is_alarm_active':False, 'last_patrol':'01:30'},
            {'pos_id':'PR-03', 'name':'Pos Ronda 3 - RT 03', 'is_online':True, 'is_sorot_on':False, 'is_alarm_active':False, 'last_patrol':'22:45'},
            {'pos_id':'PR-04', 'name':'Pos Ronda 4 - RT 04', 'is_online':False, 'is_sorot_on':False, 'is_alarm_active':False, 'last_patrol':'-'},
            {'pos_id':'PR-05', 'name':'Pos Ronda 5 - RT 05', 'is_online':True, 'is_sorot_on':False, 'is_alarm_active':True, 'last_patrol':'02:15'},
        ]
        for data in posronda_data:
            PosRonda.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'✅ {len(posronda_data)} data Pos Ronda berhasil ditambahkan!'))