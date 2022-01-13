def quick_sort(start, end, l: list):
    if end <= start:
        return
    index = q2(start, end, l)
    quick_sort(index + 1, end, l)
    quick_sort(start, index - 1, l)


def q2(start, end, l):
    a = l[start]
    mark = start
    for i in range(start + 1, end+1):
        if l[i] < a:
            mark += 1
            l[mark], l[i] = l[i], l[mark]
    l[start], l[mark] = l[mark], l[start]
    return mark


l = [5, 3, 6, 8, 5, 1, 3]
quick_sort(0, len(l) - 1, l)
print(l)
