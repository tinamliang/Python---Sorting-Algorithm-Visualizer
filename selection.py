import time
def selection_sort(data, drawData, speed):
    for i in range(len(data)-1, 0, -1):
        max_num = 0
        for j in range(1, i+1):
            if data[j] > data[max_num]:
                max_num = j
        temp = data[i]
        data[i] = data[max_num]
        data[max_num] = temp
        drawData(data, ['green' if x == max_num or x == i else 'red' for x in range(len(data))])
        time.sleep(speed)
    drawData(data, ['green' for x in range(len(data))])