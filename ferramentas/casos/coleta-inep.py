"""Coleta automática do painel do INEP (repositório público Scraping-Inep)."""
import modelo as M

SLUG = "coleta-inep"

CASO = dict(
    nome="Coleta automática do painel do INEP",
    area="dados",
    resumo="Robô que percorre o painel do Censo da Educação Superior e grava ingressantes e concluintes por UF.",
    tec="Python · Playwright · pandas · openpyxl",
    lead="Robô que abre o painel público do Censo da Educação Superior, filtra a área de engenharia, percorre as 27 UFs e grava as séries de ingressantes e concluintes em Excel.",
    ficha=[("Fonte", "Painel estatístico do INEP (Power BI)"), ("Recorte", "Engenharia, produção e construção"),
           ("Período", "2010 a 2024"), ("Saída", "2 planilhas com 28 abas cada")],
    numeros=[("27", "UFs percorridas"), ("2", "indicadores: ingresso e conclusão"), ("15", "anos por UF"),
             ("5", "categorias de instituição")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-filtro-area.webp", "Página de ingresso com o filtro de área aplicado pelo robô."),
            ("02-tabela.webp", "Gráfico aberto como tabela: o robô lê as linhas e volta ao relatório."),
        ]), "Painel público do INEP, capturado pelo robô durante a coleta.", "larga"),

        ("Fluxo do processo", M.fluxograma([
            ("Abertura", [("Painel do INEP", "Power BI público")], "espera carregar"),
            ("Página", [("Ingresso", "hexágono do menu"), ("Conclusão", "hexágono do menu")], "para cada página"),
            ("Filtros", [("Área do curso", "Engenharia, produção e construção"), ("UF", "uma das 27, com rolagem da lista")], "abre o gráfico"),
            ("Leitura", [("Mostrar como tabela", "ano e 5 categorias"), ("Volta ao relatório", "limpa o filtro de UF")], "repete 27 vezes"),
            ("Saída", [("Ingressante.xlsx", "aba Consolidado + 27 abas"), ("Concluinte.xlsx", "aba Consolidado + 27 abas")]),
        ], "Antes de Sergipe e Tocantins o robô recarrega a página: depois de cerca de 25 leituras o painel deixa de responder."), "", "larga"),

        ("Funcionalidades", M.lista([
            ("Modo teste", "Confere se as 27 UFs aparecem no filtro antes da coleta."),
            ("Lista virtual", "O filtro só mostra parte das UFs; o robô rola a lista até achar a UF."),
            ("Colunas padronizadas", "Federal, estadual, municipal, privada com e sem fins e total, mesmo quando a UF não tem uma categoria."),
            ("Capturas", "Grava uma imagem a cada etapa para conferir falhas."),
        ])),

        ("Pontos de manutenção", M.colunas(
            M.lista([("Alta", "Posição do filtro de área, textos dos hexágonos e da área.")]),
            M.lista([("Média", "Caixas de seleção das UFs, opção Mostrar como tabela, colunas da tabela.")]),
            M.lista([("Baixa", "Indicador de página e botão Voltar ao relatório.")]),
        ), "Mudanças no layout do painel do INEP quebram a coleta nestes pontos."),

        ("Linhas gravadas", M.barras([("Ingressantes", 386, True), ("Concluintes", 377)],
                                     titulo="Linhas da aba Consolidado (UF e ano)",
                                     nota="27 UFs vezes 15 anos dão 405 linhas; algumas UFs têm menos anos na tabela do INEP.")),
    ],
    stack=["Python", "Playwright", "pandas", "openpyxl"],
)
