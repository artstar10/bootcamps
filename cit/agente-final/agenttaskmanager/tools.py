import os
import requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")

def obter_listas_do_quadro() -> str:
    """Obtém todas as listas do quadro atual do Trello. Use isso para descobrir o ID da lista antes de criar ou mover uma tarefa."""
    url = f"https://api.trello.com/1/boards/{TRELLO_BOARD_ID}/lists"
    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN
    }
    
    response = requests.get(url, params=query)
    
    if response.status_code == 200:
        listas = response.json()
        return "Listas disponíveis:\n" + "\n".join([f"- Nome: {lista['name']} | ID: {lista['id']}" for lista in listas])
    return f"Erro ao obter listas: {response.text}"

def criar_tarefa_trello(nome_tarefa: str, id_lista: str, descricao: str = "") -> str:
    """Cria um novo card (tarefa) em uma lista específica no Trello.
    
    Args:
        nome_tarefa: O título da tarefa.
        id_lista: O ID da lista onde a tarefa será criada.
        descricao: A descrição detalhada da tarefa.
    """
    url = "https://api.trello.com/1/cards"
    query = {
        'idList': id_lista, 'key': TRELLO_API_KEY, 'token': TRELLO_TOKEN,
        'name': nome_tarefa, 'desc': descricao
    }
    
    response = requests.post(url, params=query)
    return f"Tarefa '{nome_tarefa}' criada com sucesso!" if response.status_code == 200 else f"Erro: {response.text}"