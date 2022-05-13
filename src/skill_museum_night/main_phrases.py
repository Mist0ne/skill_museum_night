# flake8: noqa

welcome_text = {
    "text": """Васнецов или Серебрякова? «Девочка с персиками» или «с крынкой молока»? Попробуйте угадать!

Вместе с Культура РФ мы выбрали 53 картины русских художников, а нейросеть перерисовала их в непривычных стилях: экспрессионизм, палитивизм и импрессионизм. Теперь полотна выглядят по-другому, и ваша задача — отгадать оригинал.

Пройдите игру и узнайте, как выиграть умную колонку со мной внутри.

Начнём играть?
""",
    "tts": """Васнецов или Серебрякова? «Девочка ^с персиками»^ или «с крынкой молока»? ^Попробуйте^ угадать! Вместе с Культура РФ мы выбрали 53 картины русских художников, а нейросеть перерисовала их в непривычных стилях. ^Экспрессионизм^, палитивизм и импрессионизм. Теперь пол`отна выглядят по-другому, и ^ваша^ задача — отгадать оригинал. Пройдите игру и узнайте, ^как^ выиграть умную колонку со мной внутри. Начнём играть?""",
    "suggests": [
        "Начать",
        "Как выиграть Капсулу Мини"
    ]
}

exit_texts = [
    {
        "text": "Очень жаль, но, если что, возвращайтесь. У меня ещё много картин.",
        "tts": "Очень жаль, но, если что, возвращайтесь. У меня ещё ^много^ картин."
    },
    {
        "text": "Устали? Возвращайтесь в любой момент. Буду ждать вас тут.",
        "tts": "Устали? Возвращайтесь в любой ^момент^. Буду ждать вас тут."
    },
    {
        "text": "Надеюсь вы ещё вернётесь. У меня осталось много интересного.",
        "tts": "^Надеюсь^ вы ещё вернётесь. У меня осталось много интересного."
    },
    {
        "text": "Если что, я всегда тут. Так что возвращайтесь в любой момент.",
        "tts": "Если ^что^, я всегда тут. Так что возвращайтесь в любой момент."
    }
]

exit_call = {
    "title": "Участвуйте в розыгрыше.",
    "text": "Всего пара кликов, и вы уже на шаг ближе к Капсуле Мини.",
    "url": "https://vk.com/marusia",
    "image_url": "https://psv4.userapi.com/c237131/u71480982/docs/d44/1fb5d43c0268/logo_RGB-03_2.png?extra=aXZF0gpFytTulqA2xYrSJntSgE97SwBH-0XQoFIFFy3nEUtZ1ZoOAuZ4fzDk9weno__yBbM3SWirqvZxQGeGtThpsOWpciIc7k9rT3Vg3iwUAc4GlIHmPrdEiB2LLPJTgEzrAS5V5h2SHsnS8k9v"
}

rules = {
    "text": """Мы обещали рассказать, как выиграть Капсулу Мини

1) Подпишитесь на группу Маруси и Культура РФ в ВКонтакте 
2) Выложите на стену понравившуюся нейрокартину или свой статус
3) Поставьте к записи хэштег #нейромаруся

Мы разыграем среди участников специальные призы.
Результаты розыгрыша мы объявим 26.05 в нашей группе ВКонтакте""",
    "tts": "Мы обещали рассказать, ^как^ выиграть Капсулу Мини. ^Подпишитесь^ на группу Маруси и Культура РФ в ВКонтакте. Выложите на стену понравившуюся нейракарт`ину или свой ^статус^. Поставьте к записи ^хэшт`ег^ ^нейрамаруся^. Мы разыграем среди участников специальные ^призы^. Результаты розыгрыша мы объявим двадцать шестого мая в нашей группе ВКонтакте."
}

