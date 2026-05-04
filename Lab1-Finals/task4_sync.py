from mpi4py import MPI
from multiprocessing import Manager, Lock
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

manager = Manager()
shared_orders = manager.list()
lock = Lock()

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

    comm.Barrier()
    print("\n[Master] Final consistent list of completed orders:")
    for o in shared_orders:
        print(f"  - Order {o['id']}: {o['item']} (handled by Worker {o['worker']})")

else:
    while True:
        order = comm.recv(source=0)
        if order is None:
            break
        delay = random.uniform(0.5, 1.5)
        time.sleep(delay)
        order["worker"] = rank
        with lock:
            shared_orders.append(order)
            print(f"[Worker {rank}] Safely wrote Order {order['id']} to shared memory")

    comm.Barrier()