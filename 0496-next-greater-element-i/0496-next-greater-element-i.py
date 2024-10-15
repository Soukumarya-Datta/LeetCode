class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng = {}
        st = []
        
        for num in reversed(nums2):
            while st and st[-1] <= num:
                st.pop()
            
            #st[-1] gets the top element of the stack, if empty assign -1
            ng[num] = st[-1] if st else -1 
            st.append(num)
        
        return [ng[num] for num in nums1]