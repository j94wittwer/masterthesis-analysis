from textdistance import levenshtein


def process_array(arr):
    arr = remove_zeros(arr)

    arr = extract_first_scan(arr)

    new_arr = remove_concurrent_duplicates(arr)

    return new_arr


def remove_concurrent_duplicates(arr):
    new_arr = [arr[0]]
    for num in arr[1:]:
        if num != new_arr[-1]:
            new_arr.append(num)
    return new_arr


def extract_first_scan(arr):
    indices_to_remove = []
    for num in [32, 61, 50]:
        if num in arr:
            index = arr.index(num)
            indices_to_remove.append(index)
    if indices_to_remove:
        min_index = min(indices_to_remove)
        arr = arr[:min_index + 1]
    return arr


def remove_zeros(arr):
    arr = [x for x in arr if x != 0]
    return arr


run1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 78, 5, 0, 10, 0, 10, 11, 0, 1, 0, 11, 0, 1, 10, 5, 0, 11, 1, 11, 1, 0, 1, 0, 1,
        0, 10, 13, 0, 1, 0, 78, 0, 1, 0, 1, 0, 1, 0, 1, 0, 13, 0, 13, 0, 11, 0, 10, 0, 34, 0, 12, 11, 12, 11, 12, 0, 11,
        0, 15, 0, 15, 0, 15, 0, 6, 0, 16, 0, 16, 0, 16, 0, 37, 0, 37, 0, 37, 16, 37, 0, 37, 0, 16, 37, 0, 37, 0, 16, 37,
        0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 54, 0, 6, 0, 6, 0, 19, 0, 40, 0, 19, 40, 0, 41, 0, 19, 0, 39, 0, 39, 0, 39, 0,
        20, 0, 20, 0, 39, 0, 39, 0, 39, 0, 40, 0, 20, 0, 55, 0, 19, 0, 20, 0, 40, 19, 40, 55, 0, 39, 19, 0, 19, 40, 0,
        55, 0, 20, 0, 55, 0, 19, 0, 19, 40, 0, 42, 0, 21, 0, 43, 0, 43, 0, 43, 0, 43, 0, 3, 8, 3, 0, 3, 8, 0, 3, 0, 3,
        0, 3, 0, 3, 62, 8, 3, 8, 0, 62, 0, 62, 0, 62, 0, 62, 0, 63, 0, 63, 0, 63, 0, 22, 0, 63, 0, 63, 0, 63, 0, 63, 0,
        63, 0, 22, 0, 22, 0, 23, 0, 24, 0, 24, 0, 63, 23, 0, 25, 0, 25, 0, 25, 0, 25, 0, 63, 0, 25, 0, 25, 0, 25, 0, 25,
        0, 25, 0, 25, 0, 26, 0, 25, 0, 23, 0, 21, 0, 1, 78, 0, 78, 10, 5, 10, 78, 1, 78, 11, 0, 11, 0, 33, 11, 0, 12, 0,
        78, 0, 1, 10, 12, 13, 1, 0, 13, 0, 33, 1, 13, 0, 1, 0, 35, 15, 36, 13, 10, 11, 12, 0, 11, 0, 12, 0, 35, 6, 0,
        52, 0, 18, 54, 0, 6, 0, 12, 11, 0, 6, 52, 0, 53, 0, 51, 0, 51, 53, 0, 51, 53, 51, 52, 6, 0, 11, 5, 0, 5, 6, 0,
        51, 0, 17, 53, 0, 53, 6, 0, 54, 0, 17, 0, 51, 0, 18, 0, 18, 0, 18, 0, 54, 51, 0, 51, 0, 6, 0, 33, 78, 12, 11,
        13, 0, 6, 7, 0, 7, 6, 0, 6, 0, 11, 0, 12, 0, 11, 0, 12, 11, 33, 0, 34, 0, 36, 0, 13, 0, 6, 7, 6, 0, 7, 0, 53, 0,
        51, 0, 38, 0, 54, 17, 0, 7, 6, 0, 10, 78, 0, 1, 13, 6, 0, 41, 0, 43, 3, 8, 62, 0, 63, 0, 24, 0, 53, 6, 7, 6, 0,
        53, 38, 0, 53, 0, 51, 0, 38, 0, 38, 0, 38, 0, 51, 0, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 0, 6, 0, 6, 0, 6, 0, 6, 52,
        0, 7, 6, 0, 53, 0, 53, 0, 17, 0, 53, 0, 53, 0, 53, 0, 53, 0, 53, 0, 17, 0, 53, 0, 17, 0, 53, 17, 0, 17, 0, 53,
        0, 53, 0, 53, 0, 53, 0, 53, 0, 17, 0, 53, 0, 53, 17, 0, 51, 0, 53, 0, 53, 0, 53, 17, 0, 20, 0, 20, 0, 3, 62, 0,
        63, 0, 22, 0, 22, 0, 22, 63, 0, 22, 0, 63, 0, 22, 0, 56, 0, 54, 0, 54, 0, 53, 0, 53, 0, 53, 0, 53, 0, 53, 0, 18,
        0, 53, 0, 53, 0, 53, 0, 53, 0, 53, 0, 53, 0, 53, 0, 53, 0, 17, 0, 17, 53, 17, 0, 53, 0, 53, 0, 53, 0, 53, 0, 51,
        0, 51, 0, 54, 0, 51, 0, 54, 0, 54, 0, 54, 0, 54, 0, 51, 0, 51, 0, 18, 0, 51, 0, 38, 51, 0, 17, 0, 17, 0, 53, 0,
        53, 0, 53, 0, 17, 0, 51, 0, 18, 51, 0, 51, 0, 51, 0, 40, 55, 0, 55, 0, 55, 0, 55, 0, 55, 0, 55, 0, 55, 0, 55, 0,
        19, 0, 55, 0, 55, 40, 0, 40, 0, 40, 55, 0, 40, 0, 55, 0, 55, 0, 55, 0, 40, 0, 55, 0, 55, 0, 40, 0, 55, 0, 55, 0,
        55, 0, 55, 0, 55, 0, 55, 0, 55, 0, 55, 41, 0, 41, 0, 55, 0, 55, 0, 41, 0, 55, 39, 0, 41, 0, 41, 0, 41, 0, 41, 0,
        39, 0, 41, 0, 41, 0, 55, 0, 40, 55, 0, 55, 0, 41, 0, 41, 0, 41, 0, 20, 0, 20, 0, 20, 0, 20, 0, 3, 8, 3, 62, 0,
        62, 0, 8, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 8, 3, 0, 42, 0, 6, 36, 0, 10, 0, 78, 11, 33, 11, 0, 11, 13, 0, 78, 5,
        10, 1, 78, 10, 12, 11, 33, 78, 33, 12, 0, 34, 0, 34, 0, 15, 0, 6, 0, 6, 0, 6, 0, 6, 0, 15, 6, 0, 6, 52, 7, 0,
        17, 0, 39, 19, 0, 19, 40, 55, 0, 20, 0, 42, 0, 42, 56, 0, 21, 43, 0, 3, 62, 0, 3, 0, 3, 0, 63, 0, 63, 24, 0, 26,
        24, 0, 23, 0, 23, 0, 24, 0, 25, 0, 25, 0, 25, 0, 4, 64, 0, 59, 0, 30, 0, 30, 0, 30, 0, 30, 0, 30, 0, 30, 0, 30,
        0, 59, 0, 28, 0, 28, 0, 28, 0, 58, 0, 58, 0, 30, 0, 30, 0, 28, 0, 58, 0, 59, 0, 28, 0, 60, 0, 60, 0, 60, 0, 31,
        0, 60, 0, 60, 0, 31, 0, 60, 0, 60, 0, 60, 0, 60, 0, 60, 0, 60, 0, 60, 0, 60, 0, 60, 0, 59, 0, 60, 30, 0, 60, 0,
        60, 0, 60, 0, 60, 0, 31, 0, 31, 0, 31, 0, 31, 0, 31, 0, 31, 0, 31, 60, 31, 0, 31, 0, 60, 31, 0, 31, 0, 31, 0,
        32, 0, 60, 0, 60, 0, 60, 0, 31, 0, 31, 0, 60, 0, 61, 0, 31, 0, 31, 0, 57, 9, 4, 64, 4, 0, 36, 0, 1, 78, 5, 78,
        5, 11, 0, 13, 0, 12, 11, 0, 12, 0, 33, 0, 33, 10, 78, 0, 10, 11, 33, 0, 12, 13, 0, 33, 0, 78, 0, 33, 0, 34, 0,
        35, 0, 35, 0, 35, 0, 35, 0, 35, 0, 35, 0, 15, 36, 6, 7, 0, 51, 0, 18, 0, 51, 0, 18, 54, 18, 0, 54, 0, 18, 0, 18,
        54, 0, 18, 0, 51, 0, 54, 18, 0, 18, 0, 53, 6, 53, 0, 53, 0, 35, 0, 14, 0, 34, 0, 35, 0, 34, 14, 0, 14, 6, 53, 0,
        53, 0, 51, 0, 18, 54, 0, 54, 0, 38, 18, 54, 0, 39, 0, 39, 0, 40, 0, 40, 0, 40, 0, 19, 55, 0, 40, 0, 55, 0, 55,
        0, 54, 18, 0, 54, 38, 0, 38, 0, 38, 0, 38, 0, 18, 0, 19, 0, 41, 0, 41, 0, 41, 0, 39, 0, 38, 0, 51, 0, 18, 0, 18,
        54, 0, 54, 0, 54, 51, 0, 40, 0, 41, 0, 40, 0, 20, 0, 42, 0, 21, 0, 21, 0, 43, 0, 21, 0, 21, 62, 3, 8, 3, 0, 63,
        0, 63, 0, 8, 0, 62, 8, 62, 0, 63, 0, 64, 4, 64, 4, 64, 4, 27, 0, 28, 58, 0, 61, 0, 32, 0, 32, 0, 61, 0, 50, 0,
        50, 61, 0, 40, 0, 1, 0, 1, 0, 1, 0, 1, 0]
