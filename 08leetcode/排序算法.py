# 快速排序
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index - 1, nums)
    quick_sort(pivot_index + 1, end, nums)


def partition(begin, end, nums):
    # 取第一个数作为基准数
    pivot = nums[begin]
    # 记录基准数的索引
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark


# 归并排序
def merge(array, left, mid, right):
    tmp = [0] * (right - left + 1)
    i = left
    j = mid + 1
    k = 0
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = array[i]
        k += 1
        i += 1
    while j <= right:
        tmp[k] = array[j]
        k += 1
        j += 1
    array[left:right + 1] = tmp


def mergeSort(array, left, right):
    if right <= left:
        return
    mid = left + right >> 1
    mergeSort(array, left, mid)
    mergeSort(array, mid + 1, right)
    merge(array, left, mid, right)
l = [5, 3, 6, 8, 5, 1, 3]
# quick_sort(0, len(l) - 1, l)
mergeSort(l,0, len(l) - 1)
print(l)


# def merge_sort(arr):
#     # 对最后一个数组进行拆分
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     # 在两个部分上递归执行merge_sort
#     left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
#
#     # 合并在一起
#     return merge(left, right, arr.copy())
#
#
# def merge(left, right, merged):
#     left_cursor, right_cursor = 0, 0
#     while left_cursor < len(left) and right_cursor < len(right):
#
#         # 将每一个排序并放入结果
#         if left[left_cursor] <= right[right_cursor]:
#             merged[left_cursor + right_cursor] = left[left_cursor]
#             left_cursor += 1
#         else:
#             merged[left_cursor + right_cursor] = right[right_cursor]
#             right_cursor += 1
#
#     for left_cursor in range(left_cursor, len(left)):
#         merged[left_cursor + right_cursor] = left[left_cursor]
#
#     for right_cursor in range(right_cursor, len(right)):
#         merged[left_cursor + right_cursor] = right[right_cursor]
#
#     return merged


