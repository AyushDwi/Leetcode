import heapq

class TaskManager:
    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        # Max heap for (priority, taskId) pairs
        self.heap = []
        # Map taskId -> (userId, priority)
        self.task_info = {}
        
        # Initialize with given tasks
        for userId, taskId, priority in tasks:
            # Store negative priority for max heap behavior
            heapq.heappush(self.heap, (-priority, -taskId))
            self.task_info[taskId] = (userId, priority)
    
    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        # Add to heap with negative values for max heap
        heapq.heappush(self.heap, (-priority, -taskId))
        self.task_info[taskId] = (userId, priority)
    
    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        # Update task info
        userId, _ = self.task_info[taskId]
        self.task_info[taskId] = (userId, newPriority)
        
        # Add new entry to heap (old entry becomes stale)
        heapq.heappush(self.heap, (-newPriority, -taskId))
    
    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        # Remove from task info (heap entries become stale)
        del self.task_info[taskId]
    
    def execTop(self):
        """
        :rtype: int
        """
        # Find the valid task with highest priority
        while self.heap:
            neg_priority, neg_taskId = heapq.heappop(self.heap)
            priority = -neg_priority
            taskId = -neg_taskId
            
            # Check if this is a valid, current task
            if taskId in self.task_info:
                userId, current_priority = self.task_info[taskId]
                
                # Check if this heap entry matches current priority
                if current_priority == priority:
                    # Execute this task
                    del self.task_info[taskId]
                    return userId
            # If not valid, continue to next heap entry
        
        # No tasks available
        return -1
              
