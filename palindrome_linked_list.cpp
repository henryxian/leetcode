/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode *midNode = getMid(head);
        ListNode *rhead = reverseList(midNode);
        while (rhead) {
            if (head->val != rhead->val) {
                return false;
            }
            head = head->next;
            rhead = rhead->next;
        }
        return true;
    }
    
    ListNode* reverseList(ListNode* head) {
        ListNode node(0);
        ListNode* L = &node;
        ListNode* q;
        while (head) {
            q = head->next;
            head->next = L->next;
            L->next = head;
            head = q;
        }
        return L->next;
    }
    
    ListNode* getMid(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};