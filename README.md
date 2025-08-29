Email-Classifier: Classificador e Priorizador de E-mails com IA
Aplicação web desenvolvida como parte de um desafio técnico para um processo seletivo de estágio. A ferramenta utiliza Inteligência Artificial para analisar o conteúdo de e-mails em formato PDF, classificá-los como "Produtivo" ou "Improdutivo" e exibi-los em uma fila priorizada.

🚀 Link da Aplicação
Você pode acessar e testar a aplicação online no seguinte link:

https://email-classifier-desafio.onrender.com ---

✨ Funcionalidades
Interface Web Intuitiva: Design limpo e moderno para uma experiência de usuário agradável.

Upload de Múltiplos Arquivos: Permite o envio de vários e-mails em formato PDF simultaneamente.

Área de Preparação (Staging): Visualiza os arquivos anexados antes do envio, com a opção de remover arquivos individualmente.

Extração Automática de Texto: Utiliza a biblioteca PyMuPDF para ler e extrair o conteúdo textual de cada PDF.

Classificação com IA: Integra-se com a API de Inferência da Hugging Face para classificar o texto dos e-mails.

Fila Priorizada: Exibe os resultados em uma lista ordenada, com os e-mails classificados como "Produtivo" no topo para facilitar a tomada de ação.

🛠️ Tecnologias Utilizadas
Este projeto foi construído com as seguintes tecnologias e ferramentas:

Backend:

Python

Flask (Micro-framework web)

Gunicorn (Servidor WSGI para produção)

Inteligência Artificial:

API de Inferência da Hugging Face

Modelo de Zero-Shot Classification: valhalla/distilbart-mnli-12-3

Processamento de Arquivos:

PyMuPDF (para extração de texto de PDFs)

Frontend:

HTML5

CSS3

JavaScript (puro, com Fetch API para requisições assíncronas)

Deploy (Hospedagem):

Render.com

Versionamento:

Git & GitHub

⚙️ Como Executar o Projeto Localmente
Para executar esta aplicação na sua máquina, siga os passos abaixo.

Pré-requisitos
Python 3.8+

Git

Passo a Passo
Clone o repositório:

Bash

git clone https://github.com/Madjhonny/email-classifier.git
Navegue até a pasta do projeto:

Bash

cd email-classifier
Crie e ative um ambiente virtual:

No Windows:

Bash

python -m venv .venv
.\.venv\Scripts\activate
No macOS/Linux:

Bash

python3 -m venv .venv
source .venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Configure as variáveis de ambiente:

Crie um arquivo chamado .env na raiz do projeto.

Dentro dele, adicione sua chave da API da Hugging Face no seguinte formato:

HF_API_KEY="hf_SuaChaveSecretaAqui"
Execute a aplicação:

Bash

flask run
Acesse no navegador:

Abra seu navegador e acesse http://127.0.0.1:5000
