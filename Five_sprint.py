
# ID успешной отправки - 121413199

CONSTANT_NUM = set('0123456789')

def decode_string(data: str) -> str:
    stack: list = []
    current_symbol, current_num = "", ""  # сохраняем его как строку


    for char in data:
        # если char будет число
        if char in CONSTANT_NUM:
            current_num += char  # просто добавляем к current_num значение char
            # если char открывающая скобка, просто добавляю в список stack
            # символы и числа (current_num преврашаем в инт)
        elif char == '[':
            stack.append((current_symbol, int(current_num)))
            # преобразовали current_num в инт
            # и нужно сбрасывать текущие значения current_symbol и current_num
            current_symbol = ""
            current_num = ""  # тут должен быть опять строкой
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
