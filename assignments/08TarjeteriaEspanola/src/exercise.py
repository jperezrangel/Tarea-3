def tarjetas(pliegos,plumones):
    tarjetas1=(pliegos*12)
    tarjetas2=(plumones*35)
    
    if tarjetas1 < tarjetas2:
        return (tarjetas1)

    else:
        return (tarjetas2)

def main():
    #escribe tu código abajo de esta línea
    pliegos=int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones=int(input('Dame la cantidad de plumones: '))
    print("El número máximo de tarjetas que se pueden hacer es:",tarjetas(pliegos,plumones))
    
if __name__ == '__main__':
    main ()
