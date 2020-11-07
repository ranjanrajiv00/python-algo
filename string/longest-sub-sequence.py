def longestSubseqWithK(str, k):
    n = len(str)

    freq = {}
    for i in range(n):
        if str[i] not in freq:
            freq[str[i]] = 1
        else:
            freq[str[i]] += 1

    for i in range(n):
        if (freq[str[i]] >= k):
            print(str[i], end="")
    print("")
str = "geekswaforgeekswas"
k = 2
longestSubseqWithK(str, k)
