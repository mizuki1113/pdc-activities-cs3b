import threading
import time
import random
import queue

NUM_CUSTOMERS       = 10
NUM_BARISTA_THREADS = 3
TAKE_ORDER_TIME     = 0.2
PREPARE_DRINK_TIME  = 0.8
SERVE_TIME          = 0.1

# SHARED STATE
order_queue  = queue.Queue()
serve_lock   = threading.Lock()
served_count = 0


def order_taker():
    """Takes orders and puts them into the shared queue."""
    for customer_id in range(1, NUM_CUSTOMERS + 1):
        print(f"  [Order Taker] Taking order for customer {customer_id:02d}...")
        time.sleep(TAKE_ORDER_TIME + random.uniform(0, 0.05))
        order_queue.put(customer_id)

    for _ in range(NUM_BARISTA_THREADS):
        order_queue.put(None)


def barista_worker(thread_id):
    """Pulls orders from the queue, prepares and serves drinks."""
    global served_count

    while True:
        customer_id = order_queue.get()  

        if customer_id is None:          
            order_queue.task_done()
            break

        print(f"  [Barista-{thread_id}] Preparing drink for customer {customer_id:02d}...")
        time.sleep(PREPARE_DRINK_TIME + random.uniform(0, 0.05))

        print(f"  [Barista-{thread_id}] Serving customer {customer_id:02d}...")
        time.sleep(SERVE_TIME + random.uniform(0, 0.05))

        with serve_lock:
            served_count += 1
            print(f"  > Customer {customer_id:02d} done. (Total served: {served_count})\n")

        order_queue.task_done()


def run_parallel():
    global served_count, order_queue
    served_count = 0
    order_queue  = queue.Queue()

    print("\n" + "=" * 45)
    print(f"  PARALLEL — 1 Order Taker + {NUM_BARISTA_THREADS} Baristas")
    print("=" * 45)

    start = time.perf_counter()
    taker = threading.Thread(target=order_taker, name="OrderTaker")

    baristas = [
        threading.Thread(target=barista_worker, args=(i + 1,), name=f"Barista-{i+1}")
        for i in range(NUM_BARISTA_THREADS)
    ]

    taker.start()
    for b in baristas:
        b.start()

    taker.join()
    for b in baristas:
        b.join()

    elapsed = time.perf_counter() - start
    print(f"  Total time: {elapsed:.4f} seconds")
    return elapsed


if __name__ == "__main__":
    run_parallel()