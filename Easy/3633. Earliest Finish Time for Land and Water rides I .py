class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        minFinishTime=float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_start=landStartTime[i]
                land_end=land_start+landDuration[i]
                water_start=max(land_end,waterStartTime[j])
                water_end=water_start+waterDuration[j]
                finish_time1=water_end

                water_start=waterStartTime[j]
                water_end=water_start+waterDuration[j]
                land_start=max(water_end,landStartTime[i])
                land_end=land_start+landDuration[i]
                finish_time2=land_end

                minFinishTime=min(minFinishTime,finish_time1,finish_time2)
        return minFinishTime        

                
        
