# for j in range(1, 10):
#     for i in range(1, 10):
#         print(j * i, end=' ')
#     print()
#
Row = int((input('行数を入力してください > ')))
Column = int((input('桁数を入力してください > ')))

for row in range(1, Row + 1):
    for col in range(1, Column + 1):
        value = row * col
        print(f'{col} ✕ {row} = {value} | ', end=' ')
    print()
