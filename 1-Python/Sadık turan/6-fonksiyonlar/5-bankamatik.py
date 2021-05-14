# -*- coding: utf-8 -*

murat_hesap = {
    "ad":"murat aykurt",
    "hesap_no":"12344411",
    "bakiye":4000,
    "ek_hesap":2000
    }


selin_hesap = {
    "ad":"selin aykurt",
    "hesap_no":"42344411",
    "bakiye":6000,
    "ek_hesap":3000
    }

def para_cek(hesap,miktar):
    print(f"merhaba {hesap['ad']}")
    
    if hesap["bakiye"] >= miktar :
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz")
        bakiye_sorgu(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ek_hesap"]
        
        if (toplam >= miktar):
            ek_hesap_kullanimi = input("ek hesap kullanılsın mı (e/h) : ").lower()
            
            if ek_hesap_kullanimi == "e":
                
                ek_hesaptan_kullanim = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ek_hesap"] -= ek_hesaptan_kullanim
                
                print("ek hesap ile beraber paranızı cekebilirsiniz")
                bakiye_sorgu(hesap)

            else:
                print(f"{hesap['hesap_no']} nolu hesapta {hesap['bakiye']} bulunmaktadır")
        else:
            print("üzgünüz bakiyeniz yetersiz")
            bakiye_sorgu(hesap)


def  bakiye_sorgu(hesap):
    print(f"{hesap['hesap_no']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz {hesap['ek_hesap']} TL dir")
    

para_cek(murat_hesap, 3000)
print("******************")
