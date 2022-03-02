def even_fib(n):
    """Возвращает n четных чисел из последовательности Фибоначчи"""
    if n > 0:
        # Первое четное значение Фибоначчи это 0, сразу его и добавим.
        even_fib_list = [0]
        # Решил использовать динамическое программирование вместо рекурсивного.
        fib_list = [0, 1]
        count = 2
        while len(even_fib_list) < n:
            fib_list.append(fib_list[count-1] + fib_list[count-2])
            if fib_list[count] % 2 == 0:
                even_fib_list.append(fib_list[count])
            count += 1
        return even_fib_list
    return "Мы это не обговорили, но я решил что функция работает только для положительных n"
