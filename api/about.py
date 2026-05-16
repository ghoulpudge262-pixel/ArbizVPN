from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>О сервисе — ArbizzVPN</title>
    <style>
        body { font-family: -apple-system, sans-serif; background: #0f172a; color: white; line-height: 1.8; margin: 0; padding: 40px 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { font-size: 36px; margin-bottom: 30px; }
        h2 { font-size: 24px; margin-top: 30px; margin-bottom: 15px; color: #667eea; }
        p { margin-bottom: 15px; opacity: 0.9; }
        ul { margin-left: 25px; margin-bottom: 15px; }
        li { margin-bottom: 8px; opacity: 0.9; }
        .back { display: inline-block; margin-bottom: 20px; color: #667eea; text-decoration: none; }
        a { color: #667eea; }
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="back">← Главная</a>
        <h1>📖 О сервисе ArbizzVPN</h1>

        <h2>Что такое ArbizzVPN?</h2>
        <p>ArbizzVPN — это сервис подписок, предоставляющий доступ к защищённым VPN-серверам в странах Европы. Сервис помогает обеспечить безопасность ваших данных в публичных Wi-Fi сетях и защищает от слежки в интернете.</p>

        <h2>Какую услугу мы оказываем?</h2>
        <p>Мы предоставляем доступ к собственным VPN-серверам по подписочной модели:</p>
        <ul>
            <li>Подписка на 1 месяц — 149 ₽</li>
            <li>Подписка на 3 месяца — 349 ₽</li>
            <li>Подписка на 6 месяцев — 599 ₽</li>
            <li>Подписка на 12 месяцев — 999 ₽</li>
        </ul>

        <h2>Как работает сервис?</h2>
        <ol style="margin-left: 25px;">
            <li style="margin-bottom: 10px;">Клиент оплачивает подписку через Telegram-бот @ArbizzVPNbot</li>
            <li style="margin-bottom: 10px;">В течение 1 минуты клиент получает ссылку на VPN-подписку</li>
            <li style="margin-bottom: 10px;">Клиент устанавливает приложение (Happ, V2Box или другие)</li>
            <li style="margin-bottom: 10px;">Подписка добавляется в приложение по одной кнопке</li>
            <li style="margin-bottom: 10px;">Клиент пользуется VPN весь оплаченный период</li>
        </ol>

        <h2>Зачем нужен VPN?</h2>
        <ul>
            <li><strong>Защита данных в публичных Wi-Fi</strong> — кафе, аэропорты, отели</li>
            <li><strong>Безопасный доступ</strong> к корпоративным ресурсам при удалённой работе</li>
            <li><strong>Доступ к стриминговым сервисам</strong> — Netflix, Spotify и другим</li>
            <li><strong>Защита персональных данных</strong> от слежки</li>
            <li><strong>Стабильное соединение</strong> для видеоконференций</li>
        </ul>

        <h2>Технические характеристики</h2>
        <ul>
            <li>Скорость: до 1 Гбит/с</li>
            <li>Лимит трафика: 100 ГБ в месяц</li>
            <li>Количество серверов: 8 (в разных странах Европы)</li>
            <li>Протокол: VLESS (современный, защищённый)</li>
            <li>Поддерживаемые ОС: iOS, Android, Windows, macOS, Linux</li>
        </ul>

        <h2>Юридическая информация</h2>
        <p>ArbizzVPN — это сервис цифровой подписки. Услуга предоставляется в соответствии с законодательством РФ. Сервис предназначен только для законного использования.</p>

        <h2>Контакты</h2>
        <p>📱 Telegram-бот: <a href="https://t.me/ArbizzVPNbot">@ArbizzVPNbot</a></p>
        <p>💬 Поддержка: <a href="https://t.me/Spprt05Arbz">@Spprt05Arbz</a></p>
    </div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())
