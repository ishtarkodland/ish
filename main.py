meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "Tanggapan terhadap lelucon",
            "SHEESH" : "Sedikit ketidaksetujuan",
            "CREEPY" : "Menakutkan,tidak menyenangkan",
            "AGGRO" : "Untuk menjadi agresif/marah"
            }
word = input("Ketik kata yang tidak Kamu mengerti (GUNAKAN HURUF BESAR SEMUA!): ")
if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("kata tidak di temukan silahkan coba lagi")
