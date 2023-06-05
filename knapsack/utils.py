from knapsack.config import ITEMS, MAX_WEIGHT


def evaluate(individual: list[int]) -> tuple[int]:
    total_value = total_weight = 0

    for bit, item in zip(individual, ITEMS):
        if bit == 1:
            total_weight += item.weight
            total_value += item.value

    if total_weight > MAX_WEIGHT:
        return 0,

    return total_value,
