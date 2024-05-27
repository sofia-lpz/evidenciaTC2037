import re

pattern = r

def getArchivo(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()


def sustituye(objeto):
    return '<font color="red">' + objeto.group(0) + '</font>'

b = re.sub(pattern, sustituye, f)

file_html = open('resultado.html', 'w')
file_html.write(b)
file_html.close()