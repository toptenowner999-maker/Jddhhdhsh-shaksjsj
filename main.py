from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler
import os
import requests
from io import BytesIO

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APK_URL = os.environ.get("APK_URL")
VIDEO_URL = os.environ.get("VIDEO_URL")      # main video
VIDEO2_URL = os.environ.get("VIDEO2_URL")    # second video

APK_CACHE = None

# ================= APK LOAD =================
def load_apk():
    global APK_CACHE
    try:
        r = requests.get(APK_URL)
        APK_CACHE = r.content
        print("✅ APK Loaded")
    except:
        print("❌ APK load failed")

# ================= BUTTONS =================
def main_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📩 GET VIP APK", url="https://t.me/MANAGER_ARYAN_BOT?start=vip")],
        [
            InlineKeyboardButton("📸 PROOF CHANNEL", url="https://t.me/ARYAN_PENEL_SET_UP_HACK"),
            InlineKeyboardButton("👑 VIP CHANNEL", url="https://t.me/+0ogG7zQhrLJhYzJl")
        ],
        [
            InlineKeyboardButton("🎁 GIFT CODE", url="https://t.me/+s7aocEiTgIU4ZDg1"),
            InlineKeyboardButton("📝 REGISTRATION", url="https://www.jaiclub25.com/#/register?invitationCode=21223676469")
        ],
        [
            InlineKeyboardButton("🧿 CONTACT ADMIN", url="https://t.me/MANAGER_ARYANN"),
            InlineKeyboardButton("🚨 LIVE SUPPORT", url="https://t.me/sandeepjaiswal123")
        ],
        [
            InlineKeyboardButton("🎉 PERSONAL RECOVERY", url="https://t.me/MANAGER_ARYANN")
        ]
    ])

# ✅ Second video button (FINAL)
def second_video_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Message", url="https://t.me/MANAGER_ARYANN")]
    ])

# ================= JOIN =================
async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = update.chat_join_request.chat.id

    try:
        await context.bot.approve_chat_join_request(chat_id, user.id)

        # ✅ 1. Welcome
        await context.bot.send_message(
            chat_id=user.id,
            text="""✅ I have successfully approved your request to join Bhai ( Jaiwin Games )!

👤 Request To: 𝘼𝙍𝙔𝘼𝙉

🚀 Click below & get instant access 👇"""
        )

        # ✅ 2. MAIN VIDEO + BUTTONS
        if VIDEO_URL:
            await context.bot.send_video(
                chat_id=user.id,
                video=VIDEO_URL,
                caption="""📊 Your Hack is Ready Like a Pro!! ✨

🛑 Welcome To Vip Number Panel Bot 🔷

🚨 Join All Channels To Get Vip Number Panel 🔓
https://www.jaiclub25.com/#/register?invitationCode=21223676469

ADMIN CONTACT:- @MANAGER_ARYANN
➕Minimum Deposit -₹300/500₹
🟢 Daily Profit Limit
📈 UpTo ~ ₹50000

🛑 JAI CLUB TOOL INSTALL NOW 🛑""",
                reply_markup=main_buttons()
            )

        # ✅ 3. SECOND VIDEO + MESSAGE BUTTON (NO CAPTION)
        if VIDEO2_URL:
            await context.bot.send_video(
                chat_id=user.id,
                video=VIDEO2_URL,
                reply_markup=second_video_button()
            )

        # ✅ 4. APK SEND
        if APK_CACHE:
            file = BytesIO(APK_CACHE)
            file.name = "VIP.apk"

            await context.bot.send_document(
                chat_id=user.id,
                document=file,
                filename="VIP.apk",
                caption="""✔️ JAI CLUB GAME 2026 PRO ➡️HACK ⚡️

💯 GURANTEED LOSS RECOVER BY ARYAN X SURESHOT TOOL 💯 ➕Minimum Deposit -₹300/500₹
🟢 Daily Profit Limit
📈 UpTo ~ ₹50000

🛑 JAI CLUB TOOL INSTALL NOW 🛑"""
            )

    except Exception as e:
        print(e)

# ================= MAIN =================
def main():
    load_apk()

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(join_request))

    print("🚀 Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
