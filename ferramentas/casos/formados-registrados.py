"""Ingressantes, concluintes e registrados (repositório confea-inep-sic; página pública InepCNF)."""
import modelo as M

SLUG = "formados-registrados"


def _funil():
    itens = [(100, "ingressantes", "#FFD25E"), (38, "concluem em até 6 anos", "#4FB3E8"), (17, "registram-se no Sistema", "#5CC98A")]
    p = ['<svg viewBox="0 0 960 250" role="img" aria-label="De cada 100 ingressantes, 38 concluem e 17 se registram">']
    for i, (v, rot, cor) in enumerate(itens):
        w = 7.2 * v
        y = 20 + i * 76
        x = 260
        p.append(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="56" rx="8" fill="{cor}" opacity="0.9"/>')
        p.append(f'<text x="{x - 16}" y="{y + 37}" fill="#EAF1F6" font-family="JetBrains Mono" font-size="26" font-weight="700" text-anchor="end">{v}</text>')
        tx = x + w + 14 if v < 60 else x + 16
        cor_t = "#EAF1F6" if v < 60 else "#162A37"
        p.append(f'<text x="{tx:.0f}" y="{y + 35}" fill="{cor_t}" font-family="Sora" font-size="16">{rot}</text>')
    p.append("</svg>")
    return "".join(p)


CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-brasil.webp", "Brasil: série de 2010 a 2024 e totais do período."),
            ("02-regiao.webp", "Região Sudeste selecionada: os estados da região ficam em destaque."),
            ("03-estado.webp", "São Paulo: totais comparados com a região e com o Brasil, em percentual."),
        ]), "Capturas da página pública.", "larga"),

        ("Fluxo de páginas", M.fluxograma([
            ("Entrada", [("Brasil", "série e totais nacionais")], "escolhe o recorte"),
            ("Filtros", [("Região", "5 botões"), ("Estado", "27 botões"), ("Unidade", "em milhares ou absoluto")], "atualiza"),
            ("Saída", [("Gráfico", "3 séries, 2010 a 2024"), ("Cartões", "de cada 100 ingressantes"),
                       ("Tabela", "estado, região e Brasil"), ("Imagem", "cópia do painel")]),
        ]), "", "larga"),

        ("Série", M.painel("", '<div id="leg" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px"></div><div id="g-serie"></div>', "Brasil, 2010 e 2024.")),

        ("Fluxo do processo", M.fluxograma([
            ("Coleta", [("Portal de dados abertos do INEP", "microdados por ano, raspagem com BeautifulSoup")], "homologa os arquivos"),
            ("Recorte", [("Cursos de engenharia", "filtro por código CINE")], "agrega por ano e UF"),
            ("Cruzamento", [("Registros profissionais", "consultas por ano, Crea, gênero e modalidade")], "calcula"),
            ("Indicador", [("Conclusão e registro", "por 100 ingressantes, defasagem de 6 anos")], "publica"),
            ("Saída", [("Painel web", "Plotly"), ("Excel", "mesmos dados")]),
        ]), "", "larga"),

        ("De cada 100 ingressantes", M.diagrama(_funil(), "Brasil. Os registrados são 45% dos concluintes."), "", "larga"),

        ("Correção da consulta", M.texto([
            "A primeira versão usava a primeira ativação no histórico como data de ingresso.",
            "O histórico só começou entre 2005 e 2007, e isso inflava os ingressos de 2010 em cerca de 24%.",
            "A consulta passou a usar a data do primeiro registro do cadastro. Em 97,2% dos casos com várias ativações (163.038 de 167.730), essa data fica mais perto da primeira ativação.",
        ])),

        ("Achados", M.achados([
            ("5.055.431", "ingressantes em engenharia de 2010 a 2024"),
            ("1.942.988", "concluintes no mesmo período"),
            ("903.681", "novos registros profissionais"),
            ("-56%", "ingressantes de 2014 para 2024 (503 mil para 219 mil)"),
            ("28,1%", "dos ingressantes do Brasil estão em SP (1.421.589)"),
            ("50,8%", "dos novos registros são do Sudeste (459.136)"),
        ])),
    ],
)
