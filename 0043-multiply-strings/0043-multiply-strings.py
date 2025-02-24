class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def stringToInt(str):
            n = len(str)
            count = sum = 0
            for i in str[::-1]:
                sum+=int(i)*(10**count)
                count+=1
            return sum
        
        nums1 = stringToInt(num1)
        nums2 = stringToInt(num2)
        return str(nums1*nums2)