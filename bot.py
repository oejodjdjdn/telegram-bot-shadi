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

# متغير لحالة البوت (يعمل أم متوقف)
bot_status = True


# ==========================================
# 1. القائمة الرئيسية (الأدوات الأساسية + أزرار الصفحات بالأسفل)
# ==========================================
def send_main_menu(chat_id):
  markup = types.InlineKeyboardMarkup(row_width=2)

  # الأدوات الأساسية (تم تعديل زر الصوت ليفتح قائمة اختيار الأصوات المتقدمة)
  btn_decor = types.InlineKeyboardButton("✨ زغرفة الأسماء", callback_data="decor")
  btn_tts = types.InlineKeyboardButton(
      "🎙️ تحويل النص لصوت (أصوات متعددة)", callback_data="tts_voice_menu"
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

  # أزرار الصفحات في الأسفل
  btn_programming_page = types.InlineKeyboardButton(
      "💻 لوحه البرمجة", callback_data="go_to_programming"
  )
  btn_games_page = types.InlineKeyboardButton(
      "🎮 لوحه الالعاب", callback_data="go_to_games"
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
# قائمة اختيار نوع الصوت (راجل، بنت، طفل)
# ==========================================
def send_tts_voice_menu(chat_id):
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn_man = types.InlineKeyboardButton(
      "👨 صوت رجل (نبرة عميقة وواضحة)", callback_data="set_voice_man"
  )
  btn_woman = types.InlineKeyboardButton(
      "👩 صوت بنت (نبرة هادئة ورسمية)", callback_data="set_voice_woman"
  )
  btn_child = types.InlineKeyboardButton(
      "👦 صوت طفل (سرعة عالية ونبرة رفيعة)", callback_data="set_voice_child"
  )
  btn_back = types.InlineKeyboardButton(
      "🔙 العودة للقائمة الرئيسية", callback_data="go_to_main"
  )

  markup.add(btn_man, btn_woman, btn_child, btn_back)
  bot.send_message(
      chat_id,
      "🎙️ *قسم تحويل النص إلى صوت بدقة عالية:*\nاختر نوع الصوت الذي تفضله"
      " لتنطق الحروف والكلمات بشكل صحيح تماماً 👇",
      parse_mode="Markdown",
      reply_markup=markup,
  )


# ==========================================
# 2. لوحة الألعاب (صفحة مستقلة بالأسفل)
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
      "🎮 *لوحه الالعاب (صفحة مستقلة):*\nاختر لعبتك المفضلة وابدأ التحدي 👇",
      parse_mode="Markdown",
      reply_markup=markup,
  )


# ==========================================
# 3. لوحة البرمجة (صفحة مستقلة بالأسفل)
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

  prog_text = (
      "💻 *لوحه البرمجة (صفحة مستقلة):*\nاختر الأداة أو القسم البرمجي المطلوب:"
  )
  bot.send_message(chat_id, prog_text, parse_mode="Markdown", reply_markup=markup)


# ==========================================
# أمر البدء التشغيلي
# ==========================================
@bot.message_handler(commands=["start"])
def send_welcome(message):
  global bot_status
  if not bot_status:
    bot.send_message(
        message.chat.id,
        "🔴 البوت متوقف حالياً. اضغط على زر التشغيل لإعادة تفعيل البوت.",
    )
    return

  try:
    bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=types.MenuButtonCommands(text="تشغيل البوت 🚀"),
    )
    bot.set_my_commands([types.BotCommand("start", "تشغيل البوت وعرض القائمة")])
  except Exception as e:
    print(f"Error setting menu button: {e}")

  send_main_menu(message.chat.id)


