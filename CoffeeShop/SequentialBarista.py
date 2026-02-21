import time
import random

NUM_CUSTOMERS      = 10
TAKE_ORDER_TIME    = 0.2
PREPARE_DRINK_TIME = 0.8
SERVE_TIME         = 0.1


def take_order(customer_id):
    print(f"  [Customer {customer_id:02d}] Taking order...")
    time.sleep(TAKE_ORDER_TIME + random.uniform(0, 0.05))


def prepare_drink(customer_id):
    print(f"  [Customer {customer_id:02d}] Preparing drink...")
    time.sleep(PREPARE_DRINK_TIME + random.uniform(0, 0.05))


def serve_customer(customer_id):
    print(f"  [Customer {customer_id:02d}] Serving customer...")
    time.sleep(SERVE_TIME + random.uniform(0, 0.05))


def run_sequential():
    print("\n" + "=" * 45)
    print("  SEQUENTIAL — Single Barista")
    print("=" * 45)

    start = time.perf_counter()

    for customer_id in range(1, NUM_CUSTOMERS + 1):
        take_order(customer_id)
        prepare_drink(customer_id)
        serve_customer(customer_id)
        print(f"  > Customer {customer_id:02d} done.\n")

    elapsed = time.perf_counter() - start
    print(f"  Total time: {elapsed:.4f} seconds")
    return elapsed


if __name__ == "__main__":
    run_sequential()