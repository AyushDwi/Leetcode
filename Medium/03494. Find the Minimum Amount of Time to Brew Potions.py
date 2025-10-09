class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n = len(skill)
        m = len(mana)
        
        # Total processing time per potion
        sum_skill = sum(skill)
        
        # First potion: wizards work sequentially
        prev_wizard_done = sum_skill * mana[0]
        
        # Process each subsequent potion
        for j in range(1, m):
            prev_potion_done = prev_wizard_done
            
            # Work backwards to find optimal start time
            for i in range(n - 2, -1, -1):
                prev_potion_done -= skill[i + 1] * mana[j - 1]
                prev_wizard_done = max(
                    prev_potion_done,
                    prev_wizard_done - skill[i] * mana[j]
                )
            
            prev_wizard_done += sum_skill * mana[j]
        
        return prev_wizard_done