run2 = [1, 11, 5, 11, 1, 11, 1, 10, 1, 11, 1, 10, 1, 11, 0, 33, 0, 33, 0, 33, 13, 34, 0, 34, 0, 14, 0, 14, 0, 34, 13,
        34, 0, 33, 0, 34, 0, 34, 0, 35, 14, 13, 0, 35, 0, 34, 0, 33, 14, 35, 0, 6, 7, 6, 52, 6, 52, 0, 52, 53, 52, 53,
        51, 17, 0, 51, 0, 17, 0, 18, 0, 17, 0, 51, 0, 17, 0, 51, 0, 51, 0, 51, 0, 51, 54, 0, 51, 0, 51, 0, 15, 33, 34,
        35, 17, 0, 54, 17, 53, 0, 54, 0, 54, 0, 54, 0, 18, 54, 0, 18, 54, 0, 54, 0, 54, 0, 54, 0, 38, 0, 39, 0, 39, 38,
        54, 0, 54, 0, 38, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0, 38, 0, 38, 0, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0, 38, 0, 38,
        0, 39, 0, 39, 0, 38, 0, 39, 38, 0, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0, 39, 0,
        39, 0, 40, 19, 0, 40, 55, 0, 55, 0, 41, 0, 55, 0, 55, 0, 41, 0, 41, 0, 41, 0, 20, 43, 0, 43, 21, 0, 20, 0, 42,
        20, 0, 42, 20, 0, 42, 0, 20, 0, 56, 0, 56, 0, 42, 0, 43, 0, 3, 8, 63, 62, 0, 63, 22, 0, 23, 0, 22, 0, 4, 64, 65,
        0, 65, 27, 57, 0, 57, 0, 29, 59, 0, 58, 0, 30, 59, 30, 61, 0, 61, 0, 61, 32, 31, 32, 0, 57, 27, 65, 4, 9, 64,
        65, 27, 0, 65, 0, 65, 27, 65, 0, 65, 0, 57, 0, 28, 0, 57, 0, 57, 0, 58, 0, 58, 0, 58, 0, 58, 0, 58, 0, 58, 0, 4,
        29, 30, 0, 31, 0, 60, 0, 31, 0, 61, 0, 4, 63, 0, 53, 35, 1, 0, 33, 11, 33, 0, 34, 0, 35, 6, 52, 53, 52, 53, 37,
        0, 11, 0, 37, 0, 37, 36, 6, 52, 18, 0, 34, 0, 11, 37, 0, 10, 5, 33, 34, 35, 0, 36, 37, 0, 36, 37, 0, 36, 35, 0,
        35, 34, 35, 0, 35, 0, 35, 36, 35, 36, 34, 0, 6, 52, 53, 17, 0, 17, 51, 17, 51, 0, 53, 0, 51, 0, 51, 54, 0, 53,
        52, 0, 51, 0]
