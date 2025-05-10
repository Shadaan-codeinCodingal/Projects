def subarrsum(a,s,sum_):
    for i in range(s):
        curr_sum = a[i]
        j = i +1
        while j <= s:
            if curr_sum ==sum_:
                print('Sub-array  sum matched from index',i,'to',j-1)
                return 1
            if j == s or curr_sum>sum_:
                break
            curr_sum += a[j]
            j+=1
    print('No subarray sum found')
    return 0
a = [3,2,4,8,9,5,10,23]
sum_ = 23
subarrsum(a,len(a),sum_)