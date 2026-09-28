import keep_alive
keep_alive.keep_alive()
import os
import json
import time
import telebot
from telebot import types

BOT_TOKEN = "8765918360:AAH7xZQX_polc8Tk-ugJwBsda7MTX34ZKQ8"
ADMIN_ID = 8886164132
DEV_ID = 8886164132

CHANNELS = ["@xtramods", "@ffhacks_off"]
CHANNEL_LINKS = [
    ("⚡ Join XtraMods", "https://t.me/xtramods"),
    ("🔥 Join FF Hacks", "https://t.me/ffhacks_off")
]

DB_FILE = "bot_database.json"

DEFAULT_DATA = {
    "users": [],
    "user_lang": {},
    "accepted_terms": [],
    "links": {
        "proofs": "https://t.me/xtramods",
        "admin_dm": "https://t.me/xtramods",
        "limited_bot": "https://t.me/SpamBot",
        "dev_dm": "https://t.me/xtramods"
    },
    "free_files": [],
    "paid_items": {
        "xreg": {
            "title": "⚡ X-REG VIP PANEL",
            "desc": "🎯 High Accuracy Recoil Reducer\n🛡️ Safe For Main IDs\n⚡ 100% Anti-Blacklist",
            "price": "₹299 / 7 Days\n₹599 / 30 Days\n₹1299 / Lifetime",
            "media_id": None,
            "media_type": None
        },
        "aimhack": {
            "title": "🎯 AUTO AIM & TRACKING",
            "desc": "🔥 Instant Bullet Track\n🏹 360° Silent Aim\n⚡ Stream Proof Support",
            "price": "₹399 / 7 Days\n₹799 / 30 Days\n₹1599 / Lifetime",
            "media_id": None,
            "media_type": None
        },
        "troll": {
            "title": "🎭 TROLL & GHOST MODS",
            "desc": "👻 Ghost Invisible Walk\n🚀 Super Speed Run\n💣 Instant Kill Tricks",
            "price": "₹199 / 7 Days\n₹499 / 30 Days\n₹999 / Lifetime",
            "media_id": None,
            "media_type": None
        }
    }
}

