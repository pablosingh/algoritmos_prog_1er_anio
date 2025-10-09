class Cuenta:
    def __init__(self, numero: int,nombre: str, apellido: str, tipo: str, saldo: float ) -> None:
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo
        self.saldo = saldo

    def __str__(self) -> str:
        return f"Cuenta {self.numero} | {self.nombre} \t| {self.apellido} \t| {self.tipo} \t| {self.saldo}"

