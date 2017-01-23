#!/user/bin/env python
# _*_coding:utf-8_*_
# @Time   :2017/1/23 14:05
# @Author :Kira
# @Software：PyCharm


def insert_sort(array, **kwargs):

    if not kwargs:

        length = len(array)

        for i in range(1, length):
            j = i - 1
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                j -= 1
                while j >= 0 and array[j] > temp:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = temp
    try:
        if kwargs['reverse']:

            length = len(array)

            for i in range(1, length):
                j = i - 1
                if array[i] > array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    j -= 1
                    while j >= 0 and array[j] < temp:
                        array[j + 1] = array[j]
                        j -= 1
                    array[j + 1] = temp
    except:
        pass
    return array

if __name__ == "__main__":
    _list = [49, 38, 65, 97, 76, 13, 27, 49]
    print(insert_sort(_list))