run3 = [0, 1, 0, 1, 11, 0, 1, 10, 1, 11, 10, 1, 10, 1, 5, 0, 11, 0, 11, 12, 11, 0, 33, 13, 33, 0, 33, 0, 33, 0, 34, 0,
        34, 11, 0, 35, 0, 35, 0, 36, 0, 36, 37, 0, 37, 0, 35, 0, 15, 37, 0, 37, 0, 37, 0, 37, 14, 0, 11, 6, 0, 6, 0, 7,
        0, 6, 7, 53, 6, 0, 6, 7, 6, 52, 53, 7, 53, 0, 17, 0, 51, 71, 51, 71, 54, 71, 51, 71, 51, 71, 51, 71, 0, 51, 71,
        0, 71, 0, 18, 0, 72, 38, 72, 54, 72, 51, 71, 51, 71, 0, 71, 72, 38, 72, 38, 72, 38, 72, 39, 72, 39, 72, 39, 72,
        39, 72, 0, 72, 54, 72, 54, 72, 54, 72, 38, 72, 38, 72, 39, 54, 39, 72, 39, 72, 39, 72, 39, 72, 39, 72, 39, 72,
        54, 40, 73, 40, 55, 73, 55, 73, 40, 73, 41, 73, 41, 73, 41, 55, 73, 41, 0, 55, 41, 73, 41, 73, 41, 73, 41, 73,
        41, 40, 73, 41, 55, 73, 41, 73, 0, 73, 41, 55, 72, 39, 73, 40, 41, 73, 0, 73, 0, 55]
run4 = [0, 1, 0, 6, 41, 3, 0, 31, 32, 0, 4, 18, 0, 1, 10, 1, 5, 1, 10, 1, 5, 0, 10, 5, 0, 10, 11, 12, 33, 12, 33, 13,
        34, 13, 34, 0, 10, 11, 0, 34, 13, 34, 13, 34, 13, 35, 14, 0, 35, 14, 35, 14, 0, 35, 0, 6, 53, 18, 6, 16, 0, 35,
        15, 36, 15, 36, 37, 16, 37, 0, 35, 13, 34, 0, 33, 12, 13, 0, 35, 0, 14, 35, 7, 53, 71, 54, 0, 19, 54, 40, 73,
        40, 19, 6, 0, 15, 35, 14, 33, 11, 10, 5, 16, 37, 0, 1, 0, 6, 0, 6, 7, 0, 7, 52, 53, 0, 53, 0, 17, 71, 17, 51,
        71, 51, 71, 51, 71, 51, 71, 0, 54, 18, 54, 18, 54, 18, 72, 54, 72, 54, 18, 54, 72, 18, 54, 72, 54, 72, 54, 72,
        54, 72, 54, 0, 54, 0, 54, 18, 0, 72, 38, 72, 38, 72, 54, 18, 54, 38, 39, 72, 38, 72, 39, 72, 39, 72, 39, 72, 39,
        72, 39, 0, 40, 19, 0, 40, 73, 55, 73, 55, 73, 55, 42, 20, 55, 42, 56, 42, 56, 74, 56, 42, 74, 56, 74, 56, 74,
        56, 42, 74, 56, 74, 42, 40, 19, 74, 75, 42, 56, 74, 42, 56, 74, 0, 74, 20, 42, 20, 42, 21, 0, 40, 73, 55, 73,
        55, 40, 19, 40, 55, 73, 41, 73, 41, 73, 41, 73, 41, 73, 41, 73, 41, 73, 74, 20, 56, 74, 21, 75, 43, 75, 43, 75,
        43, 75, 43, 75, 0, 3, 62, 63, 66, 67, 66, 67, 63, 62, 23, 68, 63, 62, 25, 62, 68, 69, 0, 69, 70, 26, 0, 8, 0, 3,
        0, 3, 8, 3, 0, 3, 8, 3, 0, 3, 0, 3, 62, 8, 0, 62, 0, 62, 0, 63, 0, 63, 66, 22, 66, 68, 0, 4, 64, 65, 0, 27, 65,
        27, 0, 27, 57, 0, 68, 67, 0, 68, 69, 24, 0, 66, 63, 66, 22, 66, 0, 68, 67, 0, 23, 67, 68, 25, 0, 69, 0, 25, 63,
        23, 0, 66, 23, 0, 23, 24, 67, 68, 0, 25, 69, 70, 68, 25, 69, 70, 0, 4, 0, 70, 0, 70, 0, 4, 65, 4, 0, 4, 9, 64,
        65, 27, 0, 27, 0, 27, 0, 4, 0, 63, 62, 3, 73, 74, 53, 0, 1, 5, 10, 1, 11, 10, 1, 11, 33, 0, 33, 34, 0, 35, 0,
        35, 0, 13]
