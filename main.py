from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    ChatJoinRequestHandler
)
import os
import requests
from io import BytesIO

BOT_TOKEN = os.environ.get("BOT_TOKEN")
VOICE_URL = os.environ.get("VOICE_URL")

# 🔥 VIDEO (NO CAPTION)
VIDEO_URL = "https://raw.githubusercontent.com/toptenowner999-maker/Jddhhdhsh-shaksjsj/cfa3e77fb4dfd4d8fb76f9442cb291b529507672/VID_20260415_165231_028.mp4"

# 🔥 APK
APK_URL = "https://raw.githubusercontent.com/toptenowner999-maker/Jddhhdhsh-shaksjsj/f1cc6c9d44c256dbbf0ff266269afd32cf387196/ARYAN%20X%20SURESHOT%20PENEL_.apk"

APK_CACHE = None

# ================= LOAD APK =================
def load_apk():
    global APK_CACHE
    try:
        r = requests.get(APK_URL)
        APK_CACHE = r.content
        print("APK Loaded")
    except:
        print("APK load failed")

# ================= BUTTONS =================
def main_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("REGISTRATION LINK 🔗", url="https://www.jaiclub25.com/#/register?invitationCode=21223676469")],

        [InlineKeyboardButton("VIP HACK DOWNLOAD 📩", url="https://t.me/MANAGER_ARYAN_BOT?start=vip")],

        [
            InlineKeyboardButton("GIFT CODE 🎁", url="https://t.me/+s7aocEiTgIU4ZDg1"),
            InlineKeyboardButton("HACK PROOF 🖇️", url="https://t.me/ARYAN_PENEL_SET_UP_HACK")
        ],

        [
            InlineKeyboardButton("ADMIN CONTACT ❤️", url="https://t.me/MANAGER_ARYANN"),
            InlineKeyboardButton("SURESHOT VIP 🎯", url="https://t.me/MANAGER_ARYANN")
        ],

        [InlineKeyboardButton("PERSONAL LOSS RECOVERY 💎", url="https://t.me/m/Xg7IhuhdZWM1")],

        [InlineKeyboardButton("LIVE CHAT SUPPORT 🎧", url="https://t.me/sandeepjaiswal123")]
    ])

# ================= JOIN =================
async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    await context.bot.approve_chat_join_request(
        update.chat_join_request.chat.id, user.id
    )

    # 1. WELCOME MSG
    await context.bot.send_message(
        chat_id=user.id,
        text="""✅ I have successfully approved your request to join Bhai ( Jaiwin Games )!

👤 Request To: Aryan

🚀 Click below & get instant access 👇"""
    )

    # 2. VIDEO (NO CAPTION + BUTTONS)
    await context.bot.send_video(
        chat_id=user.id,
        video=VIDEO_URL,
        reply_markup=main_buttons()
    )

    # 3. APK
    if APK_CACHE:
        file = BytesIO(APK_CACHE)
        file.name = "ARYAN X SURESHOT PENEL.apk"

        await context.bot.send_document(
            chat_id=user.id,
            document=file,
            filename="ARYAN X SURESHOT PENEL.apk",
            caption="""✓𝗝𝗔𝗜 𝗖𝗟𝗨𝗕 𝗚𝗔𝗠𝗘 𝟮𝟬𝟮𝟲 𝗣𝗥𝗢 𝗛𝗔𝗖𝗞...

✓ 𝗚𝗨𝗥𝗔𝗡𝗧𝗘𝗘𝗗 𝗟𝗢𝗦𝗦 𝗥𝗘𝗖𝗢𝗩𝗘𝗥 𝗕𝗬 𝗔𝗥𝗬𝗔𝗡 𝗫 𝗦𝗨𝗥𝗘𝗦𝗛𝗢𝗧 𝗧𝗢𝗢𝗟>>>

https://t.me/ARYAN_PENEL_SET_UP_HACK
https://t.me/ARYAN_PENEL_SET_UP_HACK"""
        )

    # 4. VOICE MESSAGE (LAST)
    if VOICE_URL:
        await context.bot.send_voice(
            chat_id=user.id,
            voice=VOICE_URL
        )

# ================= MAIN =================
def main():
    load_apk()

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(join_request))

    print("Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
