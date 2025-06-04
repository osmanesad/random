from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sayısal Loto Tahmini</title>
</head>
<body>
    <h2>Sayısal Loto Tahmini</h2>
    <form method="post">
        <button type="submit">Tahmin Üret</button>
    </form>
    {% if numbers %}
        <h3>Ana Numaralar: {{ numbers|join(', ') }}</h3>
        <h3>Joker (SuperStar): {{ joker }}</h3>
    {% endif %}
</body>
</html>
"""

def generate_lottery_numbers():
    main_numbers = random.sample(range(1, 91), 6)
    main_numbers.sort()
    while True:
        joker = random.randint(1, 90)
        if joker not in main_numbers:
            break
    return main_numbers, joker

@app.route('/', methods=['GET', 'POST'])
def index():
    numbers, joker = None, None
    if request.method == 'POST':
        numbers, joker = generate_lottery_numbers()
    return render_template_string(HTML_PAGE, numbers=numbers, joker=joker)

def run_console():
    print("Sayısal Loto Tahmin Uygulaması (Konsol)")
    while True:
        input("Yeni tahmin için Enter'a basın...")
        numbers, joker = generate_lottery_numbers()
        print(f"Ana Numaralar: {numbers}")
        print(f"Joker (SuperStar): {joker}\n")

def main():
    mode = input("Uygulama nasıl çalışsın? (1: Konsol, 2: Web) Seçiminiz: ")
    if mode == '1':
        run_console()
    elif mode == '2':
        print("Web arayüzü başlatılıyor... http://127.0.0.1:5000 adresine gidin.")
        app.run(debug=False)
    else:
        print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
