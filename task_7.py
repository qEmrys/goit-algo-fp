import random
import matplotlib.pyplot as plt


def monte_carlo_dice(n=1000000):
    counts = {i: 0 for i in range(2, 13)}

    for _ in range(n):
        roll = random.randint(1, 6) + random.randint(1, 6)
        counts[roll] += 1

    probabilities = {s: counts[s] / n for s in counts}
    return probabilities

def print_table(probabilities):
    analytical = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    print(f"{'Сума':<6} {'Монте-Карло':>12} {'Аналітично':>12}")
    print("-" * 32)
    for s in range(2, 13):
        print(f"{s:<6} {probabilities[s]*100:>11.2f}% {analytical[s]*100:>11.2f}%")

def plot(probabilities):
    analytical = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    sums = list(range(2, 13))
    mc_vals = [probabilities[s] * 100 for s in sums]
    an_vals = [analytical[s] * 100 for s in sums]

    x = range(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar([i - width/2 for i in x], mc_vals, width, label="Монте-Карло", color="steelblue")
    ax.bar([i + width/2 for i in x], an_vals,  width, label="Аналітично",  color="orange", alpha=0.7)
    ax.set_xticks(list(x))
    ax.set_xticklabels(sums)
    ax.set_xlabel("Сума")
    ax.set_ylabel("Імовірність (%)")
    ax.set_title("Імовірності сум при киданні двох кубиків")
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    probs = monte_carlo_dice(1000000)
    print_table(probs)
    plot(probs)
