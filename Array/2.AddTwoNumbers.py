
##############################
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example:

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
#################################

# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        temp = l1.val + l2.val + carry
        carry = int(temp / 10)
        result = ListNode(temp % 10)
        if l1.next != None or l2.next != None or carry != 0:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            result.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return result


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()