"""Partes comuns das páginas de caso: topo, rodapé e blocos."""
from html import escape

TOPO = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo_aba} · Bruno Lima</title>
<meta name="description" content="{descricao}">
<meta name="theme-color" content="#0B1820">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/css/portfolio.css">
<style>:root{{--acento:{acento}}}{css}</style>
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo"><div class="topo__in">
  <a class="marca" href="../index.html"><img src="../assets/img/logo-negativo.svg" alt="HoldUp" width="132" height="38"><span>Portfólio · Bruno Lima</span></a>
  <nav class="nav" aria-label="Seções"><a href="../index.html#areas">Áreas</a><a href="../index.html#casos">Casos</a><a href="../index.html#projetos">Todos os projetos</a><a href="../index.html#contato">Contato</a></nav>
  <a class="btn btn--mini btn--linha" href="../index.html#projetos">Ver todos</a>
</div></header>
"""

RODAPE = """
<footer class="rodape"><div class="wrap rodape__in">
  <img src="../assets/img/logo-negativo.svg" alt="HoldUp" width="104" height="30">
  <p>Bruno Lima · <a href="https://holdupsolucoes.com.br/">holdupsolucoes.com.br</a> · <a href="https://github.com/Bruno-LSo">github.com/Bruno-LSo</a></p>
</div></footer>

<script src="../assets/js/graficos.js"></script>
<script src="../assets/js/projetos.js"></script>
<script src="../assets/js/mosaico.js"></script>
{script}
</body>
</html>
"""


def hero(c, area_nome, area_id):
    ficha = "".join(f'<div><dt>{escape(k)}</dt><dd>{v}</dd></div>' for k, v in c["ficha"])
    return f"""<main id="conteudo">
<section class="caso-hero"><div class="wrap">
  <p class="migalha entra"><a href="../index.html">Portfólio</a><span aria-hidden="true">/</span><a href="../index.html#area-{area_id}">{area_nome}</a></p>
  <h1 class="entra" style="--o:1">{c['h1']}</h1>
  <p class="lead entra" style="--o:2">{c['lead']}</p>
  <dl class="ficha entra" style="--o:3">{ficha}</dl>
</div></section>
"""


def kpis(lista):
    itens = "".join(
        f'<div class="kpi"><strong class="num">{v}</strong><span>{t}</span>{f"<small>{n}</small>" if n else ""}</div>'
        for v, t, *resto in lista for n in [resto[0] if resto else ""]
    )
    return f'<section class="bloco"><div class="wrap"><div class="kpis revela">{itens}</div></div></section>\n'


def bloco(rotulo, titulo, texto, corpo):
    lado = f'<div><p class="rotulo"><i></i>{rotulo}</p><h2>{titulo}</h2>{f"<p>{texto}</p>" if texto else ""}</div>'
    return f'<section class="bloco"><div class="wrap bloco__grid">{lado}<div class="revela">{corpo}</div></div></section>\n'


def lista(itens):
    return '<ul class="lista">' + "".join(f"<li><strong>{t}</strong>{d}</li>" for t, d in itens) + "</ul>"


def fluxo(itens, nota=""):
    corpo = '<div class="fluxo">' + "".join(f"<div><b>{b}</b><h4>{h}</h4><p>{p}</p></div>" for b, h, p in itens) + "</div>"
    return corpo + (f'<p class="nota">{nota}</p>' if nota else "")


def texto(paragrafos):
    return '<div class="texto">' + "".join(f"<p>{p}</p>" for p in paragrafos) + "</div>"


def painel(barra, interno, nota=""):
    n = f'<p class="nota">{nota}</p>' if nota else ""
    b = f'<div class="painel__barra"><i></i><i></i><i></i><span>{barra}</span></div>' if barra else ""
    return f'<div class="painel">{b}<div class="painel__corpo">{interno}{n}</div></div>'


def stack(itens):
    s = "".join(f"<span>{i}</span>" for i in itens)
    return f'<section class="bloco"><div class="wrap"><p class="rotulo"><i></i>Tecnologias</p><div class="stack" style="margin-top:16px">{s}</div></div></section>\n'


def proximos(slug):
    return f'<section class="bloco"><div class="wrap"><p class="rotulo"><i></i>Continue vendo</p><div class="proximos" style="margin-top:20px" data-proximos="{slug}"></div></div></section>\n</main>\n'
