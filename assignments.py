values = (1, 2, 3, 4, 5)

#a, b, *c = values -> Burda * işaretiyle a ve b ye birer değer kalan değerleri de c ye atadık

#a, *b, c = values -> Burda * işareti b ye verildiği için baştaki ve sondaki sayılar a ve c ye ortadaki değerler b ye atandı.
a, b, *c = values

print(a, b, c)