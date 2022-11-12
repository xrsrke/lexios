from lexios.utils import (
    camel_to_snake,
    str2fml,
    fml2str
)


def test_camel_to_snake():
    assert camel_to_snake("IdealGasLaw") == "ideal_gas_law"


def test_str2fml():
    H2O = str2fml("H2O")
    assert H2O == "H₂O"


def test_fml2str():
    H2O = fml2str("H₂O")
    assert H2O == "H2O"