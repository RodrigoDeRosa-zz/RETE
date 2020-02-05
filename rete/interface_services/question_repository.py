import json

from os.path import abspath, join, dirname
from typing import Dict, Set


class QuestionRepository:

    def __init__(self, questions: Dict[str, str]):
        self.questions = questions

    @classmethod
    def load_from_file(cls, path: str):
        file_path = f'{abspath(join(dirname(__file__), "../../"))}{path}'
        with open(file_path, 'r') as fd:
            raw_rules = json.load(fd)
        return QuestionRepository(raw_rules)

    def questions_for(self, fields_to_ask: Set[str]):
        return [{'field_name': key, 'question': self.questions.get(key)} for key in fields_to_ask]
