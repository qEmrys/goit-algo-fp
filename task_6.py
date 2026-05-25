items = {
    "pizza":     {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog":   {"cost": 30, "calories": 200},
    "pepsi":     {"cost": 10, "calories": 100},
    "cola":      {"cost": 15, "calories": 220},
    "potato":    {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1]["calories"] / x[1]["cost"],
                          reverse=True)
    chosen = []
    total_calories = 0

    for name, data in sorted_items:
        if budget >= data["cost"]:
            chosen.append(name)
            total_calories += data["calories"]
            budget -= data["cost"]

    return chosen, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    calories = [items[n]["calories"] for n in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])

    chosen = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= costs[i - 1]

    return chosen, dp[n][budget]


if __name__ == "__main__":
    budget = 100

    greedy_items, greedy_cal = greedy_algorithm(items, budget)
    print(f"Жадібний:  {greedy_items}, калорії: {greedy_cal}")

    dp_items, dp_cal = dynamic_programming(items, budget)
    print(f"Динамічне: {dp_items}, калорії: {dp_cal}")
