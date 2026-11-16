"""Caso detalhado: Vibe Coding Toolkit (repositórios vibe-toolkit, Vibe-Coding-Toolkit e AiAmmo)."""
import modelo as M

SLUG = "vibe-toolkit"

ARVORE = """<pre style="margin:0;white-space:pre;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.5;overflow-x:auto">loja-exemplo/
├─ backend/
│  ├─ src/
│  │  ├─ routes/
│  │  │  ├─ pedidos.js
│  │  │  └─ produtos.js
│  │  ├─ app.js
│  │  └─ db.js
│  └─ package.json
├─ frontend/
│  ├─ src/
│  │  ├─ Carrinho.jsx
│  │  ├─ Catalogo.jsx
│  │  └─ main.jsx
│  └─ index.html
├─ notebooks/
│  └─ vendas.ipynb
├─ .gitignore
└─ README.md</pre>"""

CASO = dict(
    nome="Vibe Coding Toolkit",
    resumo="Programa que junta a estrutura e o código de um projeto em dois arquivos para colar num chat com IA.",
    tec="Python · tkinter",
    area="produtos",
    lead="Programa de computador que recebe uma pasta de projeto e gera dois arquivos: a árvore de pastas e o conteúdo de todos os arquivos. Os dois servem de contexto completo para um chat com IA. Respeita o .gitignore e limpa notebooks Jupyter.",
    ficha=[("Tipo", "Ferramenta própria, versão pública no GitHub"), ("Interface", "tkinter"),
           ("Saída", "NomeArquitetura.bash e NomeConteudo.txt"), ("Arquivos do projeto", "Somente leitura")],
    numeros=[("2", "arquivos gerados por pasta"), ("3", "repositórios: AiAmmo, Vibe-Coding-Toolkit e vibe-toolkit"), ("5", "versões do toolkit, de março a novembro de 2025")],
    blocos=[
        ("Tela", M.telas(SLUG, [("01-janela.webp", "Janela principal: árvore do projeto com a coluna Ignorar. Marcar uma pasta marca tudo dentro dela. Dados fictícios.")]),
         "Tela reproduzida a partir do código da interface (mesmos textos e disposição).", "larga"),
        ("Processo", M.fluxograma([
            ("Escolha", [("Selecionar Diretório", "projeto inteiro"), ("Selecionar Arquivo", "um arquivo só")]),
            ("Árvore", [("Marcar o que ignorar", "pasta marcada leva os filhos junto")]),
            ("Perguntas", [("Remover __pycache__?", "se houver"), ("Usar o .gitignore?", "se houver")], "executar"),
            ("Geração", [("Arquitetura.bash", "árvore com ├─ e └─"), ("Conteudo.txt", "caminho e conteúdo de cada arquivo, separados por linha de /")]),
            ("Limpeza", [("Notebooks .ipynb", "mantém células e saída de texto"), ("Imagens em base64", "trocadas por uma descrição curta")]),
        ]), "", "larga"),
        ("Saída", M.colunas(
            M.painel("loja-exemploArquitetura.bash", ARVORE, "Árvore gerada para o projeto da tela. As pastas marcadas não aparecem. Dados fictícios."),
            M.lista([
                ("Contexto inteiro", "Os dois arquivos vão juntos para o chat. A IA vê a estrutura e o código de uma vez."),
                ("Nada é alterado", "O programa só lê o projeto e grava os 2 arquivos novos."),
                ("Notebook limpo", "Saídas em imagem e blocos de metadados saem, para caber no limite do chat."),
                ("Arquivo único", "Também extrai o conteúdo de um arquivo só, sem a árvore."),
            ]))),
        ("Versões", M.fluxo([
            ("fev. 2025", "AiAmmo", "6 scripts: árvore e conteúdo, remoção de imagem em base64 e a primeira interface com a coluna Ignorar."),
            ("mar. 2025", "Vibe-Coding-Toolkit", "Versão 1, pública no GitHub, com README e instruções de uso."),
            ("mai. a nov. 2025", "vibe-toolkit", "Versões 2 a 5: leitura do .gitignore, remoção de __pycache__ e limpeza de notebooks."),
        ])),
    ],
    stack=["Python", "tkinter", "fnmatch", "json"],
)
