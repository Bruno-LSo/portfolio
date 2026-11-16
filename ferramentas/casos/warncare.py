import modelo as M

SLUG = "warncare"

_SVG = (
    '<svg viewBox="0 0 960 350" role="img" aria-label="Arquitetura do WarnCare: app Flutter, Firebase, função na nuvem, Cloud Vision e Gemini">'
    '<defs><marker id="warncare-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker>'
    '<marker id="warncare-seta2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0 0 L10 5 L0 10z" fill="#FFD25E"/></marker></defs>'
    # app
    '<rect x="20" y="125" width="180" height="90" rx="12" fill="#162A37" stroke="#4FD1D4" stroke-width="2"/>'
    '<text x="110" y="162" fill="#EAF1F6" font-family="Sora" font-size="16" text-anchor="middle">App Flutter</text>'
    '<text x="110" y="186" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">BLoC · go_router</text>'
    # firebase
    '<rect x="290" y="20" width="210" height="70" rx="12" fill="#162A37" stroke="#4FB3E8"/>'
    '<text x="395" y="50" fill="#EAF1F6" font-family="Sora" font-size="15" text-anchor="middle">Firebase Auth</text>'
    '<text x="395" y="72" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">e-mail ou Google</text>'
    '<rect x="290" y="135" width="210" height="70" rx="12" fill="#162A37" stroke="#4FB3E8"/>'
    '<text x="395" y="165" fill="#EAF1F6" font-family="Sora" font-size="15" text-anchor="middle">Storage</text>'
    '<text x="395" y="187" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">foto da receita</text>'
    '<rect x="290" y="250" width="210" height="70" rx="12" fill="#162A37" stroke="#4FB3E8"/>'
    '<text x="395" y="280" fill="#EAF1F6" font-family="Sora" font-size="15" text-anchor="middle">Firestore</text>'
    '<text x="395" y="302" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">receitas, logs, medicamentos</text>'
    # função
    '<rect x="580" y="135" width="180" height="70" rx="12" fill="#162A37" stroke="#5CC98A"/>'
    '<text x="670" y="165" fill="#EAF1F6" font-family="Sora" font-size="15" text-anchor="middle">processReceipt</text>'
    '<text x="670" y="187" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">Cloud Function</text>'
    # IA
    '<rect x="810" y="60" width="135" height="70" rx="12" fill="#162A37" stroke="#F08A7E"/>'
    '<text x="877" y="90" fill="#EAF1F6" font-family="Sora" font-size="15" text-anchor="middle">Cloud Vision</text>'
    '<text x="877" y="112" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">texto da foto</text>'
    '<rect x="810" y="210" width="135" height="70" rx="12" fill="#162A37" stroke="#F08A7E"/>'
    '<text x="877" y="240" fill="#EAF1F6" font-family="Sora" font-size="15" text-anchor="middle">Gemini</text>'
    '<text x="877" y="262" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">texto em JSON</text>'
    # setas
    '<path d="M200 150 L288 60" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#warncare-seta)"/>'
    '<path d="M200 170 H288" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#warncare-seta)"/>'
    '<path d="M200 190 L288 280" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#warncare-seta)"/>'
    '<path d="M500 170 H578" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#warncare-seta)"/>'
    '<text x="539" y="160" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">URL</text>'
    '<path d="M760 155 L808 105" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#warncare-seta)"/>'
    '<path d="M760 185 L808 235" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#warncare-seta)"/>'
    '<path d="M670 205 V338 H110 V217" stroke="#FFD25E" stroke-width="2" stroke-dasharray="6 5" fill="none" marker-end="url(#warncare-seta2)"/>'
    '<text x="560" y="325" fill="#FFD25E" font-family="Sora" font-size="13" text-anchor="middle">medicamentos para conferência</text>'
    '</svg>'
)

