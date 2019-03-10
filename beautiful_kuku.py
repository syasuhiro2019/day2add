def main():
    Row = int((input('行数を入力してください > ')))
    Column = int((input('桁数を入力してください > ')))
    for row in range(1, Row + 1):
        for col in range(1, Column + 1):
            value = row * col
            print(f'{col} ✕ {row} = {value} | ', end='   ')
        print()


if __name__ == '__main__':
    main()
