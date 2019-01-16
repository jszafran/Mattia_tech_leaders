import pytest
import to_upper as up


def test_convert_to_upper():
    assert up.convert_to_upper('Just Testing') == 'JUST TESTING'

    
def test_convert_to_upper_with_punctuation():
    assert up.convert_to_upper('test, with.punctuation') == 'TEST, WITH.PUNCTUATION'

    
def test_raise_typerror_exception():
    with pytest.raises(TypeError):
        up.convert_to_upper(1000)