CASO = dict(
    numeros=[("10", "telas com rota no app"), ("2", "funções na nuvem: receita e embalagem"),
             ("7", "campos lidos por medicamento"), ("4", "faixas de estoque")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-login.webp", "Entrada por e-mail e senha ou conta Google. Dados fictícios."),
            ("02-inicio.webp", "Início: totais de medicamentos e receitas, ações rápidas e receitas recentes. Dados fictícios."),
            ("03-nova-receita.webp", "Nova receita: foto pela câmera ou imagem da galeria. Dados fictícios."),
            ("04-confirmar.webp", "Conferência dos campos lidos pela IA antes de salvar. Dados fictícios."),
            ("05-receitas.webp", "Lista de receitas; arrastar para o lado exclui, com confirmação. Dados fictícios."),
            ("06-detalhe.webp", "Detalhe da receita, com edição e histórico de alterações. Dados fictícios."),
            ("07-medicamentos.webp", "Estoque de cada remédio, dias restantes e faixa de situação. Dados fictícios."),
            ("08-adicionar.webp", "Cadastro do estoque em 3 passos: receita, remédio, quantidade e horários. Dados fictícios."),
        ], celular=True), "Telas reproduzidas a partir do código Dart do app: mesmo layout, cores e textos.", "larga"),
        ("Fluxo de navegação", M.fluxograma([
            ("Abertura", [("Splash", "2 segundos")], "com sessão vai ao início; sem sessão, ao login"),
            ("Acesso", [("Login", "e-mail ou Google"), ("Cadastro", "nome, e-mail, telefone e senha")]),
            ("Início", [("Painel", "medicamentos, receitas e doses de hoje")], "ações rápidas"),
            ("Áreas", [("Nova receita", "câmera ou galeria"), ("Minhas receitas", "lista e exclusão"),
                       ("Meus medicamentos", "estoque e compras")]),
            ("Detalhe", [("Confirmar receita", "revisão dos campos"), ("Detalhes da receita", "edição com histórico"),
                         ("Adicionar medicamento", "receita, remédio e estoque")]),
        ], "Rota sem sessão volta ao login. Rota de login com sessão vai ao início."), "", "larga"),
        ("Leitura da receita", M.fluxograma([
            ("Foto", [("Câmera ou galeria", "qualidade 85, até 1.920 px")], "envio"),
            ("Storage", [("Pasta do usuário", "users/{uid}/prescriptions")], "URL da imagem"),
            ("Texto", [("Cloud Vision", "documentTextDetection")]),
            ("Estrutura", [("Gemini 1.5 Flash", "nome, dose, comprimidos, frequência, horários, duração, instruções")], "JSON"),
            ("Conferência", [("Confirmar receita", "nome e dose obrigatórios; incluir ou excluir remédio")], "Salvar receita"),
            ("Cadastro", [("Firestore", "users/{uid}/prescriptions")]),
        ], "A função exige usuário autenticado e tem limite de 120 segundos e 512 MB. Sem resposta da função, o app abre a conferência com dados de exemplo."), "", "larga"),
        ("Funcionalidades", M.lista([
            ("Acesso", "E-mail e senha com no mínimo 6 caracteres, ou conta Google."),
            ("Leitura por foto", "A Vision lê o texto da receita. O Gemini devolve os campos de cada remédio."),
            ("Conferência", "O usuário corrige, inclui ou exclui remédios antes de salvar."),
            ("Histórico", "Cada edição grava o valor anterior e o novo de cada campo."),
            ("Estoque", "Quantidade, doses por dia e horários. O botão Registrar compra soma ao estoque."),
            ("Exclusão", "Arrastar a receita para o lado pede confirmação e exclui."),
        ])),
        ("Estoque", M.colunas(
            M.texto(["Dias restantes = estoque dividido pelas doses por dia, arredondado para baixo.",
                     "Exemplo: 10 comprimidos e 2 doses por dia dão 5 dias, faixa baixa."]),
            M.achados([("0 dias", "sem estoque"), ("1 a 3", "dias: crítico, em vermelho"),
                       ("4 a 7", "dias: baixo, em amarelo"), ("8 ou mais", "dias: estoque ok, em verde")]),
        )),
        ("Arquitetura", M.diagrama(_SVG, "O app grava a foto no Storage e chama a função. A função lê o texto com a Vision, estrutura com o Gemini e devolve os medicamentos para conferência."), "", "larga"),
        ("Situação", M.texto([
            "Protótipo: 29 de 80 arquivos Dart têm código. As 10 telas acima funcionam.",
            "A função de leitura da embalagem está pronta (nome, dose, comprimidos e fabricante), sem tela no app.",
            "Notificações, perfil e preferências têm rota declarada e arquivo vazio.",
        ])),
    ],
)
