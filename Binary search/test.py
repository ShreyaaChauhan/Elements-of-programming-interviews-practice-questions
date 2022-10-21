import math

a = [1, 2, 3, 4, 5, 6, 7, 8]

low = 0
high = len(a) - 1

"""while low < high:
    mid = math.floor((high - low) / 2)
    
    if a[mid] 
    print(mid)
    high = mid"""


def locate_card(cards, query):
    low = 0
    high = len(cards) - 1

    while low <= high:
        mid = (low + high) // 2

        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            high = mid - 1
        elif cards[mid] > query:
            low = mid + 1
        else:
            return False


cards = [13, 11, 7, 4, 3, 1, 0]
query = 7

print(locate_card(cards, query))
