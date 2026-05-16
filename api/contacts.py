from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Контакты — ArbizzVPN</title>
    <style>
        body { font-family: -apple-system, sans-serif; background: #0f172a; color: white; line-height: 1.8; margin: 0; padding: 40px 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { font-size: 32px; margin-bottom: 20px; }
        h2 { font-size: 22px; margin-top: 30px; margin-bottom: 10px; color: #667eea; }
        p { margin-bottom: 15px; opacity: 0.9; }
        .back { display: inline-block; margin-bottom: 20px; color: #667eea; text-decoration: none; }
        a { color: #667eea; }
        .contact-card { background: #1e293b; padding: 25px; border-radius: 15px; margin: 20px 0; }
        .contact-card h3 { font-size: 20px; margin-bottom: 10px; }
        .seller-info { background: #1e293b; padding: 25px; border-radius: 15px; margin-top: 40px; border-left: 4px solid #667eea; }
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="back">← Главная</a>
        <h1>💬 Контакты</h1>

        <div class="contact-card">
            <h3>📱 Telegram-бот</h3>
            <p>Главный канал общения с сервисом — наш Telegram-бот.</p>
            <p>В боте можно: купить подписку, посмотреть свои подписки, получить инструкцию.</p>
            <p>🔗 <a href="https://t.me/ArbizzVPNbot">@ArbizzVPNbot</a></p>
        </div>

        <div class="contact-card">
            <h3>💬 Техническая поддержка</h3>
            <p>По всем вопросам:</p>
            <ul style="margin-left: 25px;">
                <li>Проблемы с подключением</li>
                <li>Возврат средств</li>
                <li>Технические сбои</li>
                <li>Вопросы по тарифам</li>
            </ul>
            <p>🔗 <a href="https://t.me/Spprt05Arbz">@Spprt05Arbz</a></p>
            <p>⏰ Время работы: 24/7</p>
            <p>⌚ Среднее время ответа: 1-3 часа</p>
        </div>

        <div class="contact-card">
            <h3>📧 Email</h3>
            <p>Для серьёзных вопросов и предложений:</p>
            <p>📨 <a href="mailto:support@arbizzvpn.com">support@arbizzvpn.com</a></p>
        </div>

        <div class="seller-info">
            <h2 style="margin-top: 0;">📋 Информация о продавце</h2>
            <p><strong>Сервис:</strong> ArbizzVPN</p>
            <p><strong>Деятельность:</strong> Предоставление VPN-подписок</p>
            <p><strong>Способ работы:</strong> Самозанятый / Физическое лицо</p>
            <p><strong>Регион:</strong> Российская Федерация</p>
            <p><strong>Способ связи:</strong> Telegram</p>
        </div>

        <div class="contact-card" style="margin-top: 30px;">
            <h3>📜 Документы</h3>
            <p>• <a href="/terms">Пользовательское соглашение</a></p>
            <p>• <a href="/refund">Политика возврата</a></p>
            <p>• <a href="/privacy">Политика конфиденциальности</a></p>
            <p>• <a href="/about">О сервисе</a></p>
        </div>
    </div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())
