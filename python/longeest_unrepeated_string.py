#usr/bin/env/py3

def function(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    i1 = 0
    i2 = 0
    count = 0
    q = []
    while (count != int((m+n)/2)+1):
        if i1 < m and i2 < n:
            temp = min(nums1[i1], nums2[i2])
            if temp == nums1[i1]:
                if len(q) == 2:
                    q.pop(0)
                q.append(nums1[i1])
                i1 += 1
            else:
                if len(q) == 2:
                    q.pop(0)
                q.append(nums2[i2])
                i2 += 1
        elif i1 < m:
            if len(q) == 2:
                q.pop(0)
            q.append(nums1[i1])
            i1 += 1
        else:
            if len(q) == 2:
                q.pop(0)
            q.append(nums2[i2])
            i2 += 1
        count += 1
    if (m+n)%2 == 0:
        return float((q[0] + q[1])/2)
    else:
        return q[1]
    
                
            
    
if __name__== "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(function(nums1, nums2))
    print(nums1[-2])
