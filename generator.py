def first_last(letter, start, end, step=1):
    if start > 0 and end < len(letter):
        return letter[start:end:step]



# Тесты
print(first_last('ghghgha', 1, 2))
