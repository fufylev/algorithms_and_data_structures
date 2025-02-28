import random


def cumsum(lst):
    cumulative_sum = 0
    result = []
    for num in lst:
        cumulative_sum += num
        result.append(cumulative_sum)
    return result


def weighted_choice(probs, size):
    cums = cumsum(probs)
    print(cums);
    res = []
    for i in range(size):
        r = random.uniform(0, 1)
        print(r);
        for i, c in enumerate(cums):
            if r <= c:
                res.append(i)
                break
    return res


if __name__ == "__main__":
    stream = [0.1, 0.3, 0.4, 0.2];
    n = len(stream);
    k = 10;
    print(weighted_choice(stream, k));