<<<<<<< HEAD
import telebot
from telebot import types
import random
from datetime import date
import os
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
user_answers = {}
user_scores = {}
user_total = {}
quiz_count = {}
best_score = {}
daily_words = {}
from datetime import date
technical_answers = {}
technical_score = {}
technical_total = {}
word_bank = [...]
questions = [...]
technical_questions = [
    {
        "question": "What does Transformer mean?",
        "options": ["A) Rele", "B) Transformator", "C) Generator", "D) Kabel"],
        "answer": "B"
    },
    {
        "question": "What does Relay mean?",
        "options": ["A) Rele", "B) O'chirgich", "C) Generator", "D) Shina"],
        "answer": "A"
    },
    {
        "question": "What does Circuit Breaker mean?",
        "options": ["A) Transformator", "B) Kabel", "C) O'chirgich", "D) Rele"],
        "answer": "C"
    }
]
@bot.message_handler(commands=['tquiz'])
def technical_quiz(message):

    chat_id = message.chat.id

    technical_score[chat_id] = 0
    technical_total[chat_id] = 0

    q = random.choice(technical_questions)

    technical_answers[chat_id] = q

    text = f"""
⚡ Technical Quiz

Question 1/10

{q['question']}

{chr(10).join(q['options'])}

Reply with A, B, C or D.
"""
technical_topics = [

"""
⚡ Transformers

Transformer — Transformator
Core — O'zak
Winding — Chulg'am
Cooling System — Sovitish tizimi
Tap Changer — Tarmoqlagich

Example:

The transformer is operating normally.

Transformator normal ishlamoqda.
""",

"""
⚡ Relay Protection

Relay — Rele
Protection — Himoya
Fault — Nosozlik
Overcurrent — Ortiqcha tok
Earth Fault — Yerga tutashuv

Example:

The relay detected an earth fault.

Rele yerga tutashuvni aniqladi.
""",

"""
⚡ Circuit Breakers

Circuit Breaker — O'chirgich
Trip — O'chish
Close — Yopish
Open — Ochish

Example:

The circuit breaker tripped due to a fault.

Nosozlik sababli o'chirgich ishladi.
""",

"""
⚡ SCADA

SCADA — Monitoring System
Alarm — Signal
Monitoring — Kuzatish
Control — Boshqaruv

Example:

The SCADA system shows an alarm.

SCADA tizimi signal ko'rsatmoqda.
""",

"""
⚡ Wind Turbine

Blade — Parraq
Generator — Generator
Pitch System — Pitch tizimi
Yaw System — Yaw tizimi

Example:

The wind turbine is generating power.

Shamol turbinasi energiya ishlab chiqarmoqda.
""",

"""
⚡ Substation

Substation — Podstansiya
Busbar — Shina
Bay — Yacheyka
Switchgear — KRU

Example:

The substation is operating normally.

Podstansiya normal ishlamoqda.
"""]
bot.send_message(chat_id, text)
grammar_topics = [...]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True)

    btn1 = types.KeyboardButton("📚 Daily Words")
    btn2 = types.KeyboardButton("⚡ Technical English")
    btn3 = types.KeyboardButton("📝 Quiz")
    btn4 = types.KeyboardButton("📖 Grammar")
    btn5 = types.KeyboardButton("💎 Premium")
    btn6 = types.KeyboardButton("🤖 AI Teacher")
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5, btn6)

    bot.send_message(
        message.chat.id,
        "🇬🇧 Welcome to English Teacher Bot!\n\nChoose an option:",
        reply_markup=markup
    )

@bot.message_handler(commands=['words'])
def words(message):

    chat_id = message.chat.id
    today = str(date.today())

    if chat_id not in daily_words:
        daily_words[chat_id] = {}

    if today not in daily_words[chat_id]:
        daily_words[chat_id][today] = random.sample(word_bank, 10)

    words_today = daily_words[chat_id] [today]
    text = " 📚 today's 10 Words\n\n"

    for i, word in enumerate(words_today, start=1):
        text += f"{i}. {word[0]} — {word[1]}\n"

    bot.send_message(chat_id, text)
