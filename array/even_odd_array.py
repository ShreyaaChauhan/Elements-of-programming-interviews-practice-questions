"""-----*OPTIMISED APPROACH*-----*TIME COMPLEXITY- O(n)*-----*SPACE COMPLEXITY - O(1)*-----"""


def even_odd_array(data):
    for i in range(0, len(data)):
        if data[i] % 2 == 0:
            pass
        flag = 1
        for j in range(i + 1, len(data)):
            if flag:
                if data[j] % 2 == 0:
                    flag = 0
                    data[i], data[j] = data[j], data[i]
    return data


"""-----*INPUT*-----"""
input = [1, 5, 8, 3, 7, 2, 10]
input = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]

"""-----*OUTPUT*-----"""
outpul = [8, 2, 10, 5, 3, 7, 1]


"""-----*EXECUTION*-----"""
data = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
print(even_odd_array(data))
