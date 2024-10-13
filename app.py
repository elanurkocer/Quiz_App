from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Oturum yönetimi için gizli anahtar

# Quiz verileri
quiz_data = [
    {
    "question": "Soru 1: Robotların çevresini algılamak için en çok hangi sensör kullanılır?",
    "options": ["Ultrasonik Sensör", "Ses Sensörü", "Işık Sensörü"],
    "answer": "Ultrasonik Sensör"  # Doğru cevap
},
{
    "question": "Soru 2: Hangi programlama dili robotik uygulamalarda en yaygın olarak kullanılır?",
    "options": ["Python", "Java", "HTML"],
    "answer": "Python"  # Doğru cevap
},
{
    "question": "Soru 3: Arduino ile robot yapmak için hangi bileşen gereklidir?",
    "options": ["Mikrodenetleyici", "LCD Ekran", "Ses Kartı"],
    "answer": "Mikrodenetleyici"  # Doğru cevap
},
{
    "question": "Soru 4: Hangi yazılım, robotların simülasyonunu yapmak için en sık kullanılır?",
    "options": ["MATLAB", "Blender", "Robotics Toolbox"],
    "answer": "Robotics Toolbox"  # Doğru cevap
},
{
    "question": "Soru 5: Robotların çevresini algılaması için hangi tür yazılım algoritması yaygın olarak kullanılır?",
    "options": ["Makine Öğrenimi", "HTML", "CSS"],
    "answer": "Makine Öğrenimi"  # Doğru cevap
},
{
    "question": "Soru 6: Hangi robotik uygulama, otonom araçlarda kullanılır?",
    "options": ["Görsel Algılama", "Veri Girişi", "Dijital Tasarım"],
    "answer": "Görsel Algılama"  # Doğru cevap
},
{
    "question": "Soru 7: Robotik sistemlerde motor kontrolü için hangi protokol sıklıkla kullanılır?",
    "options": ["I2C", "HTTP", "FTP"],
    "answer": "I2C"  # Doğru cevap
},
{
    "question": "Soru 8: Robotların doğru hareket etmesi için hangi tür yazılımlar kullanılır?",
    "options": ["Gömülü Yazılım", "Veritabanı Yönetim Yazılımı", "Web Geliştirme Yazılımı"],
    "answer": "Gömülü Yazılım"  # Doğru cevap
},
{
    "question": "Soru 9: Robotik projelerde hangi tür motor genellikle tercih edilir?",
    "options": ["Stepper Motor", "DC Motor", "AC Motor"],
    "answer": "Stepper Motor"  # Doğru cevap
},
{
    "question": "Soru 10: Robotik sistemlerde veri iletişimi için en yaygın kullanılan iletişim protokolü hangisidir?",
    "options": ["Bluetooth", "SMTP", "TCP/IP"],
    "answer": "TCP/IP"  # Doğru cevap
}

    
    
]

@app.route('/')
def index():
    # İlk sorudan başlamak için oturumu sıfırla
    session['current_question'] = 0
    session['score'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    current_question = session.get('current_question', 0)
    
    if request.method == 'POST':
        # Kullanıcının cevapladığı soruyu al
        user_answer = request.form.get('answer')
        
        # Cevap doğruysa skoru artır
        if user_answer == quiz_data[current_question]['answer']:
            session['score'] += 1
        
        # Sonraki soruya geç
        current_question += 1
        session['current_question'] = current_question
        
        # Tüm sorular bittiğinde sonucu göster
        if current_question >= len(quiz_data):
            return redirect(url_for('result'))

    # Şu anki soruyu görüntüle
    question_data = quiz_data[current_question]
    return render_template('quiz.html', question_data=question_data, question_number=current_question + 1)

@app.route('/result')
def result():
    score = session.get('score', 0)
    total_questions = len(quiz_data)
    return render_template('result.html', score=score, total_questions=total_questions)

if __name__ == '__main__':
    app.run(debug=True)
