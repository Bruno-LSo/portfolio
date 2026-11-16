"""PoMap: telas reproduzidas a partir do código Flutter (lib/presentation/screens)."""
import modelo as M

SLUG = "pomap"

ARQ = ('<svg viewBox="0 0 960 330" role="img" aria-label="Arquitetura do PoMap">'
       '<defs><marker id="pomap-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
       '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
       '<g font-family="Sora" text-anchor="middle">'
       # app
       '<rect x="20" y="105" width="210" height="120" rx="12" fill="#162A37" stroke="#4FD1D4" stroke-width="2"/>'
       '<text x="125" y="145" fill="#EAF1F6" font-size="17">App Flutter</text>'
       '<text x="125" y="170" fill="#A9B8C6" font-size="13">Riverpod e go_router</text>'
       '<text x="125" y="192" fill="#A9B8C6" font-size="13">Android, iOS, PT e EN</text>'
       # firebase
       '<rect x="340" y="20" width="270" height="170" rx="12" fill="#162A37" stroke="#FFD25E" stroke-width="2"/>'
       '<text x="475" y="50" fill="#FFD25E" font-size="16">Firebase</text>'
       '<text x="475" y="80" fill="#EAF1F6" font-size="14">Auth: email e Google</text>'
       '<text x="475" y="104" fill="#EAF1F6" font-size="14">Firestore: árvores, votos, rotas</text>'
       '<text x="475" y="128" fill="#EAF1F6" font-size="14">Storage: fotos</text>'
       '<text x="475" y="152" fill="#EAF1F6" font-size="14">Messaging: alertas</text>'
       '<text x="475" y="176" fill="#A9B8C6" font-size="13">Analytics e Crashlytics</text>'
       # functions
       '<rect x="700" y="20" width="240" height="170" rx="12" fill="#162A37" stroke="#5CC98A" stroke-width="2"/>'
       '<text x="820" y="50" fill="#5CC98A" font-size="16">Cloud Functions</text>'
       '<text x="820" y="80" fill="#EAF1F6" font-size="14">16 funções, Node 18</text>'
       '<text x="820" y="104" fill="#EAF1F6" font-size="14">geohash da árvore</text>'
       '<text x="820" y="128" fill="#EAF1F6" font-size="14">contagem de votos e notas</text>'
       '<text x="820" y="152" fill="#EAF1F6" font-size="14">foto reduzida (sharp)</text>'
       '<text x="820" y="176" fill="#A9B8C6" font-size="13">relatório diário de uso</text>'
       # maps
       '<rect x="340" y="230" width="270" height="80" rx="12" fill="#162A37" stroke="#4FB3E8" stroke-width="2"/>'
       '<text x="475" y="263" fill="#4FB3E8" font-size="16">Google Maps e Places</text>'
       '<text x="475" y="287" fill="#A9B8C6" font-size="13">mapa, busca de endereço, rotas</text>'
       # pagamentos
       '<rect x="700" y="230" width="240" height="80" rx="12" fill="#162A37" stroke="#F08A7E" stroke-width="2"/>'
       '<text x="820" y="263" fill="#F08A7E" font-size="16">RevenueCat e AdMob</text>'
       '<text x="820" y="287" fill="#A9B8C6" font-size="13">assinatura e anúncios</text>'
       '</g>'
       '<g stroke="#4FD1D4" stroke-width="2" fill="none">'
       '<path d="M230 145 L338 110" marker-end="url(#pomap-seta)"/>'
       '<path d="M230 190 L338 265" marker-end="url(#pomap-seta)"/>'
       '<path d="M610 105 L698 105" marker-end="url(#pomap-seta)"/>'
       '<path d="M230 215 C420 330 560 330 698 285" marker-end="url(#pomap-seta)"/>'
       '</g></svg>')

