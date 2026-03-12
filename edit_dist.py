# function to calculate edit distance
def editDistance(str1, str2, m, n):

    # if first string is empty → insert all characters of second
    if m == 0:
        return n

    # if second string is empty → remove all characters of first
    if n == 0:
        return m

    # if last characters are same → ignore them
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    # if characters are different → consider insert, remove, replace
    return 1 + min(
        editDistance(str1, str2, m, n-1),   # insert
        editDistance(str1, str2, m-1, n),   # remove
        editDistance(str1, str2, m-1, n-1)  # replace
    )


# main program
str1 = "nature"
str2 = "creature"

print("Edit Distance is:", editDistance(str1, str2, len(str1), len(str2)))