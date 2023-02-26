# 第一种使用方法
import queue
queue.Queue()
# 第二种使用方法
from multiprocessing import queues
queues.Queue()
# 第三种用法
from multiprocessing import Queue
q = Queue(6)  # maxsize 消息队列最大保存的消息数目
		  # 不传值，默认为326767
# 队列是先进先出
q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')
q.put('f')

print(q.full()) # 判断队列是否满了

q.put('h')  # 存第个元素的时候程序阻塞
q.put_nowait('h')  # raise Full 报错，queue.Full
q.put('h', timeout=3)  # 3s之内还是满的，会报错

v1 = q.get()
print(v1)
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()
v6 = q.get()

print(q.empty())

v7 = q.get()  # 阻塞，什么时候有数据，继续往下执行
v7 = q.get_nowait()  # 无数据报错 raise Empty _queue.Empty
v7 = q.get(timeout=3) # 无数据等待3s,3s后仍无数据就报错

"""
q.put()
q.get()


q.full()
q.empty()
q.put_nowait()
q.get_nowait()
这四个函数在多进程极限条件下可能不太准确，这个进程刚满了，存数据报错，下一个进程可能就取了数据

"""