CASO = dict(
    lead="Aplicativo de celular para encontrar e compartilhar árvores frutíferas em espaço público, com mapa, cadastro por foto e localização, rotas de colheita e alertas de proximidade.",
    ficha=[("Tipo", "Produto próprio, em desenvolvimento"), ("Plataformas", "Android e iOS"), ("Idiomas", "Português e inglês"), ("Modelo", "Gratuito e assinatura")],
    numeros=[("26", "telas previstas, 10 com layout no código"), ("45", "tipos de árvore e 51 subtipos"), ("16", "funções na nuvem")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-login.webp", "Entrada com email e senha ou conta Google. Dados fictícios."),
            ("02-cadastro.webp", "Cadastro com medidor de força da senha e aceite dos termos. Dados fictícios."),
            ("03-inicio.webp", "Mapa com árvores por fase de colheita, grupos de marcadores e resumo da área. Dados fictícios."),
            ("04-arvore.webp", "Árvore selecionada: fase, votos, notas e ações de confirmar ou pedir rota. Dados fictícios."),
            ("05-adicionar.webp", "Botão central: três formas de marcar o local de uma árvore nova. Dados fictícios."),
            ("06-lista.webp", "Mesma área em lista, com a fase de colheita e a nota de cada árvore. Dados fictícios."),
            ("07-rotas.webp", "Rotas de colheita: lista pessoal, rotas da comunidade e dicas. Dados fictícios."),
            ("08-perfil.webp", "Perfil com nível de reputação, pontos e contribuições. Dados fictícios."),
            ("09-configuracoes.webp", "Configurações: tema, idioma, mapa e privacidade; recursos pagos marcados. Dados fictícios."),
        ], celular=True), "Telas reproduzidas em HTML a partir do código Flutter, com as cores, os textos e o layout do app.", "larga"),
        ("Fluxo de navegação", M.fluxograma([
            ("Abertura", [("Verificação de sessão", "sem login vai para a entrada")]),
            ("Entrada", [("Login", "email ou Google"), "Cadastro", "Recuperar senha"], "após o login"),
            ("Barra inferior", [("Início", "mapa e lista"), "Mapa", ("Adicionar", "botão central"), "Rotas", "Perfil"]),
            ("Detalhe", [("Árvore", "editar, fotos"), ("Nova árvore", "local, foto, tipo"), ("Rota", "editar, seguir"), ("Busca", "endereço ou tipo")]),
            ("Conta", [("Perfil", "editar, minhas árvores, favoritos"), ("Configurações", "idioma, notificações, privacidade, sobre"), ("Premium", "alertas de proximidade"), "Ranking"]),
        ], "Rotas definidas em app_router.dart (go_router). 16 telas ainda são marcadores de posição no código."), "", "larga"),
        ("Funcionalidades", M.lista([
            ("Mapa", "Árvores próximas com cor por fase de colheita: dormência, floração, frutos verdes e pronta."),
            ("Cadastro", "Local pela posição atual, pelo mapa ou por endereço, com foto e tipo de árvore."),
            ("Validação", "Votos de confirmação, notas de 1 a 5 e situação verificada, pendente ou disputada."),
            ("Tipos", "45 tipos e 51 subtipos de carga inicial; tipo novo passa por votação e aprovação."),
            ("Rotas", "Roteiro de colheita entre árvores, com distância, tempo estimado e progresso."),
            ("Reputação", "Seis níveis, de iniciante a guardião, por pontos de contribuição."),
            ("Assinatura", "Alertas de proximidade e mapas offline no plano pago."),
        ])),
        ("Controle de custos", M.fluxo([
            ("Cota", "Limite diário", "40.000 leituras e 15.000 escritas no Firestore, 500 chamadas de rota e 1 GB de fotos."),
            ("80%", "Modo econômico", "O relatório diário avisa a administração; o alerta de orçamento liga o modo econômico na configuração do app."),
            ("95%", "Modo de emergência", "O alerta de orçamento liga o modo de emergência e registra o motivo."),
        ], "Limites em app_config.dart; regras nas funções onBudgetAlert e dailyUsageReport."), "Limites para manter o custo do Firebase sob controle."),
        ("Arquitetura", M.diagrama(ARQ, "O app fala com o Firebase e o Google Maps; as funções na nuvem atualizam contagens e tratam fotos."), "", "larga"),
    ],
)
