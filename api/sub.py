from http.server import BaseHTTPRequestHandler
import base64
import time

# ===== ТВОИ VLESS ССЫЛКИ =====
VLESS_LINKS = [
    "vless://29fd1aa4-b0a3-4cf6-9df8-071b3eb521be@de6.joybang.site:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=Xh2KakYrLA2ob_ldEk76FbT8PKILpuT3rTJj8wKhizY&security=reality&sid=0880&sni=kion.ru&spx=%2FJK1t2ttc9manJEz&type=tcp#🇩🇪%20Германия%20—%20Premium",
    "vless://c186e71d-630d-480a-82e5-8c5535f47c3d@ee3.joybang.site:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=sPX1OEUYYV3jtT1087zuVu7xmWQJ3O6X2FdYAQeg-3w&security=reality&sid=49bc&sni=kinopoisk.ru&spx=%2FP5Fs6G7WmlPAdwE&type=tcp#🇪🇪%20Эстония%20—%20Premium",
]

# ===== НАЗВАНИЕ ПОДПИСКИ В ПРИЛОЖЕНИИ =====
PROFILE_TITLE = "💎 ArbizzVPN Premium"

# Срок действия (в днях)
EXPIRE_DAYS = 30


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        plain_text = "\n".join(VLESS_LINKS)
        encoded = base64.b64encode(plain_text.encode()).decode()

        expire_timestamp = int(time.time()) + (EXPIRE_DAYS * 86400)
        title_encoded = base64.b64encode(PROFILE_TITLE.encode()).decode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Profile-Title", f"base64:{title_encoded}")
        self.send_header("Profile-Update-Interval", "24")
        self.send_header(
            "Subscription-Userinfo",
            f"upload=0; download=0; total=107374182400; expire={expire_timestamp}"
        )
        self.send_header("Support-URL", "https://t.me/Spprt05Arbz")
        self.end_headers()
        self.wfile.write(encoded.encode())
        return
