class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        frst=nums1[0]
        flag=True
        for i in range(1,len(nums1)):
            if (nums1[i]%2!=frst%2):
                flag=False
                break

        if flag :return True

        mn=min(nums1)
        return mn%2==1
        