import pytest

from calculator import square
"""
def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4  #Assert anlamındaki gibi iddia anlamına gelir ve burada kodu test ederken 2'nin karesinin 4 olduğunu iddia ediyoruz.Eğer doğruysa ekranda bir şey yazılmaz ama yanlışsa hata verir.
    except AssertionError:
        print("2 squared was not equal to 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not equal to 9")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not equal to 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not equal to 0")

if __name__ == "__main__":
    main()
"""                                     #2 satırlık bir kodu test etmek için 26 satırlık bir kod yazmak yerine pytest kullanmak daha iyi

def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4                       # Yaptığımız testleri ayırmamızın sebebi özellikle hangi durumlarda hatalarla karşılaştığımızı ayırt edebilmek
    assert square(-3) ==9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")