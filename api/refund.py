from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Политика возврата — ArbizzVPN</title>
    <style>
        body { font-family: -apple-system, sans-serif; background: #0f172a; color: white; line-height: 1.8; margin: 0; padding: 40px 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { font-size: 32px; margin-bottom: 20px; }
        h2 { font-size: 22px; margin-top: 30px; margin-bottom: 10px; color: #667eea; }
        p { margin-bottom: 15px; opacity: 0.9; }
        ol, ul { margin-left: 25px; margin-bottom: 15px; }
        li { margin-bottom: 8px; opacity: 0.9; }
        .back { display: inline-block; margin-bottom: 20px; color: #667eea; text-decoration: none; }
        a { color: #667eea; }
        .date { opacity: 0.6; margin-bottom: 30px; }
        .highlight { background: #1e293b; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 4px solid #667eea; }
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="back">← Главная</a>
        <h1>💰 Политика возврата средств</h1>
        <p class="date">Дата обновления: 16 мая 2025 г.</p>

        <div class="highlight">
            <strong>Кратко:</strong> Возврат возможен в течение 24 часов после оплаты при условии, что услуга не использовалась.
        </div>

        <h2>1. Условия возврата</h2>
        <p>1.1. Возврат денежных средств осуществляется в течение <strong>24 часов</strong> после оплаты подписки.</p>
        <p>1.2. Для возврата подписка не должна быть использована (объём использованного трафика = 0 МБ).</p>
        <p>1.3. После истечения 24 часов или начала использования услуги возврат не производится.</p>

        <h2>2. Как запросить возврат</h2>
        <ol>
            <li>Напишите в поддержку: <a href="https://t.me/Spprt05Arbz">@Spprt05Arbz</a></li>
            <li>Укажите ID платежа (можно посмотреть в Telegram-боте)</li>
            <li>Укажите дату и время оплаты</li>
            <li>Опишите причину возврата</li>
            <li>Дождитесь рассмотрения заявки (до 24 часов)</li>
        </ol>

        <h2>3. Срок зачисления средств</h2>
        <p>3.1. После одобрения заявки возврат производится в течение <strong>3-5 рабочих дней</strong>.</p>
        <p>3.2. Возврат осуществляется тем же способом, что и оплата:</p>
        <ul>
            <li>Оплата картой → возврат на карту</li>
            <li>Оплата через СБП → возврат на счёт</li>
            <li>Оплата криптой → возврат на крипто-кошелёк</li>
        </ul>

        <h2>4. Случаи, когда возврат НЕ производится</h2>
        <ul>
            <li>Истёк срок 24 часа с момента оплаты</li>
            <li>Услуга была использована (трафик более 0 МБ)</li>
            <li>Нарушены правила сервиса (см. <a href="/terms">Соглашение</a>)</li>
            <li>Подписка получена бесплатно (промокоды, бонусы)</li>
        </ul>

        <h2>5. Частичный возврат</h2>
        <p>5.1. Если клиент использовал часть подписки и хочет вернуть остаток — возможен частичный возврат пропорционально неиспользованному времени.</p>
        <p>5.2. Частичный возврат рассматривается индивидуально.</p>

        <h2>6. Спорные ситуации</h2>
        <p>6.1. Если возврат был отклонён, но клиент считает решение несправедливым — можно подать апелляцию через техподдержку.</p>
        <p>6.2. Все спорные ситуации решаются в индивидуальном порядке через @Spprt05Arbz.</p>

        <h2>7. Контакты для возврата</h2>
        <p>💬 Поддержка: <a href="https://t.me/Spprt05Arbz">@Spprt05Arbz</a></p>
        <p>📱 Telegram-бот: <a href="https://t.me/ArbizzVPNbot">@ArbizzVPNbot</a></p>
    </div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())
