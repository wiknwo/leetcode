'''Bus Routes

    William Ikenna-Nwosu (wiknwo)

    You are given an array routes representing bus routes 
    where routes[i] is a bus route that the ith bus repeats 
    forever.

    - For example, if routes[0] = [1, 5, 7], this means that 
    the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 
    5 -> 7 -> 1 -> ... forever.

    You will start at the bus stop source (You are not on 
    any bus initially), and you want to go to the bus stop 
    target. You can travel between bus stops by buses only.

    Return the least number of buses you must take to 
    travel from source to target. Return -1 if it is not 
    possible.
'''
import collections
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_route_dict = collections.defaultdict(set) # Dictionary mapping stops to all the bus routes they are on.
        stops_to_visit_queue = [] # Queue to represent stops to be processed (1st value is stop number, 2nd value is number of bus routes been on up to this point).
        visited_stops_set = set() # Set to keep track of stops we have already been to so we don't revisit them.
        
        # Fill in stop_to_route_dict
        for bus_index, route in enumerate(routes):
            for bus_stop in route:
                stop_to_route_dict[bus_stop].add(bus_index)
        
        # Setup the initial variables for BFS
        stops_to_visit_queue.append((source, 0)) # The source is the first stop we will visit and at this point we have entered 0 buses
        visited_stops_set.add(source) # We have now visited the source bus stop so we will not revisit it
        
        # Process the bus stops until there are no more buses to process or journey is impossible
        while stops_to_visit_queue:
            current_bus_stop = stops_to_visit_queue[0][0] # Getting stop number
            number_of_buses_been_on = stops_to_visit_queue[0][1] # Getting number of buses been on up to that point
            
            if current_bus_stop == target:
                return number_of_buses_been_on
            stops_to_visit_queue.pop(0) # Remove the pairing of bus stop and buses been on as it has been processed
            
            # For each route that this stop can get to
            for bus_index in stop_to_route_dict[current_bus_stop]:
                # For each of the stops on that route
                for next_bus_stop in routes[bus_index]:
                    # If stop has not been visited add it to visited stops and to stops to visit queue
                    if next_bus_stop not in visited_stops_set:
                        visited_stops_set.add(next_bus_stop)
                        stops_to_visit_queue.append((next_bus_stop, number_of_buses_been_on + 1))
                routes[bus_index].clear() # Clear current route that has just been processed
        return -1 # Journey is impossible
                
            