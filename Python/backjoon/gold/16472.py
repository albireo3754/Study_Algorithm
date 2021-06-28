import threading 
x = 0 # A shared value

def foo():
    global x
    for i in range(1000000): 
        x += 1 
def bar(): 
    global x 
    for i in range(1000000): 
        x -= 1 
t1 = threading.Thread(target=foo) 
t2 = threading.Thread(target=bar) 
t1.start() 
t2.start() 
t1.join() 
t2.join() # Wait for completion

print(x)