STRINGS = {
    "hi": {
        "force_join_text": "⚠️ <b>Access Denied!</b>\n\nIs bot ko use karne ke liye pehle niche diye gaye dono official channels join karein:",
        "btn_verify": "✅ Maine Dono Channels Join Kar Liye",
        "verify_success": "✅ Verification Successful!",
        "verify_fail": "❌ Aapne dono channels join nahi kiye hain! Pehle join karein.",
        "terms_text": (
            "📜 <b>Terms & Conditions / Rules</b>\n\n"
            "1. Yahan provide kiye gaye files aur mods strictly educational/testing ke liye hain.\n"
            "2. Reselling ya leaks strictly prohibited hain.\n"
            "3. Any abusive behavior admin ke sath direct ban lead karega.\n\n"
            "<i>Kya aap in sharton ko accept karte hain?</i>"
        ),
        "btn_accept": "✅ Accept Terms",
        "btn_decline": "❌ Decline",
        "terms_declined": "⛔ Aapne terms decline kar diye hain. Dobara shuru karne ke liye /start karein.",
        "main_menu_title": (
            "👑 <b>— XtraMods VIP Hub —</b> 👑\n\n"
            "👋 <b>Hello, {name}!</b>\n"
            "⚡ <i>Fastest APK Modding & VIP Access Center.</i>\n\n"
            "📦 <b>Status:</b> Active\n"
            "🛡️ <b>Protection:</b> 100% Anti-Ban Verified\n\n"
            "<i>Niche diye gaye options me se select karein:</i>"
        ),
        "btn_free": "🎁 ╸Free Section ╸🎁",
        "btn_paid": "💎 Paid Section",
        "btn_proofs": "🟢 Feedback & Proofs ↗",
        "btn_contact_admin": "👤 Direct Admin ↗",
        "btn_limited_bot": "🤖 DM If Limited ↗",
        "btn_own_bot": "🚀 Make Your Own Bot ↗",
        "btn_back_shop": "🔴 Back to Shop",
        "free_empty": "📂 <b>Free Section</b>\n\nAbhi koi free file upload nahi hai. Stay tuned!",
        "free_title": "🎁 <b>Free Mods & Tools List:</b>\nDownload karne ke liye tap karein:",
        "paid_title": "💎 <b>VIP Paid Hacks & Tools</b>\n\nPreview aur price dekhne ke liye select karein:",
        "buy_now": "💳 Buy Now (Direct Admin) ↗",
        "back_paid": "🔴 Back to Paid Section",
        "own_bot_text": (
            "🤖 <b>Make Your Own Premium Telegram Bot!</b> 🚀\n\n"
            "✨ <b>Bot Highlights:</b>\n"
            "• 🌐 3-Language System (Hindi, English, Russian)\n"
            "• 🔒 Dual Force Join Protection\n"
            "• 📜 Terms & Acceptance Gate\n"
            "• 💥 Vaporize Animation Auto-Deletions\n"
            "• ⚙️ Complete In-Chat Admin Panel\n"
            "• 🎁 Auto-Deliver Free & Paid Tools\n\n"
            "Apna bot order karne ke liye developer ko message karein:"
        )
    },
    "en": {
        "force_join_text": "⚠️ <b>Access Denied!</b>\n\nTo access this bot, please join both official channels below:",
        "btn_verify": "✅ I Have Joined Both Channels",
        "verify_success": "✅ Verification Successful!",
        "verify_fail": "❌ You haven't joined both channels yet! Please join first.",
        "terms_text": (
            "📜 <b>Terms & Conditions / Rules</b>\n\n"
            "1. All files and mods provided are strictly for educational and testing use.\n"
            "2. Reselling, distributing, or unauthorized leaks are strictly prohibited.\n"
            "3. Any toxic or abusive behavior will result in an instant ban.\n\n"
            "<i>Do you accept these terms?</i>"
        ),
        "btn_accept": "✅ Accept Terms",
        "btn_decline": "❌ Decline",
        "terms_declined": "⛔ You have declined the terms. Send /start to begin again.",
        "main_menu_title": (
            "👑 <b>— XtraMods VIP Hub —</b> 👑\n\n"
            "👋 <b>Hello, {name}!</b>\n"
            "⚡ <i>Fastest APK Modding & VIP Access Center.</i>\n\n"
            "📦 <b>Status:</b> Active\n"
            "🛡️ <b>Protection:</b> 100% Anti-Ban Verified\n\n"
            "<i>Please select an option below:</i>"
        ),
        "btn_free": "🎁 ╸Free Section ╸🎁",
        "btn_paid": "💎 Paid Section",
        "btn_proofs": "🟢 Feedback & Proofs ↗",
        "btn_contact_admin": "👤 Direct Admin ↗",
        "btn_limited_bot": "🤖 DM If Limited ↗",
        "btn_own_bot": "🚀 Make Your Own Bot ↗",
        "btn_back_shop": "🔴 Back to Shop",
        "free_empty": "📂 <b>Free Section</b>\n\nNo free files available right now. Check back later!",
        "free_title": "🎁 <b>Free Mods & Tools:</b>\nClick any button below to download:",
        "paid_title": "💎 <b>VIP Paid Hacks & Tools</b>\n\nSelect a product to view video showcase and pricing:",
        "buy_now": "💳 Buy Now (Direct Admin) ↗",
        "back_paid": "🔴 Back to Paid Section",
        "own_bot_text": (
            "🤖 <b>Get Your Own Custom Telegram Bot!</b> 🚀\n\n"
            "✨ <b>Bot Highlights:</b>\n"
            "• 🌐 Multi-Language Support (English, Hindi, Russian)\n"
            "• 🔒 Dual Force Join Channel Gate\n"
            "• 📜 Terms of Service Verification\n"
            "• 💥 Vaporize Deletion & Loading Animations\n"
            "• ⚙️ Full In-Bot Control Panel (No Coding)\n"
            "• 🎁 Auto-Deliver Free & VIP Content\n\n"
            "Contact our bot developer directly to purchase:"
        )
    },
    "ru": {
        "force_join_text": "⚠️ <b>Доступ ограничен!</b>\n\nЧтобы использовать бота, подпишитесь на оба официальных канала ниже:",
        "btn_verify": "✅ Я подписался на оба канала",
        "verify_success": "✅ Проверка успешно пройдена!",
        "verify_fail": "❌ Вы еще не подписались на оба канала! Сделайте это.",
        "terms_text": (
            "📜 <b>Правила и Условия</b>\n\n"
            "1. Все предоставленные файлы предназначены исключительно для ознакомления.\n"
            "2. Перепродажа и распространение строго запрещены.\n"
            "3. Оскорбления и спам ведут к мгновенной блокировке.\n\n"
            "<i>Вы принимаете эти условия?</i>"
        ),
        "btn_accept": "✅ Принять условия",
        "btn_decline": "❌ Отклонить",
        "terms_declined": "⛔ Вы отклонили условия. Отправьте /start, чтобы попробовать снова.",
        "main_menu_title": (
            "👑 <b>— XtraMods VIP Hub —</b> 👑\n\n"
            "👋 <b>Привет, {name}!</b>\n"
            "⚡ <i>Центр модификаций APK и VIP-доступа.</i>\n\n"
            "📦 <b>Статус:</b> Активен\n"
            "🛡️ <b>Защита:</b> 100% Anti-Ban Verified\n\n"
            "<i>Выберите нужный раздел ниже:</i>"
        ),
        "btn_free": "🎁 ╸Бесплатный раздел ╸🎁",
        "btn_paid": "💎 Платный раздел",
        "btn_proofs": "🟢 Отзывы и гарантии ↗",
        "btn_contact_admin": "👤 Связь с админом ↗",
        "btn_limited_bot": "🤖 Написать при спам-блоке ↗",
        "btn_own_bot": "🚀 Заказать такого же бота ↗",
        "btn_back_shop": "🔴 Назад в меню",
        "free_empty": "📂 <b>Бесплатный раздел</b>\n\nНа данный момент файлов нет. Следите за обновлениями!",
        "free_title": "🎁 <b>Список бесплатных файлов:</b>\nНажмите для скачивания:",
        "paid_title": "💎 <b>VIP Платные Моды</b>\n\nВыберите категорию для просмотра видео и цен:",
        "buy_now": "💳 Купить (Связь с админом) ↗",
        "back_paid": "🔴 Назад к платным",
        "own_bot_text": (
            "🤖 <b>Закажите своего VIP Telegram-бота!</b> 🚀\n\n"
            "✨ <b>Возможности бота:</b>\n"
            "• 🌐 Поддержка языков (Hindi, English, Russian)\n"
            "• 🔒 Двойная обязательная подписка на каналы\n"
            "• 📜 Соглашение с правилами\n"
            "• 💥 Анимации растворения сообщений\n"
            "• ⚙️ Полная панель администратора прямо в боте\n"
            "• 🎁 Автоматическая раздача бесплатных и VIP файлов\n\n"
            "Для заказа напишите разработчику:"
        )
    }
}

