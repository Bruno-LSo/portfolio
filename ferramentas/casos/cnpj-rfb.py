"""Caso novo: carga dos dados abertos de CNPJ da Receita Federal."""
import modelo as M

SLUG = "cnpj-rfb"

_F = 'font-family="Sora" font-size="14" fill="#EAF1F6" text-anchor="middle"'


def _cx(x, y, w, h, cor, t1, t2=""):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#162A37" stroke="{cor}"/>'
    if t2:
        s += f'<text x="{x + w / 2}" y="{y + h / 2 - 4}">{t1}</text><text x="{x + w / 2}" y="{y + h / 2 + 16}" fill="#A9B8C6" font-size="13">{t2}</text>'
    else:
        s += f'<text x="{x + w / 2}" y="{y + h / 2 + 5}">{t1}</text>'
    return s


_TAB = [("Empresas", "#4FB3E8"), ("Estabelecimentos", "#4FB3E8"), ("Simples", "#4FB3E8"),
        ("CNAE", "#A9B8C6"), ("Municípios", "#A9B8C6"), ("Naturezas", "#A9B8C6")]

_SVG = (f'<svg viewBox="0 0 960 360" role="img" aria-label="Tabelas e junção">'
        '<defs><marker id="rfb-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
        f'<g {_F}>'
        + "".join(_cx(20, 16 + i * 56, 220, 44, c, t) for i, (t, c) in enumerate(_TAB))
        + _cx(330, 110, 260, 130, "#4FD1D4", "Tabelas temporárias", "índices por CNPJ básico")
        + '<text x="460" y="214" fill="#A9B8C6" font-size="13">e por código de domínio</text>'
        + _cx(680, 110, 260, 130, "#5CC98A", "cadastro_pj_AAAAMM", "um estabelecimento por linha")
        + '<text x="810" y="214" fill="#A9B8C6" font-size="13">lotes de 100.000</text>'
        + '<text x="810" y="300" fill="#A9B8C6" font-size="13">Azul: dados. Cinza: domínios.</text>'
        + '</g><g stroke="#4FD1D4" stroke-width="2" fill="none">'
        + "".join(f'<path d="M240 {38 + i * 56} H285 V175"/>' for i in range(6))
        + '<path d="M285 175 H326" marker-end="url(#rfb-seta)"/>'
        '<path d="M590 175 H676" marker-end="url(#rfb-seta)"/>'
        '</g><text x="633" y="165" font-family="Sora" font-size="13" fill="#A9B8C6" text-anchor="middle">junção</text></svg>')

CASO = dict(
    nome="Carga dos dados abertos de CNPJ",
    resumo="Baixa o cadastro aberto de CNPJ da Receita Federal e monta uma tabela única num PostgreSQL, com retomada após queda.",
    tec="Python · PostgreSQL · Receita Federal",
    area="dados",
    lead="Ferramenta que baixa o cadastro aberto de CNPJ publicado todo mês pela Receita Federal, extrai os arquivos e carrega tudo num PostgreSQL. "
         "Depois junta as tabelas numa tabela única por mês, usada pela fiscalização do Crea-SP para cruzar empresas e registros.",
    ficha=[("Instituição", "Crea-SP"), ("Fonte", "Dados abertos de CNPJ da Receita Federal"), ("Banco", "PostgreSQL"),
           ("Volume", "cerca de 30 GB por mês de referência")],
    numeros=[("10", "tipos de arquivo carregados"), ("100.000", "linhas por bloco de carga"), ("1", "tabela final por mês"),
             ("2", "versões: com banco e só download")],
    blocos=[
        ("Fluxo da carga", M.fluxograma([
            ("Origem", [("Portal da Receita Federal", "uma pasta por mês de referência")]),
            ("Escolha", [("Mês", "lista os meses publicados"), ("UF", "opcional, filtra estabelecimentos")], "pergunta ao usuário"),
            ("Arquivos", [("Download", "zip, com barra de progresso"), ("Extração", "CSV renomeado por tipo")]),
            ("Banco", [("Carga", "COPY em blocos de 100.000 linhas"), ("Checkpoint", "arquivo e bloco já gravados")], "retoma do ponto"),
            ("Saída", [("cadastro_pj_AAAAMM", "tabela final"), ("Relatório", "linhas por tabela e erros")]),
        ]), "", "larga"),
        ("Junção das tabelas", M.diagrama(_SVG, "Quatro arquivos de dados e seis de domínio viram uma tabela com as descrições já aplicadas. A figura mostra seis dos dez."), "", "larga"),
        ("Tolerância a falhas", M.lista([
            ("Checkpoint", "Um arquivo JSON registra downloads, extrações e o último bloco carregado de cada CSV."),
            ("Nova tentativa", "Queda de rede ou de banco espera a volta da conexão e repete a operação."),
            ("Sem duplicata", "Cada bloco entra numa transação; um bloco incompleto é desfeito e carregado de novo."),
            ("Controle de lotes", "A montagem da tabela final grava cada intervalo de linhas processado numa tabela de controle."),
        ])),
        ("Uso", M.texto(["A tabela final permite filtrar empresas ativas por UF, município e CNAE e cruzar com as empresas registradas no Crea-SP. "
                         "O cruzamento é usado para priorizar a fiscalização e alimenta, de forma agregada, o painel de emprego formal na engenharia.",
                         "A versão só de download é pública no GitHub e serve a quem quer os arquivos sem montar o banco."])),
        ("Documentação", M.lista([
            ("Dicionário de dados", "Layout de todas as tabelas e domínios, conferido na fonte em 20/10/2025."),
            ("SQL de exemplo", "Consulta de unificação para PostgreSQL, SQL Server e MySQL."),
        ])),
    ],
    stack=["Python", "requests", "BeautifulSoup", "PostgreSQL", "psycopg2", "SQLAlchemy", "tqdm"],
    link=("Ver o código público", "https://github.com/Bruno-LSo/RFB-Scraping-Local"),
)
