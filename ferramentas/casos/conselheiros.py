import modelo as M

SLUG = "conselheiros"
F = "Painel real com respostas do banco trocadas por dados fictícios."

CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-inicio.webp", "Página inicial: conselheiros por terço, processos por fase, pauta por mês e ranking."),
            ("02-conselheiros.webp", "Detalhado por conselheiro: posse, relatos, tempo médio, uso de IA e presença."),
            ("03-processos.webp", "Detalhado por processo, com alerta de dias na fase e dias desde a abertura."),
            ("04-processo.webp", "Ficha do processo: relatos, pautas e histórico de movimentações."),
        ]), F, "larga"),
        ("No celular", M.telas(SLUG, [("05-celular.webp", "Página inicial em abas no celular.")], celular=True), F, "larga"),
        ("Fluxo de páginas", M.fluxograma([
            ("Entrada", [("Login", "e-mail e senha; sessão encerra após 30 minutos sem uso")]),
            ("Filtros", [("Câmara", "só as liberadas ao usuário"), ("Período", "data inicial e final"), ("Fase e tipo", "grupos e fases do GovAdm")], "valem em todas as páginas"),
            ("Páginas", [("Página inicial", "resumo, pauta, fases, ranking"), ("Por conselheiro", "ficha e ranking ordenável"),
                         ("Por processo", "busca, filtros e planilha"), ("Administração", "usuários, acessos, regras, pendências")]),
            ("Detalhe", [("Lista do cartão", "clique em um número"), ("Ficha do processo", "histórico completo")]),
        ], "O painel confere a cada 30 segundos se há dados novos e se redesenha sozinho."), "", "larga"),
        ("Carga de dados", M.fluxograma([
            ("Fontes", [("SICOP", "SQL Server, só leitura: mandatos, relatos, pautas, presença"),
                        ("GovAdm", "robô Playwright: relatório de processos e painéis das câmaras")]),
            ("Extração", [("Comparação", "checksum por registro"), ("Gravação", "só o que é novo ou mudou")], "carga incremental"),
            ("Banco", [("Cruzamento", "conselheiro, processo e fase nos dois sistemas"), ("Conferência", "lista de pendências")]),
            ("Saída", [("Funções do painel", "uma consulta por página, com o perfil do usuário")]),
        ]), "", "larga"),
        ("Números da última carga", M.achados([
            ("4.847", "processos nas câmaras"),
            ("455", "assentos em 9 câmaras"),
            ("81.119", "registros novos gravados"),
            ("12", "arquivos SQL: esquema, acesso, cruzamento, painel e conferência"),
        ])),
        ("Regras do painel", M.lista([
            ("Alerta na fase", "Amarelo a partir de 30 dias e vermelho a partir de 60 dias na fase atual."),
            ("Alerta total", "Amarelo a partir de 90 dias e vermelho a partir de 180 dias desde a abertura."),
            ("Grupos de fase", "Manifestação, Pauta, Em Posse, P/ Análise e Outras; o administrador reagrupa."),
            ("Uso de IA", "Parte dos relatos assinados com apoio da IA do VoteNet, por conselheiro."),
            ("Acesso", "Cada usuário vê só as câmaras liberadas; toda ação fica registrada."),
        ])),
    ],
)
