from multiprocessing import Process

def loop(num1,num2):
	for i in range(num1,num2):
		print(i)

def create_subprocess(num1,num2):
	Process(target=loop, args=(num1,num2)).start()

if __name__ == '__main__':
    for i in range(0,10):
    	create_subprocess((i*10)+1,(i*10)+11)

