from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ArbizzVPN — Безопасный доступ в интернет</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: #0f172a;
            color: white;
            line-height: 1.6;
        }
        nav {
            background: #1e293b;
            padding: 20px 40px;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        nav .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            flex-wrap: wrap;
            gap: 15px;
        }
        nav .logo { font-size: 24px; font-weight: bold; }
        nav .menu { display: flex; gap: 25px; flex-wrap: wrap; }
        nav .menu a {
            color: white;
            text-decoration: none;
            opacity: 0.8;
            transition: opacity 0.2s;
        }
        nav .menu a:hover { opacity: 1; }
        .hero {
            background: linear-gradient(135deg, #667eea, #764ba2);
            padding: 100px 20px;
            text-align: center;
        }
        h1 { font-size: 56px; margin-bottom: 20px; }
        .subtitle { font-size: 22px; opacity: 0.95; margin-bottom: 40px; }
        .btn {
            display: inline-block;
            background: white;
            color: #667eea;
            padding: 18px 50px;
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            font-size: 18px;
            transition: transform 0.2s;
        }
        .btn:hover { transform: scale(1.05); }
        .container { max-width: 1100px; margin: 0 auto; padding: 60px 20px; }
        .section-title { font-size: 36px; text-align: center; margin-bottom: 50px; }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
        }
        .feature {
            background: #1e293b;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
        }
        .feature-icon { font-size: 48px; margin-bottom: 15px; }
        .feature h3 { font-size: 22px; margin-bottom: 10px; }
        .feature p { opacity: 0.8; }
        .pricing {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin-top: 40px;
        }
        .price-card {
            background: #1e293b;
            padding: 35px 25px;
            border-radius: 15px;
            text-align: center;
            border: 2px solid transparent;
            transition: transform 0.2s;
        }
        .price-card:hover { transform: translateY(-5px); }
        .price-card.popular {
            border-color: #667eea;
            transform: scale(1.05);
        }
        .price-card h3 { font-size: 24px; margin-bottom: 15px; }
        .price { font-size: 48px; font-weight: bold; color: #667eea; margin: 15px 0; }
        .price small { font-size: 18px; opacity: 0.7; }
        .period { opacity: 0.8; margin-bottom: 20px; }
        footer {
            background: #1e293b;
            padding: 40px 20px;
            text-align: center;
            margin-top: 60px;
        }
        footer .links {
            display: flex;
            justify-content: center;
            gap: 25px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        footer a {
            color: #667eea;
            text-decoration: none;
        }
        footer .copyright { opacity: 0.6; margin-top: 15px; }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <div class="logo">🎉 ArbizzVPN</div>
            <div class="menu">
                <a href="/">Главная</a>
                <a href="/about">О сервисе</a>
                <a href="/terms">Соглашение</a>
                <a href="/refund">Возврат</a>
                <a href="/privacy">Конфиденциальность</a>
                <a href="/contacts">Контакты</a>
            </div>
        </div>
    </nav>

    <section class="hero">
        <h1>🎉 ArbizzVPN</h1>
        <p class="subtitle">Безопасный и быстрый доступ в интернет<br>через защищённые VPN-серверы в Европе</p>
        <a href="https://t.me/ArbizzVPNbot" class="btn">📱 Купить подписку</a>
    </section>

    <div class="container">
        <h2 class="section-title">🌟 Возможности сервиса</h2>
        <div class="features">
            <div class="feature">
                <div class="feature-icon">🌍</div>
                <h3>8 стран Европы</h3>
                <p>Германия, Нидерланды, Швейцария, Швеция, Финляндия, Эстония, Латвия и другие</p>
            </div>
            <div class="feature">
                <div class="feature-icon">⚡️</div>
                <h3>Высокая скорость</h3>
                <p>До 1 Гбит/с на каждом сервере. Подходит для видеоконференций и стриминга</p>
            </div>
            <div class="feature">
                <div class="feature-icon">🔒</div>
                <h3>Защита данных</h3>
                <p>Современный протокол VLESS обеспечивает безопасность ваших данных</p>
            </div>
            <div class="feature">
                <div class="feature-icon">📱</div>
                <h3>Все устройства</h3>
                <p>iPhone, Android, Windows, macOS — одна подписка для всех ваших устройств</p>
            </div>
            <div class="feature">
                <div class="feature-icon">📊</div>
                <h3>100 ГБ трафика</h3>
                <p>Достаточно для активного использования весь месяц</p>
            </div>
            <div class="feature">
                <div class="feature-icon">💬</div>
                <h3>Поддержка 24/7</h3>
                <p>Быстрая помощь в Telegram-чате с любыми вопросами</p>
            </div>
        </div>

        <h2 class="section-title" style="margin-top: 80px;">💎 Тарифы</h2>
        <div class="pricing">
            <div class="price-card">
                <h3>1 месяц</h3>
                <div class="price">149<small>₽</small></div>
                <p class="period">Подписка на 30 дней</p>
                <a href="https://t.me/ArbizzVPNbot" class="btn" style="background: #667eea; color: white;">Купить</a>
            </div>
            <div class="price-card popular">
                <h3>⭐️ 3 месяца</h3>
                <div class="price">349<small>₽</small></div>
                <p class="period">Подписка на 90 дней</p>
                <a href="https://t.me/ArbizzVPNbot" class="btn" style="background: #667eea; color: white;">Купить</a>
            </div>
            <div class="price-card">
                <h3>6 месяцев</h3>
                <div class="price">599<small>₽</small></div>
                <p class="period">Подписка на 180 дней</p>
                <a href="https://t.me/ArbizzVPNbot" class="btn" style="background: #667eea; color: white;">Купить</a>
            </div>
            <div class="price-card">
                <h3>1 год</h3>
                <div class="price">999<small>₽</small></div>
                <p class="period">Подписка на 365 дней</p>
                <a href="https://t.me/ArbizzVPNbot" class="btn" style="background: #667eea; color: white;">Купить</a>
            </div>
        </div>
    </div>

    <footer>
        <div class="links">
            <a href="/about">О сервисе</a>
            <a href="/terms">Соглашение</a>
            <a href="/refund">Возврат</a>
            <a href="/privacy">Конфиденциальность</a>
            <a href="/contacts">Контакты</a>
        </div>
        <p>📱 Telegram-бот: <a href="https://t.me/ArbizzVPNbot">@ArbizzVPNbot</a></p>
        <p>💬 Поддержка: <a href="https://t.me/Spprt05Arbz">@Spprt05Arbz</a></p>
        <p class="copyright">© 2025 ArbizzVPN. Все права защищены.</p>
    </footer>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())
