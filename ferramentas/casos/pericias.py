import modelo as M

SLUG = "pericias"
F = "Tela reproduzida a partir da especificação. Dados fictícios."

_ARQ = '''<svg viewBox="0 0 960 330" role="img" aria-label="Arquitetura: cofre, robô somente leitura, tribunais, banco, motor de eventos, motor de documentos e avisos">
<defs><marker id="pericias-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>
<g font-family="Sora" font-size="14" text-anchor="middle">
<rect x="20" y="30" width="170" height="70" rx="10" fill="#162A37" stroke="#FFD25E"/><text x="105" y="60" fill="#EAF1F6">Cofre</text><text x="105" y="82" fill="#A9B8C6" font-size="13">senhas cifradas</text>
<rect x="20" y="130" width="170" height="70" rx="10" fill="#162A37" stroke="#4FB3E8"/><text x="105" y="160" fill="#EAF1F6">Robô de leitura</text><text x="105" y="182" fill="#A9B8C6" font-size="13">1 vez por dia</text>
<rect x="20" y="230" width="170" height="70" rx="10" fill="#162A37" stroke="#F08A7E"/><text x="105" y="260" fill="#EAF1F6">Tribunais</text><text x="105" y="282" fill="#A9B8C6" font-size="13">eproc, PJe, e-SAJ</text>
<rect x="270" y="130" width="180" height="70" rx="10" fill="#162A37" stroke="#4FD1D4"/><text x="360" y="160" fill="#EAF1F6">Captura bruta</text><text x="360" y="182" fill="#A9B8C6" font-size="13">original imutável</text>
<rect x="530" y="130" width="180" height="70" rx="10" fill="#162A37" stroke="#4FD1D4"/><text x="620" y="160" fill="#EAF1F6">Motor de eventos</text><text x="620" y="182" fill="#A9B8C6" font-size="13">etapa, prazo, tarefa</text>
<rect x="790" y="40" width="150" height="70" rx="10" fill="#162A37" stroke="#5CC98A"/><text x="865" y="70" fill="#EAF1F6">Documentos</text><text x="865" y="92" fill="#A9B8C6" font-size="13">11 modelos</text>
<rect x="790" y="130" width="150" height="70" rx="10" fill="#162A37" stroke="#5CC98A"/><text x="865" y="160" fill="#EAF1F6">Financeiro</text><text x="865" y="182" fill="#A9B8C6" font-size="13">em centavos</text>
<rect x="790" y="220" width="150" height="70" rx="10" fill="#162A37" stroke="#5CC98A"/><text x="865" y="250" fill="#EAF1F6">Avisos</text><text x="865" y="272" fill="#A9B8C6" font-size="13">WhatsApp e e-mail</text>
</g>
<g stroke="#4FD1D4" stroke-width="2" fill="none">
<path d="M105 100 V128" marker-end="url(#pericias-seta)"/><path d="M105 200 V228" marker-end="url(#pericias-seta)"/>
<path d="M190 165 H268" marker-end="url(#pericias-seta)"/><path d="M450 165 H528" marker-end="url(#pericias-seta)"/>
<path d="M710 150 L788 85" marker-end="url(#pericias-seta)"/><path d="M710 165 H788" marker-end="url(#pericias-seta)"/><path d="M710 180 L788 245" marker-end="url(#pericias-seta)"/>
</g></svg>'''

CASO = dict(
    blocos=[
        ("Telas da plataforma", M.telas(SLUG, [
            ("01-painel.webp", "Painel do dia: prazos, vistorias, dinheiro e leitura de cada tribunal."),
            ("02-quadro.webp", "Quadro por etapa, com a soma do valor em cada coluna."),
            ("03-pericia.webp", "Perícia: cada dado extraído mostra a página de origem."),
            ("04-honorarios.webp", "Proposta de honorários calculada por código, em centavos."),
            ("05-financeiro.webp", "Ciclo do honorário, idade do a receber e conciliação em três pontas."),
        ]), F, "larga"),
        ("No celular", M.telas(SLUG, [
            ("06-vistoria.webp", "Vistoria sem internet: cada foto e medição ligada a um quesito."),
            ("07-codigo.webp", "Pedido do código de segurança do tribunal por mensagem."),
        ], celular=True), F, "larga"),
        ("Ciclo da perícia", M.fluxograma([
            ("Entrada", [("E0 Cadastro", "uma vez; revisão a cada 6 meses"), ("E1 Captura diária", "processos, eventos e prazos")], "nomeação"),
            ("Aceite", [("E2 Nomeação", "aceite, proposta, declínio ou escusa"), ("E3 Honorários", "homologação, impugnação, redução")], "valor homologado"),
            ("Preparação", [("E4 Depósito", "alvará de até 50%"), ("E5 Agendamento", "partes cientes 5 dias antes"), ("E6 Preparação", "lista única de quesitos")], "vistoria"),
            ("Trabalho", [("E7 Vistoria", "aplicativo sem internet"), ("E8 Cálculos", "código testado"), ("E9 Laudo", "avisos D-15 a D-1")], "laudo protocolado"),
            ("Fechamento", [("E10 Complementar", "ponto a ponto"), ("E11 Audiência", "quando houver"), ("E12 Saldo", "levantamento e repasses"), ("E13 Encerramento", "horas reais x propostas")]),
        ], "14 etapas. Cada uma tem sinal, ação da plataforma, documento pronto, conferências, prazo e efeito no financeiro."), "", "larga"),
        ("Arquitetura", M.diagrama(_ARQ, "O robô só lê. Nunca peticiona nem abre prazo no sistema do tribunal."), "", "larga"),
        ("Regras de projeto", M.lista([
            ("Nada sem fonte", "Todo dado de um documento indica o processo, o evento e a página de onde veio."),
            ("A IA não cria fatos", "Falta de informação vira pendência visível [FALTA: ...] e trava a liberação."),
            ("Contas só por código", "Valores, áreas e honorários saem de funções testadas, em centavos."),
            ("Nenhum resto de outro caso", "O texto é comparado com o acervo antes de liberar o documento."),
            ("O perito homologa", "Nada é protocolado sem aprovação; o protocolo é feito pelo perito."),
            ("Falha nunca silenciosa", "Toda leitura termina como \"lida e conferida\" ou \"não conferida\", com aviso."),
        ])),
        ("Funcionalidades", M.lista([("Captura", "Leitura incremental: só processos com novidade e só eventos novos."),
                     ("Código de segurança", "Pedido por mensagem; lembrete em 30 minutos e em 2 horas."),
                     ("Documentos", "11 modelos de petição e modelos de laudo por tipo de perícia."),
                     ("Honorários", "Hora técnica do IBAPE de cada estado, com vigência e fonte."),
                     ("Financeiro", "Livro imutável: esperado, homologado, depositado, liberado, recebido, conciliado."),
                     ("Avisos", "15 regras de aviso por evento, prazo e falha de captura.")])),
    ],
)
