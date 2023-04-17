描述
给定一棵二叉树(保证非空)以及这棵树上的两个节点对应的val值 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。

public int lowestCommonAncestor(TreeNode root, int o1, int o2) {
    //记录遍历到的每个节点的父节点。
    Map<Integer, Integer> parent = new HashMap<>();
    Queue<TreeNode> queue = new LinkedList<>();
    parent.put(root.val, Integer.MIN_VALUE);//根节点没有父节点，给他默认一个值
    queue.add(root);
    //直到两个节点都找到为止。
    while (!parent.containsKey(o1) || !parent.containsKey(o2)) {
        //队列是一边进一边出，这里poll方法是出队，
        TreeNode node = queue.poll();
        if (node.left != null) {
            //左子节点不为空，记录下他的父节点
            parent.put(node.left.val, node.val);
            //左子节点不为空，把它加入到队列中
            queue.add(node.left);
        }
        //右节点同上
        if (node.right != null) {
            parent.put(node.right.val, node.val);
            queue.add(node.right);
        }
    }
    Set<Integer> ancestors = new HashSet<>();
    //记录下o1和他的祖先节点，从o1节点开始一直到根节点。
    while (parent.containsKey(o1)) {
        ancestors.add(o1);
        o1 = parent.get(o1);
    }
    //查看o1和他的祖先节点是否包含o2节点，如果不包含再看是否包含o2的父节点……
    while (!ancestors.contains(o2))
        o2 = parent.get(o2);
    return o2;
}

from collections import deque
class Solution:
    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        # write code here
        m = {}
        q = deque()
        q.append(root)
        while not m.get(o1) or not m.get(o2):
            obj = q.pop()
            if obj.left:
                m[obj.left.val] = obj.val
                q.appendleft(obj.left)
            if obj.right:
                m[obj.right.val] = obj.val
                q.appendleft(obj.right)
        s = set()
        while m.get(o1):
            s.add(o1)
            o1 = m.get(o1)
        while o2 not in s:
            o2 = m.get(o2)
        return o2