import flet as ft
from datetime import datetime
from uuid import uuid4

class Pessoa:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)
        self.__id_cliente = str(uuid4())

    def get_id(self):
        return self.__id_cliente

    def exibir_informacoes(self):
        return f"ID: {self.__id_cliente}, " + super().exibir_informacoes()

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.__disponivel = True

    def is_disponivel(self):
        return self.__disponivel

    def set_disponibilidade(self, estado):
        self.__disponivel = estado

    def exibir_informacoes(self):
        status = "Disponível" if self.__disponivel else "Ocupado"
        return f"Quarto {self.numero} ({self.tipo}) - R${self.preco}/noite - {status}"

class Reserva:
    def __init__(self, cliente, quarto, check_in, check_out):
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.status = "Ativa"

    def cancelar_reserva(self):
        self.status = "Cancelada"
        self.quarto.set_disponibilidade(True)

    def exibir_informacoes(self):
        return f"Reserva de {self.cliente.nome} no Quarto {self.quarto.numero} ({self.status}) - {self.check_in} a {self.check_out}"

class GerenciadorDeReservas:
    def __init__(self):
        self.quartos = []
        self.clientes = []
        self.reservas = []

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_quartos_disponiveis(self):
        return [q for q in self.quartos if q.is_disponivel()]

    def criar_reserva(self, cliente, quarto, check_in, check_out):
        if quarto.is_disponivel():
            reserva = Reserva(cliente, quarto, check_in, check_out)
            self.reservas.append(reserva)
            quarto.set_disponibilidade(False)
            return reserva
        return None

    def listar_reservas(self):
        return self.reservas

    def cancelar_reserva(self, reserva):
        reserva.cancelar_reserva()
        self.reservas.remove(reserva)

def main(page: ft.Page):
    page.title = "Refúgio dos Sonhos - Gerenciamento de Reservas"
    
    hotel = GerenciadorDeReservas()
    
    hotel.adicionar_quarto(Quarto(101, "Single", 200))
    hotel.adicionar_quarto(Quarto(102, "Double", 350))
    hotel.adicionar_quarto(Quarto(201, "Suite", 500))

    hotel.adicionar_cliente(Cliente("Alice Silva", "99999-1234", "alice@email.com"))
    hotel.adicionar_cliente(Cliente("Bruno Lima", "98888-5678", "bruno@email.com"))

    def atualizar_lista_quartos():
        lista_quartos.controls.clear()
        for quarto in hotel.quartos:
            lista_quartos.controls.append(
                ft.Text(quarto.exibir_informacoes())
            )
        page.update()

    def atualizar_lista_reservas():
        lista_reservas.controls.clear()
        for reserva in hotel.listar_reservas():
            lista_reservas.controls.append(
                ft.Text(reserva.exibir_informacoes())
            )
        page.update()

    lista_quartos = ft.Column()
    lista_reservas = ft.Column()

    atualizar_lista_quartos()
    atualizar_lista_reservas()

    page.add(
        ft.Text("Gerenciamento de Reservas - Refúgio dos Sonhos", size=20, weight="bold"),
        ft.Text("Quartos Disponíveis:", size=16, weight="bold"),
        lista_quartos,
        ft.Text("Reservas Ativas:", size=16, weight="bold"),
        lista_reservas,
    )
    
ft.app(target=main)
