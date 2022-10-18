# Brute Force approach
def locate_card(cards, query):
    print(cards)
    pos = 0
    for card in cards:
        if card == query:
            return pos

        pos += 1
        if pos == len(cards):
            return False


cards = [4, 2, 1, -1]
query = 4
tests = []

tests.append({"input": {"cards": [13, 11, 7, 4, 3, 1, 0], "query": 7}, "output": 3})
tests.append({"input": {"cards": [13, 11, 7, 4, 3, 1, 0], "query": 1}, "output": 6})
tests.append({"input": {"cards": [4, 2, 1, -1], "query": 4}, "output": 0})
tests.append({"input": {"cards": [4, 2, 1, -127], "query": -127}, "output": 3})
tests.append({"input": {"cards": [6], "query": 6}, "output": 0})

print(tests)
result = locate_card(cards, query)
print(result)

# print("testing use case--------",locate_card(**test['input']) == test['output'])
