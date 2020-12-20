from threading import Thread
def PR():
	return 0 
def proizvedenie_array(line):
    a=1;
    for i in range(len(line)):
        a*=line[i]
    return a
 
if __name__ == '__main__':
	n=10
	a=[[(i*13)**3 for i in range(1,n+1)] for j in range(1,n+1)]
	for i in range(5):
		my_thread=Thread(target=proizvedenie_array, args=(a[i],))
		my_thread.start()
	print(my_thread)