run5 = [0, 1, 0, 1, 10, 0, 10, 5, 0, 8, 47, 0, 47, 0, 60, 0, 60, 0, 60, 0, 60, 47, 0, 60, 47, 60, 0, 60, 0, 60, 0, 47,
        0, 30, 0, 29, 28, 45, 44, 57, 0, 64, 9, 64, 27, 65, 45, 0, 30, 0, 30, 0, 47, 0, 46, 0, 59, 46, 0, 46, 29, 59, 0,
        30, 0, 59, 46, 45, 46, 59, 46, 0, 46, 45, 0, 44, 27, 57, 44, 0, 44, 0, 44, 27, 65, 4, 64, 65, 0, 65, 70, 0, 68,
        23, 63, 62, 0, 3, 63, 67, 23, 0, 66, 67, 66, 63, 75, 0, 19, 40, 75, 43, 75, 43, 75, 43, 75, 43, 75, 43, 75, 43,
        75, 0, 74, 56, 74, 56, 74, 56, 42, 43, 56, 74, 42, 56, 74, 42, 56, 42, 74, 42, 56, 0, 74, 56, 74, 56, 42, 74,
        73, 41, 73, 40, 73, 40, 55, 73, 41, 73, 41, 20, 73, 41, 73, 41, 73, 41, 73, 41, 73, 41, 73, 41, 55, 40, 73, 40,
        73, 55, 73, 55, 73, 40, 73, 19, 40, 55, 41, 73, 41, 73, 41, 73, 41, 73, 0]
run6 = [0, 6, 0, 6, 0, 6, 7, 0, 6, 0, 6, 52, 0, 52, 0, 7, 0, 52, 0, 52, 0, 6, 0, 7, 52, 53, 0, 52, 0, 53, 52, 7, 53, 17,
        0, 6, 17, 0, 17, 0, 17, 71, 51, 0, 51, 0, 71, 0, 51, 0, 72, 54, 38, 54, 72, 38, 72, 38, 72, 7, 6, 7, 52, 6, 52,
        6, 38, 39, 0, 7, 72, 38, 39, 72, 39, 0, 54, 72, 38, 72, 39, 72, 54, 51, 0, 51, 18, 0, 6, 0, 6, 0, 6, 52, 0, 6,
        0, 7, 6, 52, 0, 53, 52, 53, 52, 0, 53, 52, 0, 52, 53, 17, 71, 51, 52, 0, 71]
run7 = [0, 1, 11, 12, 33, 0, 33, 0, 33, 0, 35, 0, 33, 0, 33, 0, 34, 33, 35, 36, 35, 0, 13, 0, 12, 34, 33, 13, 0, 12, 14,
        0, 12, 33, 13, 0, 14, 34, 0, 35, 0, 35, 0, 36, 37, 36, 15, 34, 13, 34, 0, 14, 0, 13, 0, 13, 0, 13, 0, 14, 0, 13,
        0, 12, 0, 12, 11, 0, 35, 0, 35, 0, 36, 0, 37, 0, 6, 17, 0, 53, 73, 0, 53, 52, 53, 0, 11, 6, 17, 0, 53, 0, 17,
        53, 0, 53, 51]
run8 = [0, 1, 0, 1, 0, 10, 11, 1, 13, 0, 16, 0, 10, 1, 11, 1, 0, 1, 0, 1, 5, 0, 1, 5, 10, 1, 5, 11, 6, 53, 6, 53, 72,
        54, 72, 18, 51, 72, 40, 73, 74, 75, 3, 0, 3, 62, 69, 26, 0, 4, 27, 44, 46, 47, 31, 47, 0, 46, 0, 4, 24, 63, 74,
        3, 73, 7, 13, 1, 5, 0, 1, 5, 1, 5, 10, 5, 10, 1, 10, 11, 0, 11, 1, 14, 0, 15, 0, 35, 1, 5, 1, 5, 0, 11, 1, 5,
        10, 0, 11, 1, 33, 14, 35, 34, 0, 13, 14, 35, 0, 34, 15, 36, 12, 33, 13, 0, 12, 34, 33, 0, 33, 11, 10, 16, 0, 1,
        0, 35, 0, 34, 1, 10, 11, 13, 14, 0, 14, 35, 0, 16, 37, 16, 37, 0, 36, 0, 15, 36, 15, 36, 0, 36, 15, 0, 35, 36,
        0, 35, 1, 0, 1, 0, 34, 14, 0, 36, 0, 11, 0, 12, 33, 12, 13, 0, 13, 33, 10, 11, 12, 1, 0, 11, 0, 13, 33, 0, 34,
        0, 34, 0, 34, 35, 0, 15, 35, 36, 15, 36, 0]
run9 = [0, 5, 0, 1, 0, 1, 0, 1, 11, 10, 0, 1, 5, 1, 0, 1, 5, 10, 5, 0, 66, 36, 1, 0, 13, 12, 33, 11, 10, 11, 10, 5, 10,
        11, 10, 11, 1, 11, 0, 10, 11, 10, 11, 10, 11, 10, 11, 33, 11, 0, 10, 0, 16, 37, 16, 35, 0, 12, 10, 0, 11, 10,
        11, 12, 11, 10, 0, 12, 33, 0, 33, 11, 0, 11, 0, 33, 0, 33, 0, 33, 13, 0, 33, 0, 34, 0, 34, 13, 33, 34, 33, 0, 1,
        0, 34, 1, 13, 34, 0, 34, 0, 33, 34, 0, 14, 35, 0, 14, 0, 13, 34, 33, 0, 34, 0, 10, 11, 0, 35, 0, 34, 0, 35, 0,
        35, 0, 36, 0, 36, 0, 36, 0, 15, 35, 0, 35, 0, 37, 6, 37, 0, 37, 0, 37, 36, 0, 35, 0, 35, 0, 6, 0, 11, 1, 0, 1,
        5, 1, 5, 10, 5, 0, 10, 11, 10, 1, 11, 10, 11, 10, 1, 0, 1, 0, 1, 11, 0, 6, 37, 6, 53, 52, 53, 52, 53, 0, 53, 0,
        53, 0, 17, 51, 7, 0, 52, 71, 51, 53, 51, 0, 51, 71, 51, 71, 51, 71, 51, 6, 0, 6, 0, 18, 51, 0, 51, 71, 0, 71,
        51, 71, 0, 18, 51, 71, 51, 71, 0, 51, 71, 51, 71, 51, 71, 51, 71, 51, 71, 51, 71, 17, 71, 51, 54, 0, 54, 0, 54,
        0, 54, 0, 54, 0, 54, 0, 54, 0, 54, 0, 38, 0, 72, 0, 38, 0, 72, 54, 0, 54, 0, 54, 0, 54, 0, 72, 0, 74, 20, 0, 72,
        0, 72, 74, 0, 72, 0, 74, 20, 0, 73, 56, 0, 73, 0, 73, 0, 73, 0, 54, 0, 74, 73, 0, 73, 0, 72, 0, 39, 0, 73, 0,
        72, 0, 73, 56, 0, 72, 0, 72, 0, 54, 0, 54, 0, 72, 39, 72, 39, 72, 39, 73, 40, 73, 55, 73, 41, 55, 73, 41, 73,
        41, 73, 41, 73, 40, 73, 40, 0, 54, 0, 39, 72, 0, 54, 73, 55, 73, 41, 73, 40, 73, 40, 55, 18, 54, 18, 54, 0, 39,
        72, 39, 72, 0, 38, 72, 38, 0, 39, 0, 18, 0]
