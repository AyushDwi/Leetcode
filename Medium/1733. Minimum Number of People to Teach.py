class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        
    
        cannot_communicate = set()
        
        
        for u, v in friendships:
            
            user1 = u - 1
            user2 = v - 1
            
           
            lang1_set = set(languages[user1])
            lang2_set = set(languages[user2])
            
            
            if not lang1_set.intersection(lang2_set):
                cannot_communicate.add(u) 
                cannot_communicate.add(v)
        
        
        if not cannot_communicate:
            return 0
        
        
        language_count = {}
        for user in cannot_communicate:
            user_idx = user - 1  # Convert to 0-indexed
            for lang in languages[user_idx]:
                language_count[lang] = language_count.get(lang, 0) + 1
        
       
        max_frequency = max(language_count.values()) if language_count else 0
        
        
        return len(cannot_communicate) - max_frequency
