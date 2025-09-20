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
    
    