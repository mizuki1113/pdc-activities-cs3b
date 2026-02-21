### Benchmarking Requirement
-- Execution time --
Sequential: 11.6384 seconds
Parallel: 3.9923 seconds

-- Speed up --
Speedup = 11.6384/3.9923
Speedup = 2.91

-- A short explanation of whether the result approaches ideal linear scaling --
The ideal speedup for this setup is 4x (3 barista threads + 1 order taker), but we achieved 2.91x, which does not fully reach ideal linear scaling. The gap is mainly due to thread overhead, lock contention on the shared order queue, and Python's Global Interpreter Lock (GIL) limiting true parallel execution. Despite this, a 2.91x speedup still demonstrates a significant performance improvement over the sequential model.
