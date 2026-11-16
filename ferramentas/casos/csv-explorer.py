import modelo as M

SLUG = "csv-explorer"

_m = ('<defs><marker id="csv-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>')


def _cx(x, y, w, t, s, cor="#4FD1D4"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="64" rx="10" fill="#162A37" stroke="{cor}"/>'
            f'<text x="{x + w / 2}" y="{y + 28}" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{t}</text>'
            f'<text x="{x + w / 2}" y="{y + 48}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{s}</text>')


def _ln(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#csv-s)"/>'


_svg = ('<svg viewBox="0 0 960 240" role="img" aria-label="Leitura em blocos: arquivo, worker, índice de posições e tabela virtual">' + _m
        + _cx(10, 20, 170, "Arquivo CSV", "fica no computador", "#4FB3E8")
        + _cx(230, 20, 200, "Web Worker", "blocos de 32 MB")
        + _cx(480, 20, 210, "Índice", "posição de cada linha", "#5CC98A")
        + _cx(740, 20, 210, "Tabela virtual", "lê só as linhas na tela", "#FFD25E")
        + _cx(480, 150, 210, "Filtro e ordem", "lista de linhas", "#5CC98A")
        + _cx(740, 150, 210, "Exportar", "grava em fluxo", "#FFD25E")
        + _ln(180, 52, 228, 52) + _ln(430, 52, 478, 52) + _ln(690, 52, 738, 52)
        + _ln(585, 84, 585, 148) + _ln(690, 182, 738, 182)
        + '<text x="330" y="140" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">a interface não trava:</text>'
        + '<text x="330" y="160" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">todo o trabalho pesado roda no worker</text>'
        + '</svg>')

CASO = dict(
    nome="CSV Explorer",
    area="dados",
    resumo="Leitor de arquivos CSV grandes no navegador, com filtro, ordenação, estatísticas e exportação.",
    tec="JavaScript · Web Worker · HTML",
    lead="Ferramenta de página única para abrir arquivos CSV de vários gigabytes no navegador. O arquivo não sai do computador. A ferramenta lê em blocos e guarda só a posição de cada linha.",
    ficha=[("Formato", "Página única, sem servidor"), ("Dados", "Ficam no computador do usuário"), ("Publicação", "GitHub Pages"), ("Ano", "2026")],
    numeros=[("400.000", "linhas no arquivo de teste (23 MB)"), ("3,05 MB", "de índice em memória para essas linhas"),
             ("0,5 s", "para filtrar 66.988 linhas"), ("14", "operadores de filtro")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-abrir.webp", "Tela inicial: escolher ou arrastar o arquivo."),
            ("02-tabela.webp", "Arquivo aberto: separador, codificação e decimal detectados; 400.000 linhas e 9 colunas."),
            ("03-estatisticas.webp", "Estatísticas de uma coluna: vazios, distintos, soma, média, desvio, quantis e valores mais frequentes."),
            ("04-filtro.webp", "Filtro por coluna: 66.988 de 400.000 linhas em 0,5 s."),
        ]), "Capturas da página publicada, com um arquivo de vendas fictício. Dados fictícios.", "larga"),
        ("Como lê o arquivo", M.diagrama(_svg, "O worker percorre o arquivo em blocos e anota onde cada linha começa. A tabela busca no arquivo só as linhas visíveis."), "", "larga"),
        ("Fluxo de uso", M.fluxograma([
            ("Abrir", [("Selecionar ou arrastar", "CSV, TXT ou TSV")]),
            ("Detectar", [("Separador", "| ; , ou tabulação"), ("Codificação", "UTF-8, Windows-1252, ISO-8859-1"), ("Decimal", "ponto ou vírgula")], "automático"),
            ("Explorar", [("Busca", "em todas as colunas"), ("Filtros", "E ou OU"), ("Ordenar", "clique no cabeçalho"), ("Estatísticas", "por coluna"), ("Ir para linha", "número")]),
            ("Exportar", [("Visão atual", "filtros, ordem e colunas visíveis")]),
        ]), "Os ajustes detectados podem ser trocados na barra superior; o botão Reprocessar relê o arquivo.", "larga"),
        ("Funcionalidades", M.lista([
            ("Filtros", "14 operadores: contém, igual, começa com, vazio, maior que, entre, expressão regular e outros."),
            ("Estatísticas", "Média, soma, mínimo e máximo exatos; quantis sobre amostra de até 100.000 valores."),
            ("Colunas", "Mostrar ou esconder colunas e ajustar a largura arrastando a borda."),
            ("Registro", "Painel com todos os campos de uma linha."),
            ("Exportação", "Quantidade de linhas e separador à escolha; grava direto em disco quando o navegador permite."),
            ("Cancelar", "Operações longas podem ser interrompidas."),
        ])),
    ],
    stack=["HTML", "CSS", "JavaScript", "Web Worker", "File System Access API", "GitHub Pages"],
    link=("Abrir o CSV Explorer", "https://bruno-lso.github.io/opencsv/"),
)
