from hello import hello

def test_argument():
    assert hello("Yiğit") == "hello, Yiğit"
    
    
def test_default():    
    assert hello() == "hello, world"