from flask import Blueprint, render_template, request
from app.database.models.client import Client

client_route = Blueprint('client', __name__)

@client_route.route("/")
def client_list():
    """listar os clientes"""
    clients = Client.select()
    return render_template("list_clients.html", clients=clients)

@client_route.route("/", methods=["POST"])
def insert_client():
    """inserir os dados do cliente"""
    data = request.json
    
    new_client = Client.create(
        name = data['name'], 
        email = data['email'])
    
    return render_template('item_client.html', client=new_client)

@client_route.route("/new")
def form_client():
    """formulario para cadastrar um cliente"""
    return render_template("form_client.html")

@client_route.route("/<int:client_id>")
def detail_client(client_id):
    """Exibir os detalhes do cliente""" 
    client = Client.get_by_id(client_id)
    return render_template("detail_client.html", client=client)

@client_route.route("/<int:client_id>/edit")
def form_edit_client(client_id):
    """formulario para editar um cliente"""
    client = Client.get_by_id(client_id)
    
    return render_template("form_client.html", client=client)

@client_route.route("/<int:client_id>/update", methods=["PUT"])
def update_client(client_id):
    """atualizar informações do cliente"""
    data = request.json
    
    client_edited = Client.get_by_id(client_id)
    client_edited.name = data['name']
    client_edited.email = data['email']
    client_edited.save()
            
    return render_template('item_client.html', client=client_edited)

@client_route.route("/<int:client_id>/delete", methods=["DELETE"])
def delete_client(client_id):
    """deletar informações do cliente"""
    client = Client.get_by_id(client_id)
    client.delete_instance()
    
   
    return {"deleted": "ok"}
