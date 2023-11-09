from NAoM import NAoM, Rule

alph = ['a', 'b', 'c', 'd'] # Алфавит
example = NAoM(alph) # Образец алгоритма
example.show_alph()

# Пример задания правил
example.add_rule('a', '->',  'b')
example.add_rule('d', '->.', 'c')
example.add_rule('c', '->.', 'd')

# Пример замены правила
example.replace_rule('b', '->', 'c', position=1)

# Пример вставки правила
example.insert_rule('c', '->', 'd', position=2)


# Отображение правил
example.show_rules()

# Примеры перехваченных ошибок:
# Неправильная заменяемая подстрока
#example.add_rule('z', '->', 'a')
# Неправильная заменяющая подстрока
#example.add_rule('a', '->', 'fna')
# Неправильный оператор
#example.add_rule('a', '--', 'b')

# Обработка
result = example.processing('aaaa', show_process = False)
print(result)