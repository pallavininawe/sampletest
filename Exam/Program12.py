import logging
import sys
logging.basicConfig(filename='logged.log',format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
class Solution(object):
logging.info('DFS: iterative implement.')
    def is_additive_number(self, num):
        length = len(num)
        for i in range(1, int(length/2+1)):
            for j in range(1, int((length-i)/2 + 1)):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return True
        return False

    def isValid(self, first, second, others):
        if ((len(first) > 1 and first[0] == "0") or
                (len(second) > 1 and second[0] == "0")):
            return False
        sum_str = str(int(first) + int(second))
        if sum_str == others:
            return True
        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])
        else:
            return False

if __name__ == "__main__":
    a=raw_input("enter a sequence like(66121830 or 235813) to check is it a additive sequence: ")
    print(Solution().is_additive_number(a))
 