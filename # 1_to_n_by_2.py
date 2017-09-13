# 1_to_n_by_2.py

n = input("Enter your number: ")
n = int(n)

start = 1
end = 2

while start <= n:
    print(start)

    start += end
