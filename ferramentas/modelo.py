"""Partes comuns das páginas: cabeçalho, rodapé, blocos e navegação."""
from html import escape

CABECA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · HoldUp</title>
<meta name="description" content="{descricao}">
<meta name="theme-color" content="#0B1820">
<link rel="icon" href="{raiz}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{raiz}favicon-32px.png" sizes="32x32">
<link rel="apple-touch-icon" href="{raiz}apple-touch-icon.png">
<link rel="stylesheet" href="{raiz}assets/css/portfolio.css">
<style>:root{{--acento:{acento}}}{css}</style>
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo"><div class="topo__in">
  <a class="marca" href="{raiz}index.html"><img src="{raiz}assets/img/logo-negativo.svg" alt="HoldUp" width="132" height="38"><span>Portfólio</span></a>
  <nav class="nav" aria-label="Áreas">{menu}</nav>
</div></header>
"""

RODAPE = """
<footer class="rodape"><div class="wrap rodape__in">
  <img src="{raiz}assets/img/logo-negativo.svg" alt="HoldUp" width="104" height="30">
  <p>HoldUp · <a href="https://holdupsolucoes.com.br/">holdupsolucoes.com.br</a> · <a href="https://github.com/Bruno-LSo">GitHub</a></p>
</div></footer>
{scripts}
</body>
</html>
"""


def menu(areas, raiz, atual=None):
    return "".join(
        f'<a href="{raiz}areas/{a["id"]}.html"{" aria-current=\"page\"" if a["id"] == atual else ""}>{a["curto"]}</a>'
        for a in areas
    )


def hero(p, area, raiz):
    ficha = "".join(f"<div><dt>{escape(k)}</dt><dd>{v}</dd></div>" for k, v in p.get("ficha", []))
    ficha_html = f'<dl class="ficha entra" style="--o:3">{ficha}</dl>' if ficha else ""
    return f"""<main id="conteudo">
<section class="caso-hero"><div class="wrap">
  <p class="migalha entra"><a href="{raiz}index.html">Portfólio</a><span aria-hidden="true">/</span><a href="{raiz}areas/{area['id']}.html">{area['nome']}</a></p>
  <h1 class="entra" style="--o:1">{p['nome']}</h1>
  <p class="lead entra" style="--o:2">{p['lead']}</p>
  {ficha_html}
</div></section>
"""


def numeros(lista):
    if not lista:
        return ""
    itens = "".join(f'<div class="kpi"><strong class="num">{v}</strong><span>{t}</span></div>' for v, t in lista)
    return f'<section class="bloco"><div class="wrap"><div class="kpis revela">{itens}</div></div></section>\n'


def secao(titulo, corpo, apoio=""):
    lado = f'<div><h2>{titulo}</h2>{f"<p>{apoio}</p>" if apoio else ""}</div>'
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


def tecnologias(itens, link=None):
    s = "".join(f"<span>{i}</span>" for i in itens)
    l = f'<p style="margin-top:22px"><a class="btn btn--mini btn--linha" href="{link[1]}" rel="noopener">{link[0]} <span class="seta" aria-hidden="true">→</span></a></p>' if link else ""
    return f'<section class="bloco"><div class="wrap bloco__grid"><div><h2>Tecnologias</h2></div><div><div class="stack">{s}</div>{l}</div></div></section>\n'


def navegacao(ant, prox, area, raiz):
    def item(p, rot, cls):
        if not p:
            return f'<span class="navp__item {cls}" aria-hidden="true"></span>'
        return f'<a class="navp__item {cls}" href="{raiz}projetos/{p["slug"]}.html"><small>{rot}</small><span>{p["nome"]}</span></a>'
    return (f'<nav class="navp" aria-label="Projetos da área"><div class="wrap navp__in">'
            f'{item(ant, "Anterior", "navp__ant")}'
            f'<a class="navp__item navp__sum" href="{raiz}areas/{area["id"]}.html"><small>Sumário</small><span>{area["nome"]}</span></a>'
            f'{item(prox, "Próximo", "navp__prox")}</div></nav>\n</main>\n')
