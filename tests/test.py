import numpy as np


def dcg_at_k(r, k):
    t = np.asfarray(r)[:k]

    if t.size:
        return np.sum(t[0:] / np.log2(np.arange(2, t.size + 2)))
    return 0.


def ndcg_at_k(r, k):
    dcg_max = dcg_at_k(sorted(r, reverse=True), k)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k) / dcg_max


def map_at_k(r, k):
    t = np.asfarray(r)[:k]

    if t.size:
        res = 0
        summ = 0
        for i in range(k):
            summ += t[i]
            res += t[i] * summ / (i + 1)
        return res / k
    return 0.


def print_metrics(map_arr, ndsg_arr):
    ndcg5 = [ndcg_at_k(i, 5) for i in ndsg_arr]
    ndcg10 = [ndcg_at_k(i, 10) for i in ndsg_arr]
    map5 = [map_at_k(i, 5) for i in map_arr]
    map10 = [map_at_k(i, 10) for i in map_arr]
    print("NDCG@5: ", np.mean(ndcg5))
    print("NDCG@10: ", np.mean(ndcg10))
    print("MAP@5: ", np.mean(map5))
    print("MAP@10: ", np.mean(map10))


map_arr = [[1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
           [0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1, 1]]

ndsg_arr = [[2, 2, 1, 2, 2, 2, 2, 1, 2, 2],
            [2, 2, 1, 1, 1, 1, 2, 2, 0, 2],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 2, 0, 0, 2, 0, 0, 0, 2],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 2, 1, 2, 2, 1, 0, 2, 1]]

print("find resume")
print_metrics(map_arr, ndsg_arr)

map_arr = [[0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
           [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]]

ndsg_arr = [[1, 2, 2, 0, 2, 0, 0, 0, 0, 0],
            [2, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [2, 2, 0, 1, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 1, 0, 2, 0],
            [2, 0, 2, 2, 0, 0, 0, 0, 0, 0],
            [1, 2, 2, 1, 2, 1, 1, 2, 1, 2],
            [2, 1, 2, 2, 0, 2, 0, 2, 0, 0],
            [2, 2, 2, 0, 2, 0, 0, 0, 0, 2],
            [1, 2, 1, 0, 2, 2, 0, 1, 0, 1],
            [0, 2, 2, 0, 0, 0, 0, 0, 0, 0]]
print("\nfind vacancies")
print_metrics(map_arr, ndsg_arr)
