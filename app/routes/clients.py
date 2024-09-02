from flask import Blueprint, render_template
from app.database.client import CLIENTS

client_route = Blueprint('client', __name__)

@client_route.route("/")
def client_list():
    """listar os clientes"""
    return render_template("list_clients.html", clients=CLIENTS)

@client_route.route("/", methods=["POST"])
def insert_client():
    """inserir os dados do cliente"""
    pass

@client_route.route("/new")
def form_client():
    """formulario para cadastrar um cliente"""
    return render_template("form_client.html")

@client_route.route("/<int:client_id>")
def detail_client(client_id):
    """Exibir os detalhes do cliente""" 
    return render_template("detail_client.html")

@client_route.route("/<int:client_id>/edit")
def form_edit_client(client_id):
    """formulario para editar um cliente"""
    return render_template("form_edit_client.html")

@client_route.route("/<int:client_id>/update", methods=["PUT"])
def update_client(client_id):
    """atualizar informações do cliente"""
    pass

@client_route.route("/<int:client_id>/delete", methods=["DELETE"])
def delete_client(client_id):
    """deletar informações do cliente"""
    pass
