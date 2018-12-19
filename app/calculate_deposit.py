def calculate_simple_deposit(deposit_sum, percent_in_year, year_quantity):
    """
    >>> calculate_simple_deposit(100_000, 10, 5) #doctest: +ELLIPSIS
    150000...

    >>> calculate_simple_deposit(100_000, 0, 5) #doctest: +ELLIPSIS
    100000...

    >>> calculate_simple_deposit(100_000, 10, 0) #doctest: +ELLIPSIS
    100000...

    >>> calculate_simple_deposit(0 , 10, 5) #doctest: +ELLIPSIS
    0...

    >>> calculate_simple_deposit(123_459, 15.66, 2) #doctest: +ELLIPSIS
    162126.3...
    """
    profit = deposit_sum * (percent_in_year / 100) * year_quantity
    total_sum = profit + deposit_sum
    return total_sum


print(calculate_simple_deposit(123_459, 15.66, 2))


def calculate_hard_deposit_annually_capitalization(deposit_sum, percent_in_year, years_for_deposit):
    """
    >>> calculate_hard_deposit_annually_capitalization(100_000, 50, 3) #doctest: +ELLIPSIS
    337500.0...

    >>> calculate_hard_deposit_annually_capitalization(100_000, 0 , 3) #doctest: +ELLIPSIS
    100000.0...

    >>> calculate_hard_deposit_annually_capitalization(100_000, 50, 0) #doctest: +ELLIPSIS
    100000.0...

    >>> calculate_hard_deposit_annually_capitalization(100_000, 0, 0) #doctest: +ELLIPSIS
    100000.0...

    >>> calculate_hard_deposit_annually_capitalization(0, 50, 5) #doctest: +ELLIPSIS
    0.0
    """
    total_sum = deposit_sum * (1 + percent_in_year / 100) ** years_for_deposit
    return total_sum


# print(calculate_hard_deposit_annually_capitalization(100_000, 50, 3))


def calculate_hard_deposit_monthly_capitalization(deposit_sum, percent_in_year, months_for_deposit):
    """
    >>> calculate_hard_deposit_monthly_capitalization(100_000, 12, 6) # doctest: +ELLIPSIS
    106273.0...

    >>> calculate_hard_deposit_monthly_capitalization(100_000, 0, 6) # doctest: +ELLIPSIS
    100000...

    >>> calculate_hard_deposit_monthly_capitalization(100_000, 12, 0) # doctest: +ELLIPSIS
    100000...

    >>> calculate_hard_deposit_monthly_capitalization(100_000, 0, 0) # doctest: +ELLIPSIS
    100000...
    """

    capitalization_period = 31
    hundred_percent = 100
    days_in_year = 365
    total_sum = deposit_sum * (
            1 + percent_in_year / hundred_percent * capitalization_period / days_in_year) ** months_for_deposit
    return total_sum


# print(calculate_hard_deposit_monthly_capitalization(100_000, 100, 6))
