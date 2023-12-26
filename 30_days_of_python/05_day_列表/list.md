# DAY5

## 列表

Python 中有四种集合数据类型：

* List: 是一个有序且可更改（可修改）的集合。允许重复成员。
* Tuple: 是一个有序、不可更改或不可修改（immutable）的集合。允许重复成员。
* Set: 是一个无序、无索引、不可修改的集合，但我们可以向集合中添加新项目。不允许有重复的成员。
* Dictionary: 是一个无序、可更改（可修改）和有索引的集合。没有重复的成员。

列表是不同数据类型的集合，有序且可修改（可变）。列表可以是空的，也可以有不同数据类型的项目。

### 生成列表

在 Python 中，我们可以通过两种方式创建列表：

* 内置函数list()
  ```
  # syntax
  lst = list()
  ```
* 使用方括号 []
  ```
  # syntax
  lst = []
  ```

带初始值的列表我们使用 len() 查找列表的长度。

```
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```

```
output
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```

列表可以包含不同数据类型的项目

```
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] 
```

### 使用正向索引访问列表项

我们使用索引来访问列表中的每个项目。列表索引从 0 开始，下图清楚地显示了索引的起始位置

![List index](https://github.com/Asabeneh/30-Days-Of-Python/raw/master/images/list_index.png)

### 使用负索引访问列表项

负索引表示从末尾开始，-1 表示最后一项，-2 表示倒数第二项。

![List negative indexing](https://github.com/Asabeneh/30-Days-Of-Python/raw/master/images/list_negative_indexing.png)

### 解包list

```
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

```

### 从列表中切分项目

* 正索引：我们可以通过指定开始、结束和步长来指定一个正索引范围，返回值将是一个新的列表。(默认值为 start = 0，end = len(lst) - 1（最后一项），step = 1）

  ```
  fruits = ['banana', 'orange', 'mango', 'lemon']
  all_fruits = fruits[0:4] # 返回完整的新的列表fruits
  all_fruits = fruits[0:] # 如果我们没有设置停止的位置，它就会把剩下的都拿走
  orange_and_mango = fruits[1:3] # 不包含第一个item
  orange_mango_lemon = fruits[1:]
  orange_and_lemon = fruits[::2] # step为2,跳过orange ['banana', 'mango']
  ```
* 负索引：我们可以通过指定开始、结束和步长来指定负索引范围，返回值将是一个新列表。

  ```
  fruits = ['banana', 'orange', 'mango', 'lemon']
  all_fruits = fruits[-4:] 
  orange_and_mango = fruits[-3:-1] 
  orange_mango_lemon = fruits[-3:] 
  reverse_fruits = fruits[::-1] # step为-1会翻转列表,['lemon', 'mango', 'orange', 'banana']
  ```

### 修改列表

列表是一个可变或可修改的有序项目集合。

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

### 检查列表中的项目

使用 in 运算符检查项目是否为列表成员。

```
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### 将项目添加到列表

要将项目添加到现有列表的末尾，我们使用 append() 方法。

```
lst = list()
lst.append(item)
```

### 将项目插入列表

我们可以使用 insert() 方法在列表的指定索引处插入单个项目。请注意，其他项目会向右移动。insert() 方法有两个参数：索引和要插入的项目。

```
lst = ['item1', 'item2']
lst.insert(index, item)
```

### 从列表中删除项目

删除方法从列表中删除指定项目

```
lst = ['item1', 'item2']
lst.remove(item)
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
```

### 使用 Pop 移除项目

pop() 方法会删除指定的索引（如果未指定索引，则删除最后一项）：

```
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

### 使用 Del 删除项目

del 关键字可删除指定的索引，也可用于删除索引范围内的项目。它还可以完全删除列表

```
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely

```

### 清除列表项目

clear() 方法会清空列表：

```
lst = ['item1', 'item2']
lst.clear()
```

### 复制列表

可以通过以下方式将列表重新赋值给一个新变量来复制列表：list2 = list1。现在，list2 是 list1 的引用，我们对 list2 所做的任何修改也会修改原来的 list1。但在很多情况下，我们并不希望修改原始变量，而是希望有一个不同的副本。避免上述问题的方法之一就是使用 copy()。

```
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

### 加入列表

在 Python 中，有几种方法可以连接或串联两个或多个列表。

```
list3 = list1 + list2
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
```

### 计算列表中的项目

count() 方法返回项目在列表中出现的次数：

```
lst = ['item1', 'item2']
lst.count(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### 查找项目索引

index() 方法返回列表中项目的索引：

```
lst = ['item1', 'item2']
lst.index(item)
```

### 翻转列表

reverse() 方法可以颠倒列表的顺序。

```
lst = ['item1', 'item2']
lst.reverse()
```

### 列表排序

要对列表进行排序，我们可以使用 sort() 方法或 sorted() 内置函数。sort() 方法按升序重新排列列表项，并修改原始列表。如果 sort() 方法的参数 reverse 等于 true，则会按降序排列列表。

* sort()：该方法修改原始列表

```
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```

* sorted()： 在不修改原始列表的情况下返回有序列表：
  ```
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
  # Reverse order
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits,reverse=True)
  print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
  ```
