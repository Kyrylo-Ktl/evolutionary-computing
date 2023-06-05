from functools import cache

from config import ITEMS


def knapsack(weights: list[int], profits: list[int], max_weight: int) -> int:
    @cache
    def dp(i: int, weight: int) -> int:
        if i >= len(weights) or weight == 0:
            return 0

        if weight < weights[i]:
            return dp(i + 1, weight)

        return max(
            dp(i + 1, weight - weights[i]) + profits[i],
            dp(i + 1, weight),
        )

    return dp(0, max_weight)


if __name__ == '__main__':
    result = knapsack(
        weights=[item.weight for item in ITEMS],
        profits=[item.value for item in ITEMS],
        max_weight=400,
    )
    print(result)
