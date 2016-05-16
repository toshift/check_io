def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    val = 0
    if not len(array) == 0:
        for i,cn in enumerate(array):
            if (i%2) == 0:
                val += array[i]
        val*=array[len(array)-1]
    return val

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"


# スライス表記(:: 0から2つ置きに取得)
# -1 arrayの最大値

#     if len(array) == 0: return 0
#     return sum(array[0::2]) * array[-1]
