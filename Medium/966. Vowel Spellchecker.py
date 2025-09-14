class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        # Store exact matches
        exact_set = set(wordlist)
        
        # Store case-insensitive matches (lowercase -> first original word)
        case_map = {}
        
        # Store vowel pattern matches (pattern -> first original word)
        vowel_map = {}
        
       
        def create_pattern(word):
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())
        
        
        for word in wordlist:
            lowercase = word.lower()
            pattern = create_pattern(word)
            
            
            if lowercase not in case_map:
                case_map[lowercase] = word
            
            
            if pattern not in vowel_map:
                vowel_map[pattern] = word
        
        result = []
        
        
        for query in queries:
            
            if query in exact_set:
                result.append(query)
                continue
            
            
            query_lower = query.lower()
            if query_lower in case_map:
                result.append(case_map[query_lower])
                continue
            
            
            query_pattern = create_pattern(query)
            if query_pattern in vowel_map:
                result.append(vowel_map[query_pattern])
                continue
            
            
            result.append("")
        
        return result
      
