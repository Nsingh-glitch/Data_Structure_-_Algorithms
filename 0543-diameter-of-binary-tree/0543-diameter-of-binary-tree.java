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
    int maxi = Integer.MIN_VALUE;

    private int fun(TreeNode root){
        if(root == null)return 0;
        int lH = fun(root.left);
        int rH = fun(root.right);
        maxi = Math.max(maxi ,lH+rH);
        return 1+Math.max(lH,rH);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        if(root == null) return 0;
        int t = fun(root);
        return maxi;
        
    }
}