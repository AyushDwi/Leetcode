class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        
        events.sort(key=lambda e: (int(e[1]), e[0][2]))
        
        mentions = [0] * numberOfUsers
        onlineUntil = [0] * numberOfUsers
        lazyAll = 0
        
        for eventType, timestamp, data in events:
            ts = int(timestamp)
            
            if eventType[0] == 'O':
                userId = int(data)
                onlineUntil[userId] = ts + 60
                
            elif data[0] == 'A':
                lazyAll += 1
                
            elif data[0] == 'H':
                for userId in range(numberOfUsers):
                    if onlineUntil[userId] <= ts:
                        mentions[userId] += 1
                        
            else:
                userIds = data.split()
                for mention in userIds:
                    userId = int(mention[2:])
                    mentions[userId] += 1
        
        for userId in range(numberOfUsers):
            mentions[userId] = (mentions[userId] + lazyAll) % MOD
        
        return mentions
