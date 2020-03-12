from models.parser import Parser


def test_Parser_clean():
    """Cleaning function test"""

    question = 'Ou se trouve le musée du Louvre?'
    parser = Parser(question)
    result = parser.clean()
    assert result == "musee du louvre"


def test_Parser_extract_place():
    """Place extraction function test"""

    question = 'ou se trouve le musee du louvre?'
    parser = Parser(question)
    result = parser._extract_place(question)
    assert result == " le musee du louvre"


def test_Parser_delete_article():
    """Test article deletion function"""

    question = 'le musee du louvre?'
    parser = Parser(question)
    result = parser._delete_article(question)
    assert result == " musee du louvre?"
