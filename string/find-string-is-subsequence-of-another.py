def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)

    i, j = 0, 0

    while i < m and j < n:
        if str1[i] == str2[j]:
            i = i+1
        j = j+1

    return i == m


print(isSubSequence("geks", "geeksofgeeks"))