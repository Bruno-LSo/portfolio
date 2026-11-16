"""Índice de Infraestrutura do Brasil (InfraBR): bases, ponderação, painel de acessos e o Desafio InfraBR."""
import modelo as M

SLUG = "infrabr"

_SVG = (
    '<svg viewBox="0 0 960 330" role="img" aria-label="Arquitetura do Desafio InfraBR">'
    '<defs><marker id="infrabr-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
    # jogo
    '<rect x="20" y="30" width="230" height="110" rx="12" fill="#162A37" stroke="#FFD25E"/>'
    '<text x="135" y="66" fill="#EAF1F6" font-family="Sora" font-size="16" text-anchor="middle">Jogo</text>'
    '<text x="135" y="92" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">celular do visitante</text>'
    '<text x="135" y="114" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">perguntas e propostas</text>'
    # admin
    '<rect x="20" y="190" width="230" height="110" rx="12" fill="#162A37" stroke="#F08A7E"/>'
    '<text x="135" y="226" fill="#EAF1F6" font-family="Sora" font-size="16" text-anchor="middle">Administração</text>'
    '<text x="135" y="252" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">login da equipe</text>'
    '<text x="135" y="274" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">perguntas, selos, moderação</text>'
    # supabase
    '<rect x="365" y="60" width="230" height="210" rx="12" fill="#162A37" stroke="#4FD1D4"/>'
    '<text x="480" y="96" fill="#EAF1F6" font-family="Sora" font-size="16" text-anchor="middle">Supabase</text>'
    '<text x="480" y="126" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">jogadores e respostas</text>'
    '<text x="480" y="150" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">perguntas por UF e eixo</text>'
    '<text x="480" y="174" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">propostas e selos</text>'
    '<text x="480" y="198" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">ranking (view)</text>'
    '<text x="480" y="232" fill="#4FD1D4" font-family="JetBrains Mono" font-size="13" text-anchor="middle">RLS por papel</text>'
    # painel
    '<rect x="710" y="105" width="230" height="120" rx="12" fill="#162A37" stroke="#5CC98A"/>'
    '<text x="825" y="141" fill="#EAF1F6" font-family="Sora" font-size="16" text-anchor="middle">Painel ao vivo</text>'
    '<text x="825" y="167" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">telão do estande</text>'
    '<text x="825" y="189" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">ranking e mural de ideias</text>'
    # setas
    '<path d="M250 85 H365" stroke="#4FD1D4" stroke-width="2" marker-end="url(#infrabr-s)"/>'
    '<text x="307" y="76" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">grava</text>'
    '<path d="M250 245 H365" stroke="#4FD1D4" stroke-width="2" marker-end="url(#infrabr-s)"/>'
    '<text x="307" y="236" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">edita</text>'
    '<path d="M595 165 H710" stroke="#4FD1D4" stroke-width="2" marker-end="url(#infrabr-s)"/>'
    '<text x="652" y="156" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">tempo real</text>'
    '</svg>')

