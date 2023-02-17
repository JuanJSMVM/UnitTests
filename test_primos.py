"""
Your module description
"""
from program import es_primo
def test_pares():
    assert es_primo(2)==True
    assert es_primo(4)==False
    assert es_primo(100)==False
    assert es_primo(0)==False
    assert es_primo(2230)==False
    assert es_primo(4902382370)==False
def test_impares():
    assert es_primo(1)==True
    assert es_primo(3)==True
    assert es_primo(5)==True
    assert es_primo(7)==True
    assert es_primo(9)==False
    assert es_primo(1113)==False