try:
    filtre = "Tüm Dosyalar (*);;Metin Dosyaları (*.txt);;Python Dosyaları (*.py)"
    dosya_adlari, _ = QFileDialog.getOpenFileNames(None, "Dosya Seç", "", filtre)

    for dosya_adi in dosya_adlari:
        print(f"Seçilen Dosya : {dosya_adi}")

except Exception as ex:
    print(f"Message Errror : {ex}")