import heapq as hq

def connect_cables(heap: list):
    heap = heap[:]
    hq.heapify(heap)
    print('Heap: ', heap)
    total = 0
    connect_order = []

    while len(heap) > 1:
        first = hq.heappop(heap)
        second = hq.heappop(heap)
        current_sum = first + second
        total += current_sum
        hq.heappush(heap, current_sum)
        connect_order.append(f'{first} + {second} = {current_sum}, total = {total}, cables = {heap}')
    return total, connect_order

if __name__ == "__main__":
    cables = [4, 10, 1, 2, 8, 17, 3, 9, 5, 6]
    print('Cables: ', cables)
    connects = connect_cables(cables)
    print('Cost: ', connects[0])
    for _ in connects[1]: print(_)
