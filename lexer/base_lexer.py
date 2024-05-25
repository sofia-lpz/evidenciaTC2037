# Programa que realiza el análisis léxico de un archivo de texto que contiene expresiones aritméticas
# y muestra los tokens encontrados en el archivo de texto.
# Nicole Dávila A01784217

def lexerAritmetico(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    for linea in lineas:
        p = 0
        lexema = ''
        while p < len(linea):
            if linea[p] == '-' and p + 1 < len(linea) and linea[p + 1].isdigit():
                lexema += linea[p]
                p += 1
            if linea[p].isdigit():
                while p < len(linea) and (linea[p].isdigit() or linea[p] == '.' or linea[p] == 'E' or linea[p] == 'e' or (linea[p] == '-' and lexema and lexema[-1] in 'Ee')):
                    lexema += linea[p]
                    p += 1
                if '.' in lexema or 'E' in lexema or 'e' in lexema:
                    print(lexema, 'REAL')
                else:
                    print(lexema, 'ENTERO')
                lexema = ''
            elif linea[p].isalpha() or linea[p] == '_':
                while p < len(linea) and (linea[p].isalnum() or linea[p] == '_'):
                    lexema += linea[p]
                    p += 1
                print(lexema, 'VARIABLE')
                lexema = ''
            elif linea[p] == '+':
                print('+', 'SUMA')
                p += 1
            elif linea[p] == '-':
                print('-', 'RESTA')
                p += 1
            elif linea[p] == '*':
                print('*', 'MULTIPLICACION')
                p += 1
            elif linea[p] == '/':
                if p + 1 < len(linea) and linea[p + 1] == '/':
                    print(linea[p:].strip(), 'COMENTARIO')
                    break
                else:
                    print('/', 'DIVISION')
                    p += 1
            elif linea[p] == '^':
                print('^', 'POTENCIA')
                p += 1
            elif linea[p] == '(':
                print('(', 'ABRE_PARENTESIS')
                p += 1
            elif linea[p] == ')':
                print(')', 'CIERRA_PARENTESIS')
                p += 1
            elif linea[p] == '=':
                print('=', 'ASIGNACION')
                p += 1
            else:
                p += 1

lexerAritmetico("expresiones.txt")