what_picture_questions = [
    {
        "text": "Какая это картина?",
        "tts": "^Какая^ это картина?"
    },
    {
        "text": "Что это за картина?",
        "tts": "^Что^ это за картина?"
    },
    {
        "text": "Как называется эта картина?",
        "tts": "Как называется ^эта^ картина?"
    },
    {
        "text": "Название картины?",
        "tts": "^Название^ картины?"
    },
    {
        "text": "Имя этой картины?",
        "tts": "^Имя^ этой картины?"
    },
    {
        "text": "Эта картина называется?",
        "tts": "Эта картина ^называется^?"
    }
]

dont_know_phrases = [
    {
        "text": "Ну ничего. Наверняка вы угадаете остальные. Это {0}.",
        "tts": "Ну ничего. Наверняка вы угадаете остальные. ^Это^ {0}."
    },
    {
        "text": "Ничего страшного, мы все чего-то не знаем. Это {0}.",
        "tts": "Ничего страшного, мы все чего-то не знаем. Это {0}."
    },
    {
        "text": "Это и правда сложный вопрос. Картина называется {0}.",
        "tts": "Это и правда сложный вопрос. Картина ^называется^ {0}."
    },
    {
        "text": "Нестрашно. Я подскажу. Это {0}.",
        "tts": "^Нестрашно^. Я подскажу. ^Это^ {0}."
    },
    {
        "text": "Это {0}. Зато теперь знаете!",
        "tts": "^Это^ (название картины). Зато ^теперь^ знаете!"
    }
]

correct_answer_phrases = [
    {
        "text": "Вы правы! Это {0}.",
        "tts": "Вы ^правы^! Это {0}."
    },
    {
        "text": "Точно! Это {0}.",
        "tts": "^Точно!^. Это {0}."
    },
    {
        "text": "Всё верно! Это {0}.",
        "tts": "Всё ^верно!^. Это {0}."
    },
    {
        "text": "Браво! Это действительно {0}.",
        "tts": "^Браво!^. Это ^действительно^ {0}."
    },
    {
        "text": "Вы не перестаёте меня восхищать! Это и правда {0}.",
        "tts": "Вы не перестаёте меня восхищать! Это и ^правда^ {0}."
    },
    {
        "text": "Так держать! Это действительно {0}.",
        "tts": "Так держать! Это действительно {0}."
    }
]

incorrect_answer_phrases = [
    {
        "text": "Почти...но нет. Это {0}.",
        "tts": "^Почти^...но нет. ^Это^ {0}."
    },
    {
        "text": "Не совсем. Это {0}.",
        "tts": "Не ^совсем^. ^Это^ {0}."
    },
    {
        "text": "Вы были близки. Но это {0}.",
        "tts": "Вы были ^близки^. Но ^это^ {0}."
    },
    {
        "text": "Очень близко, но всё-таки нет. Это {0}.",
        "tts": "^Очень^ ^близко^, но всё-таки нет. ^Это^ {0}."
    },
    {
        "text": "Очень не хочу вас расстраивать. Но это {0}.",
        "tts": "Очень не хочу вас расстраивать. Но ^это^ {0}."
    }
]

go_next_question_phrases = [
    {
        "text": "Пойдём дальше?",
        "tts": "^Пойдём^ дальше?"
    },
    {
        "text": "Перейдём к следующему вопросу?",
        "tts": "^Перейдём^ к ^следующему^ вопросу?"
    },
    {
        "text": "Показать следующую картину?",
        "tts": "^Показать^ следующую картину?"
    },
    {
        "text": "Следующий вопрос?",
        "tts": "^Следующий^ вопрос?"
    },
    {
        "text": "Показать новую картину?",
        "tts": "^Показать^ новую картину?"
    }
]