run11 = [0, 1, 10, 1, 0, 1, 5, 1, 5, 1, 5, 10, 11, 5, 0, 33, 11, 1, 0, 10, 0, 10, 1, 10, 0, 11, 0, 11, 1, 11, 12, 33,
         11, 33, 0, 33, 12, 10, 12, 10, 5, 1, 11, 12, 33, 0, 33, 12, 11, 33, 11, 33, 12, 11, 10, 0, 5, 10, 0, 11, 33,
         12, 0, 33, 12, 0, 12, 0, 33, 12, 33, 0, 33, 0, 33, 11, 33, 0, 12, 33, 0, 33, 0, 33, 0, 12, 0, 33, 0, 14, 16, 0,
         6, 0, 6, 0, 35, 14, 34, 0, 36, 35, 34, 0, 11, 5, 0, 6, 52, 7, 52, 7, 6, 7, 0, 7, 0, 6, 0, 7, 0, 7, 6, 7, 6, 0,
         6, 7, 0, 52, 0, 7, 52, 6, 52, 6, 0, 6, 7, 52, 0, 6, 0, 52, 7, 52, 6, 0, 6, 0, 52, 7, 0, 52, 0, 6, 52, 6, 0, 52,
         7, 0, 52, 0, 52, 0, 52, 0, 53, 52, 0, 52, 7, 0, 52, 0, 52, 7, 0, 6, 0, 10, 11, 0, 6, 0, 18, 54, 18, 0, 18, 0,
         18, 54, 18, 54, 0, 18, 54, 0, 54, 0, 51, 0, 18, 0, 54, 0, 54, 0, 54, 0, 54, 0, 54, 0, 6, 7, 52, 0, 53, 6, 0,
         16, 0, 16, 0, 35, 15, 0, 15, 36, 0, 15, 35, 14, 0, 6, 17, 0, 7, 0, 7, 0, 6, 52, 71, 0, 52, 6, 7, 6, 17, 0, 7,
         6, 7, 6, 17, 53, 7, 53, 7, 6, 53, 6, 52, 0, 7, 6, 0, 6, 0, 6, 0, 6, 0, 53, 52, 6, 0, 51, 0, 73, 0, 39, 0, 76,
         0, 76, 0, 39, 0, 3, 0, 63, 0, 3, 0, 8, 62, 0, 3, 0, 3, 75, 0, 19, 0, 52, 37, 0, 1, 0, 14, 0, 6, 53, 0, 76, 0,
         76, 0, 76, 0, 39, 72, 0, 72, 0, 72, 0, 39, 0, 72, 0, 72, 39, 72, 0, 72, 0, 39, 72, 0, 6, 13, 0, 13, 34, 13, 34,
         0, 39, 0, 72, 0, 39, 72, 0, 72, 0, 72, 0, 72, 39, 72, 0, 19, 0, 19, 0, 39, 19, 0, 40, 0, 19, 40, 55, 0, 39, 0,
         72, 19, 0, 73, 0, 73, 0, 73, 0, 73, 0, 73, 0, 73, 41, 0, 73, 41, 73, 41, 73, 41, 73, 0, 73, 0, 73, 55, 0, 40,
         19, 40, 55, 73, 0, 73, 0, 73, 0, 73, 0, 20, 0, 73, 0, 73, 0, 73, 0, 73, 19, 72, 19, 40, 73, 0, 40, 55, 0, 72,
         0, 19, 0, 72, 55, 0, 55, 0, 72, 41, 73, 0, 73, 0, 73, 0, 73, 41, 0, 73, 41, 73, 41, 73, 0, 73, 20, 73, 20, 73,
         0, 73, 20, 0, 73, 0, 73, 20, 73, 0, 73, 0, 42, 0, 42, 0, 42, 0, 42, 0, 42, 0, 42, 0, 56, 0, 24, 0, 68, 0, 68,
         24, 68, 0, 73, 0, 20, 0, 73, 0, 73, 0, 42, 0, 56, 0, 42, 0, 42, 0, 74, 0, 74, 0, 74, 0, 74, 0, 4, 0, 68, 24,
         68, 0, 25, 0, 68, 0, 3, 8, 0, 74, 0, 74, 0, 74, 0, 74, 0, 74, 0, 74, 0, 74, 0, 74, 0, 74, 0, 74, 0, 74, 0, 56,
         0, 56, 0, 42, 0, 20, 0, 72, 0, 73, 0, 74, 0, 43, 75, 0, 3, 43, 3, 75, 0, 3, 8, 3, 8, 3, 0, 3, 8, 3, 8, 0, 3, 0,
         78, 0, 63, 0, 22, 0, 22, 0, 63, 0, 22, 0, 66, 0, 66, 23, 66, 0, 3, 0, 22, 66, 0, 22, 0, 3, 0, 75, 0, 66, 23, 0,
         66, 0, 66, 0, 24, 0, 24, 0, 23, 0, 66, 0, 26, 0, 68, 67, 26, 67, 0, 26, 0, 26, 0, 26, 69, 0, 69, 70, 0, 4, 0,
         4, 0, 4, 0, 4, 0, 4, 23, 0, 73, 0, 76, 0, 6, 0, 6, 0, 71, 6, 0, 6, 0, 76, 73, 0, 3, 0, 63, 0, 4, 0, 9, 0, 4,
         64, 4, 0, 65, 64, 65, 4, 64, 9, 64, 65, 64, 9, 4, 64, 65, 64, 65, 64, 65, 0, 64, 65, 64, 65, 0, 65, 0, 65, 0,
         65, 0, 65, 0, 65, 0, 65, 0, 57, 27, 57, 27, 57, 27, 57, 27, 0, 27, 57, 0, 57, 27, 57, 0, 57, 0, 29, 59, 0, 29,
         59, 0, 30, 60, 30, 0, 31, 0, 60, 0, 30, 60, 30, 0, 60, 30, 60, 59, 0, 30, 0, 30, 60, 0, 30, 60, 30, 76, 38, 4,
         0, 29, 60, 30, 0, 27, 0, 4, 9, 0, 31, 0, 30, 0, 30, 0, 59, 0, 60, 30, 60, 0, 27, 57, 0, 27, 0, 27, 57, 27, 0,
         27, 57, 0, 27, 0, 28, 0, 57, 0, 27, 0, 27, 0, 57, 0, 27, 0, 27, 0, 58, 28, 0, 29, 59, 29, 28, 29, 59, 0, 59,
         58, 0, 58, 0, 59, 0, 59, 0, 30, 0, 30, 0, 30, 60, 0, 29, 0, 60, 0, 28, 57, 27, 0, 27, 0, 30, 0, 32, 0, 32, 0,
         32, 0, 32, 0, 32, 0, 32, 0, 32, 0, 29, 28, 0, 27, 0, 27, 0, 57, 0, 27, 58, 0, 27, 58, 0, 30, 0, 60, 0, 30, 60,
         30, 60, 0, 60, 30, 0, 60, 0, 60, 0, 30, 0, 28, 58, 28, 58, 28, 58, 0, 58, 28, 0, 58, 60, 30, 0, 30, 60, 0, 60,
         0, 60, 0, 60, 0, 30, 0, 60, 0, 30, 0, 30, 0, 4, 0, 4, 3, 0, 6, 0, 5, 1, 12, 0, 13, 34, 0, 11, 10, 11, 0, 12,
         11, 0, 13, 34, 13, 14, 34, 13, 35, 36, 37, 16, 0, 13, 14, 35, 14, 35, 14, 0, 15, 36, 15, 36, 37, 0, 37, 16, 37,
         16, 0, 6, 7, 52, 53, 71, 52, 0, 53, 7, 0, 51, 53, 52, 7, 53, 17, 51, 7, 0, 71, 17, 53, 52, 53, 71, 0, 54, 18,
         0, 76, 0, 76, 38, 76, 0, 40, 0, 73, 0, 42, 0, 42, 0, 42, 0, 75, 3, 0, 62, 8, 0, 78, 0, 78, 0, 66, 63, 0, 70, 0,
         4, 64, 9, 0, 65, 0, 65, 0, 31, 0, 32, 0, 32, 0, 50, 0, 50, 0, 32, 0, 32, 0, 61, 0, 50, 0]
