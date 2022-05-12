# flake8: noqa: E501
import random
from typing import Dict, List, Any
from . import main_phrases, pictures_data


class Skill:
    def __init__(self) -> None:
        self._sessionStorage: Dict = dict()  # Хранилище данных о сессиях.

    # Функция для непосредственной обработки диалога.
    def handle_dialog(self, req, res) -> None:
        res['version'] = req['version']
        res['session'] = req['session']
        res['response'] = {
            'end_session': False
        }

        user_id = req['session']['user_id']
        original_utterance = req['request']['original_utterance'].lower()

        # Обрабатываем вход в скилл
        if req['session']['new']:
            self._sessionStorage[user_id] = {
                'suggests': main_phrases.welcome_text['suggests']
            }

            res['response']['text'] = main_phrases.welcome_text['text']
            res['response']['tts'] = main_phrases.welcome_text['tts']
            res['response']['buttons'] = self.get_suggests(user_id)
            res['session_state'] = {'second_step': 'next_picture',
                                    'remaining_pictures': generate_remaining_pictures(),
                                    'right_answers': 0}
            return

        elif req['state']['session']['second_step'] == 'next_picture' and \
                (original_utterance in main_phrases.start_synonims
                 or original_utterance in main_phrases.next_picture_synonims):
            is_last = False
            remaining_pictures = req['state']['session']['remaining_pictures']
            right_answers = req['state']['session']['right_answers']
            remaining_pictures_array = remaining_pictures.split(',')
            picture_number = int(remaining_pictures_array[0])
            random_phrase = random.choice(main_phrases.what_picture_questions)
            right_answer = pictures_data.pictures[picture_number]['title']
            random_answer_numbers = random.choices(
                list(range(0, picture_number)) + list(range(picture_number + 1, len(pictures_data.pictures))), k=2)
            flag = True
            while flag:
                flag = False
                random_answer_numbers = random.choices(
                    list(range(0, picture_number)) + list(range(picture_number + 1, len(pictures_data.pictures))), k=2)
                for i in random_answer_numbers:
                    if right_answer['text'].split()[1] in pictures_data.pictures[i]['title']['text']:
                        flag = True
            answers = [right_answer, pictures_data.pictures[random_answer_numbers[0]]['title'],
                       pictures_data.pictures[random_answer_numbers[1]]['title']]
            random.shuffle(answers)
            right_answer_number = answers.index(right_answer)
            if len(remaining_pictures_array) == 1:
                is_last = True

            res['response']['card'] = {
                'type': 'BigImage',
                'image_url': pictures_data.pictures[picture_number]['url']
            }
            res['response']['text'] = random_phrase['text'] + "\n1) {0}\n2) {1}\n3) {2}".format(answers[0]['text'],
                                                                                                answers[1]['text'],
                                                                                                answers[2]['text'])
            res['response']['tts'] = random_phrase['tts'] + "\n{0}. {1}. {2}".format(answers[0]['tts'],
                                                                                     answers[1]['tts'],
                                                                                     answers[2]['tts'])
            self._sessionStorage[user_id] = {
                'suggests': [
                    "1",
                    "2",
                    "3",
                ]
            }
            res['response']['buttons'] = self.get_suggests(user_id)
            res['session_state'] = {'second_step': 'check_picture',
                                    'remaining_pictures': delete_remaining_picture(remaining_pictures),
                                    'checking_picture': picture_number,
                                    'is_last': is_last,
                                    'right_answer': f'{right_answer_number + 1}',
                                    'right_answers': right_answers}
            return

        elif req['state']['session']['second_step'] == 'check_picture':
            remaining_pictures = req['state']['session']['remaining_pictures']
            checking_picture = req['state']['session']['checking_picture']
            right_answers = req['state']['session']['right_answers']
            right_answer = req['state']['session']['right_answer']
            is_last = req['state']['session']['is_last']
            random_next_phrase = random.choice(main_phrases.go_next_question_phrases)
            random_more_facts_phrase = random.choice(main_phrases.more_facts)

            second_step = 'next_picture'
            if is_last:
                second_step = 'result'
                self._sessionStorage[user_id] = {
                    'suggests': [
                        "Узнать результат",
                        "Как выиграть Капсулу Мини",
                    ]
                }
                random_next_phrase = random.choice(['Хотите посмотреть ваш результат?', 'Посмотрим ваш результат?'])

            if original_utterance in main_phrases.dont_know_synonims:
                random_phrase = random.choice(main_phrases.dont_know_phrases)
            elif original_utterance in pictures_data.pictures[checking_picture]['synonims'] or \
                    (right_answer == '1' and original_utterance in main_phrases.first_option_synonims) or \
                    (right_answer == '2' and original_utterance in main_phrases.second_option_synonims) or \
                    (right_answer == '3' and original_utterance in main_phrases.third_option_synonims):
                random_phrase = random.choice(main_phrases.correct_answer_phrases)
                right_answers += 1
            else:
                random_phrase = random.choice(main_phrases.incorrect_answer_phrases)

            res['response']['text'] = random_phrase['text'].format(
                pictures_data.pictures[checking_picture]['title']['text']) + \
                                      "\n\n" + pictures_data.pictures[checking_picture]['description']['text'] + \
                                      "\n\n" + random_more_facts_phrase['text'] + \
                                      "\n\n" + random_next_phrase['text']
            res['response']['tts'] = random_phrase['tts'].format(
                pictures_data.pictures[checking_picture]['title']['tts']) + \
                                     "\n" + pictures_data.pictures[checking_picture]['description']['tts'] + \
                                     "\n\n" + random_more_facts_phrase['tts'] + \
                                     "\n" + random_next_phrase['tts']
            self._sessionStorage[user_id] = {
                'suggests': [
                    "Следующая картина",
                    "Как выиграть Капсулу Мини",
                ]
            }
            res['response']['buttons'] = self.get_suggests(user_id)
            res['session_state'] = {'second_step': second_step,
                                    'remaining_pictures': remaining_pictures,
                                    'right_answers': right_answers}
            return

        elif req['state']['session']['second_step'] == 'result' and \
                original_utterance in main_phrases.check_results_synonims:
            ciphers = {
                0: "ноль",
                1: "один",
                2: "два",
                3: "три",
                4: "четыре",
                5: "пять",
                6: "шесть",
                7: "семь",
                8: "восемь",
                9: "девять",
                10: "десять",
                11: "одиннадцать",
                12: "двенадцать",
            }
            right_answers = req['state']['session']['right_answers']
            if right_answers < 4:
                phrase_number = 0
            elif right_answers < 9:
                phrase_number = 1
            elif right_answers < 12:
                phrase_number = 2
            else:
                phrase_number = 3
            phrase = main_phrases.result_phrases[phrase_number]
            res['response']['text'] = phrase['text'].format(right_answers) + "\n\n" + main_phrases.rules['text']
            res['response']['tts'] = phrase['tts'].format(ciphers[right_answers]) + "\n" + main_phrases.rules['tts']
            res['response']['card'] = {
                'type': 'Link',
                'url': main_phrases.exit_call['url'],
                'title': main_phrases.exit_call['title'],
                'text': main_phrases.exit_call['text'],
                'image_url': main_phrases.exit_call['image_url'],
            }
            return

        elif original_utterance in main_phrases.stop_synonims:
            random_phrase = random.choice(main_phrases.exit_texts)
            res['response']['text'] = random_phrase['text'] + "\n\n" + main_phrases.rules['text']
            res['response']['tts'] = random_phrase['tts'] + "\n" + main_phrases.rules['tts']
            res['response']['card'] = {
                'type': 'Link',
                'url': main_phrases.exit_call['url'],
                'title': main_phrases.exit_call['title'],
                'text': main_phrases.exit_call['text'],
                'image_url': main_phrases.exit_call['image_url'],
            }
            res['response']['end_session'] = True
            return

        elif original_utterance in main_phrases.how_to_win_marusia_synonims:
            res['response']['text'] = main_phrases.rules['text']
            res['response']['tts'] = main_phrases.rules['tts']
            res['response']['card'] = {
                'type': 'Link',
                'url': main_phrases.exit_call['url'],
                'title': main_phrases.exit_call['title'],
                'text': main_phrases.exit_call['text'],
                'image_url': main_phrases.exit_call['image_url'],
            }
            self._sessionStorage[user_id] = {
                'suggests': [
                    "Продолжить играть"
                ]
            }
            res['session_state'] = {}
            for key in req['state']['session'].keys():
                res['session_state'][key] = req['state']['session'][key]
            return

        else:
            random_phrase = random.choice(main_phrases.repeat_phrases)
            res['response']['text'] = random_phrase['text']
            res['response']['tts'] = random_phrase['tts']
            res['session_state'] = {}
            for key in req['state']['session'].keys():
                res['session_state'][key] = req['state']['session'][key]
                return

    # Функция возвращает подсказки для ответа.
    def get_suggests(self, user_id: str) -> List:
        session = self._sessionStorage.get(user_id) or {'suggests': []}

        suggests: List = [
            {'title': suggest, 'hide': True}
            for suggest in session['suggests']
        ]

        return suggests


skill: Skill = Skill()


def generate_remaining_pictures():
    res = ""
    for i in random.choices(list(range(0, len(pictures_data.pictures))), k=12):
        res += f"{i},"
    return res[:-1]


def delete_remaining_picture(remaining_pictures):
    array = remaining_pictures.split(",")[1:]
    res = ""
    for i in array:
        res += f"{i},"
    return res[:-1]
