Tenemos dos árboles y la clase `Nodo`, recordemos que un árbol esta definido por uno o varios nodos.

```python
class Nodo:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

```python
# Como aniadir un nodo a otro nodo, es decir como construir una arbol.

n1 = Nodo(3)

n2 = Nodo(0, n1)
n3 = Nodo(4, n2)

n4 = Nodo(8) # Nodo(8, ,4)

n3.right = n4

n5 = Nodo(10, None, n2)

```


Dado un árbol `a1` y un árbol `a2` implementar un método que me diga si estos árboles son iguales.
