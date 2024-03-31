#Amrit BKL
def subsets_bana_bc(nums): #[1,2,3]
    def tu_phir_aagaya(start, path):
        print("Index Value before for:",start)
        final.append(path)
        for i in range(start, len(nums)):
            print("Index Value after for:",i)
            tu_phir_aagaya(i + 1, path + [nums[i]])

    final = []
    tu_phir_aagaya(0, [])
    return final

Test_Case_ki_MKC = [2, 5, 8, 4]
print(subsets_bana_bc(Test_Case_ki_MKC))

