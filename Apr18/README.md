# Reflection for Sequential vs Parallel Algorithms Group Activity
## Gamalo, Precious B
REFLECTION:
For my part, I worked on the parallel search implementation. Honestly, it was a bit confusing at first especially the part where we had to use a Queue to collect results from each process since they can't just return values normally like regular functions. But once I got the hang of it, it made sense why it's needed.

I also structured my code using classes which I thought made everything more organized and easier to follow. Testing it on small, medium, and large datasets was interesting because you could actually see the difference in execution time as the data got bigger, which made the whole point of using multiprocessing click for me.
## Canios, Keissha Louise
Reflection:
The activity showed me the practical differences between parallel algorithm execution and sequential algorithm execution which I had previously only understood on a theoretical level. The surface level understanding I had about the concept became deeper when I developed both methods through programming because I needed to study their underlying operations.

I discovered that executing tasks in parallel does not guarantee improved performance. Our tests showed that sequential methods outperformed their parallel counterparts when we used a 1,000 element test dataset. The time required for process creation and data splitting and data integration exceeded the time needed for computation. The situation appeared strange to me until I realized that light work becomes obstructed by excessive coordination.

The larger datasets made the differences between two methods easier to observe. Parallel sorting and searching began to demonstrate actual performance improvements at 100,000 elements and particularly at 1,000,000 elements. The execution times started to show different patterns as I increased the dataset size which enabled me to understand the concept better than I could through reading.

The top obstacle I faced involved achieving correct global index results through parallel search methods. The index found by each process represents only the data contained in its specific section. I needed to calculate the exact beginning point of each segment to convert their locations back to original list positions. The logical framework required multiple attempts to establish correctly because the system showed accurate results which turned out to be incorrect.

Synchronization was another thing I underestimated. Even with multiprocessing and queues, you have to be deliberate about how results are collected and in what order. If the target isn't found, every process needs to handle that gracefully and communicate it properly rather than just returning nothing and leaving the main process hanging.

Overall, what I took away from this is that parallelism is a tool, not a default upgrade. It shines when the workload is large enough to justify the coordination cost, and it struggles when the problem is small or when the subproblems aren't truly independent. Knowing when to use it is just as important as knowing how.

## Carabanes, Vince Christian P.


## de Ramas, Josh Andrie

