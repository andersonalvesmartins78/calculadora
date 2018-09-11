import pytest
from calc import soma
def test_app():
 assert soma(1,1)==2
 assert soma('1','1')==2
