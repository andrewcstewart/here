from pathlib import Path
from here import here

def test_here():
    assert here('/') == Path('/')