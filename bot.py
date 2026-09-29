import os
import random
import string
from gtts import gTTS
import telebot
from telebot import types

# ضع توكن البوت الخاص بك هنا
TOKEN = "8922686534:AAEjaQAcrWzu42GTaDIG1m-LdUyVXhQqOLs"
bot = telebot.TeleBot(TOKEN)

# اليوزر الخاص بك كمطور للبوت
DEVELOPER_USERNAME = "@ahmed6486570"

# متغير لحالة البوت
bot_status = True


# ==========================================
# القائمة الرئيسية
# ==========================================
def send_main_menu(chat_id):
  markup = types.InlineKeyboardMarkup(row_width=2)

  btn_decor = types.InlineKeyboardButton("✨ زغرفة الأسماء", callback_data="decor")
  btn_tts = types.InlineKeyboardButton(
      "🎙️ تحويل النص لصوت", callback_data="tts_voice_menu"
  )
  btn_pass = types.InlineKeyboardButton(
      "🔒 توليد كلمة مرور", callback_data="gen_pass"
  )
  btn_calc = types.InlineKeyboardButton("🧮 حاسبة العمر", callback_data="calc_age")
  btn_photo_age = types.InlineKeyboardButton(
      "📸 تخمين العمر بالصورة", callback_data="photo_age_menu"
  )
  btn_rev = types.InlineKeyboardButton("🔄 عكس النص", callback_data="rev_text")
  btn_count = types.InlineKeyboardButton(
      "📊 عد الحروف والكلمات", callback_data="count_text"
  )
  btn_binary = types.InlineKeyboardButton(
      "💻 نظام ثنائي", callback_data="bin_text"
  )
  btn_time = types.InlineKeyboardButton(
      "⏰ الوقت والتاريخ", callback_data="show_time"
  )
  btn_joke = types.InlineKeyboardButton(
      "😂 نكتة عشوائية", callback_data="random_joke"
  )
  btn_quote = types.InlineKeyboardButton(
      "💡 حكمة اليوم", callback_data="daily_quote"
  )
  btn_color = types.InlineKeyboardButton(
      "🎨 لون عشوائي", callback_data="random_color"
  )
  btn_coin = types.InlineKeyboardButton("🪙 قلب عملة", callback_data="flip_coin")
  btn_fact = types.InlineKeyboardButton(
      "🧠 هل تعلم؟", callback_data="random_fact"
  )
  btn_dev = types.InlineKeyboardButton(
      "👨‍💻 مطور البوت", callback_data="dev_info"
  )

  markup.add(
      btn_decor,
      btn_tts,
      btn_pass,
      btn_calc,
      btn_photo_age,
      btn_rev,
      btn_count,
      btn_binary,
      btn_time,
      btn_joke,
      btn_quote,
      btn_color,
      btn_coin,
      btn_fact,
      btn_dev,
  )

  btn_programming_page = types.InlineKeyboardButton(
      "💻 لوحة البرمجة", callback_data="go_to_programming"
  )
  btn_games_page = types.InlineKeyboardButton(
      "🎮 لوحة الألعاب", callback_data="go_to_games"
  )
  btn_power = types.InlineKeyboardButton(
      "🛑 إيقاف / تشغيل البوت", callback_data="toggle_power"
  )

  markup.add(btn_programming_page)
  markup.add(btn_games_page)
  markup.add(btn_power)

  welcome_text = (
      "🚀 *مرحباً بك في القائمة الرئيسية للبوت!*\nتستطيع استخدام الأدوات"
      " الأساسية بالأسفل، أو الانتقال للأقسام المخصصة عبر الأزرار في نهاية"
      " القائمة 👇"
  )
  bot.send_message(
      chat_id, welcome_text, parse_mode="Markdown", reply_markup=markup
  )


