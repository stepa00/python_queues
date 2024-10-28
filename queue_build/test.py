from queues import Queue

fifo = Queue()
fifo.enqueue('1st')
fifo.enqueue('2nd')
fifo.enqueue('3rd')
print(f'fifo = {fifo}')

fifo.dequeue()
print(f'fifo after 1st dequeue = {fifo}')

fifo.dequeue()
print(f'fifo after 2nd dequeue = {fifo}')

fifo.dequeue()
print(f'fifo after 3rd dequeue = {fifo}')