def load_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump(DEFAULT_DATA, f, indent=4)
        return DEFAULT_DATA
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_DATA

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

db = load_db()
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
admin_states = {}

def get_text(uid, key, **kwargs):
    lang = db.get("user_lang", {}).get(str(uid), "hi")
    template = STRINGS.get(lang, STRINGS["hi"]).get(key, "")
    return template.format(**kwargs)

def vaporize_delete(chat_id, message_id):
    fade_frames = [
        "░░░░░ ɢʟɪᴛᴄʜɪɴɢ... ░░░░░",
        "▒▒▒▒▒ ᴠᴀᴘᴏʀɪᴢɪɴɢ... ▒▒▒▒▒",
        "▓▓▓▓▓ ᴅᴇʟᴇᴛɪɴɢ... ▓▓▓▓▓",
        "💥 [ᴠᴀᴘᴏʀɪᴢᴇᴅ]"
    ]
    for frame in fade_frames:
        try:
            bot.edit_message_text(frame, chat_id, message_id)
            time.sleep(0.2)
        except Exception:
            pass
    try:
        bot.delete_message(chat_id, message_id)
    except Exception:
        pass

def show_loading(chat_id, text_prefix="Loading"):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    msg = bot.send_message(chat_id, f"⚡ {text_prefix} {frames[0]}")
    for f in frames[1:4]:
        time.sleep(0.2)
        try:
            bot.edit_message_text(f"⚡ {text_prefix} {f}", chat_id, msg.message_id)
        except Exception:
            pass
    return msg.message_id

