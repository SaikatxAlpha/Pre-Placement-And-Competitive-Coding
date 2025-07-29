import collections
def CountFrequency(arr):
    return collections.Counter(arr)
if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1, 6, 2, 2, 3, 3, 4, 5, 5]
    freq = CountFrequency(arr)
    for (key, value) in freq.items():
        print (key, " -> ", value)

# Output :- 1  ->  5
# 6  ->  1
# 2  ->  2
# 3  ->  2
# 4  ->  1
# 5  ->  2