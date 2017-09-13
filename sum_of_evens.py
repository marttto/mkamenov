# sum_of_evens.py

N = input("Enter your number here: ")
N = int(N)

start = 1
total_sum = 0


while start <= N:
    if start  % 2 == 0:
        total_sum += start

    start += 1

print("The total sum is " + str(total_sum))
