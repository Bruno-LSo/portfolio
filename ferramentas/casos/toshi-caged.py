"""Caso detalhado: Extrator do Novo CAGED (Toshi CAGED)."""
import modelo as M

SLUG = "toshi-caged"

_SVG = (
    '<svg viewBox="0 0 960 260" role="img" aria-label="Ajuste oficial do CAGED">'
    '<defs><marker id="tc-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
    '<g font-family="Sora" font-size="14" fill="#EAF1F6" text-anchor="middle">'
    '<rect x="20" y="20" width="220" height="62" rx="10" fill="#162A37" stroke="#5CC98A"/>'
    '<text x="130" y="47">CAGEDMOV</text><text x="130" y="68" fill="#A9B8C6" font-size="13">declarado no prazo</text>'
    '<rect x="20" y="99" width="220" height="62" rx="10" fill="#162A37" stroke="#5CC98A"/>'
    '<text x="130" y="126">CAGEDFOR</text><text x="130" y="147" fill="#A9B8C6" font-size="13">declarado fora do prazo</text>'
    '<rect x="20" y="178" width="220" height="62" rx="10" fill="#162A37" stroke="#F08A7E"/>'
    '<text x="130" y="205">CAGEDEXC</text><text x="130" y="226" fill="#A9B8C6" font-size="13">exclusões</text>'
    '<circle cx="320" cy="51" r="16" fill="#162A37" stroke="#5CC98A"/><text x="320" y="56" font-family="JetBrains Mono" font-size="16">+</text>'
    '<circle cx="320" cy="130" r="16" fill="#162A37" stroke="#5CC98A"/><text x="320" y="135" font-family="JetBrains Mono" font-size="16">+</text>'
    '<circle cx="320" cy="209" r="16" fill="#162A37" stroke="#F08A7E"/><text x="320" y="214" font-family="JetBrains Mono" font-size="16">-</text>'
    '<rect x="420" y="70" width="230" height="120" rx="12" fill="#162A37" stroke="#4FD1D4"/>'
    '<text x="535" y="104">Tabulação em blocos</text>'
    '<text x="535" y="130" fill="#A9B8C6" font-size="13">mês x UF x dimensão x código</text>'
    '<text x="535" y="154" fill="#A9B8C6" font-size="13">admissões, desligamentos,</text>'
    '<text x="535" y="174" fill="#A9B8C6" font-size="13">massa salarial</text>'
    '<rect x="730" y="30" width="210" height="62" rx="10" fill="#162A37" stroke="#FFD25E"/>'
    '<text x="835" y="57">Parquet por mês</text><text x="835" y="78" fill="#A9B8C6" font-size="13">cache para reprocessar</text>'
    '<rect x="730" y="168" width="210" height="62" rx="10" fill="#162A37" stroke="#FFD25E"/>'
    '<text x="835" y="195">CSV e painel HTML</text><text x="835" y="216" fill="#A9B8C6" font-size="13">com dicionários aplicados</text>'
    '</g>'
    '<g stroke="#4FD1D4" stroke-width="2" fill="none">'
    '<path d="M240 51 H304"/><path d="M240 130 H304"/><path d="M240 209 H304"/>'
    '<path d="M336 51 H370 V130 H416" marker-end="url(#tc-seta)"/><path d="M336 130 H370"/><path d="M336 209 H370 V130"/>'
    '<path d="M650 110 H690 V61 H726" marker-end="url(#tc-seta)"/><path d="M650 150 H690 V199 H726" marker-end="url(#tc-seta)"/>'
    '</g></svg>')