def check_user_joined(user_id):
    for ch in CHANNELS:
        try:
            member = bot.get_chat_member(ch, user_id)
            if member.status in ['left', 'kicked']:
                return False
        except Exception:
            return False
    return True

def get_lang_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🇮🇳 Hindi (Hinglish)", callback_data="lang_hi"),
        types.InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        types.InlineKeyboardButton("🇷🇺 Russian", callback_data="lang_ru")
    )
    return markup

def get_join_keyboard(uid):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for title, link in CHANNEL_LINKS:
        markup.add(types.InlineKeyboardButton(f"{title} ↗", url=link))
    markup.add(types.InlineKeyboardButton(get_text(uid, "btn_verify"), callback_data="verify_join"))
    return markup

def get_terms_keyboard(uid):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(get_text(uid, "btn_accept"), callback_data="accept_terms"),
        types.InlineKeyboardButton(get_text(uid, "btn_decline"), callback_data="decline_terms")
    )
    return markup

def get_main_dashboard(uid):
    markup = types.InlineKeyboardMarkup(row_width=2)
    b_free = types.InlineKeyboardButton(get_text(uid, "btn_free"), callback_data="sec_free")
    markup.add(b_free)
    
    b_paid = types.InlineKeyboardButton(get_text(uid, "btn_paid"), callback_data="sec_paid")
    b_proof = types.InlineKeyboardButton(get_text(uid, "btn_proofs"), url=db["links"]["proofs"])
    markup.add(b_paid, b_proof)
    
    b_adm = types.InlineKeyboardButton(get_text(uid, "btn_contact_admin"), url=db["links"]["admin_dm"])
    b_lim = types.InlineKeyboardButton(get_text(uid, "btn_limited_bot"), url=db["links"]["limited_bot"])
    markup.add(b_adm, b_lim)
    
    b_own = types.InlineKeyboardButton(get_text(uid, "btn_own_bot"), callback_data="sec_ownbot")
    markup.add(b_own)
    return markup

def route_user_flow(chat_id, user_id, first_name):
    if not check_user_joined(user_id):
        bot.send_message(
            chat_id,
            get_text(user_id, "force_join_text"),
            reply_markup=get_join_keyboard(user_id)
        )
        return

    if user_id not in db["accepted_terms"]:
        bot.send_message(chat_id, get_text(user_id, "terms_text"), reply_markup=get_terms_keyboard(user_id))
        return

    send_main_menu(chat_id, first_name, user_id)

def send_main_menu(chat_id, first_name, uid):
    text = get_text(uid, "main_menu_title", name=first_name)
    bot.send_message(chat_id, text, reply_markup=get_main_dashboard(uid))

