import modelo as M

SLUG = "planner-grii"
F = "Painel real com respostas do banco trocadas por dados fictícios."

CASO = dict(
    nome="Planner de relações institucionais e internacionais",
    resumo="Acordos, representações, missões e eventos de uma gerência do CONFEA, com painel.",
    tec="HTML · Chart.js · Supabase",
    area="gestao",
    lead="Planner e painel da área de relações institucionais e internacionais do CONFEA. Cada acordo, representação, missão ou evento é uma ação com número do processo eletrônico, responsáveis, datas e situação.",
    ficha=[("Instituição", "CONFEA"), ("Formato", "Página única"), ("Dados", "Supabase, por funções do banco"), ("Versões", "11")],
    numeros=[("79", "áreas de trabalho na árvore"), ("2", "seções: Nacional e Internacional"), ("4", "situações de cada ação"), ("5", "abas no painel")],
    stack=["Python", "HTML", "JavaScript", "Chart.js", "Supabase", "PostgreSQL"],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-dashboard.webp", "Visão geral: ações ativas, vigentes, executadas e descontinuadas."),
            ("02-distribuicao.webp", "Ações por área principal e distribuição das situações."),
            ("03-temporal.webp", "Ações por mês e acumulado no período."),
            ("04-planner.webp", "Quadro da seção Internacional, com colunas por área e subárea."),
            ("05-area.webp", "Página de uma área: subitens, contagens e tabela de processos."),
            ("06-minhas.webp", "Minhas ações, com prazo vencido e prorrogação."),
        ]), F, "larga"),
        ("Organização", M.fluxograma([
            ("Raiz", [("Gerência", "árvore de 108 nós")]),
            ("Seção", [("Nacional", "acordos, convênios, representações, Programa Mulher, eventos"),
                       ("Internacional", "mobilidade, representações, missões, protocolos, eventos")]),
            ("Área", [("Acordos de mobilidade", "por país e entidade"), ("Representações", "vigentes e arquivadas"), ("Missões", "técnicas e de representação")]),
            ("Folha", [("Ação", "título, processo, responsáveis, início, assinatura, vigência, prorrogação")]),
        ], "79 folhas recebem ações. Os contadores da barra lateral somam as ações de cada ramo."), "", "larga"),
        ("Situação de uma ação", M.fluxograma([
            ("Início", [("Em tratativa", "sem assinatura")], "assinatura"),
            ("Vigência", [("Vigente", "alerta a 30 dias do fim; prorrogação registrada")]),
            ("Fim", ["Executado", "Descontinuado"]),
        ]), "", "larga"),
        ("Funcionalidades", M.lista([
            ("Filtros", "Responsável, período e número do processo, válidos em todas as telas."),
            ("Painel", "5 abas: visão geral, distribuição, evolução no tempo, relatórios e detalhamento."),
            ("Relatórios", "Tempo médio do início até a assinatura, por seção, e processos vigentes hoje."),
            ("Mobilidade", "Módulo de remessas e requerimentos, com importação colada da planilha."),
            ("Perfis", "Administrador e operacional; exclusão de ação por pedido com aprovação."),
        ])),
    ],
)
