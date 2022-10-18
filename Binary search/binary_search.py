"""-----*BRUTE FORCE APPROACH*-----*TIME COMPLEXITY-O(n)*-----*SPACE COMPLEXITY - O(1)*-----"""


def locate_card_1(cards, query):
    print(cards)
    pos = 0
    for card in cards:
        if card == query:
            return pos

        pos += 1
        if pos == len(cards):
            return False


"""-----*OPTIMISED APPROACH*-----*TIME COMPLEXITY- *-----*SPACE COMPLEXITY - *-----"""


"""-----*CORNER TEST CASE*-----"""
tests = []
tests.append({"input": {"cards": [13, 11, 7, 4, 3, 1, 0], "query": 7}, "output": 2})
tests.append({"input": {"cards": [13, 11, 7, 4, 3, 1, 0], "query": 1}, "output": 5})
tests.append({"input": {"cards": [4, 2, 1, -1], "query": 4}, "output": 0})
tests.append({"input": {"cards": [4, 2, 1, -127], "query": -127}, "output": 3})
tests.append({"input": {"cards": [6], "query": 6}, "output": 0})

for test in tests:
    print(locate_card(**test["input"]) == test["output"])

"""-----*INPUT*-----"""
cards = [13, 11, 7, 4, 3, 1, 0]

"""-----*OUTPUT*-----"""
query = 7

"""-----*EXECUTION*-----"""
result = locate_card(cards, query)
print(result)