run12 = [0, 1, 5, 10, 11, 1, 0, 1, 0, 1, 5, 1, 5, 0, 5, 10, 5, 10, 0, 11, 10, 0, 10, 5, 1, 11, 10, 11, 10, 11, 10, 11,
         10, 5, 10, 0, 11, 12, 11, 12, 11, 0, 11, 0, 11, 33, 0, 13, 33, 0, 33, 0, 33, 11, 0, 13, 0, 13, 0, 35, 0, 34, 0,
         14, 0, 11, 12, 14, 1, 0, 1, 0, 15, 0, 15, 14, 0, 15, 36, 15, 36, 0, 16, 0, 16, 37, 16, 0, 37, 16, 0, 14, 11, 5,
         1, 6, 35, 12, 11, 0, 1, 5, 10, 11, 10, 0, 11, 5, 1, 36, 0, 6, 0, 6, 0, 6, 0, 6, 7, 0, 52, 53, 6, 52, 7, 52, 7,
         6, 52, 53, 0, 52, 0, 52, 53, 0, 6, 7, 53, 52, 0, 53, 52, 6, 52, 17, 53, 0, 17, 53, 0, 17, 0, 17, 53, 0, 17, 0,
         17, 71, 0, 53, 0, 17, 0, 17, 0, 17, 0, 17, 0, 71, 17, 0, 17, 0, 17, 0, 17, 0, 53, 6, 7, 6, 0, 11, 1, 0, 71, 17,
         0, 17, 0, 51, 0, 53, 51, 0, 51, 53, 0, 71, 0, 18, 72, 54, 0, 18, 0, 18, 0, 18, 54, 18, 72, 0, 72, 54, 0, 18,
         72, 54, 72, 38, 72, 38, 72, 38, 72, 39, 0, 6, 15, 12, 11, 35, 0, 15, 6, 0, 6, 0, 15, 0, 71, 0, 6, 52, 53, 0, 1,
         10, 6, 71, 0, 72, 54, 18, 54, 72, 54, 72, 54, 72, 38, 72, 38, 72, 38, 72, 38, 72, 38, 72, 38, 72, 38, 72, 39,
         72, 38, 72, 18, 51, 0, 72, 38, 72, 39, 72, 39, 38, 18, 0, 54, 0, 18, 54, 18, 72, 0, 18, 0, 18, 0, 18, 72, 38,
         72, 38, 72, 18, 54, 72, 38, 72, 38, 72, 38, 72, 18, 0, 18, 72, 0, 72, 54, 72, 38, 72, 39, 72, 39, 72, 39, 72,
         54, 0, 18, 72, 18, 0, 39, 72, 6, 7, 53, 0, 39, 18, 51, 0, 71, 0, 17, 53, 17, 72, 0, 35, 0, 34, 0, 14, 0, 15,
         36, 15, 0, 36, 15, 0, 15, 0, 15, 0, 14, 0, 33, 15, 0, 36, 15, 36, 0, 15, 6, 72, 55, 73, 55, 0, 73, 41, 73, 55,
         73, 41, 73, 19, 73, 0, 73, 0, 73, 0, 73, 0, 73, 0, 73, 0, 73, 0, 73, 0, 73, 19, 72, 39, 0, 20, 42, 0, 73, 0,
         42, 0, 42, 0, 20, 42, 0, 20, 0, 42, 0, 42, 0, 42, 0, 56, 0, 42, 20, 42, 0, 20, 0, 42, 0, 17, 6, 0, 35, 33, 0,
         33, 35, 0, 39, 0, 42, 0, 20, 42, 0, 42, 0, 56, 20, 0, 72, 42, 0, 20, 42, 0, 42, 0, 40, 17, 7, 0, 14, 0, 34, 0,
         33, 12, 11, 0, 11, 6, 0, 11, 0, 13, 0, 18, 73, 40, 0, 18, 0, 73, 0, 19, 72, 18, 0, 51, 0, 71, 52, 6, 7, 42, 56,
         75, 0, 56, 74, 0, 74, 0, 74, 0, 21, 75, 43, 75, 0, 75, 0, 3, 8, 3, 75, 74, 0, 74, 0, 74, 0, 74, 0, 21, 0, 21,
         43, 75, 74, 0, 74, 0, 74, 0, 74, 0, 41, 0, 72, 0, 18, 19, 0, 72, 52, 6, 0, 11, 37, 72, 40, 72, 19, 73, 55, 73,
         55, 73, 0, 73, 0, 75, 3, 0, 3, 0, 74, 0, 74, 43, 74, 75, 21, 75, 43, 74, 0, 74, 43, 74, 75, 0, 75, 0, 75, 43,
         75, 0, 75, 74, 0, 74, 21, 75, 3, 8, 3, 0, 3, 8, 3, 8, 3, 8, 0, 3, 8, 3, 8, 0, 76, 0, 63, 0, 76, 63, 23, 63, 0,
         62, 0, 76, 0, 66, 0, 66, 23, 66, 0, 23, 0, 23, 0, 24, 23, 0, 75, 0, 3, 0, 3, 0, 75, 3, 63, 66, 0, 24, 66, 0, 3,
         0, 63, 76, 0, 3, 0, 3, 0, 3, 8, 0, 76, 63, 22, 23, 0, 63, 0, 63, 3, 0, 63, 66, 23, 0, 73, 55, 72, 0, 6, 7, 6,
         53, 52, 7, 52, 53, 17, 51, 38, 18, 0, 73, 0, 73, 19, 72, 0, 71, 52, 0, 52, 0, 72, 19, 73, 0, 42, 0, 37, 0, 34,
         12, 11, 0, 12, 72, 41, 0, 37, 10, 11, 10, 71, 41, 73, 0, 75, 3, 8, 0, 63, 0, 24, 0, 67, 0, 68, 0, 75, 0, 38,
         52, 16, 1, 11, 13, 1, 0, 1, 10, 37, 16, 0, 37, 7, 73, 0, 3, 0, 67, 0, 68, 0, 68, 0, 68, 0, 25, 0, 26, 70, 69,
         26, 0, 26, 70, 0, 4, 70, 26, 0, 69, 0, 69, 0, 70, 26, 70, 26, 4, 0, 58, 0, 58, 0, 58, 0, 58, 29, 0, 58, 0, 58,
         0, 29, 0, 28, 0, 29, 0, 29, 0, 59, 29, 0, 29, 0, 29, 28, 0, 29, 59, 0, 29, 0, 29, 59, 0, 64, 4, 0, 58, 0, 4, 0,
         68, 26, 0, 70, 0, 70, 0, 4, 0, 4, 0, 4, 9, 0, 4, 0, 9, 0, 4, 0, 3, 74, 0, 74, 0, 73, 0, 73, 0, 74, 3, 63, 0, 4,
         9, 0, 65, 0, 64, 0, 65, 0, 4, 0, 76, 0, 40, 51, 0, 6, 0, 16, 0, 6, 53, 0, 28, 27, 65, 0, 27, 64, 27, 0, 27, 0,
         65, 0, 58, 0, 58, 0, 28, 58, 0, 28, 0, 28, 0, 28, 58, 28, 0, 29, 0, 23, 0, 41, 72, 0, 72, 18, 53, 6, 53, 0, 18,
         0, 20, 0, 20, 0, 73, 19, 72, 0, 18, 38, 54, 18, 0, 72, 39, 38, 72, 54, 72, 38, 72, 0, 72, 39, 72, 38, 72, 38,
         72, 19, 72, 54, 38, 72, 18, 0, 38, 72, 38, 72, 38, 72, 38, 18, 72, 38, 72, 41, 73, 72, 73, 39, 72, 38, 72, 0,
         72, 19, 72, 73, 39, 72, 38, 72, 38, 72, 73, 0, 72, 38, 72, 0, 4, 0, 32, 0, 60, 0, 59, 0, 28, 0, 29, 0, 57, 0,
         64, 9, 4, 0, 4, 0, 74, 75, 0, 74, 43, 75, 3, 0, 20, 0, 73, 72, 0, 73, 51, 0, 18, 72, 18, 0, 53, 17, 6, 16, 0,
         11, 51, 73, 55, 73, 0, 73, 0, 73, 0, 73, 0, 74, 62, 0, 68, 26, 0, 4, 0, 4, 0, 70, 0, 4, 0, 27, 65, 69, 0, 4, 0,
         69, 0, 70, 4, 0, 31, 0, 32, 0, 3, 75, 0, 75, 74, 0, 43, 75, 0, 3, 0, 6, 0, 11, 5, 0, 53, 0, 17, 51, 73, 72, 38,
         19, 55, 73, 72, 0, 73, 72, 73, 0, 72, 0, 73, 0, 72, 39, 38, 72, 0, 38, 72, 0, 19, 0, 72, 0, 19, 0, 72, 0, 73,
         72, 0, 72, 39, 72, 38, 72, 38, 72, 0, 30, 0, 60, 0, 59, 29, 0, 29, 0, 29, 0, 29, 0, 29, 59, 0, 29, 59, 0, 57,
         27, 0, 59, 29, 0, 29, 0, 59, 0, 29, 59, 0, 29, 59, 0, 29, 0, 29, 0, 29, 59, 29, 59, 29, 59, 0, 59, 29, 0, 59,
         29, 59, 29, 59, 29, 59, 0, 59, 0, 30, 0, 59, 0, 59, 29, 0, 30, 0, 30, 0, 59, 29, 0, 59, 29, 59, 0, 29, 59, 0,
         30, 0, 59, 30, 0, 30, 0, 30, 0, 30, 0, 29, 0, 29, 0, 29, 59, 0, 59, 0, 65, 0, 28, 0, 30, 0, 31, 0, 70, 0, 68,
         4, 65, 0, 65, 0, 63, 22, 0, 67, 0, 74, 0, 3, 0, 3, 8, 3, 8, 0, 62, 0, 68, 70, 4, 27, 65, 63, 0, 39, 18, 0, 6,
         52, 53, 0, 51, 18, 19, 73, 0, 74, 3, 0, 75, 3, 0, 63, 25, 28, 0, 64, 65, 4, 0, 3, 72, 52, 16, 0, 16, 11, 5, 53,
         17, 53, 17, 72, 0, 18, 0, 18, 0, 18, 54, 72, 38, 72, 38, 72, 0, 72, 18, 54, 38, 72, 0, 54, 72, 0, 72, 54, 72,
         0, 73, 0, 72, 0, 39, 72, 0, 73, 38, 72, 54, 72, 55, 73, 55, 72, 54, 72, 73, 0, 74, 21, 76, 69, 4, 64, 4, 65,
         27, 0, 57, 27, 0, 75, 0, 54, 0, 53, 0, 53, 0, 17, 0, 18, 54, 72, 55, 40, 73, 55, 73, 0, 75, 21, 0, 21, 0, 21,
         0, 75, 43, 21, 0, 8, 0, 76, 4, 0, 28, 0, 27, 57, 0, 29, 59, 0, 30, 60, 30, 0, 32, 0, 30, 0, 30, 0, 30, 0, 30,
         0, 30, 0, 29, 59, 0, 31, 0, 32, 0, 60, 30, 60, 0, 61, 0, 32, 0, 61, 0, 61, 0, 32, 0, 65, 4, 0, 26, 4, 0, 4, 0]
