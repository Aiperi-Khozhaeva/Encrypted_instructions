
# ID успешной отправки - 121189103


def decode_string(data: str) -> str:
    stack: list = []
    current_num: int = 0
    current_symbol: str = ""

    for char in data:
        # если char будет число, current_num умножаем для многозначных
        # чисел и плюсуем значание char
        if char.isdigit():
            current_num = current_num * 10 + int(char)
            # если char открывающая скобка, просто добавляю в список stack
            # символы и числа
        elif char == '[':
            stack.append((current_symbol, current_num))
            # и нужно сбрасывать текущие значения current_symbol и current_num
            current_symbol = ""
            current_num = 0
            # если char закрывающая скобка, достаем из стека строку (новая
            # переменная last_symbol) и число (num)
        elif char == ']':
            last_symbol, num = stack.pop()
            # теперь current_symbol равно будет - last_symbol плюс
            # current_symbol умноженный num раз
            current_symbol = last_symbol + current_symbol * num
        else:
            # просто возравщаем current_symbol
            current_symbol += char

    return current_symbol


if __name__ == "__main__":
    data = input().strip()
    print(decode_string(data))
