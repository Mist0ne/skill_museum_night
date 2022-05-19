import json
from pathlib import Path

import pytest

from skill_museum_night.skill import skill

base_req_file_name = Path(__file__).parent / 'base_request.json'


# flake8: noqa
@pytest.mark.parametrize('phrase_text, new_session, answer_text', [
    ('угадай картину', True, """Васнецов или Серебрякова? «Девочка с персиками» или «с крынкой молока»? Попробуйте угадать!

Вместе с «Культура.РФ» мы выбрали 32 картины русских художников, а нейросеть перерисовала их в непривычных стилях: экспрессионизм, пуантилизм и импрессионизм. Теперь полотна выглядят по-другому, и ваша задача — отгадать оригинал.

Пройдите игру и узнайте, как выиграть умную колонку со мной внутри.

Начнём играть?
"""),
])
def test_skill(phrase_text, new_session, answer_text):
    req = {}
    resp = {}
    with open(base_req_file_name) as f:
        req = json.load(f)

    req['request']['original_utterance'] = phrase_text
    req['request']['command'] = phrase_text
    req['session']['new'] = new_session

    skill.handle_dialog(req, resp)

    assert answer_text in resp['response']['text']
