from time import time, sleep

#function
def func(n):
    for i in range(n):
        print(i)
        
start = time()
func(35000)
end = time()

print(round(end - start),"secs")
