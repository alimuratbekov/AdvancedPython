import pytest

from realty import Realty


def test_can_instantiate_realty():
    Realty(name='Ali', area=40.0)


def test_realty_can_greet_a_person():
    expected_name = 'Ali'
    ali = Realty(name=expected_name, area=40.0)
    greeting = ali.greet()
    assert expected_name in greeting, (
        f"name {expected_name} should be present in greeting. "
        f"while your greeting is: {greeting}"
    )


def test_realty_calculate_monthly_payment_correctly():
    monthly_payment = Realty.calculate_monthly_payment(value=1_000_000, years=5, interest_rate=0.1)
    expected_monthly_payment = 21247
    assert monthly_payment == pytest.approx(expected_monthly_payment, abs=1.0), (
        "calculated monthly payment is incorrect"
    )


def test_can_load_realty_from_file():
    loaded_realty = Realty.load_from_file(filepath="vasya_realty.txt")
    expected_realty = Realty(name="Vasya", area=40.0)
    assert expected_realty == loaded_realty


def test_raise_exception_with_empty_area():
    with pytest.raises(ValueError):
        Realty(name='Vasya', area=None)
