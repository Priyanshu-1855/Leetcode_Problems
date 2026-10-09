class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # lmax = [0]*n
        # rmax = [0]*n

        # lmax[0] = height[0]
        # for i in range(1,n):
        #     lmax[i] = max(lmax[i-1],height[i])

        # rmax[n-1] = height[n-1]
        # for i in range(n-2 ,-1 ,-1):
        #     rmax[i] = max(rmax[i+1],height[i])

        # trapped = 0
        # for i in range(n):
        #     trapped += (min(lmax[i],rmax[i]) - height[i])

        # return trapped


        # -------------------------------------------------

        trapped = 0
        left , right = 0 , n-1
        lmax , rmax = 0 , 0

        while left < right:
            lmax = max(lmax , height[left])
            rmax = max(rmax , height[right])

            if lmax < rmax:
                trapped += lmax - height[left]
                left += 1
            else:
                trapped += rmax - height[right]
                right -= 1



        return trapped










