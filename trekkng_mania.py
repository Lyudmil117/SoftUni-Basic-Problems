num_groups = int(input())
all_ppl = 0

gr1 = 0
gr2 = 0
gr3 = 0
gr4 = 0
gr5 = 0

for _ in range(num_groups):
    group_size = int(input())
    if group_size <= 5:
        gr1 = gr1 + group_size
    elif 6 <= group_size <= 12:
        gr2 = gr2 + group_size
    elif 13 <= group_size <= 25:
        gr3 = gr3 + group_size
    elif 26 <= group_size <= 40:
        gr4 = gr4 + group_size
    else:
        gr5 = gr5 + group_size

    all_ppl = gr1 + gr2 + gr3 + gr4 + gr5

perc1 = (gr1 / all_ppl) * 100
perc2 = (gr2 / all_ppl) * 100
perc3 = (gr3 / all_ppl) * 100
perc4 = (gr4 / all_ppl) * 100
perc5 = (gr5 / all_ppl) * 100

print(f"{perc1:.2f}%")
print(f"{perc2:.2f}%")
print(f"{perc3:.2f}%")
print(f"{perc4:.2f}%")
print(f"{perc5:.2f}%")



