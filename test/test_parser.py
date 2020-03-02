from models.parser import Parser

def test_Parser_clean():
    question = 'Ou se trouve le musée du Louvre?'
    parser = Parser()
    result = parser.clean(question)
    assert result == "musee du louvre"

def test_Parser_extract_place():
    question = 'ou se trouve le musee du louvre?'
    parser = Parser()
    result = parser._extract_place(question)
    assert result == " le musee du louvre"

def test_Parser_delete_article():
    question = 'ou se trouve le musee du louvre?'
    parser = Parser()
    result = parser._delete_article(question)
    assert result == " musee du louvre?"
