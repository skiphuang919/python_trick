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

## python 多继承
* 当类是经典类的时候，按照深度优先查找属性或方法
* 当类是新式类的时候，按照广度优先查找属性或方法