from mpi4py import MPI

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
        print(f"[Master] Sent Order {order['id']} ({order['item']}) to Worker {dest}")

    # Send stop signal
    for w in range(1, size):
        comm.send(None, dest=w)

else:
    while True:
        order = comm.recv(source=0)
        if order is None:
            break
        print(f"[Worker {rank}] Handling Order {order['id']}: {order['item']}")