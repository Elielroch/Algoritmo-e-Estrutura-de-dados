class Analisador:
    def __init__(self):
        pass

    def acha_sequencia(self, valores, probs) -> int:
        n = len(valores)
        indices_ordenados = sorted(range(n), key=lambda i: (-valores[i], probs[i]))
        return indices_ordenados


