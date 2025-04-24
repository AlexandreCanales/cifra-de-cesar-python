def criptografar():
    frase_cript = input("Digite uma frase para ser criptografada: ")
    listac1 = []
    listac2 = []
    cripto1 = []
    retorno = {123: 65, 124: 66, 125: 67, 91: 97, 92: 98, 93: 99}

    for c1 in frase_cript:
        ascii = ord(c1)
        listac1.append(ascii)

    for c2 in listac1:
        c2 += 3
        listac2.append(c2)

    for c3 in listac2:
        if c3 in retorno:
            c3 = retorno[c3]
        cripto = chr(c3)
        cripto1.append(cripto)

    mensagem_c = ''.join(map(str, cripto1))
    print("Frase criptografada:", mensagem_c)

def decriptografar():
    frase_decript = input("Digite uma frase para ser decriptografada: ")
    listad1 = []
    listad2 = []
    decript1 = []
    retorno = {62: 120, 63: 121, 64: 122, 94: 88, 95: 89, 96: 90}

    for d1 in frase_decript:
        ascii = ord(d1)
        listad1.append(ascii)

    for d2 in listad1:
        d2 -= 3
        listad2.append(d2)

    for d3 in listad2:
        if d3 in retorno:
            d3 = retorno[d3]
        cripto = chr(d3)
        decript1.append(cripto)

    mensagem_d = ''.join(map(str, decript1))
    print("Frase decriptografada:", mensagem_d)

# Menu principal
if __name__ == "__main__":
    menu = int(input(
        "Escolha uma das funções:\n1 - Criptografar\n2 - Decriptografar\nOpção: "
    ))

    if menu == 1:
        criptografar()
    elif menu == 2:
        decriptografar()
    else:
        print("Digite um número válido!")
