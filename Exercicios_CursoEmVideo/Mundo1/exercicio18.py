import math
co = float(input('Insira o cateto oposto:'))
ca = float(input('Insira o cateto adjacente:'))
hip = co**2 + ca**2
hipfinal = math.sqrt(hip)
print('A hipotenusa do triângulo cujos numeros foram informados é igual à {}'.format(hipfinal))