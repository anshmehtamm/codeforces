/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int ans = 0;

    public int traverse(TreeNode root){
        if (root==null){
            return 0;
        }
        int left_h = traverse(root.left);
        int right_h = traverse(root.right);
        ans = Math.max(left_h+right_h,ans);
        return Math.max(left_h, right_h)+1;
    }


    public int diameterOfBinaryTree(TreeNode root) {
        
        traverse(root);
        return ans;
    }
}