@bot.message_handler(commands=['start'])
def start_cmd(message):
    uid = message.from_user.id
    if uid not in db["users"]:
        db["users"].append(uid)
        save_db(db)

    if str(uid) not in db.get("user_lang", {}):
        text = "🌐 <b>Select Your Language / अपनी भाषा चुनें / Выберите язык:</b>"
        bot.send_message(message.chat.id, text, reply_markup=get_lang_keyboard())
        return

    route_user_flow(message.chat.id, uid, message.from_user.first_name)

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    uid = call.from_user.id
    mid = call.message.message_id
    cid = call.message.chat.id
    fname = call.from_user.first_name

    if call.data.startswith("lang_"):
        chosen_lang = call.data.replace("lang_", "")
        if "user_lang" not in db:
            db["user_lang"] = {}
        db["user_lang"][str(uid)] = chosen_lang
        save_db(db)

        try:
            bot.delete_message(cid, mid)
        except Exception:
            pass

        route_user_flow(cid, uid, fname)
        return

    elif call.data == "verify_join":
        if check_user_joined(uid):
            bot.answer_callback_query(call.id, get_text(uid, "verify_success"))
            try:
                bot.delete_message(cid, mid)
            except Exception:
                pass
            route_user_flow(cid, uid, fname)
        else:
            bot.answer_callback_query(call.id, get_text(uid, "verify_fail"), show_alert=True)

    elif call.data == "accept_terms":
        if uid not in db["accepted_terms"]:
            db["accepted_terms"].append(uid)
            save_db(db)
        bot.answer_callback_query(call.id, "🎉 Success!")
        try:
            bot.delete_message(cid, mid)
        except Exception:
            pass
        send_main_menu(cid, fname, uid)

    elif call.data == "decline_terms":
        bot.answer_callback_query(call.id, "Declined", show_alert=True)
        vaporize_delete(cid, mid)
        bot.send_message(cid, get_text(uid, "terms_declined"))

    elif call.data == "main_menu":
        try:
            bot.delete_message(cid, mid)
        except Exception:
            pass
        send_main_menu(cid, fname, uid)

    elif call.data == "sec_free":
        load_mid = show_loading(cid, "Fetching Files")
        markup = types.InlineKeyboardMarkup(row_width=1)
        files = db.get("free_files", [])
        if not files:
            markup.add(types.InlineKeyboardButton(get_text(uid, "btn_back_shop"), callback_data="main_menu"))
            bot.delete_message(cid, load_mid)
            bot.send_message(cid, get_text(uid, "free_empty"), reply_markup=markup)
            return

        for idx, f in enumerate(files):
            markup.add(types.InlineKeyboardButton(f"📥 {f['name']}", callback_data=f"dl_free_{idx}"))
        markup.add(types.InlineKeyboardButton(get_text(uid, "btn_back_shop"), callback_data="main_menu"))
        
        bot.delete_message(cid, load_mid)
        bot.send_message(cid, get_text(uid, "free_title"), reply_markup=markup)

    elif call.data.startswith("dl_free_"):
        idx = int(call.data.replace("dl_free_", ""))
        files = db.get("free_files", [])
        if idx < len(files):
            f_item = files[idx]
            bot.answer_callback_query(call.id, "📤 Sending...")
            bot.send_document(cid, f_item["file_id"], caption=f"✅ <b>{f_item['name']}</b>\nDownloaded via @xtramods")
        else:
            bot.answer_callback_query(call.id, "File not found!", show_alert=True)

    elif call.data == "sec_paid":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("⚡ a. XREG", callback_data="paid_item_xreg"),
            types.InlineKeyboardButton("🎯 b. Aim Hack", callback_data="paid_item_aimhack"),
            types.InlineKeyboardButton("🎭 c. Troll Mods", callback_data="paid_item_troll"),
            types.InlineKeyboardButton(get_text(uid, "btn_back_shop"), callback_data="main_menu")
        )
        bot.edit_message_text(get_text(uid, "paid_title"), cid, mid, reply_markup=markup)

    elif call.data.startswith("paid_item_"):
        item_key = call.data.replace("paid_item_", "")
        item = db["paid_items"].get(item_key)
        if item:
            load_mid = show_loading(cid, "Loading Showcase")
            text = (
                f"✨ <b>{item['title']}</b> ✨\n\n"
                f"📝 <b>Features:</b>\n{item['desc']}\n\n"
                f"💰 <b>Price List:</b>\n<code>{item['price']}</code>"
            )
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton(get_text(uid, "buy_now"), url=db["links"]["admin_dm"]),
                types.InlineKeyboardButton(get_text(uid, "back_paid"), callback_data="sec_paid")
            )

            bot.delete_message(cid, load_mid)
            if item.get("media_id"):
                if item["media_type"] == "video":
                    bot.send_video(cid, item["media_id"], caption=text, reply_markup=markup)
                else:
                    bot.send_photo(cid, item["media_id"], caption=text, reply_markup=markup)
            else:
                bot.send_message(cid, text, reply_markup=markup)

    elif call.data == "sec_ownbot":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🚀 Buy Your Own Bot ↗", url=db["links"]["dev_dm"]),
            types.InlineKeyboardButton(get_text(uid, "btn_back_shop"), callback_data="main_menu")
        )
        bot.edit_message_text(get_text(uid, "own_bot_text"), cid, mid, reply_markup=markup)

    elif call.data.startswith("adm_"):
        if uid != ADMIN_ID:
            bot.answer_callback_query(call.id, "Unauthorized!", show_alert=True)
            return

        action = call.data
        if action == "adm_files":
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("➕ Add New Free File/APK", callback_data="adm_addfile"))
            for i, f in enumerate(db["free_files"]):
                markup.add(types.InlineKeyboardButton(f"❌ Delete: {f['name']}", callback_data=f"adm_delfile_{i}"))
            markup.add(types.InlineKeyboardButton("🔴 Back to Admin", callback_data="adm_home"))
            bot.edit_message_text("📂 <b>Manage Free Files:</b>", cid, mid, reply_markup=markup)

        elif action == "adm_addfile":
            admin_states[uid] = "WAIT_FREE_FILE"
            bot.send_message(cid, "📤 <b>Kripya wo APK ya File bhejo</b> jo Free Section me daalni hai:")

        elif action.startswith("adm_delfile_"):
            idx = int(action.replace("adm_delfile_", ""))
            if idx < len(db["free_files"]):
                del db["free_files"][idx]
                save_db(db)
                bot.answer_callback_query(call.id, "File deleted!")
            handle_callbacks(types.CallbackQuery(call.id, call.from_user, call.data, call.message, "adm_files"))

        elif action == "adm_links":
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("Edit Proofs Channel Link", callback_data="adm_setlink_proofs"),
                types.InlineKeyboardButton("Edit Admin DM Link", callback_data="adm_setlink_admin_dm"),
                types.InlineKeyboardButton("Edit Limited Support Bot Link", callback_data="adm_setlink_limited_bot"),
                types.InlineKeyboardButton("Edit Developer Link", callback_data="adm_setlink_dev_dm"),
                types.InlineKeyboardButton("🔴 Back to Admin", callback_data="adm_home")
            )
            bot.edit_message_text("🔗 <b>Manage Redirect Links:</b>", cid, mid, reply_markup=markup)

        elif action.startswith("adm_setlink_"):
            key = action.replace("adm_setlink_", "")
            admin_states[uid] = f"WAIT_LINK_{key}"
            bot.send_message(cid, f"🔗 Naya URL bhejo for <code>{key}</code>:")

        elif action == "adm_paid":
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("Edit XREG Showcase", callback_data="adm_editpaid_xreg"),
                types.InlineKeyboardButton("Edit Aim Hack Showcase", callback_data="adm_editpaid_aimhack"),
                types.InlineKeyboardButton("Edit Troll Mods Showcase", callback_data="adm_editpaid_troll"),
                types.InlineKeyboardButton("🔴 Back to Admin", callback_data="adm_home")
            )
            bot.edit_message_text("💎 <b>Manage Paid Sections:</b>", cid, mid, reply_markup=markup)

        elif action.startswith("adm_editpaid_"):
            key = action.replace("adm_editpaid_", "")
            admin_states[uid] = f"WAIT_PAID_MEDIA_{key}"
            bot.send_message(cid, f"🎥 <b>Send Demo Video ya Photo</b> for <code>{key}</code>:")

        elif action == "adm_stats":
            bot.answer_callback_query(call.id, f"Total Users: {len(db['users'])}", show_alert=True)

        elif action == "adm_home":
            open_admin_panel(cid, mid)

