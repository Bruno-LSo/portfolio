"""Painel do Sistema Confea/Crea (repositório confea-dash-geral). Números da extração de 20/10/2026."""
import modelo as M

SLUG = "painel-confea"


def _cascata():
    """Fluxo de 2025 em cascata: ingressos + reingressos - desligamentos = saldo."""
    k = 210 / 87470
    base = 270
    itens = [("Ingressos", 0, 65002, "#4FB3E8", "65.002"),
             ("Reingressos", 65002, 87470, "#4FD1D4", "+22.468"),
             ("Desligamentos", 38083, 87470, "#F08A7E", "-49.387"),
             ("Saldo líquido", 0, 38083, "#5CC98A", "38.083")]
    p = ['<svg viewBox="0 0 960 330" role="img" aria-label="Fluxo de registros em 2025: 65.002 ingressos, '
         '22.468 reingressos, 49.387 desligamentos e saldo de 38.083">']
    p.append(f'<line x1="60" y1="{base}" x2="900" y2="{base}" stroke="#A9B8C6" stroke-width="1"/>')
    for i, (rot, de, ate, cor, val) in enumerate(itens):
        x = 110 + i * 200
        y1, y2 = base - ate * k, base - de * k
        p.append(f'<rect x="{x}" y="{y1:.1f}" width="140" height="{y2 - y1:.1f}" rx="6" fill="{cor}" opacity="0.9"/>')
        p.append(f'<text x="{x + 70}" y="{y1 - 10:.1f}" fill="#EAF1F6" font-family="JetBrains Mono" font-size="16" '
                 f'font-weight="700" text-anchor="middle">{val}</text>')
        p.append(f'<text x="{x + 70}" y="{base + 26}" fill="#A9B8C6" font-family="Sora" font-size="14" text-anchor="middle">{rot}</text>')
        if i < 3:
            topo = base - (ate if i < 2 else de) * k
            p.append(f'<line x1="{x + 140}" y1="{topo:.1f}" x2="{x + 200}" y2="{topo:.1f}" stroke="#A9B8C6" stroke-dasharray="4 4"/>')
    p.append("</svg>")
    return "".join(p)


CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-inicio.webp", "Página inicial: quatro indicadores e oito painéis. Quatro painéis estão marcados como em breve."),
            ("02-dados-gerais.webp", "Dados gerais: 1.222.610 profissionais ativos, 20,3% mulheres, 5,7 por 1.000 habitantes."),
            ("03-piramide.webp", "Registros por gênero e ano, pirâmide etária, idade no registro e local de diplomação."),
            ("04-visao-executiva.webp", "Visão executiva por Crea, com ordenação por coluna e exportação em CSV."),
            ("05-historico.webp", "Histórico de registros, com filtro de Crea e de período."),
            ("06-fluxo.webp", "Fluxo anual, composição das saídas, saldo dos últimos 5 anos e registros dos últimos 12 meses."),
            ("07-anuidades.webp", "Anuidades de 2025: 843.535 em dia (69,0%) e situação por Crea."),
            ("08-ritmo-projecao.webp", "Ritmo de pagamento mês a mês e projeção de fechamento de 2026 por regressão linear."),
            ("09-titulos.webp", "Títulos: 417 títulos distintos e participação feminina nos 15 mais comuns."),
        ]), "Capturas do painel gerado com a extração de 20/10/2026. Só números agregados.", "larga"),

        ("Fluxo de páginas", M.fluxograma([
            ("Entrada", [("Página inicial", "4 indicadores, 8 cartões")], "escolhe o painel"),
            ("Painéis", [("Dados gerais", "perfil, idade, densidade, migração"),
                         ("Histórico", "séries de registro, coortes, fluxo"),
                         ("Anuidades", "situação, arrecadação, projeção"),
                         ("Títulos", "ranking e tabela completa")], "em cada painel"),
            ("Ações", [("Filtros", "Crea e período"), ("CSV", "tabelas por Crea"),
                       ("Memória de cálculo", "conta da projeção"), ("Tema", "claro ou escuro")]),
        ], "Página única em HTML: o botão Página inicial volta ao menu."), "", "larga"),

        ("Fluxo do processo", M.fluxograma([
            ("Origem", [("Banco nacional de registros", "SQL Server, rede interna")], "23 consultas"),
            ("Extração", [("Regras oficiais", "população de engenharia, datas futuras descartadas"),
                          ("Arquivo datado", "JSON com data e hora")], "lê o mais recente"),
            ("Geração", [("Python e pandas", "indicadores, taxas, projeção")], "grava"),
            ("Saída", [("HTML autônomo", "dados embutidos, gráficos ECharts")]),
        ], "Cada versão do painel sai de um arquivo de extração guardado. Há 11 extrações de junho a outubro de 2026."), "", "larga"),

        ("Regras de contagem", M.lista([
            ("Ativo", "Situação cadastral 2. A contagem conferida deu 1.203.786 contra 1.204.609 do painel oficial (0,07% de diferença)."),
            ("Engenharia", "Exclui os grupos de título Arquitetura e Especiais."),
            ("Anuidade em dia", "Quitada, remida ou isenta, contada pelo Crea que lançou a anuidade."),
            ("Desligamento", "Interrompido, suspenso ou cancelado (7 códigos de situação)."),
            ("Reingresso", "Reativação a mais de 60 dias do primeiro registro."),
            ("Datas", "Datas futuras de registro, nascimento ou pagamento são descartadas."),
        ])),

        ("Fluxo de 2025", M.diagrama(_cascata(), "Registros no ano: 65.002 ingressos e 22.468 reingressos menos 49.387 desligamentos dão saldo de +38.083."), "", "larga"),

        ("Saldo líquido por ano", M.barras([
            ("2019", 49551), ("2020", 45656), ("2021", 57501), ("2022", 41418),
            ("2023", 53206), ("2024", 43491), ("2025", 38083, True)],
            titulo="Ingressos mais reingressos menos desligamentos, Brasil", nota="2025 tem o menor saldo da série de 2010 a 2025.")),

        ("Achados", M.achados([
            ("20,3%", "dos ativos são mulheres (248.033 de 1.222.610)"),
            ("39,1 e 45,9", "anos de idade média: mulheres e homens"),
            ("28,5%", "dos ativos estão em SP (348.494)"),
            ("69,0%", "das anuidades de 2025 em dia (843.535)"),
            ("61.858", "registros nos últimos 12 meses"),
            ("16.252", "profissionais sem anuidade em dia nos últimos 6 anos"),
        ])),
    ],
    stack=["SQL Server", "Python", "pandas", "pymssql", "ECharts"],
)
