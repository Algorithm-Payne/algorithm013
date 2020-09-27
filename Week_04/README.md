# 学习笔记

深度与广度优先

## 深度优先遍历（DFS： Depth First Search）

深度优先遍历：（刨根问底）一个方向到尽头，后回退一步。继续到尽头，然后回溯到根节点

从根节点(root)出发，沿着左子树方向进行纵向遍历，找到叶子节点为止。

然后回溯到前一个节点，进行右子树的遍历，找到叶子节点位置。

递归实现：(Python)

```python3
# 二叉树

visted = set()
def DFS(next.node, visited):
	if node in visted: # terminnator
        # already visted
        return 
    visted.add(node)
    # process current node here
    for next_node in node.children():
        if next_node not in visited:
            DFS(next.node, visited)
            
# 多叉树
visted = set()
def DFS(next.node, visited):
    visited.add(node)
    #  process current node here
    for next_node in node.children():
        if next_node not in visited:
            DFS(next.node, visited)
```

非递归实现（基于栈）：

```python3
def DFS(self, tree):
	if tree.root is None:
        return []
    visited, stack = [], [tree.root]
    
    while stack:
        node = stack.pop()
        process(node)
        stack.push(nodes)
        
    # other processing work
```



## 广度优先遍历（BFS： Breadth First Search）

广度优先遍历：（层层递进) 从根节点出发，在横向遍历二叉树层段节点的基础上纵向遍历二叉树的层次。

循环实现（基于队列）：

~~~python3
def BFS(graph, start):
    visited = set()
    queue = []
    queue.append([start])
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
        
     # other processing work
 
import collections
def BFS(graph, start):
    visited = set()
    queue = collections.deque([start])
    while queue:
        u = queue.popleft[]
        s
        process(node)
        nodes = generate_related_nodes(node)
        queue.append(nodes)
~~~



优先级优先:

中间优先：

## 贪心算法

贪心算法：是一种在每一步都选择中都采取当前状态下最好或最优的选择，从而**希望**导致结果是是全局最好或最优的算法。但往往在现实中与工程中却并不能得到”最优“，贪心算法多用于辅助。当一旦可以使用贪心法来解决，贪心法一般是**最优的算法**

贪心算法与动态规划：

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退

动态规划：保存以前的运行结果，并**保存**以前得到结果对当前进行选择，有回退功能。

> 贪心： 当下局部最优
>
> 回溯： 回退
>
> 动态规划： 最优判断 + 回退

## 二分查找（折半查找）：

前提：

目标函数单调性（递增或递减），可简单理解为”排序“完成的

存在上下界：（bounded）

能够通过索引访问（index accessible）

```python3
def binary_search(arry, values):
    left = 0
    right = len(arry) - 1
    # 候选区有值
    while left <= right:
        mid = (right + left) / 2
        if arry[mid] == values:
            break or return mid
        elif arry[mid] > values:
            right = mid - 1
        else:
            left = mid + 1
    return None
```

