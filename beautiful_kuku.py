# for j in range(1, 10):
#     for i in range(1, 10):
#         print(j * i, end=' ')
#     print()

for row in range(1, 10):
    for col in range(1, 10):
        value = row * col
        print(f'{col} ✕ {row} = {value} | ', end=' ')
    print()
