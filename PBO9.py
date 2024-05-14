# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:39:40 2024

@author: ocanh
"""
import math

class Perhitungan:
    @staticmethod
    def hitung_volume(bentuk, *parameter):
        if bentuk == "kubus":
            sisi = parameter[0]
            return sisi ** 3
        elif bentuk == "balok":
            panjang, lebar, tinggi = parameter
            return panjang * lebar * tinggi
        elif bentuk == "tabung":
            jari_jari, tinggi = parameter
            return math.pi * jari_jari ** 2 * tinggi
        else:
            raise ValueError("Bentuk bangun ruang tidak valid")

perhitungan = Perhitungan()
hasil_kubus = perhitungan.hitung_volume("kubus", 5)
hasil_balok = perhitungan.hitung_volume("balok", 4, 3, 6)
hasil_tabung = perhitungan.hitung_volume("tabung", 2, 8)

print("Volume Kubus:", hasil_kubus, "cm^3")
print("Volume Balok:", hasil_balok, "cm^3")
print("Volume Tabung:", hasil_tabung, "cm^3")

