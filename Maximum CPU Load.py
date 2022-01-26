#  Given an array of jobs with different time requirements, where each job consists of start time, end time and CPU load. The task is to find the maximum CPU load at any time if all jobs are running on the same machine.
# Examples:
#
# Input: jobs[] = {{1, 4, 3}, {2, 5, 4}, {7, 9, 6}}
# Output: 7
import heapq


def find_max_cpu_load(jobs):
    # Sort the jobs by start time
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0

    # Min-Heap
    min_heap = []

    # Loop to iterate over the list
    # of the jobs given for the CPU
    for j in jobs:

        # Remove all the jobs from
        # the min-heap which ended
        while (len(min_heap) > 0 and
               j.start >= min_heap[0].end):
            current_cpu_load -= min_heap[0].cpu_load
            heapq.heappop(min_heap)

        # Add the current job
        # into min_heap
        heapq.heappush(min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load,
                           current_cpu_load)
    return max_cpu_load