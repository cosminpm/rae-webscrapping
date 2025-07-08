# Atajos

# En mac todos los Ctrl suelen ser el command
# Ctrl Z -> deshacer
# Ctrl Shift Z -> Rehacer

def excepciones(rae: dict):
    rae["patata2"]

    try:
        rae["patata2"]

    except:
        print("Ha saltado una excepcion pero mi programa seguira ejecutando")
    print("Estoy fuera, si hubiera un error que no este dentro del try, eso no deberia aparecer")

def diccionarios():
    rae: dict = {"patata": "tuberculo que nutre a los humanos",
                 "perro": "mejor amigo del hombre"}

    rae["pantalon"] = "usado para vestir las piernas"
    rae.update({"lapiz": "usado para escribir sobre papel", "goma": "eliminar lo que hay sobre el papel"})
    rae.update({"2": "una patata del minecraft"})

    # rae.get("patata2") -> no salta una excepcion
    # rae["patata2"]     -> salta excepcion


def pregunta_implementacion():
    ...

    # 190 mil lineas -> excel

    # SAP no puede subir 190 mil
    # Lo puedes hacer con ficheros de 15 mil lineas
    # tiene que ser un .exe

    # Se tiene que subir a SAP


def main():
    diccionarios()


if __name__ == '__main__':
    main()