# ==========================================
# قائمة الأصوات
# ==========================================
def send_tts_voice_menu(chat_id):
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn_man = types.InlineKeyboardButton("👨 صوت رجل", callback_data="set_voice_man")
  btn_woman = types.InlineKeyboardButton(
      "👩 صوت بنت", callback_data="set_voice_woman"
  )
  btn_child = types.InlineKeyboardButton(
      "👦 صوت طفل", callback_data="set_voice_child"
  )
  btn_back = types.InlineKeyboardButton(
      "🔙 العودة للقائمة الرئيسية", callback_data="go_to_main"
  )

  markup.add(btn_man, btn_woman, btn_child, btn_back)
  bot.send_message(
      chat_id,
      "🎙️ *قسم تحويل النص إلى صوت:*\nاختر نوع الصوت المناسب لك 👇",
      parse_mode="Markdown",
      reply_markup=markup,
  )


# ==========================================
# لوحة الألعاب
# ==========================================
def send_games_menu(chat_id):
  markup = types.InlineKeyboardMarkup(row_width=2)
  btn_xo = types.InlineKeyboardButton("❌⭕ لعبة إكس أوه", callback_data="game_xo")
  btn_rps = types.InlineKeyboardButton(
      "✂️ حجر ورقة مقص", callback_data="game_rps"
  )
  btn_dice = types.InlineKeyboardButton("🎲 حظ النرد", callback_data="game_dice")
  btn_basket = types.InlineKeyboardButton(
      "🏀 رمي السلة", callback_data="game_basket"
  )
  btn_dart = types.InlineKeyboardButton("🎯 رمي السهام", callback_data="game_dart")
  btn_slot = types.InlineKeyboardButton(
      "🎰 ماكينة الحظ", callback_data="game_slot"
  )
  btn_back = types.InlineKeyboardButton(
      "🔙 العودة للقائمة الرئيسية", callback_data="go_to_main"
  )

  markup.add(btn_xo, btn_rps, btn_dice, btn_basket, btn_dart, btn_slot)
  markup.add(btn_back)

  bot.send_message(
      chat_id,
      "🎮 *لوحة الألعاب:*\nاختر لعبتك المفضلة وابدأ التحدي 👇",
      parse_mode="Markdown",
      reply_markup=markup,
  )


# ==========================================
# لوحة البرمجة
# ==========================================
def send_programming_menu(chat_id):
  markup = types.InlineKeyboardMarkup(row_width=2)
  btn_termux = types.InlineKeyboardButton(
      "📱 أوامر تيرموكس", callback_data="termux_cmd"
  )
  btn_py_libs = types.InlineKeyboardButton(
      "🐍 مكتبات بايثون", callback_data="py_libs"
  )
  btn_git = types.InlineKeyboardButton(
      "🐙 أوامر جيت هاب", callback_data="git_commands"
  )
  btn_code_design = types.InlineKeyboardButton(
      "💻 تصميم الأكواد", callback_data="code_design"
  )
  btn_my_pics = types.InlineKeyboardButton(
      "🖼️ قسم صورك الخاصة", callback_data="my_pics_manager"
  )
  btn_clean_gallery = types.InlineKeyboardButton(
      "🧹 تنظيم الملفات", callback_data="clean_gallery"
  )
  btn_inventor = types.InlineKeyboardButton(
      "💡 مخترع الأفكار البرمجية", callback_data="code_inventor"
  )
  btn_snippet = types.InlineKeyboardButton(
      "📜 قالب سكربت جاهز", callback_data="ready_snippet"
  )
  btn_back = types.InlineKeyboardButton(
      "🔙 العودة للقائمة الرئيسية", callback_data="go_to_main"
  )

  markup.add(
      btn_termux,
      btn_py_libs,
      btn_git,
      btn_code_design,
      btn_my_pics,
      btn_clean_gallery,
      btn_inventor,
      btn_snippet,
  )
  markup.add(btn_back)

  bot.send_message(
      chat_id,
      "💻 *لوحة البرمجة:*\nاختر الأداة أو القسم البرمجي المطلوب:",
      parse_mode="Markdown",
      reply_markup=markup,
  )


