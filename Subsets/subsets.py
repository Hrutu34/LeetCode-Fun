#Amrit BKL
def subsets(nums): 
    def backtrack(start, path):
        final.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    final = []
    backtrack(0, [])
    return final

num_1 = [2, 5, 8, 4]
print(subsets(num_1))

