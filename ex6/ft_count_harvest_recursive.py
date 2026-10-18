def print_days(i, days) -> None:
    if (i <= days):
        print(f"Day {i}")
        print_days(i+1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    print_days(1, days)
    print("Harvest time!")
