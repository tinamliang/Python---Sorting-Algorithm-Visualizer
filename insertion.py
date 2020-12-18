import time

def insertion_sort(data, drawData, speed):
    for i in range(1,len(data)):
        j = i
        while(j > 0 and data[j] < data[j-1]):
            temp = data[j]
            data[j] = data[j-1]
            data[j-1] = temp
            j-=1
            drawData(data, ['green' if x == j or x == j - 1 else 'red' for x in range(len(data))])
            time.sleep(speed)
    drawData(data, ['green' for x in range(len(data))])