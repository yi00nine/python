# DAY13

## 列表推导

Python 中的列表理解是一种从序列创建列表的简洁方法。它是创建新 list 的简捷方法。列表理解比使用 for 循环处理列表要快得多。

```
[i for i in iterable if expression]
```

```python
# 例如，如果您想将字符串更改为字符列表。您可以使用几种方法。让我们来看看其中的几种：
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

#生成一个数字列表
numbers = [i for i in range(11)]
print(numbers)  

squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#列表理解可与 if 表达式相结合
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


```

## lambda 表达式

Lambda 函数是一个没有名称的匿名小函数。它可以接受任意数量的参数，但只能有一个表达式。Lambda 函数类似于 JavaScript 中的匿名函数。当我们想在另一个函数中编写匿名函数时，就需要它。

### 创造lambda 表达式

要创建 lambda 函数，我们要使用 lambda 关键字，然后是参数和表达式。请参见下面的语法和示例。lambda 函数不使用 return，但会明确返回表达式。

```
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

### 另一个函数内部的 Lambda 函数

在另一个函数中使用 lambda 函数

```
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # 函数电源现在需要 2 个参数才能运行，分别置于圆括号中brackets
print(cube)          # 8
```
