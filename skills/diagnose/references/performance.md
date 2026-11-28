# Measure a performance problem

Compare the same correct workload under the same conditions before and after. A faster wrong result is a failure.

1. Name the operation, its input size and the environment. Record absolute numbers, not only a percentage.
2. Run each measurement more than once and report the spread. A single run cannot separate a change from noise.
3. Find what limits the number: CPU, I/O, network, locks, a queue, or the measuring tool itself. Rule out that the faster run skipped work, hit a cache the slower run did not, or failed silently.
4. Confirm the change matters end to end. Halving a step that takes 2% of the request barely moves the user's wait.
5. Use the project's profiler or tracing when available. Keep the profile or trace with the report.
