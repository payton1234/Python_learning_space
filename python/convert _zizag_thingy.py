def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = [""]*numRows
        j = 0
        #1 = down / 0 = up
        direction = 1
        row = 0
        while j < len(s):
            ans[row] += append(s[j])
            if direction == 1:
                row += 1
                if row == numRows-1:
                    direction = 0
            else:
                row -=1
                if row == 0:
                    direction = 1
            j += 1
        ans = "".join(ans)
        return ans 
    
if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 4))