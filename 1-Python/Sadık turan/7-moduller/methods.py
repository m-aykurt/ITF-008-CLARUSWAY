# -*- coding: utf-8 -*-

import db

def urun_ekle(urun_adi,fiyat):
    db.urunler.append({
        "id":len(db.urunler)+1,
        "urun_adi":urun_adi,
        "fiyat":fiyat
        })
    

def urun_guncelle(id,urun_adi,fiyat):
    for urun in db.urunler:
        if (urun["id"]==id):
            urun["urun_adi"] = urun_adi
            urun["fiyat"] = fiyat
            break
        
def urunleri_getir():
    for urun in db.urunler:
        print(f"id: {urun['id']} urun adi : {urun['urun_adi']} fiyat: {urun['fiyat']}  ")
        