soru = input("Anlamadığınız bir kelime yazın: ").upper()

meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap :)",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }
if soru in meme_dict.keys():
    print(meme_dict[soru])
else:
    print("Ne dediğini anlayamadım. Lütfen yeniden dene.")
