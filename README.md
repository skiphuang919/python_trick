# python_trick
## 单例模式
一种设计模式，保证一个类只能有一个实例

实现：

* 装饰器
* 利用`__new__`

## 带参数的装饰器
理解闭包

LEGI原则： `locals -> enclosing function -> globals -> __builtins__`

## 协程vs多线程vs多进程
* 协程用的是gevent库
* 简单测试同一个任务用三种不同的形式执行效率
* monkey的patch对线程池的使用有影响，所以分开执行

## 多继承MRO(Method Resolution Order)
### DFS 
经典类的MRO,深度优先搜索（子节点顺序：从左到右）


缺点：
棱形继承模式，存在只能继承无法重写的问题

### BFS
新式类MRO,广度优先搜索（子节点顺序：从左到右）

缺点：
违背单调性

因为违背了单调性，所以BFS方法只在Python2.2中出现了，在其后版本中用C3算法取代了BFS。

### C3

MRO的C3算法看起来像是DFS和BFS的合体，很好的解决了以上的问题

