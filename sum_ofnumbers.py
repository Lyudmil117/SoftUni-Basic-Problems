num_numbers = int(input())
suma = 0

for _ in range(num_numbers):  #tova ste zavurti ot 0 do nesto si. moje i da stane range(1, num_numbers +1) sustotot e
    current_number = int(input())
    suma = current_number + suma

print(suma)