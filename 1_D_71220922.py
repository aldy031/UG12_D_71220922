uangdimiliki = int(input("Masukkan jumlah uang : RP"))

ketik = input("ketik Start untuk memulai : ")
ketik = ketik.upper()

while ketik == "START" and uangdimiliki != 0:
    benda = input("Apa barang yang akan anda beli?")
    if benda == "susu":
        sisauangsusu = uangdimiliki - 20000
        if uangdimiliki >= 20000:
            print("Sisa uang anda ",sisauangsusu)
        else: 
            print("Uang tidak cukup")
        uangdimiliki = sisauangsusu
        
    elif benda == "permen":
        sisauangpermen = uangdimiliki - 500
        if uangdimiliki >= 500:
            print("Sisa uang anda ",sisauangpermen)
        else: 
            print("Uang tidak cukup")
        uangdimiliki = sisauangpermen
        
    elif benda == "roti":
        sisauangroti = uangdimiliki - 15000
        if uangdimiliki >= 15000:
            print("Sisa uang anda ",sisauangroti)
        else: 
            print("Uang tidak cukup")
        uangdimiliki = sisauangroti
        
    elif benda == "indomie":
        sisauangmie = uangdimiliki - 3000
        if uangdimiliki >= 3000:
            print("Sisa uang anda ",sisauangmie)
        else: 
            print("Uang tidak cukup")
        uangdimiliki = sisauangmie
        
    elif benda == "vitamin":
        sisauangvita = uangdimiliki - 50000
        if uangdimiliki >= 50000:
            print("Sisa uang anda ",sisauangvita)
        else: 
            print("Uang tidak cukup")
        uangdimiliki = sisauangvita
    
    elif benda == "SUDAH":
        print(exit())
        
    else:
        print("Barang tidak tersedia")