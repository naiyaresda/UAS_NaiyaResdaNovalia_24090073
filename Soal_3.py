queue = []

def enqueue(value):
    queue.append(value)
    print(f'{value} ditambahkan kedalam antrian')
    print('='*20)

def dequeue():
    del queue[0]

def front():
    # print(f'data elemen pertama : {queue[0]}')
    if len (queue) == 0 :
        return'Data pertama kosong!'
    else:
        return queue[0]

def isEmpty():
    return len(queue) == 0