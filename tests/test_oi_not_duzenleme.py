# -*-  coding: utf-8 -*-
# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

from zengine.lib.test_utils import BaseTestCase
from ulakbus.models import User, OgrenciProgram, OgrenciDersi, Sinav


class TestCase(BaseTestCase):
    """
    Bu sınıf ``BaseTestCase`` extend edilerek hazırlanmıştır.

    """

    def test_oi_not_duzenleme(self):
        """
        Öğrenci işleri not düzenleme iş akışının ilk adımında fakülte karar no girilir.

        İkinci adımında ise öğrencinin kayıtlı oluduğu program seçilir.
        Veritabanından çekilen öğrenciye ait programların sayısı ile sunucudan dönen öğrenci
        programlarının sayısı karşılaştırılır.

        Üçünçü adımında ise öğrenci dersi eçilir.
        Sunucudan dönen ders sayısı ile veritabanından çekilen ders sayısı
        karşılaştırılıp test edilir.

        Dördüncü adımında ise derse ait sınav seçilir.
        Sunucudan dönen sınav sayısı ile veritabanından çekilen sınav sayısı karşılaştırılıp
        test edilir.

        Son adımda ise seçilen sınavın notu düzenlenir.
        Sunucudan dönen cevapta 'puan' field'ının olup olmadığını test eder.

        """
        
        # Veritabanından öğrenci işleri personeli seçilir.
        usr = User.objects.get(username='imran')

        # Öğrenci işleri not düzenleme iş akışı başlatılır.
        self.prepare_client('/ogrenci_isleri_not_duzenleme', user=usr)
        self.client.post(param='ogrenci_id',
                         id="T8PMMytvrHwhlRnQpBq8B5eB7Ut",
                         filters={'ogrenci_id': {'values': ["T8PMMytvrHwhlRnQpBq8B5eB7Ut"], 'type': "check"}})

        # Fakülte karar no'su girilir.
        resp = self.client.post(form={'karar': "4353", 'kaydet': 1})

        # Veritabanından öğrencinin kayıtlı olduğu programlar çekilir.
        op = OgrenciProgram.objects.filter(ogrenci_id="T8PMMytvrHwhlRnQpBq8B5eB7Ut")
        # Sunucudan dönen program sayısı ile veritabanından çekilen program sayısı
        # karşılaştırılıp test edilir.
        assert len(op) == len(resp.json['forms']['form'][1]['titleMap'])

        # Program seçilir.
        resp = self.client.post(form={'onayla': 1, 'program': "ZOQpL23OsEUWqUuslPD8CFNp74j"})

        # Veritabanından öğrencinin kayıtlı olduğu programa ait olan dersler seçilir.
        ogrenci_dersi = OgrenciDersi.objects.filter(ogrenci_program_id="ZOQpL23OsEUWqUuslPD8CFNp74j")
        # Sunucudan dönen ders sayısı ile veritabanından çekilen ders sayısı
        # karşılaştırılıp test edilir.
        assert len(ogrenci_dersi) == len(resp.json['forms']['form'][1]['titleMap'])

        # Ders seçilir.
        resp = self.client.post(form={'onayla': 1, 'ders': "3QSRTg42S9LtnUtbwbTwom7vyD"})
        # Seçilen öğrenci dersi.
        ders = OgrenciDersi.objects.get('3QSRTg42S9LtnUtbwbTwom7vyD')

        # Şubeye kayıtlı olan sınavlar
        sinav = Sinav.objects.filter(sube_id=ders.ders.key)
        # Sunucudan dönen sınav sayısı ile veritabanından çekilen sınav sayısı karşılaştırılıp
        # test edilir.
        assert len(sinav) == len(resp.json['forms']['form'][1]['titleMap'])

        # Sınav seçilir.
        resp = self.client.post(form={'sinav':"RoFKPHZNuvXcgOUtxuwEKxHgj95", 'onayla': 1})

        # Sunucudam dönen cevapta 'puan' field'nın olup olmadığını test eder.
        assert 'puan' in resp.json['forms']['model']




