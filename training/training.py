# kickstart training
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6


# Iterate over the list of students calculating the minimum number of 
# hours of coaching it would take to achieve the current skill level.
# The first calc of this takes p time, after that, constant time.
def getRes(p, s):
    # sort in ascending order
    s.sort()

    # calculate first window - sum first p elements
    window_sum = 0
    for i in range(p):
        window_sum += s[i]

    min_num_hours = -1
    for i in range(len(s)):
        # start testing using the window on the pth student
        if i >= p - 1:
            num_hours = (p * s[i]) - window_sum
            # exit early if found optimal
            if num_hours == 0:
                return 0
            # update min_num_hours
            if num_hours < min_num_hours or min_num_hours == -1:
                min_num_hours = num_hours

            # update window - constant time
            if (i < len(s) - 1):
                window_sum = window_sum - s[i - (p - 1)] + s[i + 1]

    return min_num_hours


# input and output
t = int(input())
for i in range(t):
    vals = input().split()
    p = int(vals[1])
    s_str = input().split()
    s = []
    for e in s_str:
        s.append(int(e))
    print("Case #" + str(i+1) + ": " + str(getRes(p, s)))
