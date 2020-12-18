import numpy as np
import time
def quick_sort(data, low, high, drawData, speed):

    MOVING_LEFT = 0
    MOVING_RIGHT = 1

    if low < high:
        left = low
        right = high
        direction = MOVING_LEFT
        pivot = data[low]

        while left < right:
            if direction == MOVING_LEFT:
                while data[right] > pivot and left < high:
                    right -= 1
                data[left] = data[right]
                direction = MOVING_RIGHT
            
            if direction == MOVING_RIGHT:
                while data[left] <= pivot and left < high:
                    left += 1
                data[right] = data[left]
                direction = MOVING_LEFT
        
        data[right] = pivot
        drawData(data, ['green' if x == right or x == left else 'red' for x in range(len(data))])
        time.sleep(speed)

        quick_sort(data, low, left-1, drawData, speed)
        quick_sort(data, right+1, high, drawData, speed)

    drawData(data, ['green' for x in range(len(data))])

