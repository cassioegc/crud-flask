from flask import Flask
from flask import render_template
from flask import request
import json
app = Flask(__name__)

def load_json(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    return data

def save_json(data, fname):
    with open(fname, 'w') as f:
        json.dump(data, f)
        
def save_clients(data):
    save_json(data, 'clients.json')
 
def get_clients():
    return load_json('clients.json')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/clients/')
def clients():
    clients = get_clients()
    return render_template("clients.html", clients=clients)
    
@app.route('/clients/add', methods=['POST', 'GET'])
def add_client():
    if request.method == 'POST':
        fname = request.form["fname"]
        cpf = request.form["cpf"]
        address = request.form["address"]
        clients = get_clients()
        nid = len(clients)+1
        clients.append({'id': nid, 'name': fname, 'cpf' : cpf, 'address' : address , 'persist': True})
        save_clients(clients)
        return render_template("clients.html", clients=clients)
    elif request.method == 'GET':
        clients = load_json('clients.json')
        return render_template("addclients.html", clients=clients)

@app.route('/clients/find', methods=['POST', 'GET'])
def clients_find():
    clients = get_clients()
    if request.method == 'POST':
        fname = request.form["fname"]
        filtered = [c for c in clients if fname in c["name"]]
        return render_template("searchclients.html", clients=filtered)
    return render_template("searchclients.html", clients=clients)

@app.route('/clients/delete/', methods=['POST', 'GET'])
def delete_client():
    if request.method == 'GET':
        clients = load_json('clients.json')
        return render_template('deleteClients.html', clients=clients)
    elif request.method == 'POST':
        id = request.form["id"]
        id = int(id)
        clients = get_clients()
        for c in clients:
            if(c["id"] == id):
                c["persist"] = False
        save_clients(clients)
        return render_template("clients.html", clients=clients)

def getClient(id):
    clients = get_clients()
    for client in clients:
        if(client["id"] == id):
            return client
    return None

@app.route('/clients/update/', methods=['POST', 'GET'])
def update_client():
    if request.method == 'GET':
        return render_template("updateClient.html", client = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        client = getClient(id)
        return render_template("updateClientForm.html", client=client), 404

@app.route('/clients/update/form/', methods=['POST', 'GET'])
def update_client_form():
    print()
    #return render_template('')


if __name__ == "__main__":
    app.run(debug=True)