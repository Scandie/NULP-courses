def non_uniq(X):
    new_X = []
    i = 0
    while i != len(X):
        if X.count(X[i]) > 1:
            new_X.append(X[i])
        i += 1
    return new_X
