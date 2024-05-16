import random


list = ['Was', 'Wo', 'Wann', 'Wie', 'Warum', 'Wer']


while True:
    # Kullanıcıdan kaç adet seçim yapılacağını alıyoruz
    num = int(input("Kaç adet soru seçilecek yazınız: \n" "(Çıkmak için '-1' yazınız) \n"))

    if num == -1:
        print("\nÇıkış yapılıyor...")
        break
    
    elif num<=0:
        print("\nLütfen pozitif bir sayı giriniz")
        print("\n")
        continue

    if num<=len(list):
        # Rastgele seçimleri yapıyoruz
        select = random.choices(list, k=num)

    else:
        select = list[:]
        x_select=random.choices(list, k=num-len(list))
        select.extend(x_select)

    random.shuffle(select)



    # Seçimleri ekrana yazdırıyoruz
    for i, slct in enumerate(select, 1):
        print(f" \n {i}. soru: {slct}")

    print("\n")


