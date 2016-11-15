'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Assume in reserve order the input (2 -> 4 -> 3) represent 342
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.listToNumber(l1)
        num2 = self.listToNumber(l2)
        num3 = num1 + num2
        return self.numberToList(num3)
        
    def numberToList(self, num):
        '''
        :type num: int, non-negative
        :rtype: ListNode
        '''
        if num == 0:
            return ListNode(0)
        reverseList = []
        while True:
            print(num % 10)
            reverseList.append(num % 10)
            num = num // 10
            if num == 0:
                break
        #print(reverseList)
        reverseList.reverse()
        orderList = reverseList        
        #print(orderList)
        #print(orderList)
        l1 = ListNode(orderList[0])
        head = l1
        for i in range(1,len(orderList)):
            l1.next = ListNode(orderList[i])
            l1 = l1.next
        l1 = head
        return l1
        
    def listToNumber(self,l1):
        '''
        :type l1: ListNode
        :rtype: int, non-negative
        '''
        num = 0
        digit = 1
        while l1.val != None:
            #print(l1.val)
            num += 10 ** (digit - 1) * l1.val
            if l1.next != None:
                l1 = l1.next
                digit += 1
            else:
                break
        return num
            
# testing
def main():
    orderList = [2,4,3]
    l1 = ListNode(orderList[0])
    head = l1
    for i in range(1,len(orderList)):
            l1.next = ListNode(orderList[i])
            l1 = l1.next
    l1 = head
    
    answerList = [4, 8, 6]
    l2 = ListNode(answerList[0])
    for i in range(1,len(answerList)):
            l2.next = ListNode(answerList[i])
    
    a = Solution()
    answer = a.listToNumber(l1)
    answer = a.numberToList(342)
    expected = 342
    answer = a.addTwoNumbers(l1,l1)
    print(answer.val, expected)
    #print(l2.val)
        
if __name__ == "__main__":
    main()
    
'''
 The unit test is very important. It helps me to find small bugs in localized style.
'''