word_bank = [
    ("Achieve", "Erishmoq"),
    ("Improve", "Yaxshilamoq"),
    ("Develop", "Rivojlantirmoq"),
    ("Maintain", "Saqlab turmoq"),
    ("Perform", "Bajarmoq"),
    ("Increase", "Oshirmoq"),
    ("Support", "Qo'llab-quvvatlamoq"),
    ("Require", "Talab qilmoq"),
    ("Provide", "Taqdim etmoq"),
    ("Manage", "Boshqarmoq"),
    ("Control", "Nazorat qilmoq"),
    ("Build", "Qurmoq"),
    ("Create", "Yaratmoq"),
    ("Reduce", "Kamaytirmoq"),
    ("Repair", "Ta'mirlamoq"),
    ("Check", "Tekshirmoq"),
    ("Learn", "O'rganmoq"),
    ("Understand", "Tushunmoq"),
    ("Read", "O'qimoq"),
    ("Write", "Yozmoq"),
    ("Buy", "Sotib olmoq"),
    ("Sell", "Sotmoq"),
    ("Complete", "Yakunlamoq"),
    ("Prepare", "Tayyorlamoq"),
    ("Connect", "Ulamoq"),
    ("Install", "O'rnatmoq"),
    ("Operate", "Boshqarmoq"),
    ("Protect", "Himoya qilmoq"),
    ("Monitor", "Kuzatmoq"),
    ("Deliver", "Yetkazib bermoq")
]

@bot.message_handler(commands=['technical'])
def technical(message):

    topic = random.choice(technical_topics)

    bot.send_message(
        message.chat.id,
        topic
    )
    technical_topics = [

"""
⚡ Transformers

Transformer — Transformator
Winding — Chulg'am
Core — O'zak
Cooling System — Sovitish tizimi
Tap Changer — Tarmoqlagich

Example:

The transformer is operating normally.

Transformator normal ishlamoqda.
""",

"""
⚡ Circuit Breakers

Circuit Breaker — O'chirgich
Trip — O'chish
Close — Yopish
Open — Ochish
Protection Relay — Himoya relesi

Example:

The circuit breaker tripped due to a fault.

Nosozlik sababli o'chirgich ishladi.
""",

"""
⚡ Relay Protection

Relay — Rele
Protection — Himoya
Fault — Nosozlik
Overcurrent — Ortiqcha tok
Earth Fault — Yerga tutashuv

Example:

The relay detected an earth fault.

Rele yerga tutashuvni aniqladi.
""",

"""
⚡ SCADA

SCADA — Supervisory Control and Data Acquisition
Alarm — Signal
Monitoring — Kuzatish
Control — Boshqaruv
Data — Ma'lumot

Example:

The SCADA system shows an alarm.

SCADA tizimi signal ko'rsatmoqda.
""",

"""
⚡ Wind Turbine

Wind Turbine — Shamol turbinasi
Blade — Parraq
Generator — Generator
Yaw System — Yaw tizimi
Pitch System — Pitch tizimi

Example:

The wind turbine is generating power.

Shamol turbinasi energiya ishlab chiqarmoqda.
""",

"""
⚡ Substation

Substation — Podstansiya
Busbar — Shina
Transformer — Transformator
Bay — Yacheyka
Switchgear — KRU

Example:

The substation is operating normally.

Podstansiya normal ishlamoqda.
"""
]
@bot.message_handler(commands=['quiz'])
def quiz(message):

    chat_id = message.chat.id

    user_scores[chat_id] = 0
    user_total[chat_id] = 0

    q = random.choice(questions)

    user_answers[chat_id] = q

    text = f"""
Quiz

{q['question']}

{chr(10).join(q['options'])}

Reply with A, B, C or D.
"""

    bot.send_message(chat_id, text)
import random

