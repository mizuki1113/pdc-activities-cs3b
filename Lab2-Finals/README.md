# Distributed Voting System — CS323 Lab 2

## System Overview

A distributed voting system built on GCP using an edge-to-cloud pipeline:

**Edge Nodes → Cloud Run API → Pub/Sub → Worker Service → Firestore**

## Architecture

Edge nodes generate votes independently and send them via HTTP to the Cloud Run API. The API validates and publishes votes to a Pub/Sub topic. A worker service subscribes and processes messages, writing results to Firestore using idempotent document IDs.

---

## Individual Reflections

### Keissha

Running the edge node was honestly pretty straightforward at first. I just ran `edge_node.py` and watched it fire off votes one after another. What stood out to me was how different it felt compared to running things sequentially. The script didn't wait for the whole pipeline to finish before sending the next vote, it just kept going. At low volumes everything looked fine, responses came back quickly and I didn't notice any issues. But when I pushed more votes through, the API response times started getting a little slower. The edge node itself wasn't the bottleneck though, it kept sending just fine. The lag was somewhere further down the pipeline, probably Pub/Sub filling up faster than the worker could keep up. The tricky part was that from the edge node's side, everything still looked like it was working. Once the API said 200, that was it. I had no way of knowing if the vote actually made it to Firestore without checking the console manually, which felt a bit uncomfortable at first but also made me realize that's just how distributed systems work.

---

### Josh

My part involved running the edge node and also intentionally breaking things to see how the system handled it. The most interesting test was cutting the API off while the edge node was mid-run. The result was pretty blunt, votes just failed with connection errors and were lost since there was no retry logic. That was a clear gap. I also tested pausing the Pub/Sub subscription, and that actually went better than expected. Messages piled up in the queue and once I re-enabled the subscription, the worker started catching up on its own. Watching the backlog drain in the GCP console was kind of satisfying. The idempotent document IDs really saved us there because the worker was reprocessing some messages and without that design, vote counts would have been wrong. The hardest part was figuring out when the system had actually "settled." After a fault you can't just immediately check Firestore and trust what you see. You have to wait, and that kind of uncertainty is something I didn't really think about before this lab.

---

### Vince

Building the API and worker was where most of the complexity lived. The API part was fairly simple, validate the payload, publish to Pub/Sub, return a response. The worker was trickier because it had to keep polling for messages, process them, write to Firestore, and acknowledge them all in a loop. One thing I had to be careful about was using the vote's unique ID as the Firestore document ID. Without that, any message that got redelivered by Pub/Sub would create a duplicate entry and mess up the counts. Under heavier load, the worker was clearly the slowest part of the whole pipeline. The API and edge nodes could produce messages way faster than the worker could write them to Firestore, so the queue kept growing. Scaling the worker would fix that but with a single Cloud Run instance, it was a visible bottleneck. It was a good real-world example of how one slow component can back up the whole system even if everything else is running fine.

---

### Precious

My role was setting up all the GCP infrastructure and keeping an eye on things through the console. It seemed like the easier job at first but there were more moving parts than I expected. Getting the region right mattered more than I thought. We kept everything in `asia-southeast1` and that kept latency between services low. Early on I ran into some errors when trying to deploy Cloud Run before the APIs were properly enabled, which took a bit of time to track down since the error messages weren't super clear. Once everything was running, the GCP monitoring tools were actually really useful. The Pub/Sub metrics showed the message backlog building up during high-load tests, and Cloud Run showed per-request latency clearly. Firestore let me verify that the idempotent writes were working by checking that document counts matched what we expected even after re-runs. The one thing that was still annoying was correlating events across all three services since you had to manually match timestamps. For a lab-scale project it was manageable, but I can see how that would become a real problem in a larger system.