# DAY7

集合

### 生成Set

我们使用 set() 内置函数。

```
st = set()
st = {'item1', 'item2', 'item3', 'item4'}
```

### 集合长度

我们使用 len() 方法来查找集合的长度。

```
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

### 访问集合内容

我们使用循环来访问项目。我们将在循环部分看到这一点

### 检查集合item

要检查列表中是否存在项目，我们使用成员运算符。

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

### 项目添加到集合

set创建后，我们不能更改任何项目，可以添加其他项目。

```
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
st.update(['item5','item6','item7']) #添加多个item
```

### 从集合中删除项目

我们可以使用 remove() 方法从集合中删除一个项目。如果找不到 item，remove() 方法将引发错误，因此最好先检查该 item 是否存在于给定的集合中。而 discard() 方法不会引发任何错误。

```
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

pop() 方法会从列表中随机移除一个项目，并返回被移除的项目。

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
```

### 清除集合中的项目

如果我们想清除或清空集合，则使用清除方法。

```
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

### 删除集合

如果要删除集合本身，则使用 del 操作符。

```
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

### 将列表转换为集合

我们可以将列表转换为集合，也可以将集合转换为列表。将列表转换为集合可以删除重复项，只保留唯一项。

```
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'}
```

### 拼接集合

我们可以使用 union() 或 update() 方法连接两个集合。

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)

```

### 交集

交集返回两个集合中都有的项目集

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)
```

### 子集和超集

一个集合可以是其他集合的子集或超集合：

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

### 差集

它返回两组数据的差值。

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```

### 两个集合的对称差

它返回两个集合之间的对称差。这意味着它返回的集合包含了两个集合中的所有项目，除了两个集合中都存在的项目，数学上是：(A/B) ∪ (B\A)

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```

### 相交集合

如果两个集合没有一个或多个共同项，我们就称它们为不相交集合。我们可以使用 isdisjoint() 方法检查两个集合是联合还是不联合。

```
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```
