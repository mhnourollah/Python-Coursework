try:
    year_bought = int(input())
    year_sold = int(input())

    if year_bought < 1936:
        raise ValueError(
            "Year of purchase cannot start before birth year"
        )

    if year_sold < year_bought:
        raise ValueError(
            "Year of sale cannot be before purchase year"
        )

    print(year_sold - year_bought)

except ValueError as excpt:
    print(excpt)
