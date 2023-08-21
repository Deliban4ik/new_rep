
def gen():
    count=0
    while 5>=count:
        
        yield count
        count=count+1
geen=gen()
for i in range(6):
    print(next(geen))