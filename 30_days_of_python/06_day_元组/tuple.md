# DAY6

## 元组

元组是不同数据类型的集合，有序且不可更改（不可变）。元组用圆括号（）书写。一旦创建了一个元组，我们就不能更改它的值。我们不能在元组中使用添加、插入和删除方法，因为它不可修改（可变）。与 list 不同，元组的方法很少。与元组相关的方法:

* tuple(): 创建一个空元组
* count(): 来计算元组中指定项的个数
* index(): 查找元组中指定项的索引

### 生成元组

- 空元组创建空元组
  ```
  empty_tuple = ()

  empty_tuple = tuple()
  ```

- 带初始值的元组

```
tpl = ('item1', 'item2','item3')
```

### 长度

我们使用 len() 方法来获取元组的长度。

```
tpl = ('item1', 'item2', 'item3')
len(tpl)


```

### 访问元组

正向索引 与列表数据类型类似，我们使用正向或负向索引来访问元组项。

```
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

first_item = tpl[-4]
second_item = tpl[-3]
```

### 元组切片

我们可以通过指定索引范围来切分一个子元组，索引范围包括元组的开始和结束位置，返回值将是一个包含指定项的新元组。

```
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items

all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1] 不包含索引-3的值
```

### 将元组转换为列表

我们可以将元组改成列表，也可以将列表改成元组。元组是不可变的，如果我们想修改元组，就应该把它改成列表。

```
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

### 检查元组中的项目

我们可以使用 in 来检查元组中的项目是否存在，它返回一个布尔值。

```
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

### 连接元组

我们可以使用 + 运算符连接两个或多个元组

```
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

### 删除

无法删除元组中的单个项目，但可以使用 del 删除元组本身。

```
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```
