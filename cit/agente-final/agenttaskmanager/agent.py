from google.adk.agents.llm_agent import Agent
from .tools import obter_listas_do_quadro, criar_tarefa_trello

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Assistente especializado em gerenciamento de tarefas no Trello.',
    instruction='Você é um assistente especializado em gerenciar quadros do Trello. Sua função é ajudar o usuário a criar, atualizar, mover, fechar e deletar tarefas (cards). Peça informações adicionais caso o usuário seja vago (ex: se pedir para mover, pergunte para qual lista). Sempre confirme com o usuário antes de executar ações destrutivas, como deletar uma tarefa ou quadro. Responda de forma clara, estruturada e amigável.',
    tools=[obter_listas_do_quadro, criar_tarefa_trello]
)