questions = [
    {
        "question": "What does ACHIEVE mean?",
        "options": ["A) Kutmoq", "B) Erishmoq", "C) Yemoq", "D) Yugurmoq"],
        "answer": "B"
    },
    {
        "question": "What does DEVELOP mean?",
        "options": ["A) Rivojlantirmoq", "B) Yo'qotmoq", "C) Kutmoq", "D) O'tirmoq"],
        "answer": "A"
    },
    {
        "question": "What does MAINTAIN mean?",
        "options": ["A) Buzmoq", "B) Saqlab turmoq", "C) Sotmoq", "D) Kutmoq"],
        "answer": "B"
    },
    {
        "question": "What does SUPPORT mean?",
        "options": ["A) Qochmoq", "B) Qo'llab-quvvatlamoq", "C) O'qimoq", "D) Yozmoq"],
        "answer": "B"
    },
    {
    "question": "What does PROVIDE mean?",
    "options": ["A) Taqdim etmoq", "B) Kutmoq", "C) Yugurmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does REQUIRE mean?",
    "options": ["A) Talab qilmoq", "B) Sotmoq", "C) Buzmoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does MANAGE mean?",
    "options": ["A) Boshqarmoq", "B) O'qimoq", "C) Yemoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does REPAIR mean?",
    "options": ["A) Ta'mirlamoq", "B) Sotmoq", "C) Kutmoq", "D) O'chirmoq"],
    "answer": "A"
},
{
    "question": "What does CHECK mean?",
    "options": ["A) Tekshirmoq", "B) Yugurmoq", "C) Yozmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does CONTROL mean?",
    "options": ["A) Nazorat qilmoq", "B) Kutmoq", "C) Yemoq", "D) Sotmoq"],
    "answer": "A"
},
{
    "question": "What does CREATE mean?",
    "options": ["A) Yaratmoq", "B) Uchirmoq", "C) Kutmoq", "D) Buzmoq"],
    "answer": "A"
},
{
    "question": "What does BUILD mean?",
    "options": ["A) Qurmoq", "B) O'qimoq", "C) Sotmoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does LEARN mean?",
    "options": ["A) O'rganmoq", "B) Sotmoq", "C) Kutmoq", "D) Yutmoq"],
    "answer": "A"
},
{
    "question": "What does UNDERSTAND mean?",
    "options": ["A) Tushunmoq", "B) Qochmoq", "C) Yemoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does COMPLETE mean?",
    "options": ["A) Yakunlamoq", "B) Kutmoq", "C) O'chirmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does PRODUCE mean?",
    "options": ["A) Ishlab chiqarmoq", "B) Sotmoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does INCREASE mean?",
    "options": ["A) Oshirmoq", "B) Kamaytirmoq", "C) Buzmoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does REDUCE mean?",
    "options": ["A) Kamaytirmoq", "B) Oshirmoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does SELL mean?",
    "options": ["A) Sotmoq", "B) Sotib olmoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does BUY mean?",
    "options": ["A) Sotib olmoq", "B) Sotmoq", "C) Kutmoq", "D) Buzmoq"],
    "answer": "A"
},
{
    "question": "What does WAIT mean?",
    "options": ["A) Kutmoq", "B) Yugurmoq", "C) Yemoq", "D) Sotmoq"],
    "answer": "A"
},
{
    "question": "What does WRITE mean?",
    "options": ["A) Yozmoq", "B) O'qimoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does READ mean?",
    "options": ["A) O'qimoq", "B) Yozmoq", "C) Kutmoq", "D) Buzmoq"],
    "answer": "A"
},
{
    "question": "What does IMPROVE mean?",
    "options": ["A) Yaxshilamoq", "B) Buzmoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
]
@bot.message_handler(commands=['grammar'])
def grammar(message):

    topic = random.choice(grammar_topics)

    bot.send_message(
        message.chat.id,
        topic
    )
grammar_topics = [
"""
📖 Present Simple

✅ I work
✅ You work
✅ He works

Examples:

I work at a wind farm.
Men shamol elektr stansiyasida ishlayman.

He works in a substation.
U podstansiyada ishlaydi.
""",

"""
📖 Present Continuous

✅ I am working
✅ You are working
✅ He is working

Examples:

I am working now.
Men hozir ishlayapman.

He is repairing a transformer.
U transformatorni ta'mirlayapti.
""",

"""
📖 Past Simple

✅ I worked
✅ You worked
✅ He worked

Examples:

I worked yesterday.
Men kecha ishladim.

We repaired the fault.
Biz nosozlikni tuzatdik.
""",

"""
📖 Future Simple

✅ I will work
✅ You will work
✅ He will work

Examples:

I will visit the substation tomorrow.

Men ertaga podstansiyaga boraman.
""",

"""
📖 Modal Verbs

✅ Can
✅ Must
✅ Should

Examples:

You must wear PPE.

Siz PPE kiyishingiz kerak.

You should check the relay.

Siz releni tekshirishingiz kerak.
"""
]
@bot.message_handler(commands=['quiz'])
def quiz(message):

    q = random.choice(questions)

    text = f"""
Quiz

{q['question']}

{chr(10).join(q['options'])}

Reply with A, B, C or D.
"""

    bot.send_message(message.chat.id, text)

    q = random.choice(questions)

    text = f"""
    Quiz

    {q['question']}

    {chr(10).join(q['options'])}

    Reply with A, B, C or D.
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['premium'])
def premium(message):

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    btn1 = types.KeyboardButton("⭐ Basic")
    btn2 = types.KeyboardButton("🚀 Pro")
    btn3 = types.KeyboardButton("⚡ Engineer Pro")

    markup.row(btn1, btn2)
    markup.row(btn3)

bot.send_message(
        message.chat.id,
        "💎 Choose a Premium Plan:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda m: m.text in ["A", "B", "C", "D"])
def check_answer(message):

    chat_id = message.chat.id

    if chat_id not in user_answers:
        return

    q = user_answers[chat_id]

    user_total[chat_id] += 1

    if message.text == q["answer"]:
        user_scores[chat_id] += 1

        bot.send_message(
            chat_id,
            f"✅ Correct!\n\nScore: {user_scores[chat_id]}/{user_total[chat_id]}"
        )
    else:
        bot.send_message(
            chat_id,
            f"❌ Wrong!\nCorrect answer: {q['answer']}\n\nScore: {user_scores[chat_id]}/{user_total[chat_id]}"
        )

    # 10 ta savoldan keyin yakunlash

    if user_total[chat_id] >= 10:

        percent = int(
            user_scores[chat_id] * 100 / user_total[chat_id]
        )

        if percent >= 90:
            rank = "🥇 Advanced"
        elif percent >= 70:
            rank = "🥈 Intermediate"
        else:
            rank = "🥉 Beginner"

        bot.send_message(
            chat_id,
            f"""
🏁 Quiz Finished

✅ Correct: {user_scores[chat_id]}
❌ Wrong: {user_total[chat_id] - user_scores[chat_id]}

📊 Score: {percent}%

🏆 Rank: {rank}
"""
        )

        return

    next_q = random.choice(questions)

    user_answers[chat_id] = next_q

    text = f"""
    Question {user_total[chat_id] + 1}/10

    {next_q['question']}

    {chr(10).join(next_q['options'])}

    Reply with A, B, C or D.
        """

    bot.send_message(chat_id, text)
    @bot.message_handler(commands=['profile'])
    def profile(message):
                chat_id = message.chat.id
        
                best = best_score.get(chat_id, 0)
                count = quiz_count.get(chat_id, 0)
        
                if best >= 90:
                    rank = "🥇 Advanced"
                elif best >= 70:
                    rank = "🥈 Intermediate"
                else:
                    rank = "🥉 Beginner"
                    bot.send_message(
                chat_id,
                f"""
        👤 Profile
        
        🏆 Rank: {rank}
        
        📊 Best Score: {best}%
        
        ✅ Quizzes Completed: {count}
        """
            )
print("English Teacher Bot Started...")
@bot.message_handler(func=lambda message: True)
def buttons(message):

    if message.text == "📚 Daily Words":
        words(message)

    elif message.text == "⚡ Technical English":
        technical(message)

    elif message.text == "📝 Quiz":
        quiz(message)

    elif message.text == "📖 Grammar":
        grammar(message)

    elif message.text == "💎 Premium":
        premium(message)
bot.infinity_polling()
=======
import telebot
from telebot import types
import random
import os
from datetime import date
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
user_answers = {}
user_scores = {}
user_total = {}
quiz_count = {}
best_score = {}
daily_words = {}
from datetime import date
technical_answers = {}
technical_score = {}
technical_total = {}
word_bank = [...]
questions = [...]
technical_questions = [
    {
        "question": "What does Transformer mean?",
        "options": ["A) Rele", "B) Transformator", "C) Generator", "D) Kabel"],
        "answer": "B"
    },
    {
        "question": "What does Relay mean?",
        "options": ["A) Rele", "B) O'chirgich", "C) Generator", "D) Shina"],
        "answer": "A"
    },
    {
        "question": "What does Circuit Breaker mean?",
        "options": ["A) Transformator", "B) Kabel", "C) O'chirgich", "D) Rele"],
        "answer": "C"
    }
]
@bot.message_handler(commands=['tquiz'])
def technical_quiz(message):

    chat_id = message.chat.id

    technical_score[chat_id] = 0
    technical_total[chat_id] = 0

    q = random.choice(technical_questions)

    technical_answers[chat_id] = q

    text = f"""
⚡ Technical Quiz

Question 1/10

{q['question']}

{chr(10).join(q['options'])}

Reply with A, B, C or D.
"""
technical_topics = [

"""
⚡ Transformers

Transformer — Transformator
Core — O'zak
Winding — Chulg'am
Cooling System — Sovitish tizimi
Tap Changer — Tarmoqlagich

Example:

The transformer is operating normally.

Transformator normal ishlamoqda.
""",

"""
⚡ Relay Protection

Relay — Rele
Protection — Himoya
Fault — Nosozlik
Overcurrent — Ortiqcha tok
Earth Fault — Yerga tutashuv

Example:

The relay detected an earth fault.

Rele yerga tutashuvni aniqladi.
""",

"""
⚡ Circuit Breakers

Circuit Breaker — O'chirgich
Trip — O'chish
Close — Yopish
Open — Ochish

Example:

The circuit breaker tripped due to a fault.

Nosozlik sababli o'chirgich ishladi.
""",

"""
⚡ SCADA

SCADA — Monitoring System
Alarm — Signal
Monitoring — Kuzatish
Control — Boshqaruv

Example:

The SCADA system shows an alarm.

SCADA tizimi signal ko'rsatmoqda.
""",

"""
⚡ Wind Turbine

Blade — Parraq
Generator — Generator
Pitch System — Pitch tizimi
Yaw System — Yaw tizimi

Example:

The wind turbine is generating power.

Shamol turbinasi energiya ishlab chiqarmoqda.
""",

"""
⚡ Substation

Substation — Podstansiya
Busbar — Shina
Bay — Yacheyka
Switchgear — KRU

Example:

The substation is operating normally.

Podstansiya normal ishlamoqda.
"""]

grammar_topics = [...]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True)

    btn1 = types.KeyboardButton("📚 Daily Words")
    btn2 = types.KeyboardButton("⚡ Technical English")
    btn3 = types.KeyboardButton("📝 Quiz")
    btn4 = types.KeyboardButton("📖 Grammar")
    btn5 = types.KeyboardButton("💎 Premium")

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)

    bot.send_message(
        message.chat.id,
        "🇬🇧 Welcome to English Teacher Bot!\n\nChoose an option:",
        reply_markup=markup
    )

@bot.message_handler(commands=['words'])
def words(message):

    chat_id = message.chat.id
    today = str(date.today())

    if chat_id not in daily_words:
        daily_words[chat_id] = {}

    if today not in daily_words[chat_id]:
        daily_words[chat_id][today] = random.sample(word_bank, 10)

    words_today = daily_words[chat_id] [today]
    text = " 📚 today's 10 Words\n\n"

    for i, word in enumerate(words_today, start=1):
        text += f"{i}. {word[0]} — {word[1]}\n"

    bot.send_message(chat_id, text)
word_bank = [
    ("Achieve", "Erishmoq"),
    ("Improve", "Yaxshilamoq"),
    ("Develop", "Rivojlantirmoq"),
    ("Maintain", "Saqlab turmoq"),
    ("Perform", "Bajarmoq"),
    ("Increase", "Oshirmoq"),
    ("Support", "Qo'llab-quvvatlamoq"),
    ("Require", "Talab qilmoq"),
    ("Provide", "Taqdim etmoq"),
    ("Manage", "Boshqarmoq"),
    ("Control", "Nazorat qilmoq"),
    ("Build", "Qurmoq"),
    ("Create", "Yaratmoq"),
    ("Reduce", "Kamaytirmoq"),
    ("Repair", "Ta'mirlamoq"),
    ("Check", "Tekshirmoq"),
    ("Learn", "O'rganmoq"),
    ("Understand", "Tushunmoq"),
    ("Read", "O'qimoq"),
    ("Write", "Yozmoq"),
    ("Buy", "Sotib olmoq"),
    ("Sell", "Sotmoq"),
    ("Complete", "Yakunlamoq"),
    ("Prepare", "Tayyorlamoq"),
    ("Connect", "Ulamoq"),
    ("Install", "O'rnatmoq"),
    ("Operate", "Boshqarmoq"),
    ("Protect", "Himoya qilmoq"),
    ("Monitor", "Kuzatmoq"),
    ("Deliver", "Yetkazib bermoq")
]

@bot.message_handler(commands=['technical'])
def technical(message):

    topic = random.choice(technical_topics)

    bot.send_message(
        message.chat.id,
        topic
    )
    technical_topics = [

"""
⚡ Transformers

Transformer — Transformator
Winding — Chulg'am
Core — O'zak
Cooling System — Sovitish tizimi
Tap Changer — Tarmoqlagich

Example:

The transformer is operating normally.

Transformator normal ishlamoqda.
""",

"""
⚡ Circuit Breakers

Circuit Breaker — O'chirgich
Trip — O'chish
Close — Yopish
Open — Ochish
Protection Relay — Himoya relesi

Example:

The circuit breaker tripped due to a fault.

Nosozlik sababli o'chirgich ishladi.
""",

"""
⚡ Relay Protection

Relay — Rele
Protection — Himoya
Fault — Nosozlik
Overcurrent — Ortiqcha tok
Earth Fault — Yerga tutashuv

Example:

The relay detected an earth fault.

Rele yerga tutashuvni aniqladi.
""",

"""
⚡ SCADA

SCADA — Supervisory Control and Data Acquisition
Alarm — Signal
Monitoring — Kuzatish
Control — Boshqaruv
Data — Ma'lumot

Example:

The SCADA system shows an alarm.

SCADA tizimi signal ko'rsatmoqda.
""",

"""
⚡ Wind Turbine

Wind Turbine — Shamol turbinasi
Blade — Parraq
Generator — Generator
Yaw System — Yaw tizimi
Pitch System — Pitch tizimi

Example:

The wind turbine is generating power.

Shamol turbinasi energiya ishlab chiqarmoqda.
""",

"""
⚡ Substation

Substation — Podstansiya
Busbar — Shina
Transformer — Transformator
Bay — Yacheyka
Switchgear — KRU

Example:

The substation is operating normally.

Podstansiya normal ishlamoqda.
"""
]
@bot.message_handler(commands=['quiz'])
def quiz(message):

    chat_id = message.chat.id

    user_scores[chat_id] = 0
    user_total[chat_id] = 0

    q = random.choice(questions)

    user_answers[chat_id] = q

    text = f"""
Quiz

{q['question']}

{chr(10).join(q['options'])}

Reply with A, B, C or D.
"""

    bot.send_message(chat_id, text)
import random

questions = [
    {
        "question": "What does ACHIEVE mean?",
        "options": ["A) Kutmoq", "B) Erishmoq", "C) Yemoq", "D) Yugurmoq"],
        "answer": "B"
    },
    {
        "question": "What does DEVELOP mean?",
        "options": ["A) Rivojlantirmoq", "B) Yo'qotmoq", "C) Kutmoq", "D) O'tirmoq"],
        "answer": "A"
    },
    {
        "question": "What does MAINTAIN mean?",
        "options": ["A) Buzmoq", "B) Saqlab turmoq", "C) Sotmoq", "D) Kutmoq"],
        "answer": "B"
    },
    {
        "question": "What does SUPPORT mean?",
        "options": ["A) Qochmoq", "B) Qo'llab-quvvatlamoq", "C) O'qimoq", "D) Yozmoq"],
        "answer": "B"
    },
    {
    "question": "What does PROVIDE mean?",
    "options": ["A) Taqdim etmoq", "B) Kutmoq", "C) Yugurmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does REQUIRE mean?",
    "options": ["A) Talab qilmoq", "B) Sotmoq", "C) Buzmoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does MANAGE mean?",
    "options": ["A) Boshqarmoq", "B) O'qimoq", "C) Yemoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does REPAIR mean?",
    "options": ["A) Ta'mirlamoq", "B) Sotmoq", "C) Kutmoq", "D) O'chirmoq"],
    "answer": "A"
},
{
    "question": "What does CHECK mean?",
    "options": ["A) Tekshirmoq", "B) Yugurmoq", "C) Yozmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does CONTROL mean?",
    "options": ["A) Nazorat qilmoq", "B) Kutmoq", "C) Yemoq", "D) Sotmoq"],
    "answer": "A"
},
{
    "question": "What does CREATE mean?",
    "options": ["A) Yaratmoq", "B) Uchirmoq", "C) Kutmoq", "D) Buzmoq"],
    "answer": "A"
},
{
    "question": "What does BUILD mean?",
    "options": ["A) Qurmoq", "B) O'qimoq", "C) Sotmoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does LEARN mean?",
    "options": ["A) O'rganmoq", "B) Sotmoq", "C) Kutmoq", "D) Yutmoq"],
    "answer": "A"
},
{
    "question": "What does UNDERSTAND mean?",
    "options": ["A) Tushunmoq", "B) Qochmoq", "C) Yemoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does COMPLETE mean?",
    "options": ["A) Yakunlamoq", "B) Kutmoq", "C) O'chirmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does PRODUCE mean?",
    "options": ["A) Ishlab chiqarmoq", "B) Sotmoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does INCREASE mean?",
    "options": ["A) Oshirmoq", "B) Kamaytirmoq", "C) Buzmoq", "D) Kutmoq"],
    "answer": "A"
},
{
    "question": "What does REDUCE mean?",
    "options": ["A) Kamaytirmoq", "B) Oshirmoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does SELL mean?",
    "options": ["A) Sotmoq", "B) Sotib olmoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does BUY mean?",
    "options": ["A) Sotib olmoq", "B) Sotmoq", "C) Kutmoq", "D) Buzmoq"],
    "answer": "A"
},
{
    "question": "What does WAIT mean?",
    "options": ["A) Kutmoq", "B) Yugurmoq", "C) Yemoq", "D) Sotmoq"],
    "answer": "A"
},
{
    "question": "What does WRITE mean?",
    "options": ["A) Yozmoq", "B) O'qimoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
{
    "question": "What does READ mean?",
    "options": ["A) O'qimoq", "B) Yozmoq", "C) Kutmoq", "D) Buzmoq"],
    "answer": "A"
},
{
    "question": "What does IMPROVE mean?",
    "options": ["A) Yaxshilamoq", "B) Buzmoq", "C) Kutmoq", "D) Yemoq"],
    "answer": "A"
},
]
@bot.message_handler(commands=['grammar'])
def grammar(message):

    topic = random.choice(grammar_topics)

    bot.send_message(
        message.chat.id,
        topic
    )
grammar_topics = [
"""
📖 Present Simple

✅ I work
✅ You work
✅ He works

Examples:

I work at a wind farm.
Men shamol elektr stansiyasida ishlayman.

He works in a substation.
U podstansiyada ishlaydi.
""",

"""
📖 Present Continuous

✅ I am working
✅ You are working
✅ He is working

Examples:

I am working now.
Men hozir ishlayapman.

He is repairing a transformer.
U transformatorni ta'mirlayapti.
""",

"""
📖 Past Simple

✅ I worked
✅ You worked
✅ He worked

Examples:

I worked yesterday.
Men kecha ishladim.

We repaired the fault.
Biz nosozlikni tuzatdik.
""",

"""
📖 Future Simple

✅ I will work
✅ You will work
✅ He will work

Examples:

I will visit the substation tomorrow.

Men ertaga podstansiyaga boraman.
""",

"""
📖 Modal Verbs

✅ Can
✅ Must
✅ Should

Examples:

You must wear PPE.

Siz PPE kiyishingiz kerak.

You should check the relay.

Siz releni tekshirishingiz kerak.
"""
]
@bot.message_handler(commands=['quiz'])
def quiz(message):

    q = random.choice(questions)

    text = f"""
Quiz

{q['question']}

{chr(10).join(q['options'])}

Reply with A, B, C or D.
"""

    bot.send_message(message.chat.id, text)

    q = random.choice(questions)

    text = f"""
    Quiz

    {q['question']}

    {chr(10).join(q['options'])}

    Reply with A, B, C or D.
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['premium'])
def premium(message):
    bot.send_message(
        message.chat.id,
        """
💎 Premium

✅ 30 words per day
✅ IELTS Vocabulary
✅ Business English
✅ Technical English
✅ AI Teacher

49,000 UZS / month
"""
    )
@bot.message_handler(func=lambda m: m.text in ["A", "B", "C", "D"])
def check_answer(message):

    chat_id = message.chat.id

    if chat_id not in user_answers:
        return

    q = user_answers[chat_id]

    user_total[chat_id] += 1

    if message.text == q["answer"]:
        user_scores[chat_id] += 1

        bot.send_message(
            chat_id,
            f"✅ Correct!\n\nScore: {user_scores[chat_id]}/{user_total[chat_id]}"
        )
    else:
        bot.send_message(
            chat_id,
            f"❌ Wrong!\nCorrect answer: {q['answer']}\n\nScore: {user_scores[chat_id]}/{user_total[chat_id]}"
        )

    # 10 ta savoldan keyin yakunlash

    if user_total[chat_id] >= 10:

        percent = int(
            user_scores[chat_id] * 100 / user_total[chat_id]
        )

        if percent >= 90:
            rank = "🥇 Advanced"
        elif percent >= 70:
            rank = "🥈 Intermediate"
        else:
            rank = "🥉 Beginner"

        bot.send_message(
            chat_id,
            f"""
🏁 Quiz Finished

✅ Correct: {user_scores[chat_id]}
❌ Wrong: {user_total[chat_id] - user_scores[chat_id]}

📊 Score: {percent}%

🏆 Rank: {rank}
"""
        )

        return

    next_q = random.choice(questions)

    user_answers[chat_id] = next_q

    text = f"""
    Question {user_total[chat_id] + 1}/10

    {next_q['question']}

    {chr(10).join(next_q['options'])}

    Reply with A, B, C or D.
        """

    bot.send_message(chat_id, text)
    @bot.message_handler(commands=['profile'])
    def profile(message):
                chat_id = message.chat.id
        
                best = best_score.get(chat_id, 0)
                count = quiz_count.get(chat_id, 0)
        
                if best >= 90:
                    rank = "🥇 Advanced"
                elif best >= 70:
                    rank = "🥈 Intermediate"
                else:
                    rank = "🥉 Beginner"
                    bot.send_message(
                chat_id,
                f"""
        👤 Profile
        
        🏆 Rank: {rank}
        
        📊 Best Score: {best}%
        
        ✅ Quizzes Completed: {count}
        """
            )
print("English Teacher Bot Started...")
@bot.message_handler(func=lambda message: True)
def buttons(message):

    if message.text == "📚 Daily Words":
        words(message)

    elif message.text == "⚡ Technical English":
        technical(message)

    elif message.text == "📝 Quiz":
        quiz(message)

    elif message.text == "📖 Grammar":
        grammar(message)

    elif message.text == "💎 Premium":
        premium(message)
bot.infinity_polling()
>>>>>>> a31fe0841ce9a704b4780a84284710efa226d625
