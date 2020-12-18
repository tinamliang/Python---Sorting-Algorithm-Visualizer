from math import floor
import time

def shell_sort(data, drawData, speed):
    n = len(data)
    gap = floor(n / 2)

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
            drawData(data, ['green' if x == j or x == j - gap else 'red' for x in range(len(data))])
            time.sleep(speed)
        gap = floor(gap / 2)
    drawData(data, ['green' for x in range(len(data))])
