import getpass

# Kullanıcı veritabanınızı temsil etmek için basit bir sözlük
user_database = {
    'kullanici1': 'sifre123',
    'kullanici2': 'parola456',
}

def login():
    print("Hoş geldiniz! Lütfen giriş yapın.")

    # Kullanıcı adı ve parola girişi
    username = input("Kullanıcı Adı: ")
    password = getpass.getpass("Parola: ")  # Parolayı gizli şekilde almak için getpass modülünü kullan

    # Veritabanında kullanıcı adı kontrolü
    if username in user_database:
        # Kullanıcı adı doğru, parolayı kontrol et
        if user_database[username] == password:
            print("Başarıyla giriş yaptınız!")
        else:
            print("Hatalı parola! Tekrar deneyin.")
    else:
        print("Hatalı kullanıcı adı! Tekrar deneyin.")

# Giriş fonksiyonunu çağır
login()
