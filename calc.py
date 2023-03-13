# simple calculator is very simple
result = 0
txt_result = ''

while 1:
    math = input('Введите действие: ')
    if math == '+' or math == '-' or math == '*' or math == '/':
        break
    print('Доступны действия: +, - , *, /')

while 1:
    try:
        k = int(input('Сколько операндов?: '))
        break
    except ValueError:
        print('Нужно ввести целое число')

for i in range(1, k + 1):
    if result == 'E':
        break

    text = 'Введите число ' + str(i) + ': '
    while 1:
        try:
            m = int(input(text))
            break
        except ValueError:
            print('Нужно ввести целое число')

    if i == 1:
        result = m
        txt_result = str(result)

    if math == '+' and i != 1:
        txt_result += ' + ' + str(m)
        result += m

    if math == '-' and i != 1:
        txt_result += ' - ' + str(m)
        result -= m

    if math == '*' and i != 1:
        txt_result += ' * ' + str(m)
        result *= m

    if math == '/' and i != 1:
        txt_result += ' / ' + str(m)
        try:
            result /= m
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
            result = 'E'

print(txt_result + ' = ' + str(result))