result_phrases = [
    {
        "text": "Ваш счёт — {0} из 12. Вы — арт-новичок. Всё ещё впереди. Никогда не поздно узнать что-то новое.",
        "tts": "Ваш счёт — ^{0}^ из ^двенадцати^. Вы — арт-новичок. ^Всё^ ещё впереди. Никогда не поздно узнать что-то новое."
    },
    {
        "text": "Ваш счёт — {0} из 12. Вы — друг художника. О чём-то он вам рассказал, но остальное предстоит узнать самостоятельно.",
        "tts": "Ваш счёт — ^{0}^ из двенадцати. Вы — друг художника. О чём-то он вам рассказал, но остальное предстоит узнать самостоятельно."
    },
    {
        "text": "Ваш счёт — {0} из 12. Вы насмотренный эстет! У вас явно есть любимый зал в Третьяковской галерее.",
        "tts": "Ваш счёт — ^{0}^ из двенадцати. Вы ^насмотренный^ ^эстет^! У вас явно есть любимый зал в Третьяковской галерее."
    },
    {
        "text": "Ваш счёт {0} из 12! Вы точно нейросеть! Только так можно объяснить вашу поразительную эрудицию.",
        "tts": "Ваш счёт {0} из двенадцати! Вы ^точно^. ^нейросеть^! ^Только так^ можно объяснить вашу поразительную эрудицию."
    }
]

more_facts = [
    {
        "text": "Больше о картине вы можете узнать на портале Культура РФ",
        "tts": "Больше о картине вы можете узнать на портале Культура РФ"
    },
    {
        "text": "Больше интересных фактов о картине узнайте на портале Культура РФ",
        "tts": "Больше интересных фактов о картине узнайте на портале Культура РФ"
    },
]

repeat_phrases = [
    {
        "text": "Не расслышала вас. Повторите, пожалуйста",
        "tts": "Не расслышала вас. Повторите, пожалуйста"
    },
    {
        "text": "Извините, но похоже я не расслышала четкий ответ. Повторите, пожалуйста",
        "tts": "Извините, но похоже я ^не расслышала^ четкий ответ. ^Повторите^, пожалуйста"
    },
    {
        "text": "Похоже, я не разобрала ваш ответ. Повторите, пожалуйста",
        "tts": "Похоже, я не разобрала ваш ответ. ^Повторите^, пожалуйста"
    }
]

check_results_phrases = [
    {
        "text": "Хотите посмотреть ваш результат?",
        "tts": "Хотите посмотреть ваш результат?"
    },
    {
        "text": "Посмотрим ваш результат?",
        "tts": "Посмотрим ваш результат?"
    }
]

# Синонимы основных действий
check_results_synonims = [
    "узнать результат",
    "результат",
    "покажи результат",
    "хочу узнать результат",
    "хочу узнать",
    "узнать",
    "покажи",
    "посмотрим результат",
    "посмотрим мой результат",
    "давай посмотрим результат",
    "посмотреть результат",
    "хочу",
    "хочу посмотреть",
    "хочу посмотреть мой результат",
    "я хочу посмотреть",
    "давай посмотрим",
    "посмотрим",
    "давай",
    "ну давай",
    "да"
    "конечно",
    "конечно же",
    "ага",
    "возможно",
    "определенно да",
    "точно",
    "так",
    "именно так",
    "без сомнений",
    "абсолютно точно",
    "верно",
    "ну да",
    "скорее всего",
    "наверное",
    "естественно",
    "а то",
    "как же иначе",
    "без вариантов",
    "только так",
    "сто процентов",
    "по-другому и быть не может",
    "вероятно",
    "хорошо",
    "так точно",
]

dont_know_synonims = [
    'не знаю',
    'я не знаю',
    'без понятия',
    'я без понятия',
    'кто знает',
    'правильный ответ',
    'скажи правильный ответ',
    'какой правильный ответ',
    'дай правильный ответ',
    'верный ответ',
    'скажи верный ответ',
    'дай верный ответ',
    'какой верный ответ',
    'хочу правильный ответ',
    'а какой правильный',
    'а какой верный',
    'а как правильно',
    'а как верно',
    'отгадка',
    'скажи отгадку',
    'хочу отгадку',
    'какая отгадка',
    'а как правильно'
]

