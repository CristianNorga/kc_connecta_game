def find_one(list, needle) -> bool:
    return find_n(list, needle, 1)

def find_n(list, needle, n) -> bool:
    if n < 0:
        return False
    
    return list.count(needle) >= n

def find_streak(list, needle, n) -> bool:
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
    
def first_elements(matrix) -> list:
    return nth_elements(matrix, 0)

def nth_elements(matrix, n) -> list:
    return [row[n] for row in matrix if len(row) > n]

def transpose(matrix) -> list:
    result = []
    
    if len(matrix) <= 0:
        return result

    for i in range(len(matrix[0])):
        result.append(nth_elements(matrix, i))

    return result

def displace(list, distance, fill=None) -> list:
    if distance == 0:
        return list


    if distance > 0:
        filling = [fill] * distance
        return (filling + list)[:-distance]

    filling = [fill] * abs(distance)
    return (list + filling)[abs(distance):]

def displace_matrix(matrix, fill=None) -> list:
    return [displace(matrix[i], i - 1, fill) for i in range(len(matrix))]

def reverse_list(list) -> list:
    return list[::-1]

def reverse_matrix(matrix) -> list:
    return [reverse_list(row) for row in matrix]

def all_same(l) -> bool:
    if l == []:
        return True
    else:
        same = True
        first = l[0]
        for elt in l:
            if elt != first:
                same = False
                break
        return same 