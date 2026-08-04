# test suite
import pytest
from roman.converter import to_roman, from_roman, is_valid_roman, add_roman, subtract_roman, _roundtrip_differs, _count_char, RomanError


def test_one():
    assert to_roman(1) == "I"


def test_two():
    assert to_roman(2) == "II"


def test_three():
    assert to_roman(3) == "III"


def test_five():
    assert to_roman(5) == "V"


def test_ten():
    assert to_roman(10) == "X"


def test_fifty():
    assert to_roman(50) == "L"


def test_hundred():
    assert to_roman(100) == "C"


def test_five_hundred():
    assert to_roman(500) == "D"


def test_thousand():
    assert to_roman(1000) == "M"


def test_from_one():
    assert from_roman("I") == 1


def test_from_five():
    assert from_roman("V") == 5


def test_from_two():
    assert from_roman("II") == 2


def test_roundtrip_small():
    assert from_roman(to_roman(7)) == 7


def test_roundtrip_medium():
    assert from_roman(to_roman(58)) == 58


def test_lowercase_input():
    assert from_roman("xi") == 11

# Pruebas para to_roman (Líneas 42, 44, 46)
def test_to_roman_exceptions():
    with pytest.raises(RomanError, match="value must be an integer"):
        to_roman("10")
    with pytest.raises(RomanError, match="value must be >= 1"):
        to_roman(0)
    with pytest.raises(RomanError, match="value must be <= 3999"):
        to_roman(4000)

# Pruebas para from_roman  (Líneas 58, 61, 64, 72, 83)
def test_from_roman_exceptions():
    with pytest.raises(RomanError, match="value must be a string"):
        from_roman(123)
        
    with pytest.raises(RomanError, match="empty string is not a roman numeral"):
        from_roman("")
        
    with pytest.raises(RomanError, match="invalid roman character"):
        from_roman("Z")
        
    with pytest.raises(RomanError, match="invalid subtractive pair"):
        from_roman("IC") # I (1) no se puede restar de C (100) en el formato estricto
        
    with pytest.raises(RomanError, match="value out of range 1..3999"):
        from_roman("MMMM") # Genera 4000, excediendo el máximo

# Pruebas para funciones utilitarias y operacionales (Líneas 88, 92-96, 100-104, 108, 112)
def test_internal_helpers():
    assert _count_char("VIII", "I") == 3
    assert _count_char("X", "I") == 0
    assert _roundtrip_differs(10, "IX") is True
    assert _roundtrip_differs(10, "X") is False

def test_is_valid_roman():
    assert is_valid_roman("XIV") is True
    assert is_valid_roman("ABC") is False

def test_add_roman():
    assert add_roman("V", "II") == "VII"

def test_subtract_roman():
    assert subtract_roman("X", "I") == "IX"

def test_integration_add_roman_collaboration():
    resultado = add_roman("II", "II")
    
    assert is_valid_roman(resultado) is True
    
    assert resultado == "IV", f"Defecto de integración detectado: Se esperaba 'IV', pero el sistema generó '{resultado}'"

def test_acceptance_convert_four():
    numero = 4
    resultado = to_roman(numero)
    assert resultado == "IV", f"Fallo de aceptación: 4 debería ser 'IV', pero dio '{resultado}'"

def test_acceptance_invalid_repetition():
    cadena = "IIII"
    es_valido = is_valid_roman(cadena)
    assert es_valido is False, "Fallo de aceptación: 'IIII' fue considerado un número romano válido"

def test_acceptance_convert_1994():
    numero = 1994
    resultado = to_roman(numero)
    assert resultado == "MCMXCIV", f"Fallo de aceptación: 1994 debería ser 'MCMXCIV', pero dio '{resultado}'"