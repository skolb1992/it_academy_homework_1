# Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа
# от 1 до 20, а значениями кубы этих чисел.

my_dict = {x: x**3 for x in range(1, 21)}
print(my_dict)
