from collections import Counter

N = int(input())
inventory = Counter()
for i, n in enumerate(map(int, input().split()), start=1):
    inventory[i] = n
K = int(input())
recipes = {}

for _ in range(K):
    result, _, *recipe = map(int, input().split())
    recipes[result] = set(recipe)


def craft(x):
    if inventory[x] > 0:  # Already exists
        inventory[x] -= 1
        return Counter({x: 1})

    recipe = recipes.get(x)
    if recipe is None:  # Recipie doesn't exist (cannot create more)
        return None

    items_used = Counter()  # Create more using recipe
    for item in recipe:
        res = craft(item)
        if res is None:
            return None
        items_used += res

    return items_used


t = 0
while True:
    # Create one
    res = craft(N)
    if res is None:  # Not possible, limit is reached
        break
    t += 1

    # Create more using same resources
    if not all(inventory[i] >= res[i] for i in res):
        continue
    count = min(inventory[i] // res[i] for i in res)
    for i in res:
        inventory[i] -= res[i] * count
    t += count

print(t)
