import re  # regular expressions

pattern = re.compile(r"\bm[a-z]{7}")


def main():
    texto: str = """Algunas mochilas han sido compañeras fieles de estudiantes, viajeros y aventureros desde hace muchos años.
Sin importar si son grandes o pequeñas, las mochilas tienen la capacidad de guardar todo tipo de objetos importantes, 
desde libros hasta ropa, pasando por pequeños tesoros personales. Pero, ¿te imaginas si además de guardar cuadernos y lápices, 
tu mochila pudiera esconder algo mucho más increíble, como un unicornio. Las tortugas son bien lindas. Algunas tortugas caben en mochilas, 
pero no todas las tortugas caben en mochilas, por lo tanto hay algunas tortugas mas grandes que una mochila. muuuuuuu"""

    res = pattern.findall(texto)

    print(res)


if __name__ == '__main__':
    main()
