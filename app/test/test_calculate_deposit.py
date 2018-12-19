import pytest

from app import calculate_deposit


@pytest.mark.parametrize('deposit_sum, percent_in_year, year_quantity, expected', [
    (100_000, 10, 5, 150_000),
    (100_000, 0, 5, 100_000),
    (100_000, 10, 0, 100_000),
    (0, 10, 5, 0),
    (0, 0, 0, 0),
    (123_459, 15.66, 2, 162126.3)
])
def test_calculate_simple_deposit(deposit_sum, percent_in_year, year_quantity, expected):
    actual = calculate_deposit.calculate_simple_deposit(deposit_sum, percent_in_year, year_quantity)

    assert expected == pytest.approx(actual, 0.1)


@pytest.mark.parametrize('deposit_sum, percent_in_year, years_for_deposit, expected', [
    (100_000, 50, 3, 337500.0),
    (100_000, 0, 5, 100_000),
    (100_000, 10, 0, 100_000),
    (0, 10, 5, 0),
    (0, 0, 0, 0),
])
def test_calculate_hard_deposit_annually_capitalization(deposit_sum, percent_in_year, years_for_deposit, expected):
    actual = calculate_deposit.calculate_hard_deposit_annually_capitalization(deposit_sum, percent_in_year,
                                                                              years_for_deposit)

    assert expected == pytest.approx(actual, 0.1)


@pytest.mark.parametrize('deposit_sum, percent_in_year, months_for_deposit, expected', [
    (100_000, 12, 6, 106273.0),
    (100_000, 0, 6, 100_000),
    (100_000, 12, 0, 100_000),
    (100_000, 0, 0, 100_000),
    (0, 0, 0, 0),
])
def test_calculate_hard_deposit_monthly_capitalization(deposit_sum, percent_in_year, months_for_deposit, expected):
    actual = calculate_deposit.calculate_hard_deposit_monthly_capitalization(deposit_sum, percent_in_year,
                                                                             months_for_deposit)

    assert expected == pytest.approx(actual, 0.1)