run13 = [0, 1, 0, 1, 0, 1, 10, 5, 0, 1, 5, 1, 5, 10, 0, 1, 5, 1, 10, 11, 12, 11, 0, 12, 11, 12, 33, 0, 12, 13, 0, 14,
         35, 14, 15, 36, 37, 16, 36, 15, 36, 15, 0, 12, 33, 13, 14, 34, 0, 12, 13, 34, 14, 35, 14, 33, 12, 33, 12, 33,
         11, 33, 0, 6, 0, 6, 0, 6, 52, 6, 0, 6, 0, 6, 0, 52, 7, 6, 0, 52, 53, 17, 53, 17, 71, 51, 17, 71, 17, 51, 18,
         71, 0, 18, 0, 18, 0, 18, 54, 0, 18, 54, 18, 54, 18, 0, 18, 54, 0, 18, 54, 18, 0, 18, 0, 18, 0, 18, 0, 73, 0,
         39, 72, 0, 38, 72, 0, 72, 38, 72, 38, 72, 39, 72, 39, 38, 39, 72, 38, 72, 39, 72, 39, 72, 39, 72, 0, 38, 72,
         19, 38, 0]
run14 = [0, 1, 10, 0, 1, 0, 1, 0, 1, 0, 1, 5, 1, 5, 1, 10, 5, 1, 0, 5, 10, 0, 11, 0, 11, 10, 12, 33, 13, 12, 34, 13, 34,
         12, 33, 34, 13, 34, 6, 13, 11, 12, 11, 6, 33, 12, 11, 12, 6, 7, 0, 7, 6, 7, 53, 17, 71, 17, 71, 51, 17, 71, 17,
         71, 38, 72, 18, 51, 72, 19, 17, 53, 71, 51, 71, 51, 17, 51, 6, 52, 7, 0, 52, 53, 52, 53, 52, 71, 17, 52, 71,
         17, 71, 51, 17, 36, 11, 12, 33, 12, 33, 12, 33, 34, 13, 33, 11, 33, 6, 53, 17, 18, 51, 71, 72, 73, 20, 42, 20,
         42, 20, 42, 20, 42, 20, 42, 56, 42, 20, 42, 56, 42, 56, 42, 56, 42, 56, 42, 56, 42, 0, 74, 42, 56, 74, 56, 74,
         42, 20, 0, 20, 42, 20, 74, 20, 0, 73, 56, 42, 74, 42, 20, 42, 56, 42, 20, 0, 42, 75]

