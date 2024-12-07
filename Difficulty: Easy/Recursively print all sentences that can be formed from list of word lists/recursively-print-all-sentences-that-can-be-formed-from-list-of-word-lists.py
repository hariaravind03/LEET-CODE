from typing import List


from typing import List

class Solution:
    def sentences(self, list: List[List[str]]) -> List[List[str]]:
        def helper(index, current):
            # Base case: if all lists have been processed, return the current sentence
            if index == len(list):
                return [current]
            
            # Recursive case: take the words from the current list and build sentences
            result = []
            for word in list[index]:
                result.extend(helper(index + 1, current + [word]))
            return result
        
        return helper(0, [])

#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class StringMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([str(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":

    a = IntArray().Input(2)

    list = StringMatrix().Input(a[0], a[1])

    obj = Solution()
    res = obj.sentences(list)

    StringMatrix().Print(res)

# } Driver Code Ends