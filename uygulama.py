from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Kullanıcı veritabanınızı temsil etmek için basit bir sözlük
user_database = {
    'kullanici1': 'sifre123',
    'kullanici2': 'parola456',
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in user_database and user_database[username] == password:
        return f"Merhaba, {username}! Başarıyla giriş yaptınız."
    else:
        return "Hatalı kullanıcı adı veya parola. Tekrar deneyin."

if __name__ == '__main__':
    app.run(debug=True)