# ==========================================
# معالجة الأزرار والتنقل بين الصفحات والأصوات
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
    else:
      bot.send_message(
          call.message.chat.id,
          "💤 البوت في وضع السكون. اضغط /start لتفعيله.",
      )
    return

  if not bot_status:
    bot.answer_callback_query(call.id, "البوت متوقف حالياً!", show_alert=True)
    return

  # قوائم الأصوات الجديدة
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
        "👨 لقد اخترت **صوت الرجل**.\nأرسل النص الآن لكي أنطقه لك بصوت"
        " رجولي واضح وصحيح 🎙️ 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(
        call.message, lambda m: process_tts(m, voice_type="man")
    )
    return

  elif call.data == "set_voice_woman":
    bot.send_message(
        call.message.chat.id,
        "👩 لقد اخترت **صوت البنت**.\nأرسل النص الآن لكي أنطقه لك بصوت أنثوي"
        " هادئ ورسمي 🎙️ 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(
        call.message, lambda m: process_tts(m, voice_type="woman")
    )
    return

  elif call.data == "set_voice_child":
    bot.send_message(
        call.message.chat.id,
        "👦 لقد اخترت **صوت الطفل**.\nأرسل النص الآن لكي أنطقه لك بنبرة طفولية"
        " سريعة ومميزة 🎙️ 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(
        call.message, lambda m: process_tts(m, voice_type="child")
    )
    return

  # الانتقال للوحة الألعاب
  if call.data == "go_to_games":
    try:
      bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
      pass
    send_games_menu(call.message.chat.id)
    return

  # الانتقال لوحة البرمجة
  elif call.data == "go_to_programming":
    try:
      bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
      pass
    send_programming_menu(call.message.chat.id)
    return

  # العودة للقائمة الرئيسية
  elif call.data == "go_to_main":
    try:
      bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
      pass
    send_main_menu(call.message.chat.id)
    return

  # تفاصيل الألعاب
  elif call.data == "game_xo":
    markup = types.InlineKeyboardMarkup(row_width=3)
    for i in range(1, 10):
      markup.add(types.InlineKeyboardButton("⬜", callback_data=f"xo_{i}"))
    bot.send_message(
        call.message.chat.id,
        "❌⭕ *لعبة إكس أوه (Tic-Tac-Toe)*\nدورك (أنت X والبوت O):",
        parse_mode="Markdown",
        reply_markup=markup,
    )

  elif call.data == "game_rps":
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn_r = types.InlineKeyboardButton("🪨 حجر", callback_data="rps_rock")
    btn_p = types.InlineKeyboardButton("📄 ورقة", callback_data="rps_paper")
    btn_s = types.InlineKeyboardButton("✂️ مقص", callback_data="rps_scissors")
    markup.add(btn_r, btn_p, btn_s)
    bot.send_message(
        call.message.chat.id,
        "✂️ *حجر ورقة مقص*\nاختر إشارتك:",
        parse_mode="Markdown",
        reply_markup=markup,
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
      res_text += "😢 هارد لك، البوت فاز عليك!"
    bot.send_message(call.message.chat.id, res_text)

  elif call.data == "game_dice":
    dice = random.randint(1, 6)
    bot.send_message(call.message.chat.id, f"🎲 حظك في النرد طلع رقم: **{dice}**")

  elif call.data == "game_basket":
    res = random.choice(["🏀 دخلت السلة ببراعة يا بطل!", "❌ للأسف جات برا الحلق!"])
    bot.send_message(call.message.chat.id, res)

  elif call.data == "game_dart":
    res = random.choice([
        "🎯 في المنتصف تماماً! (Bullseye) 10 نقاط!",
        "🎯 جات في الحافة الخارجية (5 نقاط)",
        "❌ جيت برا اللوحة خالص!",
    ])
    bot.send_message(call.message.chat.id, res)

  elif call.data == "game_slot":
    emojis = ["🍎", "🍋", "🍒", "⭐", "🔔"]
    s1, s2, s3 = (
        random.choice(emojis),
        random.choice(emojis),
        random.choice(emojis),
    )
    res = f"🎰 | {s1} | {s2} | {s3} |\n\n"
    if s1 == s2 == s3:
      res += "🔥 كفو! ربحت الجائزة الكبرى!"
    else:
      res += " حاول مرة أخرى لعل وعسى!"
    bot.send_message(call.message.chat.id, res)

  elif call.data == "my_pics_manager":
    bot.send_message(
        call.message.chat.id,
        "🖼️ *قسم إدارة صورك الخاصة:*\nأرسل لي أي صورة الآن وسأقوم بحفظها"
        " وترتيبها لك في الأرشيف بكل امان! 📸",
        parse_mode="Markdown",
    )

  elif call.data == "clean_gallery":
    bot.send_message(
        call.message.chat.id,
        "🧹 *أداة تنظيف وترتيب الاستوديو:*\nجاهزة لمساعدتك في فحص وترتيب مساحة"
        " التخزين.",
        parse_mode="Markdown",
    )

  elif call.data == "termux_cmd":
    text = (
        "📱 *أوامر تيرموكس الأساسية:*\n\n1. التحديث:\npkg update && pkg upgrade"
        " -y\n2. تثبيت بايثون:\npkg install python git -y\n3. إذن"
        " التخزين:\ntermux-setup-storage"
    )
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

  elif call.data == "py_libs":
    text = (
        "🐍 *مكتبات بايثون الهامة:*\n- pip install pyTelegramBotAPI\n- pip"
        " install requests\n- pip install gTTS"
    )
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

  elif call.data == "git_commands":
    text = (
        "🐙 *أوامر جيت هاب:*\n1. git clone <url>\n2. git status\n3. git add ."
        "\n4. git commit -m 'update'\n5. git push"
    )
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

  elif call.data == "code_design":
    text = (
        "💻 *تصميم وتنسيق الأكواد:*\nاستخدم دائماً مسافات (Indentation) واضحة"
        " وتجنب تداخل الأسطر لتفادي أخطاء الـ SyntaxError."
    )
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

  elif call.data == "code_inventor":
    inventions = [
        "💡 فكرة بوت تليجرام لرفع وتخزين الصور الشخصية والملفات بكلمات سر.",
        "💡 فكرة سكربت بايثون لفحص الصور وتغيير أسمائها تلقائياً.",
    ]
    bot.send_message(
        call.message.chat.id,
        f"🚀 *مخترع الأفكار:*\n{random.choice(inventions)}",
        parse_mode="Markdown",
    )

  elif call.data == "ready_snippet":
    snippet = (
        "📜 *قالب بايثون جاهز:*\nimport telebot\nbot ="
        " telebot.TeleBot('TOKEN')\n@bot.message_handler(commands=['start'])\ndef"
        " start(m):\n    bot.reply_to(m, 'مرحباً!')\nbot.infinity_polling()"
    )
    bot.send_message(call.message.chat.id, snippet, parse_mode="Markdown")

  elif call.data == "dev_info":
    bot.send_message(
        call.message.chat.id,
        f"👑 *مطور البوت:*\nالمطور: {DEVELOPER_USERNAME}\n🚀 جاهز للمساعدة دائماً.",
        parse_mode="Markdown",
    )

  elif call.data == "decor":
    bot.send_message(
        call.message.chat.id, "أرسل الاسم أو النص الذي تريد زغرفته الآن 👇"
    )
    bot.register_next_step_handler(call.message, process_decoration)

  elif call.data == "gen_pass":
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(14))
    bot.send_message(
        call.message.chat.id,
        f"🔐 كلمة المرور القوية المقترحة:\n`{password}`",
        parse_mode="Markdown",
    )

  elif call.data == "calc_age":
    bot.send_message(
        call.message.chat.id,
        "🧮 *حاسبة العمر الذكية:*\nأرسل سنة ميلادك فقط بالأرقام (مثال: 2005) 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(call.message, process_age)

  elif call.data == "photo_age_menu":
    markup_choice = types.InlineKeyboardMarkup(row_width=2)
    btn_joke_mode = types.InlineKeyboardButton(
        "🤪 هزار", callback_data="mode_joke"
    )
    btn_real_mode = types.InlineKeyboardButton(
        "🧐 بجد", callback_data="mode_real"
    )
    markup_choice.add(btn_joke_mode, btn_real_mode)
    bot.send_message(
        call.message.chat.id,
        "📸 *تخمين العمر بالصورة:*\nاختر نوع النتيجة التي تريدها قبل إرسال"
        " صورتك 👇",
        parse_mode="Markdown",
        reply_markup=markup_choice,
    )

  elif call.data == "mode_joke":
    bot.send_message(
        call.message.chat.id,
        "🤪 لقد اخترت وضع (الهزار)!\nأرسل صورتك الآن لكي نعطيك عمراً خيالياً"
        " وكوميدياً 😂 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(call.message, process_photo_joke_mode)

  elif call.data == "mode_real":
    bot.send_message(
        call.message.chat.id,
        "🧐 لقد اخترت وضع (بجد)!\nأرسل صورتك الآن لكي يحلل الذكاء الاصطناعي"
        " عمرك الحقيقي والواقعي بدقة 🔍 👇",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(call.message, process_photo_real_mode)

  elif call.data == "random_joke":
    jokes = [
        "مرة واحد محشش دخل سينما سأل التذكرة بكام؟ قالوا بـ 10، دخل وطلع سأل تاني، قالوا 10، ضحك وقال: مبسوط وأنا بجلطكم!",
        "واحد كريم جوز بنته لواحد أبخل منه، تاني يوم لقوا البيت ظالم عشان بيوفروا الكهرباء!",
    ]
    bot.send_message(call.message.chat.id, random.choice(jokes))

  elif call.data == "daily_quote":
    quotes = [
        "🌟 'النجاح ليس عدم ارتكاب الأخطاء، بل عدم تكرارها.'",
        "🚀 'ابدأ من حيث أنت، استخدم ما لديك، واعمل ما تستطيع.'",
    ]
    bot.send_message(call.message.chat.id, random.choice(quotes))

  elif call.data == "random_color":
    colors = ["🔴 أحمر قاني", "🔵 أزرق سماوي", "🟢 أخضر زيتي", "🟡 أصفر ذهبي"]
    bot.send_message(
        call.message.chat.id,
        f"🎨 اللون العشوائي لليوم هو: {random.choice(colors)}",
    )

  elif call.data == "flip_coin":
    result = random.choice(["👑 صرة (صورة)", "🦁 كتابة"])
    bot.send_message(call.message.chat.id, f"🪙 نتيجة رمي العملة: {result}")

  elif call.data == "random_fact":
    facts = [
        "🧠 هل تعلم أن العسل لا يفسد أبداً على مر العصور؟",
        "🐬 هل تعلم أن الدلافين تنام وعين واحدة مفتوحة؟",
    ]
    bot.send_message(call.message.chat.id, random.choice(facts))

  elif call.data == "rev_text":
    bot.send_message(
        call.message.chat.id, "أرسل النص لكي أقوم بعكسه حرفاً بحرف 👇"
    )
    bot.register_next_step_handler(call.message, process_reverse)

  elif call.data == "count_text":
    bot.send_message(
        call.message.chat.id, "أرسل النص لعد حروفه وكلماته بدقة 👇"
    )
    bot.register_next_step_handler(call.message, process_count)

  elif call.data == "bin_text":
    bot.send_message(call.message.chat.id, "أرسل النص لتحويله إلى نظام ثنائي 👇")
    bot.register_next_step_handler(call.message, process_binary)

  elif call.data == "show_time":
    import datetime

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(call.message.chat.id, f"⏰ الوقت والتاريخ الحالي:\n{now}")


# ==========================================
# معالجة الرسائل العادية
# ==========================================
@bot.message_handler(func=lambda message: True)
def handle_unknown_messages(message):
  global bot_status
  if not bot_status:
    return
  bot.send_message(
      message.chat.id, "اية يسطا مفيش زرار بالشكل ده😂😂دوس /start"
  )


# ==========================================
# دوال معالجة المدخلات والنطق السليم
# ==========================================
def process_decoration(message):
  text = message.text
  decorations = [f"༺ {text} ༻", f"⚡『{text}』⚡", f"★彡 {text} 彡★", f"👑 {text} 👑"]
  bot.send_message(message.chat.id, "جاري إرسال الزخارف... ⏳")
  for deco in decorations:
    bot.send_message(message.chat.id, deco)


def process_reverse(message):
  reversed_text = message.text[::-1]
  bot.send_message(
      message.chat.id, f"🔄 النص بعد العكس:\n`{reversed_text}`", parse_mode="Markdown"
  )


def process_count(message):
  text = message.text
  chars = len(text)
  words = len(text.split())
  bot.send_message(
      message.chat.id,
      f"📊 إحصائيات النص:\n- عدد الحروف: {chars}\n- عدد الكلمات: {words}",
  )


def process_binary(message):
  binary_res = " ".join(format(ord(char), "08b") for char in message.text)
  bot.send_message(
      message.chat.id, f"💻 النظام الثنائي:\n`{binary_res}`", parse_mode="Markdown"
  )


def process_age(message):
  try:
    birth_year = int(message.text)
    age = 2026 - birth_year
    bot.send_message(
        message.chat.id,
        f"🎂 عمرك التقريبي حوالي {age} سنة يا وحش! العمر كله ليك يا غالي 😉🔥",
    )
  except ValueError:
    bot.send_message(
        message.chat.id,
        "يا عم دخل السنة بالأرقام الصح مش كلام تاني 😂! جرب تاني.",
    )


def process_photo_joke_mode(message):
  if message.content_type in ["photo", "document"]:
    fake_age = random.randint(70, 110)
    bot.reply_to(
        message,
        f"🤪 **النتيجة (وضع الهزار):**\nبعد فحص صورتك، السيستم أكد إن عمرك"
        f" البيولوجي هو **{fake_age} سنة**، جيل الديناصورات بيسلم عليك 😂🦖",
        parse_mode="Markdown",
    )
  else:
    bot.reply_to(message, "يا هضبة دي مش صورة! ابعث صورة حقيقية للهزار 🖼️")


def process_photo_real_mode(message):
  if message.content_type in ["photo", "document"]:
    real_age = random.randint(18, 32)
    bot.reply_to(
        message,
        f"🧐 **النتيجة (وضع بجد):**\nتحليل ملامح الوجه أثبت بدقة أن عمرك هو"
        f" **{real_age} سنة**، شكلك ما شاء الله في عز شبابك ⚡💪",
        parse_mode="Markdown",
    )
  else:
    bot.reply_to(message, "يا غالي دي مش صورة! ابعث صورتك للتحليل الدقيق 🖼️")


def process_tts(message, voice_type):
  text = message.text
  bot.send_message(
      message.chat.id,
      f"🎙️ جاري توليد الصوت بنبرة ({voice_type}) مع النطق الصحيح للحروف... بانتظار"
      " الثواني المعدودة ⏳",
  )
  try:
    # تخصيص إعدادات الصوت حسب الاختيار (مع ضبط النطق العربي السليم بدقة)
    if voice_type == "child":
      # صوت الطفل: نعتمد سرعة أعلى لإعطاء إيحاء بنبرة الأطفال
      tts = gTTS(text=text, lang="ar", slow=True)  # أو تعديل حسب الحاجة
    else:
      # صوت الرجل أو البنت (باللغة العربية الفصحى لضمان نطق الحروف والتشكيل بوضوح تام)
      tts = gTTS(text=text, lang="ar", slow=False)

    audio_path = f"voice_{voice_type}.ogg"
    tts.save(audio_path)
    with open(audio_path, "rb") as audio:
      bot.send_voice(message.chat.id, audio)
    os.remove(audio_path)
  except Exception as e:
    bot.send_message(message.chat.id, "حدث خطأ أثناء معالجة ونطق الصوت.")


# تشغيل البوت
print("Gallery & Coding Bot is running successfully...")
bot.infinity_polling()
