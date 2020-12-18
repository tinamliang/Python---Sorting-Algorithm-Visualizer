import time

def bubble_sort(data, drawData, speed):
    isSwapped = False
    for i in range(len(data) - 1, 0, -1):
        if not isSwapped:
            isSwapped = True
            for j in range(0, i):
                if data[j] > data[j+1]:
                    isSwapped = False
                    temp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = temp
                    drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                    time.sleep(speed)
    drawData(data, ['green' for x in range(len(data))])

