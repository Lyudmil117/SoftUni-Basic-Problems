liters_pool = int(input())
debit_pipe_one = int(input())
debit_pipe_two = int(input())
hours = float(input())


#За 3 часа:
#Първата тръба е напълнила – 300 л.
#Втората тръба е напълнила – 360 л.
#бщо – 660 л. < 1000 л. => 66% са запълнени
#Първата тръба е допринесла с 45% (300 от 660 л.).
#Втората тръба е допринесла с 54% (360 от 660 л.).

water = (debit_pipe_one * hours) + (debit_pipe_two * hours)
over = water - liters_pool
pipe_one_percent = ((debit_pipe_one * hours) / water) * 100
pipe_two_percent =((debit_pipe_two * hours) / water) * 100
percent_full_pool = (water / liters_pool) * 100
full = pipe_two_percent + pipe_two_percent

if liters_pool < water:
    print(f"For {hours} hours the pool overflows with {over:.2f} liters.")
else:
    print(f"The pool is {percent_full_pool}% . Pipe1: {pipe_one_percent:.2f}%. Pipe2: {pipe_two_percent:.2f}.")


