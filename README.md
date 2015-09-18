topN
====

Scans huge files and takes the top N numbers.

Run `topN.py path/to/large_file -n123` to get the 123 top numbers in `large_file`.
Additional arguments to `topN.py` can be found by passing the `-h` argument to get help information.

### Complexity
The core of the algorithm is to push the numbers through a priority queue ([heapq](http://docs.python.org/2/library/heapq.html)) and pop off the smallest.
This ensures that the queue always contains the N highest in heap sorted order.

#### Time
If N is the number of numbers to track and M is the amount of numbers in the file:
The complexity of pushing into a priority queue is `log(M)` and sorting the list is `M*log(M)` (https://wiki.python.org/moin/TimeComplexity) however the number of pushes
we will have to make is N. Assuming that N is much larger than M, i.e. the top 1000 numbers in a 2GB file the complexity
becomes `~N*log(M) + M*log(M)` which if you consider the relative size of N is approximately `N*log(M)`.
The bottom line is that the overwhelming factor in the time this will take is the size of the file you're scanning.

#### Space
The code was carefully written to avoid keeping parts of the file around in memory. So the effect of the filesize (N) is
negligble. The primary factor then is M, the size of the numbers you are tracking. In the worst case scenario this is N,
in which case you will store the entire file in memory. Thankfully this isn't too realistic.


### Improvements
Since scanning through the file is the largest part of the time complexity it makes sense to optimise there. It may
be possibly to parallelise this process by splitting the file and maintaining multiple topN lists. This would require
an additional merge of the lists at the end, but if you could shave significant amount of time off scanning N you should
gain time overall.
