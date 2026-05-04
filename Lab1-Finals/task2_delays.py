from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    orders = [
        {"id": 1, "item": "Laptop"},
        {"id": 2, "item": "Mouse"},
        {"id": 3, "item": "Keyboard"},
        {"id": 4, "item": "Monitor"},
        {"id": 5, "item": "Headset"},
        {"id": 6, "item": "Webcam"},
    ]

    workers = size - 1
    for i, order in enumerate(orders):
        dest = (i % workers) + 1
        comm.send(order, dest=dest)

    for w in range(1, size):
        comm.send(None, dest=w)

else:
    while True:
        order = comm.recv(source=0)
        if order is None:
            break
        delay = random.uniform(0.5, 2.0)
        print(f"[Worker {rank}] Processing Order {order['id']}: {order['item']} (delay: {delay:.2f}s)")
        time.sleep(delay)
        print(f"[Worker {rank}] Done with Order {order['id']}: {order['item']}")