CASO = dict(
    lead="Ferramenta de linha de comando que baixa os microdados do Novo CAGED do servidor do Ministério do Trabalho, "
         "aplica o ajuste oficial, traduz os códigos e entrega um CSV único e um painel HTML que funciona sem internet.",
    numeros=[("40.604.909", "admissões de jan/2025 a jun/2026"), ("+2.193.193", "saldo de empregos formais no período"),
             ("22", "dimensões tabuladas"), ("18", "meses no painel publicado")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-painel.webp", "Abertura: totais do período e tabela por ocupação (CBO de 6 dígitos), ordenada por admissões."),
            ("02-setores.webp", "Mesma tabela por seção da CNAE: comércio lidera em admissões (9.425.349)."),
            ("03-municipios-go.webp", "Recorte por município em Goiás: saldo de +89.687 empregos no estado."),
            ("04-detalhe-mes.webp", "Unidade da Federação detalhada por mês, com São Paulo no topo."),
            ("05-celular.webp", "Versão de celular: cartões em duas colunas e filtros empilhados."),
        ]), "Capturas do painel publicado.", "larga"),
        ("Fluxo de uso do painel", M.fluxograma([
            ("Entrada", [("Página única", "totais do período no topo")]),
            ("Filtros", [("O que exibir", "região, UF, município, CNAE, CBO, sexo, instrução e outras"),
                         ("Mês", "um mês ou os 18"), ("Território", "Brasil ou uma UF"), ("Busca", "texto livre em todas as categorias")], "aplica"),
            ("Opções", [("Detalhar por mês", ""), ("Detalhar por UF", ""), ("Só saldo negativo", "")]),
            ("Saída", [("Tabela", "ordenável, cabeçalho fixo"), ("CSV", "exatamente o que está na tela")]),
        ]), "", "larga"),
        ("Processo de extração", M.fluxo([
            ("1", "Descoberta", "Lista no FTP do Ministério do Trabalho todas as competências publicadas."),
            ("2", "Download", "Baixa os arquivos .7z de cada mês, com retomada e até 4 tentativas por conexão."),
            ("3", "Dicionários", "Lê o layout oficial em Excel e completa município e CNAE pelas APIs do IBGE."),
            ("4", "Tabulação", "Lê o texto em blocos, aplica o ajuste oficial e agrega as 22 dimensões."),
            ("5", "Saída", "Grava o CSV com código e descrição e o HTML com os dados embutidos e compactados."),
        ])),
        ("Ajuste oficial", M.diagrama(_SVG, "O saldo de cada mês soma as declarações no prazo e fora do prazo e desconta as exclusões, como na estatística oficial."), "", "larga"),
        ("Saldo por região", M.barras([("Sudeste", 943044, True), ("Nordeste", 480882), ("Sul", 358119),
                                       ("Centro-Oeste", 270644), ("Norte", 137938)],
                                      titulo="Saldo de empregos formais, jan/2025 a jun/2026", casas=0,
                                      nota="Saldo = admissões menos desligamentos. Fonte: painel publicado.")),
        ("Salário médio de admissão por setor", M.barras([
            ("Atividades financeiras", 4787.23), ("Informação e comunicação", 4056.83), ("Eletricidade e gás", 3977.25),
            ("Indústrias extrativas", 3693.07), ("Construção", 2498.11), ("Média geral", 2314.02, True),
            ("Comércio", 2051.83), ("Alojamento e alimentação", 1924.51)],
            titulo="R$ por mês, jan/2025 a jun/2026", casas=2,
            nota="Salários fora da faixa de R$ 100 a R$ 300.000 ficam fora da média.")),
        ("Opções da linha de comando", M.lista([
            ("--meses N", "Últimos N meses publicados."),
            ("--desde e --ate", "Janela por competência, no formato AAAAMM."),
            ("--todos", "Série completa desde jan/2020."),
            ("--offline e --so-saida", "Regera o CSV e o HTML a partir do cache, sem acessar a rede."),
        ])),
        ("Privacidade", M.texto(["Os microdados do CAGED não identificam a pessoa nem a empresa: não têm CPF, nome, CNPJ ou razão social. "
                                 "O painel guarda só totais por mês, UF e categoria."])),
    ],
    stack=["Python", "pandas", "pyarrow", "py7zr", "FTP do Ministério do Trabalho", "API do IBGE", "HTML e JavaScript"],
)
