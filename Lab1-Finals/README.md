# First Laboratory For Final Term—Reflection

## 1. How did you distribute orders among worker processes?
The master process (rank 0) created a list of orders and distributed them to workers.
Using round-robin distribution with MPI's 'comm.send()'. All orders were assigned 
to a worker, implement '(i% workers) + 1' so that the load is distributed evenly among available workers. 

## 2. What happens if there are more orders than workers?
Workers are provided with orders in a sequential manner. Since we utilised a loop with round-robin
assignment, no order is skipped—workers just take on more than one job each,
which is the expected behaviour in real distributed systems. 

## 3. How did processing delays affect the order completion?
Orders did not complete in the same order they were delivered. Since every worker had a
random sleep delay, quicker workers completed their orders first. Therefore the output order
was not deterministic. This reflects real-world async processing. 

## 4. How did you implement shared memory, and where was it initialized?
We utilised the 'Manager().list()' function from Python's'multiprocessing' package. It was initialised
prior to the MPI rank check, all processes could reference the same managed list.
Workers added their finished orders to the shared structure. 

## 5. What issues occurred when multiple workers wrote to shared memory simultaneously?
Without synchronisation, race conditions occurred, allowing many workers to attempt
append at the same period, resulting in incomplete writes or inconsistent list states.
Some entries appeared out of order or had been substantially erased. 

## 6. How did you ensure consistent results when using multiple processes?
We added 'Lock()' from'multiprocessing'. Each worker obtains the lock.
before writing to the shared list and releases it later, guaranteeing that only one process
writes at a time. This eliminated racing circumstances, resulting in a complete, consistent output. 

