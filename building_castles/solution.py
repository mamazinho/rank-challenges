def has_castle_on(actual, n, previous=None):
    if previous:
        return previous < actual > n or previous > actual < n
    return n != actual


def solution2(A):
    i = 0
    previous = None
    castles = []

    if len(set(A)) == 1:
        return 1

    while i < len(A):
        if i == len(A) - 1:
            castles.append("final")
            break

        actual = A[i]
        n = A[i+1]
        if actual == n:
            i += 1 
            continue

        if has_castle_on(actual, n, previous):
            castles.append(i)
        
        previous = actual
        i += 1

    return len(castles)

def solution(A):
    prev = None
    nxt = None
    castles = []
    len_heights = len(A)
    if len(set(A)) == 1:
        return 1

    for index, curr in enumerate(A):
        if index == len_heights - 1:
            castles.append("final_castle")
            break

        nxt = A[index+1]
        if nxt == curr:
            continue
        if prev is None:
            if nxt > curr:
                print("makes a valley", curr)
                castles.append("valley")
            if nxt < curr:
                print("makes a hill", curr)
                castles.append("hill")
        else: 
            if prev < curr > nxt:
                print("makes a hill", curr)
                castles.append("hill")
            if prev > curr < nxt:
                print("makes a valley", curr)
                castles.append("valley")

        prev = curr
    
    print(castles)
    return len(castles)


if __name__ == "__main__":
    tests = (
        [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5],
        [-3,-3],
        [-3, -3, -1, 3, 3, 9, 8, 7],
        [-3,-3, -1, 3, 3, 9, 8, 7, 7],
        [-3,-3, 3, 3, 9, 8, 7, 7],
        [-3, 3, 3, 2],
        [-3,-3, 3, 4, 3, 3, 2, 2],
        [-3, -3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 2, 2],
        [-3, -3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 2]
    )
    for suit in tests:
        result = solution(suit)
        print(f"\nrunning the first solution, {result=}", result)

        result = solution2(suit)
        print(f"\nrunning the second solution, {result=}", result)
