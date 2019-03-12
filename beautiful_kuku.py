def main():
    # row = int(input('行数を入力してください > '))
    # column = int(input('桁数を入力してください > '))
    row = 9
    column = 9

    for row in range(1, row + 1):
        for col in range(1, column + 1):
            product = row * col

            padded_product = str(product).rjust(2)
            print(f'{col} ✕ {row} = {padded_product} | ', end='   ')
        print()


if __name__ == '__main__':
    main()
