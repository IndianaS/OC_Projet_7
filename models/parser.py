import re

import unicodedata
from logzero import logger


class Parser:
    """User input analysis class"""

    def __init__(self, question):
        self.question = question

    def clean(self):
        """User input cleaning method"""

        question_lower = self.question.lower()
        question_without_accent = ''.join((c for c in unicodedata.normalize(
            'NFD', question_lower) if unicodedata.category(c) != 'Mn'))
        question_place = self._extract_place(
            question_without_accent).strip(' ')
        question_without_article = self._delete_article(question_place)
        return question_without_article.strip(' ')

    def _extract_place(self, question):
        """keyword extraction"""

        regex = r"(ou se trouve|ou se situe|quelle est l'adresse de|ou est|c'est ou)([^,.:;!?]*)"
        match = re.search(regex, question)

        return match.group(2)

    def _delete_article(self, question):
        """Item deletion method"""

        regex = r"(le|la|les|l'|de|des|un|une)*(.*)"
        match = re.search(regex, question)

        if match:
            logger.debug("IF MATCH ARTICLE:" + match.group(2))
        else:
            logger.debug("ELSE MATCH:" + match.group(2))
            return None

        return match.group(2)
