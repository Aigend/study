# 同步和异步：用来描述任务的提交方式
# 同步：任务提交之后，原地等待任务的返回结果
# 异步：任务提交之后，不再等待结果，而是去做其他事情

# 阻塞和非阻塞：描述进程的运行状态
# 阻塞：阻塞态
# 非阻塞：就绪和运行态，cpu利用率较高

# 同步阻塞
# 同步非阻塞
# 异步阻塞
# 异步非阻塞：目前很多的异步框架都是支持的

# 创建进程，方式很多
"""
1.os.fork()  # windows系统不支持
2.multiprocessing
3.subprocess  # 运维使用，用来执行终端代码，功能不多
"""
from multiprocessing import Process, current_process
import time
import os
age = 18
def func(name):
	print(f"任务{current_process().pid}执行中")
	print(f"任务{os.getpid()}执行中")
	print(f"父进程{os.getppid()}执行中")

	time.sleep(5)
	age = 16

# linux 查看进程 ps aux |  grep pid
# windows 查看进程 tasklist | findstr pid

# 这里推荐使用if判断的方式创建，因为windows系统和linux系统不同，
# linux 创建的时候会把函数执行的代码，和数据集全部都拷贝一份
# linux 创建的时候会把当前模块再进行一次导包，如果不加if 会进入死循环
if __name__ == "__main__":
	p = Process(target=func, args=("写讲话稿", ))
	p.start()  # 异步提交任务：提交后不会等待任务的结果
	# p.terminate() # kill -9 pid ，taskkill pid, 这里发起系统调用，杀死进程
	# p.is_alive() # 如果调用terminate后立刻调用is_alive会获取不到理想的结果，系统杀死进程需要时间，延迟0.001s
	print("主进程")
	p.join()
	print(age) # 这里会打印18,主进程和子进程数据是隔离的

# 创建进程的第二种方式，通过类的方式

class MyProcess(Process):

	def __init__(self, name):
		super().__init__()
		self.task_name = name

	def run():
		pass

if __name__ == "__main__":
	p = MyProcess("约会")
	p.start()
	p.join()  # 等待子进程执行结束，才继续往下执行
	print("主进程") # 不加join ,默认会等子进程结束，程序才完成


# 僵尸进程：
	子进程结束后，会有一些资源占用（进程号，进程运行状态，运行时间等）等待父进程通过系统调用回收
	除了init进程之外，所有的进程，最后都会进入僵死进程

	视频这里介绍主进程代码执行结束，子进程代码还未结束时，主进程会等待回收子系统资源
	实际测试发现，主进程代码执行完，子进程代码还未执行完时，主进程仍存在

	危害：
		子进程退出之后，父进程没有及时处理，僵死进程会一直占用计算机资源 
		如果产生了大量的僵死进程，系统资源占用，没有可用的进程号，导致系统产生新的进程
# 孤儿进程：
	子进程处于存活状态，但是父进程意外死亡，比如：终端中把父进程杀死掉，没有人回收子系统资源
	操作系统会开设一个孤儿院（init进程）,用来管理孤儿进程，回收孤儿进程的资源

# 守护进程：
	p.daemon = True # 这个设置要在p.start()之前配置，否则报错，主进程结束，子进程也结束
# 互斥锁
from multiprocessing import Lock 
import random
def search_tickeet(name):
	with open('data/tickets', 'r', encoding='utf-8') as f:
		dic = json.load(f)
		print(f"用户{name}查询余票，还剩{dic.get('tickets_num')}")	


def buy_ticket(name):
	with open('data/tickets', 'r', encoding='utf-8') as f:
		dic = json.load(f)
	time.sleep(random.randint(1, 5))
	if dic.get('tickets_num') > 0:
		dic['tickets_num'] -= 1
		with open('data/tickets', 'w', encoding='utf-8') as f:
			json.dump(dic, f)
		print(f"{name} 买票成功")
	else：
		print(f"余票不足，{name} 买票失败")

def task(name, mutex):
	search_tickeet(name)
	mutex.acquire()
	buy_ticket(name)
	mutex.release()

if __name__ == "__main__"":
	mutex = Lock()
	for i in range(9):
		p = Process(target=task, args=(i, mutex))
		p.start()

# 行锁
# 表锁
# 锁把并发变成串行，会造成互锁问题
