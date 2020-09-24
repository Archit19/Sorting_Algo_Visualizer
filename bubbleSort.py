import time


def bubble_sort(data, drawData, timeTick):

    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['bisque' if x == j or x == j+1 else 'RoyalBlue1' for x in range(len(data))])
                time.sleep(timeTick)
    
    drawData(data, ['OliveDrab1' for x in range(len(data))])
    

