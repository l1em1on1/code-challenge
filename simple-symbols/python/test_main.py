import main
import pytest

@pytest.mark.parametrize("string, expected", [
    ('+d+=3=+s+', True),
    ('f++d+', False),
    ('+++++++f++d+', True),
    ('+++++++f++d+++=====+a', False) 
])
def test_regex(string, expected):
    assert main.SimpleSymbols(string) is expected
