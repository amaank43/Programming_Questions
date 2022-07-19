        ans = []
        nums.sort()
        i = 0
        j,k = i+1,len(nums)-1
        while i <= len(nums)-3 :
            if nums[i]+nums[j]+nums[k] > 0 :
                k-=1
            elif nums[i]+nums[j]+nums[k] < 0 : 
                j+=1
            else :
                ans.append([nums[i],nums[j],nums[k]])
                j+=1
                while nums[j-1]==nums[j] and j<k:
                    j+=1
            if j==k:
                i +=1
                while nums[i-1]==nums[i] and i <= len(nums)-3:
                    i+=1
                j,k = i+1,len(nums)-1
        return ans   
