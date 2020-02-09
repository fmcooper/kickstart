# kickstart training
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6


# build a frequency prefix sum for each A-Z character in the sequence
def setup(s):
    ps = []
    for i in range(26):
        char = chr(ord('A') + i)
        ps_char = []
        count = 0
        for j in range(len(s)):
            if s[j] == char:
                count += 1
            ps_char.append(count)
        ps.append(ps_char)
    return ps


# returns if there exists a palindrome in the given character range
def getRes(l, r, ps):
    letter_counts = []

    # we count the number of odd characters existing in the range
    num_odd = 0
    for c in range(26):
        num_containing = 0
        # we need to minus the freq at the l-1th index from the freq
        # at the rth index
        if l == 0:
            num_containing = ps[c][r]
        else:
            num_containing = ps[c][r] - ps[c][l - 1]

        if num_containing % 2 == 1:
            num_odd += 1
            # exit early - can never have a palindrome in this case
            if num_odd > 1:
                return 0

    # determine whether we have a palindrome
    if (r - l + 1) % 2 == 0 and num_odd == 0:
        return 1
    elif (r - l + 1) % 2 == 1 and num_odd == 1:
        return 1
    return 0


# input and output
t = int(input())
for i in range(t):
    vals = input().split()
    q = int(vals[1])
    s = list(input())
    ps = setup(s)

    count = 0
    for e in range(q):
        qn = input().split()
        # turn the l and r into indices
        count += getRes(int(qn[0]) - 1, int(qn[1]) - 1, ps)
    print("Case #" + str(i+1) + ": " + str(count))
