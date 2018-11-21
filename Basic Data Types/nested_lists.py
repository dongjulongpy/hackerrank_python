if __name__ == '__main__':
    scores = list()
    for _ in range(int(input())):
        scores.append([input(), float(input())])
        scores.sort()

second_min = sorted(list(set(score for name, score in scores)))[1]
print("\n".join(i[0] for i in sorted(scores) if i[1] == second_min))
