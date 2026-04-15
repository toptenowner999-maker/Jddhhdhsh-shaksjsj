from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    ChatJoinRequestHandler,
    CommandHandler
)
import os
import requests
from io import BytesIO

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APK_URL = os.environ.get("APK_URL")
VIDEO_URL = os.environ.get("VIDEO_URL")
VOICE_URL = os.environ.get("VOICE_URL")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

APK_CACHE = None
USERS = set()

# ================= APK LOAD =================
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
        [InlineKeyboardButton("Register Link", url="https://www.jaiclub25.com/#/register?invitationCode=21223676469")],

        [InlineKeyboardButton("Vip Hack Download", url="https://t.me/MANAGER_ARYAN_BOT?start=vip")],

        [
            InlineKeyboardButton("Gift Code", url="https://t.me/+s7aocEiTgIU4ZDg1"),
            InlineKeyboardButton("Vip Channel", url="https://t.me/+0ogG7zQhrLJhYzJl")
        ],

        [
            InlineKeyboardButton("Admin Contact", url="https://t.me/MANAGER_ARYANN"),
            InlineKeyboardButton("Sureshot Vip", url="https://t.me/MANAGER_ARYANN")
        ],

        [InlineKeyboardButton("💎 Personal Loss Recover", url="https://t.me/MANAGER_ARYANN")],

        [InlineKeyboardButton("Live Chat Support", url="https://t.me/sandeepjaiswal123")]
    ])

# ================= JOIN =================
async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    USERS.add(user.id)

    await context.bot.approve_chat_join_request(
        update.chat_join_request.chat.id, user.id
    )

    # 1. Welcome
    await context.bot.send_message(
        chat_id=user.id,
        text="""✅ I have successfully approved your request to join Bhai ( Jaiwin Games )!

👤 Request To: Aryan

🚀 Click below & get instant access 👇"""
    )

    # 2. Main Video
    if VIDEO_URL:
        await context.bot.send_video(
            chat_id=user.id,
            video=VIDEO_URL,
            caption="""📊 Your Hack is Ready Like a Pro!! ✨

Welcome To Vip Number Panel Bot

Join all channels to get vip panel
https://www.jaiclub25.com/#/register?invitationCode=21223676469

Admin Contact: @MANAGER_ARYANN
Minimum Deposit: ₹300/500
Daily Profit Limit
UpTo ~ ₹50000

Install Tool Now""",
            reply_markup=main_buttons()
        )

    # 3. Voice Message
    if VOICE_URL:
        await context.bot.send_voice(
            chat_id=user.id,
            voice=VOICE_URL
        )

    # 4. APK SEND (UPDATED CAPTION)
    if APK_CACHE:
        file = BytesIO(APK_CACHE)
        file.name = "VIP.apk"

        await context.bot.send_document(
            chat_id=user.id,
            document=file,
            caption="""✓𝗝𝗔𝗜 𝗖𝗟𝗨𝗕 𝗚𝗔𝗠𝗘 𝟮𝟬𝟮𝟲 𝗣𝗥𝗢 𝗛𝗔𝗖𝗞...

✓ 𝗚𝗨𝗥𝗔𝗡𝗧𝗘𝗘𝗗 𝗟𝗢𝗦𝗦 𝗥𝗘𝗖𝗢𝗩𝗘𝗥 𝗕𝗬 𝗔𝗥𝗬𝗔𝗡 𝗫 𝗦𝗨𝗥𝗘𝗦𝗛𝗢𝗧 𝗧𝗢𝗢𝗟>>>

https://t.me/ARYAN_PENEL_SET_UP_HACK
https://t.me/ARYAN_PENEL_SET_UP_HACK"""
        )

# ================= BROADCAST =================
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to message to broadcast")
        return

    msg = update.message.reply_to_message
    sent = 0

    for user_id in USERS:
        try:
            await msg.copy(chat_id=user_id)
            sent += 1
        except:
            pass

    await update.message.reply_text(f"Broadcast sent to {sent} users")

# ================= MAIN =================
def main():
    load_apk()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(join_request))
    app.add_handler(CommandHandler("broadcast", broadcast))

    print("Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