optimal_run = [1, 5, 10, 11, 12, 33, 13, 34, 14, 35, 15, 36, 16, 37, 6, 7, 52, 53, 17, 71, 51, 18, 54, 72, 38, 39, 19,
               40, 73, 55, 41, 20, 42, 56, 74, 21, 75, 43, 3, 8, 62, 63, 22, 66, 23, 67, 24, 68, 25, 69, 26, 70, 4, 9,
               64, 65, 27, 57, 44, 28, 58, 45, 29, 59, 46, 30, 60, 31, 47, 32, 61, 50]

all_participants = {
    1: process_array(run1),
    2: process_array(run2),
    3: process_array(run3),
    4: process_array(run4),
    5: process_array(run5),
    6: process_array(run6),
    7: process_array(run7),
    8: process_array(run8),
    9: process_array(run9),
    11: process_array(run11),
    12: process_array(run12),
    13: process_array(run13),
    14: process_array(run14)
}

participants_group = {
    1: 'novice',
    2: 'expert',
    3: 'expert',
    4: 'novice',
    5: 'novice',
    6: 'novice',
    7: 'expert',
    8: 'expert',
    9: 'novice',
    11: 'expert',
    12: 'novice',
    13: 'expert',
    14: 'novice'
}

if __name__ == '__main__':
    for i in all_participants.keys():
        similarity = levenshtein.normalized_similarity(optimal_run, all_participants.get(i))
        print(f"Run {i}, Similarity: {similarity}, Group: {participants_group.get(i)}")
