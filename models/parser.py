import re

import logzero
from logzero import logger


class Parser:

    def clean(self, question):
        # 1. enlève les maj.
        question_lower = question.lower()
        # 2. enlève les accents.
        question_sans_accent = question_lower.replace("é", "e")
        # 3. extraire les suite de (ou se trouve la, ou se situe la, ou est la, quelle est l'adresse de).
        question_place = self._extract_place(question_sans_accent)
        # 4. ici eliminer les (le, la, les, l', des, un, une).
        question_sans_article = self._effacer_article(question_place)
        logger.debug(question_sans_article.strip(' '))
        return question_sans_article.strip(' ')
        
    
    def _extract_place(self, question):
        regex = r"(ou se trouve|ou se situe|quelle est l'adresse de)([^,.:;!?]*)"
        match = re.search(regex, question)
        return match.group(2)

    def _effacer_article(self, question):
        regex = r"(le|la|les|l'|des|un|une)(.*)"
        match = re.search(regex, question)
        return match.group(2)
