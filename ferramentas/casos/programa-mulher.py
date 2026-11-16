import modelo as M

SLUG = "programa-mulher"
F = "Painel real com respostas do banco trocadas por dados fictícios."

CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-dashboard.webp", "Visão geral: ações por situação, prazos vencidos e avanço de cada indicador até a meta."),
            ("02-quadro.webp", "Quadro de eixos, iniciativas e ações; a ação pode ser arrastada para outra iniciativa."),
            ("03-mapa.webp", "Mapa das 27 regionais em quartis e ranking pela métrica escolhida."),
            ("04-tarefas.webp", "Minhas tarefas: ações sob responsabilidade da pessoa e vínculos pendentes."),
        ]), F, "larga"),
        ("No celular", M.telas(SLUG, [("05-celular.webp", "Visão geral no celular, com navegação na base da tela.")], celular=True), F, "larga"),
        ("Organização do plano", M.fluxograma([
            ("Plano", [("Eixo", "tema do plano")]),
            ("Desdobramento", [("Iniciativa", "pode atender a mais de um eixo")]),
            ("Execução", [("Ação", "Crea, responsável, prazo, prioridade, percentual")], "move"),
            ("Medição", [("Indicador", "meta por Crea e meta nacional"), ("Medição", "número com data, origem e ação")]),
        ], "A meta nacional é a soma das metas dos Creas, ou a média nos indicadores em percentual."), "", "larga"),
        ("Fluxo de uma ação", M.fluxograma([
            ("Cadastro", [("Nova ação", "iniciativa e indicadores obrigatórios")]),
            ("Atribuição", [("Aceite", "a responsável aceita ou recusa com justificativa")]),
            ("Andamento", [("Pendente", "0%"), ("Em andamento", "percentual e observação"), ("Atrasada", "prazo vencido")]),
            ("Fim", [("Concluída", "100%"), ("Exclusão", "pedido com justificativa e aprovação")]),
        ]), "", "larga"),
        ("Tipos de indicador", M.lista([
            ("Contagem no período", "Cada Crea informa o que fez desde o último registro; o sistema soma."),
            ("Situação atual", "Cada Crea informa quantos existem hoje; o número troca o anterior."),
            ("Percentual", "Valor de 0 a 100, comparado com o ponto de partida de janeiro."),
            ("Leitura nacional", "Um número do país inteiro, registrado pela coordenação."),
        ]), "4 tipos. Situação atual e percentual medem o avanço a partir do valor de janeiro."),
        ("Funcionalidades", M.lista([("Unidades", "27 Creas e o CONFEA como 28ª unidade, cada um com login e perfil."),
                     ("Metas", "Meta por Crea e meta nacional calculada."),
                     ("Mapa", "6 métricas: execução média, conclusão, concluídas, número de ações, atrasadas e metas."),
                     ("Atenção", "Ações sem indicador, prazos vencidos e indicadores sem número."),
                     ("Ajuda", "Texto com exemplo em cada campo do formulário."),
                     ("Administração", "Usuárias, exclusões com aprovação e registro de alterações.")])),
    ],
)
