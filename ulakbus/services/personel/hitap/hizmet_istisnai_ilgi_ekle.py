# -*-  coding: utf-8 -*-

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

"""HITAP Istisnai Ilgi Ekle

Hitap'a personelin Istisnai Ilgi bilgilerinin eklemesini yapar.

"""

from ulakbus.services.personel.hitap.hitap_ekle import HITAPEkle
from ulakbus.models.hitap.hitap import HizmetIstisnaiIlgi


class HizmetIstisnaiIlgiEkle(HITAPEkle):
    """
    HITAP Ekleme servisinden kalıtılmış Hizmet Istisnai Bilgi Ekleme servisi

    """
    HAS_CHANNEL = True
    service_dict = {
        'service_name': 'hizmetIstisnaiIlgiInsert',
        'service_mapper': 'ns1:HizmetIstisnaiIlgiServisBean',
        'model': HizmetIstisnaiIlgi,
        'fields': {
            'kayitNo': 'kayit_no',
            'tckn': 'tckn',
            'istisnaiIlgiNevi': 'istisnai_ilgi_nevi',
            'baslamaTarihi': 'baslama_tarihi',
            'bitisTarihi': 'bitis_tarihi',
            'gunSayisi': 'gun_sayisi',
            'khaDurum': 'kha_durum',
            'kurumOnayTarihi': 'kurum_onay_tarihi'
        },
        'date_filter': ['baslama_tarihi', 'bitis_tarihi', 'kurum_onay_tarihi'],
        'long_to_string': ['kayit_no'],
        'required_fields': ['tckn', 'istisnaiIlgiNevi', 'baslamaTarihi',
                            'bitisTarihi', 'gunSayisi', 'khaDurum', 'kurumOnayTarihi']
    }