def open_admin_panel(chat_id, message_id=None):
    text = (
        "⚙️ <b>MASTER ADMIN CONTROLLER</b> ⚙️\n\n"
        f"👥 <b>Total Users:</b> <code>{len(db['users'])}</code>\n"
        f"🎁 <b>Active Free Files:</b> <code>{len(db['free_files'])}</code>\n\n"
        "<i>Select module to customize:</i>"
    )
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📁 Free Files", callback_data="adm_files"),
        types.InlineKeyboardButton("💎 Paid Showcase", callback_data="adm_paid")
    )
    markup.add(
        types.InlineKeyboardButton("🔗 Edit Links", callback_data="adm_links"),
        types.InlineKeyboardButton("📊 Bot Stats", callback_data="adm_stats")
    )
    if message_id:
        bot.edit_message_text(text, chat_id, message_id, reply_markup=markup)
    else:
        bot.send_message(chat_id, text, reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "⛔ <i>Aapko is panel ka access nahi hai!</i>")
        return
    open_admin_panel(message.chat.id)

@bot.message_handler(content_types=['document', 'video', 'photo', 'text'])
def handle_admin_inputs(message):
    uid = message.from_user.id
    if uid != ADMIN_ID or uid not in admin_states:
        return

    state = admin_states[uid]

    if state == "WAIT_FREE_FILE":
        if message.document:
            db["free_files"].append({
                "name": message.document.file_name or "Unknown File",
                "file_id": message.document.file_id
            })
            save_db(db)
            bot.reply_to(message, "✅ <b>File Free Section me add ho gayi!</b>")
            del admin_states[uid]
        else:
            bot.reply_to(message, "❌ Kripya document/file format me bhejo.")

    elif state.startswith("WAIT_LINK_"):
        key = state.replace("WAIT_LINK_", "")
        new_url = message.text.strip()
        if new_url.startswith("http"):
            db["links"][key] = new_url
            save_db(db)
            bot.reply_to(message, f"✅ Link for <b>{key}</b> updated!")
            del admin_states[uid]
        else:
            bot.reply_to(message, "❌ Valid URL bhejo (starting with http:// or https://)")

    elif state.startswith("WAIT_PAID_MEDIA_"):
        key = state.replace("WAIT_PAID_MEDIA_", "")
        if message.video:
            db["paid_items"][key]["media_id"] = message.video.file_id
            db["paid_items"][key]["media_type"] = "video"
        elif message.photo:
            db["paid_items"][key]["media_id"] = message.photo[-1].file_id
            db["paid_items"][key]["media_type"] = "photo"
        
        save_db(db)
        admin_states[uid] = f"WAIT_PAID_PRICE_{key}"
        bot.reply_to(message, f"✅ Media saved! Ab iska <b>Price List text</b> bhejo:\n(Example: ₹299 / 7 Days\\n₹599 / Month)")

    elif state.startswith("WAIT_PAID_PRICE_"):
        key = state.replace("WAIT_PAID_PRICE_", "")
        db["paid_items"][key]["price"] = message.text
        save_db(db)
        bot.reply_to(message, f"🎉 <b>{key.upper()} Showcase updated!</b>")
        del admin_states[uid]

print("👑 Fixed Multi-Language Bot is LIVE...")
bot.infinity_polling()
