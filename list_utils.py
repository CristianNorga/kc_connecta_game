def find_one(list, needle):
    return find_n(list, needle, 1)

def find_n(list, needle, n):
    if n < 0:
        return False
    
    return list.count(needle) >= n

def find_streak(list, needle, n):
    if n < 1:
        return False

    current_streak = 0
    for item in list:
        if item == needle:
            current_streak += 1
            if current_streak >= n:
                return True
        else:
            current_streak = 0

    return False
    
def first_elements(matrix):
    return nth_elements(matrix, 0)

def nth_elements(matrix, n):
    return [row[n] for row in matrix if len(row) > n]

def transpose(matrix):
    result = []
    
    if len(matrix) <= 0:
        return result

    for i in range(len(matrix[0])):
        # new_row = []
        # for row in matrix:
        #     if i < len(row):
        #         new_row.append(row[i])
        # result.append(new_row)
        result.append(nth_elements(matrix, i))

    return result
