"""Estrutura de saúde e letalidade do AVC (repositório analises-estatisticas-saude)."""
from pathlib import Path

import modelo as M

SLUG = "estatistica-avc"
_MATRIZ = (Path(__file__).resolve().parent / "estatistica-avc-matriz.svg").read_text(encoding="utf-8")

CASO = dict(
    area="modelos",
    blocos=[
        ("Objetivo", M.texto([
            "Verificar se a estrutura de atendimento de cada estado explica a letalidade do AVC.",
            "Duas perguntas: a letalidade cai onde há mais trombólise, tomógrafos e neurologistas? "
            "Estados com centro habilitado para AVC têm letalidade menor?",
        ])),
        ("Dados", M.lista([
            ("Unidade", "27 UFs, agrupadas nas 5 regiões."),
            ("Variáveis", "Letalidade, taxa de trombólise, tomógrafos por 100 mil e neurologistas por 100 mil habitantes."),
            ("Grupo", "Centro habilitado: 17 UFs com centro e 10 sem centro."),
            ("Qualidade", "Nenhum valor ausente nas 4 variáveis; percentuais limpos antes do cálculo."),
        ])),
        ("Organização da análise", M.fluxograma([
            ("Entrada", [("Planilha", "indicadores por UF")]),
            ("Preparo", [("Limpeza", "texto com % vira número"), ("Descrição", "média, mediana, quartis")]),
            ("Testes", [("spearman.py", "correlação e Kruskal-Wallis entre regiões"),
                        ("mann_whitney.py", "Shapiro-Wilk, Levene, Mann-Whitney, t, ponto-bisserial")], "α = 0,05"),
            ("Saída", [("Relatório em texto", "11 e 12 seções"), ("Excel", "7 abas, com interpretação")]),
        ]), "", "larga"),
        ("Correlação com a letalidade", M.painel("", '<div id="g-sp"></div>', "Spearman, 27 UFs. p = 0,0021; 0,0047; 0,0129.")),
        ("Matriz de correlação", M.diagrama(_MATRIZ, "Spearman entre as 4 variáveis, 27 UFs. Trombólise e tomógrafos não se correlacionam entre si (p = 0,175)."), "", "larga"),
        ("Letalidade por região", M.painel("", '<div id="g-reg"></div>', "Kruskal-Wallis: H = 10,43; p = 0,034.")),
        ("Centro habilitado", M.barras([("Sem centro (10 UFs)", 17.16), ("Com centro (17 UFs)", 16.22, True)],
                                        titulo="Letalidade média por grupo", casas=2, sufixo="%",
                                        nota="Diferença de 0,93 p.p. Mann-Whitney U = 108, p = 0,259. Teste t: p = 0,500.")),
        ("Achados", M.achados([
            ("−0,566", "correlação da taxa de trombólise com a letalidade, a mais forte das três (p = 0,002)"),
            ("p = 0,034", "a letalidade difere entre as regiões: Norte 17,95% e Sul 12,91%"),
            ("p = 0,259", "centro habilitado não muda a letalidade de forma significativa"),
            ("1,8%", "da variação da letalidade explicada pela presença de centro (r ponto-bisserial = −0,136)"),
        ])),
        ("Limites", M.lista([
            ("Agregado", "Dados por estado, não por paciente."),
            ("Transversal", "Um só período; não mede antes e depois da habilitação."),
            ("Amostra", "27 UFs; nas regiões, de 3 a 9 UFs, o que torna os testes regionais frágeis."),
            ("Causalidade", "Correlação não prova causa; variáveis como renda e população não foram controladas."),
        ])),
        ("Telas", M.telas(SLUG, [
            ("01-planilha.webp", "Planilha de saída, aba Testes Estatísticos, com os grupos, a normalidade e as regiões na mesma tela."),
        ]), "Reprodução da planilha gerada, com os resultados reais da análise.", "larga"),
    ],
    stack=["Python", "pandas", "NumPy", "SciPy", "openpyxl"],
)
