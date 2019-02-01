import time

def build_list(file):
    fin = open(file)
    t = []
    
    for line in fin:
        word = line.strip()
        t.append(word)
    
    return t


def build_list2(file):
    fin = open(file)
    t = []
    
    for line in fin:
        word = line.strip()
        t.append(word)
    
    return t



start_time = time.time()
t = build_list("words.txt")
elapsed_time = time.time()-start_time
print(len(t))
print(t[-10:])
print(elapsed_time, "seconds")




start_time = time.time()
t = build_list2("words.txt")
elapsed_time = time.time()-start_time
print(len(t))
print(t[-10:])
print(elapsed_time, "seconds")




