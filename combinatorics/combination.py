def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    print(f"n, r = {n}, {r}")
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                print(f">>>for i: i, indices[i], i+n-r = {i}, {indices[i]}, {i+n-r}")
                break
        else:
            return
        indices[i] += 1
        print(f">>i, indices[i], i = {i}, {indices[i]}")
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
            print(f">for j: j, indices[j] = {j}, {indices[j]}")
        yield tuple(pool[i] for i in indices)
