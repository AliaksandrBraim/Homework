# # Пользователь вводит Имя, Возраст и Город, сформировать
# # приветственное сообщение путем форматирования 3-мя способами
name, age, town = input(), input(), input()
print(f'Hello {name} your age {age} you live in {town}')
print('Hello {} your age {} you live in {}'.format(name, age, town))
d ='Hello %s your age %s you live in %s' % (name, age, town)
print(d)