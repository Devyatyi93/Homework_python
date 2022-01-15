# 1) Создать переменную типа String
# 2) Создать переменную типа Integer
# 3) Создать переменную типа Float
# 4) Создать переменную типа Bytes
# 5) Создать переменную типа List
# 6) Создать переменную типа Tuple
# 7) Создать переменную типа Set
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict
#
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
#
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

a = str("string")
b = int(3)
c = float(1.23)
d = bytes(10)
e = list("список")
f = tuple("кортеж")
g = set("hello")
q = frozenset("homework")
m = dict({1: "home", 2: "work"})


print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(q, type(q))
print(m, type(m))

s_1="Hello"
s_2="World"
print(s_1 + s_2)

print(a, b)

print(a+str(b))



