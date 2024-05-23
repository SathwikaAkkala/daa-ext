class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight

def knapsack_branch_bound(items, capacity):
    items.sort(key=lambda x: x.cost, reverse=True)
    n = len(items)
    max_value = 0
    max_set = []

    def bound(i, current_weight, current_value):
        if current_weight >= capacity:
            return 0
        bound_value = current_value
        j = i + 1
        total_weight = current_weight
        while j < n and total_weight + items[j].weight <= capacity:
            total_weight += items[j].weight
            bound_value += items[j].value
            j += 1
        if j < n:
            bound_value += (capacity - total_weight) * items[j].cost
        return bound_value

    def backtrack(i, current_weight, current_value, chosen_items):
        nonlocal max_value, max_set
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            max_set = chosen_items[:]
        if i < n:
            if current_weight + items[i].weight <= capacity:
                backtrack(i + 1, current_weight + items[i].weight, current_value + items[i].value, chosen_items + [i])
            if bound(i, current_weight, current_value) > max_value:
                backtrack(i + 1, current_weight, current_value, chosen_items)

    backtrack(0, 0, 0, [])
    return max_value, max_set

def main():
    n = int(input("Enter the number of items: "))
    items = []
    for i in range(n):
        weight, value = map(int, input(f"Enter weight and value for item {i + 1}: ").split())
        items.append(Item(weight, value))
    capacity = int(input("Enter the capacity of the knapsack: "))

    max_value, max_set = knapsack_branch_bound(items, capacity)

    print("Maximum value:", max_value)
    print("Items chosen:")
    for i in max_set:
        print(f"Item {i + 1}: Weight = {items[i].weight}, Value = {items[i].value}")

if __name__ == "__main__":
    main()
