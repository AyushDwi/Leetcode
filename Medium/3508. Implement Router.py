from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit):
        """
        Initialize Router with memory limit (maximum number of packets)
        """
        self.memoryLimit = memoryLimit
        self.packets = deque()  # FIFO queue for packet order
        self.uniquePackets = set()  # For duplicate detection
        self.destinationTimestamps = defaultdict(list)  # For efficient getCount
        
    def addPacket(self, source, destination, timestamp):
        """
        Add packet to router. Return False if duplicate, True if added successfully.
        Remove oldest packet if memory limit exceeded.
        """
        packet = (source, destination, timestamp)
        
        # Check for duplicate
        if packet in self.uniquePackets:
            return False
        
        # Remove oldest packet if memory limit reached
        if len(self.packets) == self.memoryLimit:
            self.forwardPacket()
        
        # Add new packet
        self.packets.append(packet)
        self.uniquePackets.add(packet)
        self.destinationTimestamps[destination].append(timestamp)
        
        return True
    
    def forwardPacket(self):
        """
        Forward (remove) oldest packet in FIFO order.
        Return packet as [source, destination, timestamp] or empty list if no packets.
        """
        if not self.packets:
            return []
        
        # Remove oldest packet
        source, destination, timestamp = self.packets.popleft()
        self.uniquePackets.remove((source, destination, timestamp))
        
        # Remove from destination timestamps (remove first occurrence)
        timestamps = self.destinationTimestamps[destination]
        timestamps.remove(timestamp)
        if not timestamps:
            del self.destinationTimestamps[destination]
        
        return [source, destination, timestamp]
    
    def getCount(self, destination, startTime, endTime):
        """
        Count packets with specified destination and timestamp in [startTime, endTime]
        """
        if destination not in self.destinationTimestamps:
            return 0
        
        timestamps = self.destinationTimestamps[destination]
        
        # Use binary search for efficient range counting
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        
        return right - left
      
