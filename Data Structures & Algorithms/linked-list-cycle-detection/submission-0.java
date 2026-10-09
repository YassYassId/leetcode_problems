/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

public class Solution {
    public boolean hasCycle(ListNode head) {
        HashMap<ListNode, Integer> nodes = new HashMap<>();
        int pos = 0;
        while(head != null && head.next != null){
            if(nodes.get(head) == null){
                nodes.put(head, pos);
                head = head.next;
                pos++;
            } else {
                return true;
            }
        }
        return false;
    }
}
