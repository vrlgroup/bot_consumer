# Barra de pesquisa na sidebar
SEARCHBAR_INPUT_XPATH = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]"

# Input do chat quando a conversa esta aberta
CHAT_INPUT_XPATH = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]"

# Botao que faz o envio da mensagem que esta no input
CHAT_SUBMIT_MESSAGE_BUTTON_XPATH = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button"

# Abrir as configuracoes do grupo, equivalente aos 3 pontinhos no canto superior direito
GROUP_SETTINGS_XPATH = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div/div"

# Lista de mensagens dentro da div do chat, cada mensagem e' uma row, sendo assim quando usar esse widget precisa adicionar na string o /div[id_da_row]
GROUP_MESSAGES_LIST_BASE_XPATH = "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]"

# Depois de abrir as configuracoes do grupo. tem um botao que tem a opcao de "selecionar mensagens" do chat
SELECT_GROUP_MESSAGES_XPATH = "/html/body/div[1]/div/span[4]/div/ul/div/div/li[2]"

# Botao de encaminhar mensagens selecionadas quando esta selecionando as mensagens do grupo
FORWARD_MESSAGE_BUTTON_DURING_SELECT_MESSAGES = "/html/body/div[1]/div/div/div[4]/div/span[2]/div/button[4]/span"

# Barra de pesquisa dentro do modal de encaminhar mensagens
FORWARDMODAL_SEARCHBAR_INPUT_XPATH = "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]"

# Primeiro grupo que apareceu na lista apos a pesquisa na searchbar
FORWARDMODAL_FIRST_RESULT_AFTER_SEARCH_XPATH = "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/button"

# Botao de encaminhar dentro do modal de encaminhamento
FORWARDMODAL_SUBMIT_GROUPS_SELECTED = "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/span/div/div"