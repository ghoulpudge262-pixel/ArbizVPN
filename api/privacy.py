from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Политика конфиденциальности — ArbizzVPN</title>
    <style>
        body { font-family: -apple-system, sans-serif; background: #0f172a; color: white; line-height: 1.8; margin: 0; padding: 40px 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { font-size: 32px; margin-bottom: 20px; }
        h2 { font-size: 22px; margin-top: 30px; margin-bottom: 10px; color: #667eea; }
        p { margin-bottom: 15px; opacity: 0.9; }
        ul { margin-left: 25px; margin-bottom: 15px; }
        li { margin-bottom: 8px; opacity: 0.9; }
        .back { display: inline-block; margin-bottom: 20px; color: #667eea; text-decoration: none; }
        a { color: #667eea; }
        .date { opacity: 0.6; margin-bottom: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="back">← Главная</a>
        <h1>🔒 Политика конфиденциальности</h1>
        <p class="date">Дата обновления: 16 мая 2025 г.</p>

        <h2>1. Какие данные мы собираем</h2>
        <p>Для оказания услуг мы собираем минимально необходимый объём данных:</p>
        <ul>
            <li><strong>Telegram ID</strong> — уникальный идентификатор для авторизации</li>
            <li><strong>Username</strong> — если указан в Telegram</li>
            <li><strong>Имя пользователя</strong> — отображаемое в Telegram</li>
            <li><strong>Информация о платежах</strong> — суммы, даты, статусы (без данных карт)</li>
            <li><strong>UUID подписки</strong> — для технической идентификации</li>
        </ul>

        <h2>2. Какие данные мы НЕ собираем</h2>
        <p>Мы не собираем и не храним:</p>
        <ul>
            <li>❌ Историю посещённых сайтов</li>
            <li>❌ Содержимое вашего интернет-трафика</li>
            <li>❌ Логи подключений</li>
            <li>❌ Личные сообщения</li>
            <li>❌ Пароли от ваших аккаунтов</li>
            <li>❌ Данные платёжных карт (их обрабатывает только LAVA)</li>
            <li>❌ Местоположение пользователя</li>
        </ul>

        <h2>3. Зачем нам нужны эти данные</h2>
        <ul>
            <li>Для создания и активации подписки</li>
            <li>Для технической поддержки клиентов</li>
            <li>Для обработки платежей и возвратов</li>
            <li>Для уведомлений об истечении подписки</li>
        </ul>

        <h2>4. Как мы храним данные</h2>
        <p>4.1. Данные хранятся в защищённой базе данных с ограниченным доступом.</p>
        <p>4.2. Доступ к данным имеют только администраторы сервиса.</p>
        <p>4.3. Данные передаются по защищённым каналам связи (HTTPS, TLS).</p>

        <h2>5. Передача данных третьим лицам</h2>
        <p>5.1. Мы НЕ передаём ваши данные третьим лицам.</p>
        <p>5.2. Исключения:</p>
        <ul>
            <li>Платёжному сервису LAVA для обработки платежей (только сумма и статус)</li>
            <li>По требованию государственных органов в соответствии с законодательством РФ</li>
        </ul>

        <h2>6. Ваши права</h2>
        <p>Вы имеете право:</p>
        <ul>
            <li>Запросить копию ваших данных</li>
            <li>Запросить удаление ваших данных</li>
            <li>Отозвать согласие на обработку данных</li>
        </ul>
        <p>Для реализации этих прав напишите в поддержку: <a href="https://t.me/Spprt05Arbz">@Spprt05Arbz</a></p>

        <h2>7. Cookie и аналитика</h2>
        <p>7.1. Сайт сервиса не использует cookie для отслеживания пользователей.</p>
        <p>7.2. Сервис не использует системы аналитики (Google Analytics, Яндекс.Метрика).</p>

        <h2>8. Изменения политики</h2>
        <p>8.1. Мы можем обновлять Политику конфиденциальности. Дата последнего обновления указана вверху страницы.</p>

        <h2>9. Контакты</h2>
        <p>По вопросам обработки персональных данных:</p>
        <p>💬 Поддержка: <a href="https://t.me/Spprt05Arbz">@Spprt05Arbz</a></p>
        <p>📱 Telegram-бот: <a href="https://t.me/ArbizzVPNbot">@ArbizzVPNbot</a></p>
    </div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())
