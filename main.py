from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler, CallbackQueryHandler
import os
import requests
from io import BytesIO

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APK_URL = os.environ.get("APK_URL")
VIDEO_URL = os.environ.get("VIDEO_URL")
VIDEO_NOTE_URL = os.environ.get("VIDEO_NOTE_URL")

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
def video_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 𝗚𝗘𝗧 𝗩𝗜𝗣 𝗔𝗣𝗞 ✅❤️", callback_data="apk")],
        [InlineKeyboardButton("📸 𝗣𝗥𝗢𝗢𝗙 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/ARYAN_PENEL_SET_UP_HACK")],
        [InlineKeyboardButton("👑 𝗩𝗜𝗣 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/+0ogG7zQhrLJhYzJl")],
        [InlineKeyboardButton("🎁 𝗚𝗜𝗙𝗧 𝗖𝗢𝗗𝗘", url="https://t.me/+s7aocEiTgIU4ZDg1")],
        [InlineKeyboardButton("📝 𝗥𝗘𝗚𝗜𝗦𝗧𝗥𝗔𝗧𝗜𝗢𝗡 🔗", url="https://www.jaiclub25.com/#/register?invitationCode=21223676469")],
        [InlineKeyboardButton("🧿 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗔𝗗𝗠𝗜𝗡", url="https://t.me/MANAGER_ARYANN?text=HELLO%20ARYAN%20BHAI%20MUJHE%20LOSS%20RECOVER%20KRWANA%20HAI")],
        [InlineKeyboardButton("🚨 𝗟𝗜𝗩𝗘 𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/sandeepjaiswal123")],
        [InlineKeyboardButton("🎉 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 𝗥𝗘𝗖𝗢𝗩𝗘𝗥𝗬", url="https://t.me/MANAGER_ARYANN")]
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

        # ✅ 2. Video + Buttons (UPDATED CAPTION)
        if VIDEO_URL:
            await context.bot.send_video(
                chat_id=user.id,
                video=VIDEO_URL,
                caption=" 📊 Your Hack is Ready Like a Pro!! ✨"

🛑 Welcome To Vip Number Panel Bot 🔷

🚨 Join All Channels To Get Vip Number Panel 🔓
 https://www.jaiclub25.com/#/register?invitationCode=21223676469

ADMIN CONTACT:- @MANAGER_ARYANN",
                reply_markup=video_buttons()
            )

        # ✅ 3. Round Video
        if VIDEO_NOTE_URL:
            await context.bot.send_video_note(
                chat_id=user.id,
                video_note=VIDEO_NOTE_URL
            )

        # ✅ 4. APK AUTO SEND
        if APK_CACHE:
            file = BytesIO(APK_CACHE)
            file.name = "VIP.APK"

            await context.bot.send_document(
                chat_id=user.id,
                document=file,
                filename="VIP.APK",
                caption="""📥 VIP APK READY ✅

✔️ JAI CLUB GAME 2026 PRO ➡️HACK ⚡️

💯 GURANTEED LOSS RECOVER BY ARYAN X SURESHOT TOOL  💯

➕Minimum Deposit -₹300/500₹
🟢 Daily Profit Limit
📈 UpTo ~ ₹50000

🛑 JAI CLUB TOOL INSTALL NOW 🛑"""
            )

    except Exception as e:
        print(e)

# ================= BUTTON CLICK =================
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "apk":
        if APK_CACHE:
            file = BytesIO(APK_CACHE)
            file.name = "VIP.APK"

            await context.bot.send_document(
                chat_id=query.from_user.id,
                document=file,
                filename="VIP.APK",
                caption="📥 ✔️ JAI CLUB GAME 2026 PRO ➡️HACK ⚡️

💯 GURANTEED LOSS RECOVER BY ARYAN X SURESHOT TOOL  💯

➕Minimum Deposit -₹300/500₹
🟢 Daily Profit Limit
📈 UpTo ~ ₹50000

🛑 JAI CLUB TOOL INSTALL NOW 🛑"
            )
        else:
            await query.message.reply_text("❌ APK not available")

# ================= MAIN =================
def main():
    load_apk()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(join_request))
    app.add_handler(CallbackQueryHandler(button_click))

    print("🚀 Bot Running...")
    app.run_polling()

if name == "main":
    main()
