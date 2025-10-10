#from Cuenta import Cuenta
#from Banco import Banco
from crud_cuentas_bancarias.Gestor_de_cuentas import Gestor_de_cuentas


def main():
    #banco = Banco()
    gestor_cuentas = Gestor_de_cuentas()
    gestor_cuentas.menu()
main()