# ==========================================
# أمر البدء
# ==========================================
@bot.message_handler(commands=["start"])
def send_welcome(message):
  global bot_status
  if not bot_status:
    bot.send_message(
        message.chat.id, "🔴 البوت متوقف حالياً. اضغط /start لإعادة التفعيل."
    )
    return
  send_main_menu(message.chat.id)


# ==========================================
# معالجة الأزرار (Callback Queries)
# ==========================================
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  global bot_status

  if call.data == "toggle_power":
    bot_status = not bot_status
    status_text = (
        "🟢 تم تشغيل البوت بنجاح!"
        if bot_status
        else "🔴 تم إيقاف البوت مؤقتاً."
    )
    bot.answer_callback_query(call.id, status_text, show_alert=True)
    if bot_status:
      send_main_menu(call.message.chat.id)
    return

  if not bot_status:
    bot.answer_callback_query(call.id, "البوت متوقف حالياً!", show_alert=True)
    return

  if call.data == "tts_voice_menu":
    try:
      bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
      pass
    send_tts_voice_menu(call.message.chat.id)
    return

  elif call.data == "set_voice_man":
    bot.send_message(
        call.message.chat.id,
        "👨 لقد اخترت **صوت الرجل**.\nأرسل النص الآن لكي أنطقه لك 🎙️ 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(
        call.message, lambda m: process_tts(m, voice_type="man")
    )
    return

  elif call.data == "set_voice_woman":
    bot.send_message(
        call.message.chat.id,
        "👩 لقد اخترت **صوت البنت**.\nأرسل النص الآن لكي أنطقه لك 🎙️ 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(
        call.message, lambda m: process_tts(m, voice_type="woman")
    )
    return

  elif call.data == "set_voice_child":
    bot.send_message(
        call.message.chat.id,
        "👦 لقد اخترت **صوت الطفل**.\nأرسل النص الآن لكي أنطقه لك 🎙️ 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(
        call.message, lambda m: process_tts(m, voice_type="child")
    )
    return

  elif call.data == "go_to_games":
    try:
      bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
      pass
    send_games_menu(call.message.chat.id)
    return

  elif call.data == "go_to_programming":
    try:
      bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
      pass
    send_programming_menu(call.message.chat.id)
    return

  elif call.data == "go_to_main":
    try:
      bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
      pass
    send_main_menu(call.message.chat.id)
    return

  elif call.data == "game_xo":
    bot.send_message(call.message.chat.id, "❌⭕ لعبة إكس أوه قيد التحديث!")

  elif call.data == "game_rps":
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn_r = types.InlineKeyboardButton("🪨 حجر", callback_data="rps_rock")
    btn_p = types.InlineKeyboardButton("📄 ورقة", callback_data="rps_paper")
    btn_s = types.InlineKeyboardButton("✂️ مقص", callback_data="rps_scissors")
    markup.add(btn_r, btn_p, btn_s)
    bot.send_message(
        call.message.chat.id, "✂️ *حجر ورقة مقص*\nاختر إشارتك:", reply_markup=markup
    )

  elif call.data.startswith("rps_"):
    user_choice = call.data.split("_")[1]
    choices = {"rock": "🪨 حجر", "paper": "📄 ورقة", "scissors": "✂️ مقص"}
    bot_choice = random.choice(list(choices.keys()))
    res_text = f"أنت اخترت: {choices[user_choice]}\nالبوت اختار: {choices[bot_choice]}\n\n"
    if user_choice == bot_choice:
      res_text += "🤝 تعادل!"
    elif (
        (user_choice == "rock" and bot_choice == "scissors")
        or (user_choice == "paper" and bot_choice == "rock")
        or (user_choice == "scissors" and bot_choice == "paper")
    ):
      res_text += "🎉 مبروك فزت يا وحش!"
    else:
      res_text += "😢 هارد لك، البوت فاز!"
    bot.send_message(call.message.chat.id, res_text)

  elif call.data == "game_dice":
    bot.send_message(
        call.message.chat.id, f"🎲 حظك في النرد: **{random.randint(1, 6)}**"
    )

  elif call.data == "game_basket":
    bot.send_message(
        call.message.chat.id,
        random.choice(["🏀 دخلت السلة ببراعة!", "❌ جات برا الحلق!"]),
    )

  elif call.data == "game_dart":
    bot.send_message(
        call.message.chat.id,
        random.choice(
            ["🎯 في المنتصف تماماً (10 نقاط)!", "🎯 جات في الحافة (5 نقاط)"]
        ),
    )

  elif call.data == "game_slot":
    emojis = ["🍎", "🍋", "🍒", "⭐", "🔔"]
    s1, s2, s3 = (
        random.choice(emojis),
        random.choice(emojis),
        random.choice(emojis),
    )
    res = f"🎰 | {s1} | {s2} | {s3} |\n\n"
    res += (
        "🔥 كفو ربحت الجائزة الكبرى!"
        if s1 == s2 == s3
        else "حاول مرة أخرى!"
    )
    bot.send_message(call.message.chat.id, res)

  elif call.data == "my_pics_manager":
    bot.send_message(
        call.message.chat.id,
        "🖼️ أرسل لي أي صورة الآن وسأقوم بحفظها وترتيبها بأمان! 📸",
    )

  elif call.data == "clean_gallery":
    bot.send_message(
        call.message.chat.id, "🧹 أداة تنظيف وترتيب الاستوديو جاهزة."
    )

  elif call.data == "termux_cmd":
    bot.send_message(
        call.message.chat.id,
        "📱 *أوامر تيرموكس:*\npkg update && pkg upgrade -y",
        parse_mode="Markdown",
    )

  elif call.data == "py_libs":
    bot.send_message(
        call.message.chat.id,
        "🐍 *مكتبات بايثون:*\npip install pyTelegramBotAPI requests gTTS",
        parse_mode="Markdown",
    )

  elif call.data == "git_commands":
    bot.send_message(
        call.message.chat.id,
        "🐙 *أوامر جيت هاب:*\ngit clone / git add . / git push",
        parse_mode="Markdown",
    )

  elif call.data == "code_design":
    bot.send_message(
        call.message.chat.id,
        "💻 استخدم مسافات واضحة لتفادي أخطاء البرمجة.",
        parse_mode="Markdown",
    )

  elif call.data == "code_inventor":
    bot.send_message(
        call.message.chat.id,
        "💡 فكرة بوت تليجرام لرفع وتخزين الصور والملفات بكلمات سر.",
        parse_mode="Markdown",
    )

  elif call.data == "ready_snippet":
    bot.send_message(
        call.message.chat.id,
        "📜 سكربت بسيط جاهز للعمل.",
        parse_mode="Markdown",
    )

  elif call.data == "dev_info":
    bot.send_message(
        call.message.chat.id,
        f"👑 *المطور:* {DEVELOPER_USERNAME}",
        parse_mode="Markdown",
    )

  elif call.data == "decor":
    bot.send_message(call.message.chat.id, "أرسل الاسم لزخرفته 👇")
    bot.register_next_step_handler(call.message, process_decoration)

  elif call.data == "gen_pass":
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(14))
    bot.send_message(
        call.message.chat.id,
        f"🔐 كلمة المرور المقترحة:\n`{password}`",
        parse_mode="Markdown",
    )

  elif call.data == "calc_age":
    bot.send_message(call.message.chat.id, "أرسل سنة ميلادك بالأرقام 👇")
    bot.register_next_step_handler(call.message, process_age)

  elif call.data == "photo_age_menu":
    bot.send_message(call.message.chat.id, "أرسل صورتك للتحليل 👇")

  elif call.data == "random_joke":
    jokes = [
        "مرة واحد دخل سينما سأل التذكرة بكام؟ قالوا بـ 10، دخل وطلع سأل تاني!",
        "واحد كريم جوز بنته لواحد أبخل منه!",
    ]
    bot.send_message(call.message.chat.id, random.choice(jokes))

  elif call.data == "daily_quote":
    bot.send_message(
        call.message.chat.id, "🌟 'النجاح ليس عدم ارتكاب الأخطاء، بل عدم تكرارها.'"
    )

  elif call.data == "random_color":
    bot.send_message(
        call.message.chat.id,
        f"🎨 اللون العشوائي: {random.choice(['أحمر', 'أزرق', 'أخضر', 'أصفر'])}",
    )

  elif call.data == "flip_coin":
    bot.send_message(
        call.message.chat.id,
        f"🪙 النتيجة: {random.choice(['صورة', 'كتابة'])}",
    )

  elif call.data == "random_fact":
    bot.send_message(
        call.message.chat.id,
        "🧠 هل تعلم أن العسل لا يفسد أبداً على مر العصور؟",
    )

  elif call.data == "rev_text":
    bot.send_message(call.message.chat.id, "أرسل النص لعكسه 👇")
    bot.register_next_step_handler(call.message, process_reverse)

  elif call.data == "count_text":
    bot.send_message(call.message.chat.id, "أرسل النص لعد حروفه 👇")
    bot.register_next_step_handler(call.message, process_count)

  elif call.data == "bin_text":
    bot.send_message(call.message.chat.id, "أرسل النص لتحويله لنظام ثنائي 👇")
    bot.register_next_step_handler(call.message, process_binary)

  elif call.data == "show_time":
    import datetime

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(call.message.chat.id, f"⏰ الوقت الحالي:\n{now}")


