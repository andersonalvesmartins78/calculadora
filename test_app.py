import pytest
from calc import soma,sub,mult,div
@pytest.mark.parametrize('a,b,x', [(1,1,2),(1,2,3),(2,3,5)])
def test_soma(a,b,x):
 assert soma(a,b)==x
@pytest.mark.parametrize('a,b,x', [(1,1,0),(1,2,-1),(2,3,-1)])
def test_sub(a,b,x):
 assert sub(a,b)==x
@pytest.mark.parametrize('a,b,x', [(1,1,1),(1,2,2),(2,3,6)])
def test_mult(a,b,x):
 assert mult(a,b)==x
@pytest.mark.parametrize('a,b,x', [(1,1,1),(1,2,0.5),(2,4,0.5)])
def test_div(a,b,x):
 assert div(a,b)==x

