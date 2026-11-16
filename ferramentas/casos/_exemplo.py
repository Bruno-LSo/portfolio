"""Modelo de caso detalhado. Copie para ferramentas/casos/<slug>.py (sem o _ no início).

Projeto já listado em conteudo.py: as chaves aqui substituem as do registro.
Projeto novo: inclua nome, resumo, tec e area ("comercio", "campo", "gestao", "dados", "saude", "produtos").
Blocos: (título, html, apoio opcional, "larga" opcional). Use "larga" para telas, fluxogramas e diagramas.
"""
import modelo as M

SLUG = "toshi-caged"

CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [("01-tabela.webp", "Tabela por ocupação, com busca e filtros."),
                                ("02-tabela.webp", "Mesma tela, outro filtro.")]), "Capturas do painel publicado.", "larga"),
        ("Fluxo de páginas", M.fluxograma([
            ("Entrada", ["Página única"]),
            ("Filtros", [("O que exibir", "ocupação, município, atividade"), ("Mês", "18 meses"), ("Território", "UF")], "aplica"),
            ("Saída", [("Tabela", "ordenável"), ("CSV", "o que está na tela")]),
        ]), "", "larga"),
        ("Achados", M.achados([("+2.193.193", "saldo de empregos formais de jan/2025 a jun/2026"),
                               ("40.604.909", "admissões no período")])),
        ("Comparação", M.barras([("Admissões", 40604909, True), ("Desligamentos", 38411716)], titulo="Brasil, 2025-01 a 2026-06")),
        ("Diagrama", M.diagrama('<svg viewBox="0 0 600 120" role="img" aria-label="Exemplo"><rect x="10" y="30" width="160" height="60" rx="10" fill="#162A37" stroke="#4FD1D4"/><text x="90" y="65" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">MTE (FTP)</text><path d="M170 60 H250" stroke="#4FD1D4" stroke-width="2" marker-end="url(#s)"/><defs><marker id="s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs><rect x="250" y="30" width="160" height="60" rx="10" fill="#162A37" stroke="#4FD1D4"/><text x="330" y="65" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Python</text></svg>', "Exemplo de diagrama."), "", "larga"),
    ],
)
