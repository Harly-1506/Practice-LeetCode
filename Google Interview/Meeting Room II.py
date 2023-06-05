"""Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required."""

# Solution: Priority Queues

"""We can't really process the given meetings in any random order. The most basic way of processing the meetings is in increasing order of their start times and this is the order we will follow. 
After all, it makes sense to allocate a room to the meeting that is scheduled for 9 a.m. in the morning before you worry about the 5 p.m. meeting, right?

Let's do a dry run of an example problem with sample meeting times and see what our algorithm should be able to do efficiently.

We will consider the following meeting times for our example (1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30). The first part of the tuple is the start time for the meeting and the second value 
represents the ending time. We are considering the meetings in a sorted order of their start times"""
"""
Algorithm

1. Sort the given meetings by their start time.
2. Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
5. If not, then we allocate a new room and add it to the heap.
6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings."""

import heapq 
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        example: (1,10), (2,7), (3,19), (8,12), (10,20), (11,30)
        The fisrt three meetings where each of them requires a new room because of collisions.
        Room 1 --> (1,10)
        Room 2 --> (2,7)
        Room 3 --> (3,19)

        The meeting room 2 is free by the time for meeting 4 is to start. 
        Room 1 --> (1,10)
        Room 2 --> (8,12) --> (2,7) was end
        Room 3 --> (3,19)
        """
        #if there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0
        
        #init the heap
        free_rooms = []

        #sort the meetings in increasing order of their start time.
        intervals.sort(key = lambda x:x[0])

        #Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        #For all the remaining meeting rooms
        for i in intervals[1:]:
            # if the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])
        

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)