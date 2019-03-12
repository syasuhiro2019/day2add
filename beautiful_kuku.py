def main():
    row = int(input('行数を入力してください > '))
    column = int(input('桁数を入力してください > '))

    for row in range(1, row + 1):
        for col in range(1, column + 1):
            value = row * col

            if value < 10:
                print(f'{col} ✕ {row} =  {value} | ', end='   ')
            else:
                print(f'{col} ✕ {row} = {value} | ', end='   ')
        print()


if __name__ == '__main__':
    main()
