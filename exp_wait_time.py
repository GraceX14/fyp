from random import *


def get_first(pattern, list_len):
    randBinList = lambda n: [randint(0, 1) for b in range(1, n + 1)]
    BinList = randBinList(list_len)
    # print BinList
    BinStr = ''.join(str(e) for e in BinList)
    # print BinStr
    return BinStr.find(pattern)


def get_sum(sum_time, bin_list_len):
    one_zero_list = []
    one_one_list = []
    one_zero_sum = 0
    one_one_sum = 0

    for i in range(sum_time):
        one_zero = get_first('10', bin_list_len)
        one_zero_list.append(one_zero)
        one_zero_sum += one_zero

        one_one = get_first('11', bin_list_len)
        one_one_list.append(one_one)
        one_one_sum += one_one
    #print one_zero_list
    #print one_one_list
    return one_zero_sum, one_one_sum


def get_sum_list(sum_time=30, bin_list_len=30, sum_list_len=20):
    one_zero_sum = []
    one_one_sum = []
    for i in range(sum_list_len):
        result = get_sum(sum_time, bin_list_len)
        one_zero_sum.append(result[0])
        one_one_sum.append(result[1])
    return one_zero_sum, one_one_sum


if __name__ == "__main__":
    print get_sum_list()[0]
    print get_sum_list()[1]
