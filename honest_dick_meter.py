import telebot
import random
import logging
import os

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TG_TOKEN = os.getenv("TG_TOKEN")

BOT_USERNAME = "honest_dick_meter_bot"  # Replace with your bot's username (without @)

bot = telebot.TeleBot(TG_TOKEN, parse_mode="HTML")  # Enable HTML parsing if needed


low_number_phrases = [
    "ый пиздорванец",
    "ый кукумбер",
    "ый елдак",
    "ый доктороский щекотунчик",
    "ый черный шофёр",
    "ый юрец на голде гиза",
    "ая сосиска муравья",
    "ый член-невидимка",
    "ая лего-версия",
    "ый короткоствол",
    "ый борин обрез",
    "ый чехол буя",
    "ый дятел в дупле",
    "ый нефритовый жезл",
    "ый молочный хуишко",
    "ая анальная затычка",
    "ое недоразумение!",
    "ая стат. погрешность!",
    "ая дудка-волосянка",
    "ое дрочило",
    "ый боброчёс",
    "ый потный мексиканец",
    "ый быстрый гонзалес",
    "ый молчаливый боб",
    "ая хуинушка",
    "ый посошок",
    "ый маленький мук",
    "ый член-корреспондента",
    "ый ванька-встанька",
    "ый часовой у мавзолея",
    "ый боец невидимого фронта",
    "ый влагалищный кракен",
    "ый шириночный левиафан",
    "ый мертвый орёл",
    "ый гонорейный камикадзе",
    "ый мелкий чиновник",
    "ый опытный аппаратчик",
    "ый ржавый обрез",
    "ый терпкий пиструн",
    "ый солоноватый гриб",
    "ый чили-вили",
    "ый шершавчик",
    "ый кыштымский карлик",
    "ый сахарный фюррер"
    ]

high_number_phrases = [
    "ый короткоствол",
    "ая богатырская колбаса",
    "ый посох Гэндальфа",
    "ая ручка передач",
    "ый болтяра",
    "ый вялый питон",
    "ый кожаный шланг",
    "ая палочка-выручалочка",
    "ый усмиритель Олекса",
    "ая сигара Фиделя",
    "ый Клякс посреди редакции",
    "ая усатая сигара",
    "ая дудка-волосянка",
    "ое дрочило",
    "ый боброчёс",
    "ый потный мексиканец",
    "ый быстрый гонзалес",
    "ый молчаливый боб",
    "ая хуинушка",
    "ый посошок",
    "ый член-корреспондента",
    "ый ванька-встанька",
    "ый часовой у мавзолея",
    "ый боец невидимого фронта",
    "ый влагалищный кракен",
    "ый шириночный левиафан",
    "ый мертвый орёл",
    "ый гонорейный камикадзе",
    "ый опытный аппаратчик",
    "ый ржавый обрез",
    "ый терпкий пиструн",
    "ый солоноватый гриб",
    "ый биг бен",
    "ая эйфелева башня",
    "ая статуя свободы",
    "ая пирамида Хеопса",
    "ый колосс Родосский",
    "ый небоскреб",
    "ый чили-вили",
    "ый шершавчик",
    "ый кыштымский карлик",
    "ый сахарный фюрер",
    "ый сломанный банан"
     ]

@bot.inline_handler(lambda query: True)  
def inline_response(query):
    
    if random.random() < 0.1:
        number = 0
        response_text = "0"
        message_text = f"Вас посетили гномы-хуекрады, член не найден"
    elif random.random() < 0.5:
        number = random.randint(11, 25)
        response_text = random.choice(high_number_phrases)
        message_text = f"{number}-сантиметров{response_text}"
    else:
        number = random.randint(1, 10)
        response_text = random.choice(low_number_phrases)
        message_text = f"{number}-сантиметров{response_text}"    

    # Log the response
    logging.info(f"User: {query.from_user.username or 'UnknownUser'} -> {number}: {response_text}")

    result = telebot.types.InlineQueryResultArticle(
        id="generate_random",
        title="щас замерим твой струч",  # Fixed option title
        #description="Tap to generate a random number and phrase",
        input_message_content=telebot.types.InputTextMessageContent(
            message_text=message_text, parse_mode="HTML"
        )
    )

    bot.answer_inline_query(query.id, [result], cache_time=1)  # Shows only this fixed option

# Start the bot
logging.info("Inline bot is running with instant random response...")
bot.polling()