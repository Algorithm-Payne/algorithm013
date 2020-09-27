# 学习笔记
## Trie
### 基本定义：

字典树，又称前缀树(Prefix Tree)、单词查找树、键树。
工程中多为有序树、多叉树结构，其键值多为**字符串**。
主要用于保存关连数组，**键并不直接保存在节点中，而是由节点所在树中的位置决定。**

一个节点的所有子孙都有相同的前缀，也就是这个节点对应的字符串，而根节点对应空字符串。一般情况下，不是所有的节点都有对应的值，只有叶子节点和部分内部节点所对应的键才有相关的值。

优点：最大限度的减少无效的字符串比较，查询效率比Hash表高

经典应用：统计、排序大量字符串。搜索引擎文本词频统计等

### 基本性质：

- 节点本身不存完整单词
- 从根节点到某一结点，路径上经过的字符连起来，为该节点对应的字符串
- 每个节点所有的子节点路径代表的字符都不相同

### 核心思想：

Trie树的核心思想是空间换时间

利用字符串的公共前缀来降低查询的时间开销，以达到提高效率的目的

### Trie树实现:

~~~python3
class Trie:
    def __init__(self):
        self.root = {} # 使用字典，而不是数组！key 可能为a，b,c...
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
            return self.end_of_word in node

    def startsWith(self, prefix):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
            return True      
~~~



## 并查集

### 基本操做

makeSet(s):建立一个新的并查集，其中包含s个单元素集合

unionSet(x,y):把元素x和元素y所在的集合合并，要求x和y所在的集合不相交。如果相交则不合并

find(x): 找到元素x所在的集合代表，该操作也可以用于判断两个元素是否位于同一个集合，只需将各自的代表比较即可

基本实现：

```python3
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```

## 高级搜索

### 朴素搜索

优化方式：去重、减枝

### 搜索方向

DFS：depth first search 深度优先搜索

~~~python3
# DFS 递归
visited = set() 

def DFS(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
 # 非递归：模拟栈

def DFS(self, tree): 
	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

		# other processing work 
~~~

BFS：Breadth first search 广度优先搜索

~~~Python3
def BFS(graph, start, end):
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
	...
~~~

双向搜索、启发式搜索

### 双向BFS

```python3
def dBFS(graph, start, end):
    visited = set()
    front = []
    back = []
    front.append(start)
    back.append(end)
    while front and back:
        nodes = set()
        for node in front:
            visited.add(node) #加入访问
            process(node) # 处理当前node
            nodes.append(generate_related_nodes(node)) #获取子节点
        front = nodes
        if len(back) < len(front):	        # 从较小的set开始
            front, back = back, front
    ...
        
```

## 启发式搜索

启发式搜索（Heuristic Search, A*）,Heuristic指的是根据某一些条件，我们不断的优化搜索方向，本质上用的就是利用优先级进行查找。核心是在定义在估价函数, h(n)。

```python3
def AstarSearch(graph, start, end):

    pq = collections.priority_queue() # 优先级 —> 估价函数
    pq.append([start]) 
    visited.add(start)

    while pq: 
        node = pq.pop() # can we add more intelligence here ?
        visited.add(node)

        process(node) 
        nodes = generate_related_nodes(node) 
         unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
```





## 红黑树和AVL树

- 思考树的结构和二叉树的结构
- 树的遍历，前中序遍历，DFS，BFS
- 二叉搜索树(BST),  查找，插入，删除

起因：二叉搜索树的极端情况，退换成链表

改进：平衡二叉树，包括2-3 树, AA 树,B+ Tree, **红黑树和AVL 树**

这些数据结构面试的时候只需要**理解原理**，不需要书写

### AVL树: 完全平衡二叉树

发明者是G. M. Adelson-Velsky和Evgenii Landis

- 平衡因子（记录左子树和右子树的高度差）
- 旋转操作（左旋，右旋，左右旋，右左旋）
- 不足: 节点需要存储额外信息，且调整次数频繁（维护成本高）

面试要点：平衡因子的由来，四种基本旋转操作，

右右子树，都在右边，左旋

### 红黑树: 近似平衡二叉树

高度绝对值差2倍，红黑树的五点性质

保证任何一个节点的左右子树**高度差**小于两倍（例如，左边是5，右边可以是10，或者2.5 ）即

- 每个节点要么是红色，要么是黑色
- 根节点是黑色
- 每个叶节点(NIL节点，空节点)是黑色
- 不能有相邻的两个红色节点（关键）
- 从任一节点到其中每个叶子的所有路径都包括**相同数目**的黑色节点（关键）

