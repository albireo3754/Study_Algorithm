/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        using namespace std;
        int temp = 0;
        ListNode* emptyNode = new ListNode(0);
        ListNode* sumNode = headNode;
        while (true)
        {
            // 1. 항상 배열은 차있다.
            // 2. 그래서 조건문에서 nullptr을 가리키는경우 EmptyNode를 가리키도록 만듬
            temp = temp + l1->val + l2->val;
            int tempNow = temp >= 10 ? temp - 10 : temp;
            temp = temp / 10;

            sumNode->val = tempNow;

            if (l1->next == nullptr && l2->next == nullptr)
            {
                if (temp > 0)
                {
                    sumNode->next = new ListNode(temp);
                }
                return headNode;
            }
            else
            {
            sumNode->next = new ListNode();
            sumNode = sumNode->next;    
            }
            
            
            if (l1->next == nullptr) {
                l1 = emptyNode;
            }
            else
            {
                l1 = l1->next;
            }
            
            if (l2->next == nullptr)
            {
                l2 = emptyNode;
            }
            else
            {
                l2 = l2->next;
            }
        }
        return nullptr;
    }
private:
    ListNode* headNode = new ListNode();
};