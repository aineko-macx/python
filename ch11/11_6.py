import time


known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    result = fibonacci(n-1) + fibonacci(n-2)
    known[n] = result

    return result


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo(n - 1) + fibo(n - 2))



start_time = time.time()
print(fibonacci(10))
elapsed_time = time.time() - start_time
print(elapsed_time)


start_time = time.time()
print(fibonacci(50))
elapsed_time = time.time() - start_time
print(elapsed_time)


start_time = time.time()
print(fibo(10))
elapsed_time = time.time() - start_time
print(elapsed_time)

start_time = time.time()
print(fibo(50))
elapsed_time = time.time() - start_time
print(elapsed_time)
