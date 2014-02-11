import heapq

__author__ = 'barryhennessy'


class TopN(object):
    """Keeps track of the top N integers pushed into TopN"""

    def __init__(self, max_to_track):
        """Initialises TopN to keep track of the top max_to_track integers"""
        if max_to_track <= 0:
            raise ValueError(
                "The number of items to track must be greater than 0"
            )

        self._max_size = int(max_to_track)
        self._heap = []

    def push(self, new_int):
        """Pushes the new_int into the top n items if it belongs there

        :param new_int: the integer to be pushed into one of the top n
                        positions
        """
        if not isinstance(new_int, int):
            raise ValueError("Non integer value pushed into TopN integers")

        if len(self._heap) == self._max_size:
            # If our heap is full push the new value in and pop the smallest
            # value off. The value popped off may be the value entered if it
            # doesn't belong.
            heapq.heappushpop(self._heap, new_int)
        else:
            # If our heap isn't full we push the new value in and it gets put
            # in place by the heap queue
            heapq.heappush(self._heap, new_int)

    def get_top_n(self):
        """Returns the top n items in sorted order, highest first

        :return: A list of integers in sorted order, highest first
        """

        # Copying by value to ensure the instance _heap doesn't get sorted and
        # break it's heap sorted invariant
        sorted_heap = self._heap[:]

        sorted_heap.sort(reverse=True)

        return sorted_heap
