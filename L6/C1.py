def energy_wh(watts: int, hours: int = 1) -> int:
    return watts*hours

watts = int(input())
hours = int(input())
print(energy_wh(watts))
print(energy_wh(watts, hours))