start_synonims = [
    'да',
    'конечно',
    'конечно же',
    'ага',
    'возможно',
    'определенно да',
    'точно',
    'так',
    'именно так',
    'без сомнений',
    'абсолютно точно',
    'верно',
    'ну да',
    'скорее всего',
    'наверное',
    'естественно',
    'а то',
    'как же иначе',
    'без вариантов',
    'только так',
    'сто процентов',
    'по-другому и быть не может',
    'вероятно',
    'хорошо',
    'так точно',
    'начнем',
    '“да, давай”',
    'давай',
    'запускай',
    'включай',
    'начинай',
    'давай запускай',
    'включись',
    'играй',
    'заводи шарманку',
    'начать',
    'давай начнем',
]

how_to_win_marusia_synonims = [
    'хочу узнать о конкурсе',
    'узнать о конкурсе',
    'узнать',
    'о конкурсе',
    'про конкурс',
    'узнать про конкурс',
    'узнать про розыгрыш',
    'узнать о розыгрыше',
    'что за розыгрыш',
    'расскажи про розыгрыш',
    'что за конкурс',
    'расскажи про конкурс',
    'подробнее о конкурсе',
    'подробнее о розыгрыше',
    'как выиграть капсулу мини',
    'выиграть капсулу',
    'как выиграть капсулу',
    'капсула мини',
    'выиграть капсулу мини',
    'хочу узнать про капсулу',
    'расскажи про капсулу',
    'хочу узнать про капсулу мини',
    'расскажи про капсулу мини',
    'выиграть капсулу мини',
    'розыгрыш капсулы мини',
    'розыгрыш капсулы',
    'расскажи про розыгрыш капсулы',
    'расскажи про розыгрыш капсулы мини',
    'расскажи о розыгрыше капсулы',
    'расскажи о розыгрыше капсулы мини',
]

next_picture_synonims = [
    'продолжить играть',
    'продолжить',
    'продолжать',
    'играть',
    'дальше',
    'далее',
    'переход',
    'далее',
    'нэкст',
    'следующая',
    'следующий',
    'следующего',
    'следующую',
    'следующая картина',
    'следующую картину',
    'следующей картиной',
    'следующие картины',
    'следующих картин',
    'следующими картинами',
    'давай следующую',
    'следующую давай',
    'давай дальше',
    'дальше давай',
    'давай далее',
    'давай следующую картину',
    'переключи дальше',
    'переключить дальше',
    'переключи следующую картину',
    'переключить следующую картину',
    'переключи на следующую',
    'переключи на следующую картину',
    'переключить следующую картину',
    'перейти дальше',
    'перейди дальше',
    'перейти к следующей',
    'перейти к следующей картине',
    'перейди к следующей',
    'перейди к следующей картине',
    'включи дальше',
]

first_option_synonims = [
    '1',
    'первое',
    'первая',
    'первую',
    'первый',
    'первый ответ',
    'первый вариант',
    'первая картина',
    'это первая картина',
    'картина номер один',
    'это первая',
    'один',
]

second_option_synonims = [
    '2',
    'вторая',
    'вторую',
    'второй',
    'вторым',
    'два',
    'второй ответ',
    'второй вариант',
    'вторая картина',
    'это вторая картина',
    'картина номер два',
    'это вторая',
]

third_option_synonims = [
    '3',
    'третья',
    'третью',
    'третий',
    'третьим',
    'три',
    'третий ответ',
    'третий вариант',
    'третья картина',
    'это третья картина',
    'картина номер три',
    'это третья',
]

stop_synonims = [
    "стоп",
    "хватит",
    "выйти",
    "остановись",
    "прекрати",
    "отстань",
    "больше не нужно",
    "не нужно",
    "не надо",
    "не включай",
    "не переключай",
    "не нужно следующую",
    "не надо следующую",
    "харэ",
    "захлопнись",
    "замолчи",
    "молчать",
    "ни звука",
    "не запускай",
    "не включай",
    "не начинай",
    "выход"
]
