# 学习笔记

[TOC]



## 位运算

* 位运算符

* 算数以为与逻辑移位

* 位运算证明

### 位运算符

|            含义             | 运算符 |     实例     |
| :-------------------------: | :----: | :----------: |
|            右移             |   >>   | 0011 => 0110 |
|            左移             |   <<   | 0110 => 0011 |
|       按位或(有1取1)        |   \|   |              |
|       按位与(有0取0)        |   &    |              |
|    按位取反(0变1，1变0)     |   ~    |              |
| 按位异或)(相同取0，不同取1) |   ^    |              |

XOR - 异或：相同为0，不同为1.也可用“进位加法”来理解

```shell
x ^ 0 = X
x ^ 1s = ~x  # 1s = ~ 0
x ^ (~x) = 1s 
x ^ x = 0
c = a ^ b  => a ^ c = b, b ^c = a # 交换两数
a ^ b ^ c = a ^(b ^ c) = (a ^ b) ^c # associative 
```

指定未知的位运算

1. 将x最右边的n位请零： x & (~0 << n )
2. 获取x的第n位值（0 或 1）： （x >> n）& 1
3. 获取x的第n位的幂值：x & （1 <<  n）
4. 仅将第n位置为 1： x | (1 << n)
5. 仅将第n位置为0：x & （~1（1 << n））
6. 将x最高位至第n位(含)清零：x & ((1 << n) - 1)

### 实战位运算要点

判断奇偶性

x % 2 == 1 - >  (x & 1) == 1

x & 2 == 0  -> (x& 1) == 0



x = x & (x - 1) 清零最低位的1

x & ~x 得到最低位的1

x & ~ x = > 0

- [布隆过滤器的原理和实现](https://www.cnblogs.com/cpselvis/p/6265825.html)
- [使用布隆过滤器解决缓存击穿、垃圾邮件识别、集合判重](https://blog.csdn.net/tianyaleixiaowu/article/details/74721877)
- [布隆过滤器 python3 代码示例](https://shimo.im/docs/UITYMj1eK88JCJTH)
- [布隆过滤器 python3 实现示例](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python3-implementation/)
- [高性能布隆过滤器 python3 实现示例](https://github.com/jhgg/pybloof)
- [布隆过滤器 Java 实现示例 1](https://github.com/lovasoa/bloomfilter/blob/master/src/main/java/BloomFilter.java)
- [布隆过滤器 Java 实现示例 2](https://github.com/Baqend/Orestes-Bloomfilter)

布隆过滤器python3实现

```python3
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```

LRU Cache 

```python3
class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```

## 排序算法:（bubbleSort）

排序算法分类表

![排序算法分类](D:\积跬Coder\算法\排序算法\排序算法分类.png)

排序算法对照表

![各排序算法对照](D:\积跬Coder\算法\排序算法\各排序算法对照.png)





### 冒泡排序

通过从前往后二者重复比较，将较大的放置在后。

![冒泡排序](D:\积跬Coder\算法\排序算法\冒泡排序.jpg)

#### 算法概述：

- 比较相邻元素，二者（N -1， N）较大者放置在后
- 获取上一次比较结果，进行（N， N＋1），进行条件一
- 每次比较完成后，长度N - 1
- 重复完成1-3步骤

```python3
def bubbleSort(nums:List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = num[j], nums[j + 1] # 交换
     return nums
```

#### 冒泡排序优化:

减少“已完成”排序比对，设置flag， 进行剪枝

~~~python3
def batter_bubbleSort(nums:List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        flag = True
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = num[j], nums[j + 1] # 交换
                flag = False
         if flag:
            break
     return nums
~~~

### 选择排序(selectionSort)

循环扫描全数组，选择最小的数，放置在最前或最后

![选择排序](D:\积跬Coder\算法\排序算法\选择排序.jpg)



#### 算法概述

- 扫描全数组，寻找最小的数
- 保存最小数的索引
- 将最小数放置在相对最前(或最后)

```python3
def selectionSort(nums:List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        min = i
        for j in range(i+1, len(nums)):
            if num[j] < nums[min]:
                min = j
     nums[i], nums[min] = nums[min], nums[i]
    return nums
```

### 插入排序(insertionSort):

通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入



#### 算法概述

- 从第一个元素开始，该元素可以认为已经被排序；
- 取出下一个元素，在已经排序的元素序列中从后向前扫描；
- 如果该元素（已排序）大于新元素，将该元素移到下一位置；
- 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
- 将新元素插入到该位置后；
- 重复步骤2~5。

```
def insertSort(nums: List[int]):
    for i in range(1, len(nums)):
        j = i - 1
        tmp = nums[i]
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp
        # print(nums)
    return nums
```



### 希尔排序(shellSort)

是简单插入排序的改进版。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫**缩小增量排序**。

#### 算法概述

- 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
- 按增量序列个数k，对序列进行k 趟排序；
- 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

```python3
def shellSort(nums: List[int]) -> List[int]:
    n = len(nums)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j = j - gap
            nums[j + gap] = temp
        gap = int(gap / 2)
    return nums
```

### 归并排序（Merge Sort）

建立在[归并](https://baike.baidu.com/item/归并/253741)操作上的一种有效，稳定的排序算法，该算法是采用[分治法](https://baike.baidu.com/item/分治法/2407337)（Divide and Conquer）的一个非常典型的应用。将已有序的子[序列](https://baike.baidu.com/item/序列/1302588)合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。

#### 算法概述

第一步：申请空间，使其大小为两个已经[排序](https://baike.baidu.com/item/排序)序列之和，该空间用来存放合并后的序列

第二步：设定两个[指针](https://baike.baidu.com/item/指针)，最初位置分别为两个已经排序序列的起始位置

第三步：比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置

重复步骤3直到某一指针超出序列尾

```python3
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result

def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
```

### 快速排序（Quick Sort）

通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

#### 算法概述

- 从数列中挑出一个元素，称为 “基准”（pivot）；
- 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
- 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

```python3
def quickSort(nums):    
    if len(nums) >= 2:  # 递归入口及出口        
        mid = nums[len(nums)//2]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        nums.remove(mid)  # 从原始数组中移除基准值        
        for num in nums:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quick_sort(left) + [mid] + quick_sort(right)    
    else:        
        return nums
```

