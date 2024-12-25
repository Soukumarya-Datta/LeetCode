class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for i in s:
            if st and i.isdigit() and st[-1].isalpha():
                st.pop()
            else:
                st.append(i)
        return ''.join(st)
