def main():
    # row = int(input('行数を入力してください > '))
    # column = int(input('桁数を入力してください > '))
    row = 12
    column = 12

    for row in range(1, row + 1):
        for col in range(1, column + 1):
            product = row * col

            padded_product = str(product).rjust(3)
            padded_row = str(row).rjust(2)
            print(f'{col} ✕ {padded_row} = {padded_product} | ', end='   ')
        print()


if __name__ == '__main__':
    main()
