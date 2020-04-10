import time


begin = time.time()

for i in range(999999):
    print(i)
    
end = time.time()
print(begin-end)

        