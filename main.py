import os
import requests


BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = "@IranMarketLive"


def send_test_message():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN پیدا نشد.")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_ID,
        "text": "✅ تست اتصال ربات IranMarketLive با موفقیت انجام شد.",
        "disable_web_page_preview": True,
    }

    response = requests.post(
        url,
        json=payload,
        timeout=20,
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"خطا در Telegram API: "
            f"{response.status_code} - {response.text}"
        )

    print("✅ پیام با موفقیت ارسال شد.")


if __name__ == "__main__":
    send_test_message()
