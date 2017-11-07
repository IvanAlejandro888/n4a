tabla = open('tabla.txt', 'r')
salida = open('silabas.txt', 'w')

content = []
final = ""

for linea in tabla:
    silaba = linea.strip().split('|')[0].strip()
    content.append(silaba)

for si in content:
    final += si + "\n"

salida.write(final)

tabla.close()
salida.close()