def partition(nums, left, right):
    p = nums[left]
    mark = left
    for i in range(left + 1, right + 1):
        if nums[i] < p:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[mark], nums[left] = nums[left], nums[mark]
    return mark


def quick_sort(nums, left, right):
    if left >= right:
        return
    part = partition(nums, left, right)
    quick_sort(nums, left, part - 1)
    quick_sort(nums, part + 1, right)


l = [5, 3, 6, 8, 5, 1, 3]
# quick_sort(0, len(l) - 1, l)
quick_sort(l, 0, len(l) - 1)
print(l)
