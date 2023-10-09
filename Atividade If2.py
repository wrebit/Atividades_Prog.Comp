codigo = int(input("Digite o código: "))

if (codigo ==1 or codigo ==2):
    print("A procedência do seu produto é do Sul")
if (codigo ==3 or codigo ==4):
    print("Seu produto tem a origem do Sudeste")
if (codigo ==5 or codigo ==6):
    print("Seu produto tem a origem do Norte")
if (codigo ==7 or codigo ==8):
    print("Seu produto tem a origem do Nordeste")
if (codigo ==9 or codigo ==10):
    print("Seu produto tem a origem do Centro-Oeste")
if (codigo > 10):
    print("Seu produto não existe")