CASO = dict(
    nome="Índice de Infraestrutura do Brasil (InfraBR)",
    resumo="Bases de dados, ponderação de indicadores, painel de acessos e jogo de perguntas sobre a infraestrutura de cada UF.",
    tec="Python · Supabase · D3.js · Plotly",
    area="campo",
    lead="Frentes de trabalho do InfraBR, o índice de infraestrutura do CONFEA: mapeamento das bases do Sistema CONFEA/CREA, tabelas de ponderação, painel de acessos do site e o Desafio InfraBR, jogo de perguntas usado em eventos.",
    ficha=[("Instituição", "CONFEA"), ("Eixos", "energia, mobilidade, água, saneamento, bem-estar e meio ambiente"),
           ("Eventos", "ENIC 2026 e SmartCity 2026"), ("Saída", "3 páginas do jogo, painel de acessos e planilhas")],
    numeros=[("6", "eixos do índice"), ("27", "UFs no mapa do jogo"), ("16", "selos pré-cadastrados"), ("4", "bancos mapeados")],
    blocos=[
        ("Desafio InfraBR", M.telas(SLUG, [
            ("01-entrada.webp", "Entrada: nome ou apelido, telefone e autorização para exibir o nome no ranking."),
            ("02-diagnostico.webp", "Escolha da UF no mapa, com o índice por eixo e o nível da rodada."),
            ("03-leitura.webp", "Fase de leitura: a pergunta aparece sozinha por 15 segundos."),
            ("04-resposta.webp", "Resposta: acerto, explicação e pontos da pergunta."),
            ("05-proposta.webp", "Proposta: o jogador escolhe o eixo e escreve até 400 caracteres."),
            ("06-resultado.webp", "Resultado da rodada: acertos, pontos e selos."),
            ("07-ranking.webp", "Ranking ao vivo. Quem não autoriza aparece como Anônimo."),
            ("08-painel.webp", "Painel do estande, versão SmartCity 2026: ranking, mural de ideias e faixa de propostas."),
        ]), "Capturas das páginas geradas, com o banco simulado. Perguntas, jogadores e propostas são fictícios. Os índices do mapa são ilustrativos.", "larga"),
        ("No celular", M.telas(SLUG, [("09-celular.webp", "Entrada do jogo no celular. Dados fictícios.")], celular=True)),
        ("Fluxo do jogo", M.fluxograma([
            ("01 Entrada", [("Identificação", "nome e telefone, sem senha"), ("Autorização", "nome no ranking público")]),
            ("02 Diagnóstico", [("UF", "mapa ou busca"), ("Índice", "geral e por eixo"), ("Nível", "fácil, médio ou difícil")]),
            ("03 Desafio", [("3 perguntas", "15 s de leitura e 20 s de resposta"), ("Pontos", "100 mais bônus de velocidade, vezes o nível")], "rodada"),
            ("04 Proposta", [("Eixo", "6 opções"), ("Texto", "até 400 caracteres ou pular")]),
            ("05 Resultado", [("Acertos e pontos", "da rodada e acumulados"), ("Selos", "regras configuráveis"), ("Ranking", "ao vivo")]),
        ], "Uma pergunta nunca aparece 3 vezes para o mesmo jogador. As alternativas são embaralhadas a cada rodada."), "", "larga"),
        ("Arquitetura", M.diagrama(_SVG, "Três páginas estáticas ligadas ao mesmo banco. O painel do estande recebe as mudanças em tempo real."), "", "larga"),
        ("Pontuação", M.barras([("Fácil", 1.0), ("Médio", 1.25), ("Difícil", 1.5, True)], titulo="Multiplicador por nível", casas=2,
                               nota="Acerto vale 100 pontos mais 1 ponto a cada 50 ms que sobram dos 20 s. O total é multiplicado pelo nível.")),
        ("Painel de acessos", M.telas(SLUG, [("10-analytics.webp", "Painel de acessos do site InfraBR, novembro de 2026: sessões, mapa por UF, evolução diária, páginas, dispositivos e canais.")]),
         "Dados agregados do Google Analytics 4, lidos por Apps Script. Atualização ao abrir e a cada 60 segundos.", "larga"),
        ("Outras frentes", M.lista([
            ("Mapeamento de bases", "Script que lista esquemas, tabelas e colunas de 4 bases do Sistema CONFEA/CREA: profissionais, passagens e diárias, registro único e ARTs."),
            ("Ponderação", "Peso por classe de indicador: A 1,8828%, B 1,4644%, C 1,0460% e D 0,6276%. A planilha soma os pesos por eixo e componente."),
            ("Tabelas de metodologia", "Conversão de 84 indicadores de redes em planilha, com uma aba por indicador e a tabela consolidada."),
            ("Versão SmartCity", "O mesmo gerador, com a marca CONFEA SmartCity 2026, serviu ao jogo Cidades Inteligentes."),
        ])),
        ("Administração", M.lista([
            ("Perguntas", "Cadastro por UF, eixo e nível, com 4 alternativas e explicação."),
            ("Selos", "16 selos pré-cadastrados, com 7 tipos de critério: acertos por eixo, acertos por região, todas as regiões, propostas, partidas, velocidade e pontos."),
            ("Moderação", "Exclusão de propostas e de jogadores, com atualização imediata no painel."),
        ])),
    ],
    stack=["Python", "Supabase", "PostgreSQL", "React", "D3.js", "Plotly", "Leaflet", "Google Apps Script", "GA4", "pandas", "openpyxl"],
)