# ==========================================
# معالجة الرسائل العادية (نظيفة وخالية من أي إعلانات)
# ==========================================
@bot.message_handler(func=lambda message: True)
def handle_unknown_messages(message):
  global bot_status
  if not bot_status:
    return
  # تم تنظيف الرد تماماً ليصبح بسيطاً وبدون أي محتوى مزعج
  bot.send_message(
      message.chat.id,
      "أهلاً بك يا غالي! استخدم الأوامر أو اضغط /start لعرض القائمة الرئيسية"
      " 🚀",
  )


# ==========================================
# دوال معالجة البيانات
# ==========================================
def process_decoration(message):
  text = message.text
  decorations = [f"༺ {text} ༻", f"⚡『{text}』⚡", f"👑 {text} 👑"]
  for deco in decorations:
    bot.send_message(message.chat.id, deco)


def process_reverse(message):
  bot.send_message(
      message.chat.id,
      f"🔄 النص بعد العكس:\n`{message.text[::-1]}`",
      parse_mode="Markdown",
  )


def process_count(message):
  text = message.text
  bot.send_message(
      message.chat.id,
      f"📊 الحروف: {len(text)} | الكلمات: {len(text.split())}",
  )


def process_binary(message):
  binary_res = " ".join(format(ord(char), "08b") for char in message.text)
  bot.send_message(
      message.chat.id,
      f"💻 النظام الثنائي:\n`{binary_res}`",
      parse_mode="Markdown",
  )


def process_age(message):
  try:
    age = 2026 - int(message.text)
    bot.send_message(
        message.chat.id, f"🎂 عمرك التقريبي حوالي {age} سنة يا وحش! 🔥"
    )
  except ValueError:
    bot.send_message(message.chat.id, "من فضلك أدخل سنة الميلاد بالأرقام الصحيحة.")


def process_tts(message, voice_type):
  text = message.text
  bot.send_message(message.chat.id, "🎙️ جاري توليد الصوت بدقة...")
  try:
    tts = gTTS(text=text, lang="ar", slow=False)
    audio_path = f"voice_{voice_type}.ogg"
    tts.save(audio_path)
    with open(audio_path, "rb") as audio:
      bot.send_voice(message.chat.id, audio)
    os.remove(audio_path)
  except Exception as e:
    bot.send_message(message.chat.id, "حدث خطأ أثناء معالجة الصوت.")


# تشغيل البوت
print("Clean Bot is running successfully...")
bot.infinity_polling()
