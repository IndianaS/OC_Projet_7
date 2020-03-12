import re

import unicodedata
from logzero import logger


class Parser:
    """User input analysis class"""

    def clean(self, question):
        """User input cleaning method"""

        question_lower = question.lower()
        question_without_accent = ''.join((c for c in unicodedata.normalize('NFD', question_lower) if unicodedata.category(c) != 'Mn'))
        question_place = self._extract_place(question_without_accent)
        question_without_article = self._delete_article(question_place)
        return question_without_article.strip(' ')

    def _extract_place(self, question):
        """keyword extraction"""

        regex = r"(ou se trouve|ou se situe|quelle est l'adresse de|ou est)([^,.:;!?]*)"
        match = re.search(regex, question)
        if match:
            return question
        else:
            return question
        return match.group(2)

    def _delete_article(self, question):
        """Item deletion method"""

        regex = r"(le|la|les|l'|de|des|un|une)(.*)"
        match = re.search(regex, question)
        if match:
            logger.debug('Entrée correct')
        else:
            logger.debug('Entrée incorrect')
            return question
        return match.group(2)
