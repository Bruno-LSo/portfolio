"""Conteúdo do portfólio. A ordem das áreas e dos projetos dentro de cada área é a ordem do site.

manual=True: a página do projeto tem demonstração própria e é editada direto no HTML;
o gerador só atualiza o cabeçalho, a migalha e a navegação dela.
"""
import modelo as M

AREAS = [
    {"id": "comercio", "nome": "Comércio eletrônico", "curto": "Comércio", "cor": "#C9E36A",
     "texto": "Lojas virtuais com catálogo, carrinho, pagamento, frete e integração com ERP."},
    {"id": "campo", "nome": "Território e infraestrutura", "curto": "Território", "cor": "#5CC98A",
     "texto": "Coleta de dados em campo, mapas, infraestrutura e bases municipais."},
    {"id": "gestao", "nome": "Sistemas e plataformas", "curto": "Sistemas", "cor": "#4FB3E8",
     "texto": "Plataformas com fluxos de aprovação, perfis de acesso e assinatura digital."},
    {"id": "dados", "nome": "Dados e painéis", "curto": "Dados", "cor": "#FFD25E",
     "texto": "Extração, conferência e visualização de bases públicas e institucionais."},
    {"id": "saude", "nome": "Saúde", "curto": "Saúde", "cor": "#4FD1D4",
     "texto": "Avaliação econômica, painéis da rede de atendimento e apoio a pareceres técnicos."},
    {"id": "modelos", "nome": "Modelos preditivos e estatística", "curto": "Modelos", "cor": "#F08A7E",
     "texto": "Classificação, séries temporais, texto, imagem e análise estatística, do dado bruto ao resultado."},
    {"id": "produtos", "nome": "Aplicativos, jogos e automação", "curto": "Aplicativos", "cor": "#D3A574",
     "texto": "Aplicativos de celular, jogos, ferramentas de áudio e vídeo e automação de rotinas."},
]

P = []


def projeto(**p):
    P.append(p)


# ================================================================ comércio
projeto(slug="canteiros-urbanos", area="comercio", manual=True, nome="Canteiros Urbanos",
        resumo="Loja virtual de hortaliças e temperos, com pedido pelo WhatsApp e painel do lojista.",
        tec="React · Node.js · MongoDB · Redis")

projeto(slug="emede", area="comercio", nome="EMEDE",
        resumo="Loja de moda integrada ao Bling, Mercado Pago e Melhor Envio.",
        tec="Supabase · Bling · Mercado Pago · Melhor Envio",
        lead="Loja virtual da EMEDE, marca de moda feminina fitness e casual. O estoque vem do Bling, o pagamento é feito pelo Mercado Pago e o frete pelo Melhor Envio.",
        ficha=[("Cliente", "EMEDE"), ("Endereço", '<a href="https://useemede.com.br/">useemede.com.br</a>'), ("Integrações", "Bling, Mercado Pago, Melhor Envio"), ("Publicação", "Cloudflare Pages")],
        numeros=[("3.743", "cadastros ativos no Bling, 393 produtos e 3.326 variações"), ("42", "regras de negócio"), ("28", "requisitos funcionais"), ("29", "cenários de segurança testados no banco")],
        blocos=[
            ("Levantamento", M.painel("", '<div class="kpis"><div class="kpi"><strong class="num">41</strong><span>pedidos em 7 dias</span></div><div class="kpi"><strong class="num">R$ 283,48</strong><span>ticket médio</span></div><div class="kpi"><strong class="num">2.335</strong><span>peças em estoque</span></div><div class="kpi"><strong class="num">12</strong><span>grafias diferentes de cor e tamanho</span></div></div>'), "Dados lidos do Bling antes do desenho da loja."),
            ("Integração", M.fluxo([("bling", "Estoque e produtos", "Produtos, variações, estoque e nota fiscal pela API v3 do Bling."),
                                   ("banco", "Normalização", "Cor e tamanho padronizados e trava contra venda sem estoque."),
                                   ("loja", "Vitrine", "Coleções, compra pelo tamanho e sacola lateral."),
                                   ("checkout", "Pagamento e frete", "Pix ou cartão sem cadastro, cotação de frete e etiqueta."),
                                   ("painel", "Administração", "Fotos, pedidos, etiquetas e permissões por usuário.")])),
            ("Escopo", M.lista([("Documentação", "Visão, escopo, regras de negócio e requisitos funcionais e não funcionais."),
                                ("Arquitetura", "Oito registros de decisão técnica."),
                                ("Modelo de dados", "Regras de acesso por linha testadas com pgTAP."),
                                ("Planejamento", "Backlog em 6 fases com 25 tarefas."),
                                ("Protótipo", "Vitrine e card de produto com seleção de cor e tamanho."),
                                ("Operação", "Roteiros de publicação e varredura de segredos no repositório.")])),
        ],
        stack=["HTML, CSS e JavaScript", "Cloudflare Pages", "Supabase", "Edge Functions", "pg_cron", "Bling API v3", "Mercado Pago", "Melhor Envio", "pgTAP", "Playwright"],
        link=("Abrir a loja", "https://useemede.com.br/"))

projeto(slug="curae", area="comercio", nome="CurAê",
        resumo="Vitrine e compra coletiva de queijos artesanais, com revenda, rateio de frete e Pix.",
        tec="Python · Supabase · Resend · Three.js",
        lead="Site de compra coletiva e vitrine de queijos artesanais de Alagoa, na Serra da Mantiqueira. Reúne catálogo, pedidos, cupons, revenda com comissão, rateio de frete e cobrança por Pix.",
        ficha=[("Cliente", "Queijaria artesanal"), ("Origem", "Alagoa, MG"), ("Entrega", "Site, painel e e-mails"), ("Versões", "5")],
        blocos=[
            ("Funcionalidades", M.lista([("Catálogo", "Categorias, selo de origem e quantidade disponível travada no banco."),
                                         ("Cupons", "Desconto por código e programa de figurinhas."),
                                         ("Revenda", "Comissão calculada para revendedores."),
                                         ("Frete", "Estimativa por unidade e rateio do frete real entre os pedidos."),
                                         ("Fechamento", "Data-limite do pedido e aviso apenas a quem teve item alterado."),
                                         ("Cobrança", "Valor de cada participante e pagamento por Pix.")])),
            ("Painel", M.texto(["Painel do administrador com exportação em CSV, controle de quantidade, data-limite e notificações. Os e-mails de pedido saem automaticamente. A página tem um modo de demonstração que funciona sem servidor."])),
        ],
        stack=["Python", "JavaScript", "Supabase", "Edge Functions", "Resend", "Three.js"])

projeto(slug="vm-merch", area="comercio", nome="Loja VM Solutions",
        resumo="Loja de produtos da marca com pagamento, estorno e acompanhamento do pedido.",
        tec="Supabase · Mercado Pago · Resend",
        lead="Loja de produtos da VM Solutions, com catálogo importado da plataforma anterior, pagamento pelo Mercado Pago e painel administrativo.",
        ficha=[("Cliente", "VM Solutions"), ("Endereço", '<a href="https://www.vmsolutions.tech/merch/">vmsolutions.tech/merch</a>'), ("Pagamento", "Mercado Pago"), ("Hospedagem", "Hostinger")],
        blocos=[
            ("Funcionalidades", M.lista([("Catálogo", "Produtos com variantes e fotos convertidas para WEBP."),
                                         ("Pedido", "Preço, estoque e frete recalculados no servidor."),
                                         ("Entrega", "Retirada, entrega na capital ou envio para outros estados."),
                                         ("Acompanhamento", "Página pública para o cliente consultar o pedido."),
                                         ("Painel", "Estorno, usuários, registro de atividades e mapa de entregas."),
                                         ("Segurança", "Verificação em duas etapas configurável no painel.")])),
            ("Arquitetura", M.fluxo([("funções", "Cinco funções no servidor", "Criar pedido, receber aviso do Mercado Pago, acompanhar pedido, enviar e-mails e ações do painel."),
                                     ("importação", "Migração do catálogo", "Importador da plataforma anterior para o banco."),
                                     ("monitor", "Verificação", "Rotina que confere se a loja está no ar e protegida.")])),
        ],
        stack=["Python", "Supabase", "Edge Functions", "Mercado Pago", "Resend", "Hostinger"],
        link=("Abrir a loja", "https://www.vmsolutions.tech/merch/"))

# ================================================================ campo
projeto(slug="pesca-artesanal", area="campo", manual=True, nome="Monitoramento da pesca artesanal",
        resumo="Registro de fichas de pesca no celular, inclusive sem sinal, com painel por perfil.",
        tec="PWA · PostgreSQL · RLS · ECharts")

projeto(slug="pontes-brasil", area="campo", nome="Pontes do Brasil",
        resumo="Base nacional de pontes, viadutos e passarelas, localizada por município.",
        tec="Python · geopandas · osmium · Leaflet",
        lead="Levantamento nacional das pontes, viadutos e passarelas a partir do OpenStreetMap, com classificação, comprimento e município de cada estrutura. Feito para o CONFEA.",
        ficha=[("Instituição", "CONFEA"), ("Fontes", "OpenStreetMap e malhas do IBGE 2022"), ("Cobertura", "27 UFs e 5.051 municípios"), ("Saída", "Painel e 8 formatos de arquivo")],
        numeros=[("147.327", "estruturas mapeadas"), ("6.177 km", "de extensão somada"), ("41,9 m", "de comprimento médio"), ("100%", "localizadas no município")],
        blocos=[
            ("Estruturas por tipo", M.painel("", '<div id="g-tipo"></div>')),
            ("Processamento", M.fluxo([("01", "Download", "Arquivo do Brasil (1,96 GB) e malhas municipais."),
                                       ("02", "Extração", "Leitura das estruturas com osmium."),
                                       ("03", "Cálculo", "Comprimento, área estimada e remoção de duplicadas."),
                                       ("04", "Localização", "Junção espacial com município e UF."),
                                       ("05", "Painel", "Mapa, mapa de calor e indicadores."),
                                       ("06", "Exportação", "KML, KMZ, GeoJSON, Shapefile, GeoPackage, GPX, Excel e CSV.")])),
            ("Por estado", M.painel("", '<div id="g-uf"></div>'), "São Paulo e Minas Gerais concentram 31% das estruturas."),
        ],
        stack=["Python", "osmium", "geopandas", "shapely", "pyproj", "Leaflet", "Chart.js"],
        script="""<script>
G.barrasH(document.getElementById('g-tipo'),[{rotulo:'Rodoviárias',valor:114565,destaque:true},{rotulo:'Passarelas',valor:15564,cor:'#9CC43B'},{rotulo:'Sem tipo definido',valor:7215,cor:'#3B5566'},{rotulo:'Viadutos',valor:5640,cor:'#1FA5A8'},{rotulo:'Ferroviárias',valor:4236,cor:'#D3A574'},{rotulo:'Aquedutos',valor:106,cor:'#4FB3E8'}],{esquerda:150,formato:v=>G.fmt(v),titulo:'Estruturas por tipo'});
G.barrasH(document.getElementById('g-uf'),[{rotulo:'São Paulo',valor:24589,destaque:true},{rotulo:'Minas Gerais',valor:21605,destaque:true},{rotulo:'Demais UFs',valor:101133,cor:'#3B5566'}],{esquerda:130,formato:v=>G.fmt(v),titulo:'Estruturas por estado'});
</script>""")

projeto(slug="saneamento", area="campo", nome="Saneamento por município",
        resumo="Indicadores de água, esgoto, perdas e investimento de todos os municípios, 2010 a 2024.",
        tec="Python · coleta paralela · Excel",
        lead="Coleta dos indicadores do Painel Saneamento Brasil para o país, os estados e todos os municípios, em todos os anos disponíveis. Feito para o CONFEA.",
        ficha=[("Instituição", "CONFEA"), ("Fonte", "Painel Saneamento Brasil (Instituto Trata Brasil), com dados do SNIS"), ("Período", "2010 a 2024"), ("Saída", "Um Excel por UF e um CSV único")],
        numeros=[("5.598", "localidades: Brasil, UFs e 5.570 municípios"), ("5", "indicadores"), ("419.850", "linhas no arquivo final")],
        blocos=[
            ("Indicadores", M.lista([("Acesso à água", "Percentual da população atendida."),
                                     ("Coleta de esgoto", "Percentual da população com coleta."),
                                     ("Esgoto tratado", "Percentual do esgoto que recebe tratamento."),
                                     ("Perdas na distribuição", "Percentual da água perdida."),
                                     ("Investimento", "Investimento por habitante.")])),
            ("Processamento", M.texto(["A coleta roda em 8 frentes paralelas, com cache e retomada. Ao final, o script confere nomes divergentes e séries idênticas entre municípios e registra as localidades sem indicador."])),
        ],
        stack=["Python", "requests", "openpyxl", "API do IBGE"])

projeto(slug="localizador", area="campo", nome="Localizador por coordenadas",
        resumo="Mostra no mapa uma coordenada em qualquer formato e completa planilhas com o endereço.",
        tec="JavaScript · Leaflet · OpenStreetMap",
        lead="Página que recebe uma coordenada em formato decimal, em graus ou com N, S, L e O, e mostra o local no mapa com imagem de satélite e endereço. Um script acrescenta a localização a uma planilha Excel.",
        ficha=[("Uso", "Público"), ("Mapa", "Leaflet com satélite"), ("Endereço", "Nominatim, OpenStreetMap"), ("Planilha", "Excel, sem alterar o original")],
        stack=["JavaScript", "Leaflet", "OpenStreetMap", "Python", "openpyxl"],
        link=("Abrir o localizador", "https://bruno-lso.github.io/LocalizadorPorLongitudeELatitude/"))

# ================================================================ gestão
projeto(slug="plataforma-inspetores", area="gestao", nome="Plataforma de Inspetores do Crea-SP",
        resumo="Indicação, validação, nomeação e mandato de inspetores, na web e no celular.",
        tec="Next.js · Expo · Supabase · gov.br",
        lead="Plataforma web e aplicativo para a indicação, validação, nomeação, acompanhamento do mandato e encerramento dos inspetores do Crea-SP, com conferência de requisitos na fonte e assinatura gov.br.",
        ficha=[("Instituição", "Crea-SP"), ("Entrega", "Web, aplicativo iOS e Android, banco e integrações"), ("Base normativa", "Regulamento das Inspetorias 2026"), ("Assinatura", "gov.br")],
        numeros=[("~2.600", "inspetores em 194 unidades"), ("82", "tabelas com regras de acesso por linha"), ("111", "funções no banco"), ("81", "requisitos funcionais")],
        blocos=[
            ("Telas", '<div style="display:grid;gap:14px"><div class="fig"><img src="../assets/img/casos/inspetores-painel-gerencial.webp" alt="Painel gerencial" width="1400" height="612" loading="lazy"></div><div class="fig"><img src="../assets/img/casos/inspetores-painel-vagas.webp" alt="Painel de vagas da regional" width="1400" height="620" loading="lazy"></div></div><p class="legenda">Protótipo com dados fictícios.</p>'),
            ("Aplicativo", '<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;max-width:560px"><div class="fig" style="background:none;box-shadow:none"><img src="../assets/img/casos/inspetores-documentos.webp" alt="Envio de documentos" width="836" height="1612" loading="lazy"></div><div class="fig" style="background:none;box-shadow:none"><img src="../assets/img/casos/inspetores-checkin.webp" alt="Check-in na reunião" width="520" height="896" loading="lazy"></div></div>', "Envio de documentos e check-in de presença por localização ou código QR."),
            ("Fluxo", M.fluxo([("01", "Indicação", "Vagas e cotas por unidade; indicação pelo sistema."),
                               ("02", "Pré-validação", "Registro, débitos e impedimentos conferidos pelo CPF."),
                               ("03", "Documentos", "Envio pelo celular e conferência de certidões na fonte."),
                               ("04", "Análise", "Fila de análise com resumo do currículo."),
                               ("05", "Assinaturas", "Formulário, termo de posse e declarações via gov.br."),
                               ("06", "Dossiê", "PDF único para o processo eletrônico."),
                               ("07", "Mandato", "Reuniões, presença, faltas, justificativas e encerramento.")])),
            ("Engenharia", M.lista([("Banco", "Toda gravação passa por funções do banco; todas as tabelas têm regra de acesso por linha."),
                                    ("Regras de negócio", "Regulamento implementado em pacote próprio, com testes."),
                                    ("Integrações", "Versões simulada e real para APIs internas, certidões e gov.br."),
                                    ("Testes", "Ponta a ponta com Playwright e acessibilidade em 6 larguras de tela."),
                                    ("Migrações", "32 migrações aplicadas pelo pipeline."),
                                    ("Documentação", "13 documentos de contexto, especificação, arquitetura e testes.")])),
        ],
        stack=["Next.js", "Expo", "TypeScript", "Supabase", "PostgreSQL", "gov.br", "Playwright", "axe", "GitHub Actions"])

projeto(slug="pericias", area="gestao", nome="Plataforma de perícias judiciais",
        resumo="Acompanhamento de processos, prazos, honorários e laudos para peritos.",
        tec="Supabase · Playwright · Python",
        lead="Especificação de uma plataforma para peritos judiciais: leitura diária dos processos nos tribunais, controle de etapas e prazos, cálculo de honorários e preparação de documentos a partir de modelos.",
        ficha=[("Cliente", "Perita judicial de engenharia civil"), ("Situação", "Especificação, versão 5.1"), ("Tribunais", "57 levantados"), ("Documento", "53 páginas")],
        numeros=[("57", "tribunais levantados"), ("14", "etapas do ciclo da perícia"), ("11", "modelos de laudo"), ("25", "tabelas no modelo de dados")],
        blocos=[
            ("Arquitetura", M.fluxo([("credenciais", "Cofre", "Credenciais dos tribunais cifradas e separadas do banco."),
                                     ("leitura", "Robô somente leitura", "Uma leitura por dia dos processos do perito."),
                                     ("código", "Verificação", "Pedido do código de segurança ao perito por WhatsApp."),
                                     ("eventos", "Prazos", "Cada movimentação vira etapa, prazo e tarefa."),
                                     ("documentos", "Modelos", "Laudos e petições preenchidos com dados do processo.")])),
            ("Regras", M.lista([("Origem dos dados", "Cada campo extraído indica o documento de onde veio."),
                                ("Cálculos", "Honorários e avaliações calculados por código testado, em centavos."),
                                ("Honorários", "Hora técnica do IBAPE de cada estado."),
                                ("Financeiro", "Depósitos, levantamentos e repasses por processo."),
                                ("Campo", "Aplicativo de vistoria que funciona sem internet.")])),
        ],
        stack=["Supabase", "Playwright", "WhatsApp Business", "Resend", "Python", "ReportLab", "Mermaid"])

projeto(slug="conselheiros", area="gestao", nome="Painel dos conselheiros do Crea-SP",
        resumo="Pauta, relatos e votos nas câmaras, com carga incremental de dois sistemas.",
        tec="SQL Server · Playwright · Supabase",
        lead="Painel que reúne processos, pautas, relatos e votos dos conselheiros do Crea-SP em todas as câmaras, atualizado a partir de dois sistemas internos.",
        ficha=[("Instituição", "Crea-SP"), ("Fontes", "SICOP e GovAdm"), ("Atualização", "Incremental"), ("Acesso", "Login e perfis")],
        numeros=[("4.847", "processos nas câmaras"), ("455", "assentos em 9 câmaras"), ("81.119", "registros novos na última carga")],
        blocos=[("Escopo", M.lista([("Extração", "Leitura somente do SICOP e robô no GovAdm para relatórios e painéis das câmaras."),
                                     ("Carga incremental", "Grava só o que é novo ou mudou, com checksum e conferência."),
                                     ("Cruzamento", "Comparação entre os dois sistemas e lista de pendências."),
                                     ("Painel", "Login, perfis e administração.")]))],
        stack=["SQL Server", "Playwright", "Supabase", "Python"])

projeto(slug="programa-mulher", area="gestao", nome="Programa Mulher 2026",
        resumo="Planejamento e acompanhamento das ações do programa nos 27 Creas.",
        tec="Alpine.js · Supabase · Python",
        lead="Painel em que os 27 Creas planejam e acompanham as ações do Programa Mulher do Sistema Confea/Crea e Mútua.",
        ficha=[("Instituição", "CONFEA"), ("Usuários", "27 Creas"), ("Versões", "13"), ("Acesso", "Login e perfis por Crea")],
        blocos=[("Funcionalidades", M.lista([("Eixos e ações", "Quadro de eixos, ações e tarefas por Crea."),
                                              ("Metas", "Metas nacionais e por Crea, com registro de medições."),
                                              ("Acompanhamento", "Ranking das regionais e ações concluídas por mês."),
                                              ("Mapa", "Situação de cada Crea no mapa."),
                                              ("Administração", "Pedidos de exclusão com aprovação e registro de alterações.")]))],
        stack=["Python", "Alpine.js", "Supabase", "IBGE"])

projeto(slug="advinhae", area="gestao", nome="AdvinhAê",
        resumo="Bolão entre amigos com placares automáticos, palpite travado e ranking.",
        tec="React · Supabase · pg_cron",
        lead="Site de bolão: os participantes criam bolões, convidam amigos por e-mail, registram palpites e acompanham o ranking. Jogos e placares são atualizados a partir de uma base esportiva.",
        ficha=[("Cliente", "AdvinhAê"), ("Esportes", "7"), ("Login", "E-mail ou Google"), ("Atualização", "A cada 5 minutos")],
        numeros=[("13", "tabelas"), ("10 min", "antes do jogo o palpite é travado"), ("3", "funções no servidor")],
        blocos=[
            ("Demonstração", M.painel("pontuação", '<div class="controles"><div class="campo"><label for="pa">Palpite, mandante <output id="pa-o">2</output></label><input id="pa" type="range" min="0" max="6" value="2"></div><div class="campo"><label for="pb">Palpite, visitante <output id="pb-o">1</output></label><input id="pb" type="range" min="0" max="6" value="1"></div><div class="campo"><label for="ra">Resultado, mandante <output id="ra-o">2</output></label><input id="ra" type="range" min="0" max="6" value="2"></div><div class="campo"><label for="rb">Resultado, visitante <output id="rb-o">0</output></label><input id="rb" type="range" min="0" max="6" value="0"></div></div><div class="kpi" style="margin-top:16px"><strong class="num" id="pts">10</strong><span id="pts-t" role="status">pontos</span></div>'), "Placar exato vale 20 pontos; acertar o vencedor ou o empate vale 10."),
            ("Funcionalidades", M.lista([("Bolões", "Criação, convite por e-mail e fuso horário de cada participante."),
                                         ("Resultados", "Ligas, times e partidas atualizados por rotina no banco."),
                                         ("Rodadas durante o jogo", "Opcionais, valendo um décimo dos pontos."),
                                         ("Ranking", "Classificação enviada por e-mail."),
                                         ("Implantação", "Guia de banco, e-mail, domínio e login com Google.")])),
        ],
        stack=["React 18", "Supabase", "PostgreSQL", "pg_cron", "Edge Functions", "TheSportsDB", "Resend", "Google OAuth"],
        script="""<script>
(function(){const ids=['pa','pb','ra','rb'],v=i=>+document.getElementById(i).value;
function calc(){ids.forEach(i=>document.getElementById(i+'-o').textContent=v(i));const s=Math.sign(v('pa')-v('pb')),r=Math.sign(v('ra')-v('rb'));let p=0,t='pontos';
if(v('pa')===v('ra')&&v('pb')===v('rb')){p=20;t='pontos, placar exato'}else if(s===r){p=10;t=r===0?'pontos, empate':'pontos, vencedor'}
document.getElementById('pts').textContent=p;document.getElementById('pts-t').textContent=t}
ids.forEach(i=>document.getElementById(i).addEventListener('input',calc));calc()})();
</script>""")

projeto(slug="homecook", area="gestao", nome="HomeCook",
        resumo="Gestão de produtos, estoque, vendas, cursos e eventos de um negócio de culinária.",
        tec="Python · Dash · Flask · Google Sheets",
        lead="Sistema de gestão da HomeCook: produtos, estoque, clientes, vendas, cursos e eventos, com os dados guardados em planilha Google.",
        ficha=[("Cliente", "HomeCook"), ("Execução", "Computador local"), ("Dados", "Google Sheets"), ("Acesso", "Login com senha")],
        blocos=[("Módulos", M.lista([("Indicadores", "Painel com os números do negócio."),
                                      ("Produtos e estoque", "Cadastro e movimentação."),
                                      ("Clientes e vendas", "Registro e histórico."),
                                      ("Cursos e eventos", "Turmas, inscrições e agenda."),
                                      ("Manutenção", "Backups, exportações e correção da estrutura da planilha.")]))],
        stack=["Python", "Dash", "Flask", "Plotly", "Google Sheets API"])

projeto(slug="planner", area="gestao", nome="Planner de projetos",
        resumo="Quadros, tarefas, anexos e registro de alterações para uma equipe de gabinete.",
        tec="HTML · Supabase",
        lead="Aplicação de gestão de projetos no formato de quadros, usada pela equipe do Gabinete da Presidência do Crea-SP.",
        ficha=[("Instituição", "Crea-SP"), ("Formato", "Página única"), ("Dados", "Supabase"), ("Anexos", "Até 10 MB")],
        blocos=[("Funcionalidades", M.lista([("Quadros", "Colunas e cartões por projeto."),
                                              ("Tarefas", "Responsável, prazo e situação."),
                                              ("Anexos", "Arquivos ligados a cada tarefa."),
                                              ("Histórico", "Registro de todas as alterações.")]))],
        stack=["HTML", "JavaScript", "Supabase", "Python"])

# ================================================================ dados
projeto(slug="painel-confea", area="dados", nome="Painel do Sistema Confea/Crea",
        resumo="Profissionais registrados por UF, sexo, idade, título, anuidade e fluxo de registros.",
        tec="SQL Server · Python · pandas",
        lead="Painel com os profissionais registrados no Sistema Confea/Crea, gerado a partir de uma extração datada do banco nacional de registros, com as regras oficiais de contagem.",
        ficha=[("Instituição", "CONFEA"), ("Fonte", "Banco nacional de registros"), ("Período", "2010 a 2026"), ("Saída", "Extração datada e painel web")],
        numeros=[("1.222.610", "profissionais registrados"), ("248.033", "mulheres"), ("417", "títulos profissionais"), ("27", "UFs")],
        blocos=[("Conteúdo", M.lista([("Estoque", "Profissionais por UF e sexo, pirâmide etária e títulos."),
                                       ("Registro", "Coortes de registro e migração entre estados."),
                                       ("Fluxo", "Ingressos, reingressos e desligamentos, com os últimos 12 meses."),
                                       ("Anuidades", "Série por ano e UF, ritmo de pagamento e parcelamento."),
                                       ("Rastreabilidade", "Cada versão do painel sai de um arquivo de extração guardado.")]))],
        stack=["SQL Server", "Python", "pandas", "pymssql", "HTML e JavaScript"])

projeto(slug="cozinhas", area="dados", nome="Cozinhas Solidárias",
        resumo="Consolidação do levantamento estadual das Cozinhas Solidárias com a base federal.",
        tec="Python · pandas · ReportLab",
        lead="Consolidação das planilhas estaduais do levantamento das Cozinhas Solidárias 2025 com a base do Ministério do Desenvolvimento e Assistência Social, para a Conab.",
        ficha=[("Instituição", "Conab"), ("Programa", "Cozinhas Solidárias 2025"), ("Entradas", "26 planilhas estaduais"), ("Saída", "Painel, Word e PDF")],
        blocos=[("Escopo", M.lista([("Consolidação", "Leitura das 26 planilhas e junção numa tabela única."),
                                     ("Municípios", "Correspondência de nomes por similaridade, com relatório das correspondências."),
                                     ("Painel", "Consulta das cozinhas por estado e município."),
                                     ("Documentos", "Lista das cozinhas em Word e PDF.")]))],
        stack=["Python", "pandas", "difflib", "python-docx", "ReportLab"])

projeto(slug="formados-registrados", area="dados", nome="Ingressantes, concluintes e registrados",
        resumo="Censo da Educação Superior cruzado com os registros profissionais, 2010 a 2024.",
        tec="Python · INEP · Plotly",
        lead="Painel que cruza os dados de cursos de engenharia do INEP com os novos registros profissionais, por ano, estado, gênero e modalidade.",
        ficha=[("Instituição", "CONFEA"), ("Fontes", "INEP e registros profissionais"), ("Período", "2010 a 2024"), ("Painel", '<a href="https://bruno-lso.github.io/InepCNF/">bruno-lso.github.io/InepCNF</a>')],
        numeros=[("503.025", "ingressantes em 2014, maior valor da série"), ("219.192", "ingressantes em 2024"), ("38 de 100", "concluem em até 6 anos"), ("17 de 100", "chegam ao registro")],
        blocos=[("Série", M.painel("", '<div id="leg" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px"></div><div id="g-serie"></div>', "Brasil, 2010 e 2024.")),
                ("Escopo", M.lista([("Coleta", "Raspagem do portal de dados abertos do INEP e homologação dos arquivos."),
                                     ("Consultas", "Registros por ano, Crea, gênero e modalidade, documentados."),
                                     ("Indicador", "Conclusão e registro para cada 100 ingressantes, com defasagem de 6 anos."),
                                     ("Publicação", "Painel web e exportação para Excel.")]))],
        stack=["Python", "pandas", "BeautifulSoup", "SQL Server", "Plotly"],
        link=("Abrir o painel", "https://bruno-lso.github.io/InepCNF/"),
        script="""<script>
const S=[{nome:'Ingressantes',cor:'#FFD25E'},{nome:'Concluintes',cor:'#4FB3E8'},{nome:'Novos registros',cor:'#5CC98A'}];
G.legenda(document.getElementById('leg'),S);
G.colunas(document.getElementById('g-serie'),[{rotulo:'2010',valores:[281011,82936,43882]},{rotulo:'2024',valores:[219192,105064,64486]}],S,{esquerda:64,formatoY:v=>G.fmt(v/1000)+' mil',formato:v=>G.fmt(v),titulo:'Ingressantes, concluintes e novos registros'});
</script>""")

projeto(slug="mapa-profissoes", area="dados", nome="Mapa das profissões",
        resumo="Cursos de engenharia, agronomia e geociências por município, presencial e EaD.",
        tec="Python · INEP · IBGE",
        lead="Painel municipal com os cursos da área tecnológica e seus ingressantes e concluintes, de 2010 a 2024, separando presencial e EaD. Feito para o CONFEA.",
        ficha=[("Instituição", "CONFEA"), ("Fonte", "INEP, Censo da Educação Superior"), ("Período", "2010 a 2024"), ("Saída", "Painel e Excel")],
        numeros=[("3.175", "municípios com cursos"), ("125", "cursos"), ("420", "combinações de ano e UF conferidas"), ("463.562", "ingressantes em 2024")],
        blocos=[("Conferência", M.texto(["Os totais municipais são conferidos contra os estaduais em cada ano antes da geração do painel. As malhas do IBGE são carregadas por UF."]))],
        stack=["Python", "pandas", "Plotly", "IBGE"])

projeto(slug="acervo-tecnico", area="dados", nome="Priorização do Acervo Técnico",
        resumo="Ordena os pedidos de certidão pelo valor do edital e pela data da licitação.",
        tec="DB2 · Python · Plotly",
        lead="Painel que lê os pedidos de certidão de acervo técnico do Crea-SP, cruza com o edital de cada um e ordena a análise pela data da sessão pública e pelo valor da licitação.",
        ficha=[("Instituição", "Crea-SP"), ("Fonte", "DB2 e documentos dos protocolos"), ("Publicação", "Servidor interno"), ("Atualização", "Rotina programada")],
        numeros=[("1.365", "pedidos em análise"), ("R$ 25,8 bi", "em editais"), ("259", "sessões vencidas ou em até 3 dias"), ("246", "alertas de capital social")],
        blocos=[("Regras", M.fluxo([("01", "Pedidos", "Protocolos de certidão lidos do banco."),
                                     ("02", "Edital", "Valor e data da sessão extraídos; duplicados removidos."),
                                     ("03", "Prazo", "Faixas: vencida, até 3 dias, até 7 dias, demais."),
                                     ("04", "Capital", "Alerta quando o capital social é menor que 10% do edital."),
                                     ("05", "Fila", "Ordem por prazo e valor.")]))],
        stack=["DB2", "Python", "pandas", "Plotly", "SFTP"])

projeto(slug="caged", area="dados", nome="Emprego formal na engenharia",
        resumo="Novo CAGED cruzado com as profissões do sistema e salários de concursos.",
        tec="Python · Parquet · CAGED",
        lead="Painel sobre emprego formal e salários nas ocupações da engenharia, com base no Novo CAGED, e levantamento de concursos com salário abaixo do piso profissional.",
        ficha=[("Instituição", "CONFEA"), ("Fontes", "Novo CAGED, INEP e registros profissionais"), ("Período", "2020 a 2026"), ("Saída", "Painel web")],
        numeros=[("206.333", "movimentações em 25 meses"), ("13", "famílias de ocupação"), ("425", "vagas públicas abaixo do piso")],
        stack=["Python", "pandas", "Parquet", "Plotly"])

projeto(slug="toshi-caged", area="dados", nome="Extrator do Novo CAGED",
        resumo="Download e tradução dos microdados de emprego formal, com painel.",
        tec="Python · pandas · Parquet",
        lead="Ferramenta de linha de comando que baixa os microdados do Novo CAGED, traduz os códigos de município, ocupação e atividade e entrega um CSV único e um painel.",
        ficha=[("Fonte", "Ministério do Trabalho"), ("Dicionários", "Layout oficial e APIs do IBGE"), ("Formato", "Parquet e CSV"), ("Painel", '<a href="https://bruno-lso.github.io/ToshiCaged/">bruno-lso.github.io/ToshiCaged</a>')],
        stack=["Python", "pandas", "pyarrow", "py7zr"],
        link=("Abrir o painel", "https://bruno-lso.github.io/ToshiCaged/"))

projeto(slug="renda-real", area="dados", nome="Renda Real",
        resumo="Calculadora de juros compostos e correção pela inflação com dados do Banco Central.",
        tec="JavaScript · API do Banco Central",
        lead="Calculadora de juros compostos, retirada sustentável de patrimônio e correção pelo IPCA, com a série atualizada do Banco Central.",
        ficha=[("Uso", "Público"), ("Fonte", "SGS do Banco Central, série 433"), ("Saída", "Tabela ano a ano e gráfico"), ("Endereço", '<a href="https://bruno-lso.github.io/PrevisaoOrcamentariaApiBacen/">bruno-lso.github.io</a>')],
        stack=["Python", "JavaScript", "API do Banco Central"],
        link=("Abrir a calculadora", "https://bruno-lso.github.io/PrevisaoOrcamentariaApiBacen/"))

# ================================================================ saúde
projeto(slug="calculadora-avc", area="saude", manual=True, nome="Calculadora de custos do AVC",
        resumo="Impacto orçamentário de tenecteplase e alteplase no AVC isquêmico, por território.",
        tec="JavaScript · Supabase · PostgreSQL · Python")

projeto(slug="risco-cardiovascular", area="modelos", manual=True, nome="Predição de risco cardiovascular",
        resumo="Comparação de cinco algoritmos, com seleção de variáveis por Boruta e interpretação por SHAP.",
        tec="Python · TabPFN · CatBoost · SHAP")

projeto(slug="telemedicina-avc", area="saude", manual=True, nome="Telemedicina no AVC",
        resumo="Custo e impacto da telemedicina em 16 hospitais municipais de São Paulo, 2023 a 2025.",
        tec="Python · pandas · ReportLab")

projeto(slug="estatistica-avc", area="saude", nome="Estrutura de saúde e letalidade do AVC",
        resumo="Correlação entre estrutura de atendimento e letalidade do AVC nas 27 UFs.",
        tec="Python · SciPy",
        lead="Análise estatística da relação entre a estrutura de atendimento de cada estado, como tomógrafos, neurologistas e taxa de trombólise, e a letalidade do AVC.",
        ficha=[("Cliente", "Pesquisa em saúde pública"), ("Unidade", "27 UFs"), ("Testes", "Spearman, Kruskal-Wallis, Mann-Whitney, t"), ("Saída", "Relatórios em texto e Excel")],
        numeros=[("16,6%", "letalidade média entre as UFs"), ("−0,566", "correlação da trombólise com a letalidade"), ("p = 0,034", "diferença entre regiões"), ("p = 0,26", "centros habilitados, sem diferença significativa")],
        blocos=[("Correlação com a letalidade", M.painel("", '<div id="g-sp"></div>', "Spearman, 27 UFs. p = 0,0021; 0,0047; 0,0129.")),
                ("Letalidade por região", M.painel("", '<div id="g-reg"></div>')),
                ("Escopo", M.lista([("Correlações", "Spearman entre letalidade e indicadores de estrutura."),
                                     ("Regiões", "Kruskal-Wallis entre as cinco regiões."),
                                     ("Centros habilitados", "Mann-Whitney, teste t, tamanho de efeito e correlação ponto-bisserial."),
                                     ("Pressupostos", "Shapiro-Wilk e Levene antes da escolha do teste."),
                                     ("Relatório", "Excel com 7 abas, incluindo interpretação dos resultados.")]))],
        stack=["Python", "pandas", "NumPy", "SciPy", "openpyxl"],
        script="""<script>
G.barrasH(document.getElementById('g-sp'),[{rotulo:'Taxa de trombólise',valor:.566,destaque:true},{rotulo:'Tomógrafos / 100 mil',valor:.527,cor:'#4FB3E8'},{rotulo:'Neurologistas / 100 mil',valor:.472,cor:'#3B5566'}],{max:.7,esquerda:180,formato:v=>'−'+G.fmt(v,3),titulo:'Correlação com a letalidade'});
G.barrasH(document.getElementById('g-reg'),[{rotulo:'Norte',valor:17.95,cor:'#F08A7E'},{rotulo:'Nordeste',valor:17.88,cor:'#F08A7E'},{rotulo:'Sudeste',valor:15.79,cor:'#3B5566'},{rotulo:'Centro-Oeste',valor:14.73,cor:'#3B5566'},{rotulo:'Sul',valor:12.91,destaque:true}],{min:8,max:20,esquerda:120,formato:v=>G.fmt(v,1)+'%',titulo:'Letalidade média por região'});
</script>""")

projeto(slug="covid", area="saude", nome="Painel da COVID-19",
        resumo="Casos e óbitos por estado de 2020 a 2025, com mapa e comparação entre estados.",
        tec="Python · Dash · Plotly",
        lead="Painel interativo com a evolução da COVID-19 no Brasil e nos estados, a partir dos dados do Ministério da Saúde.",
        ficha=[("Fonte", "Ministério da Saúde"), ("Período", "25/02/2020 a 25/04/2025"), ("Unidade", "Brasil e 27 UFs"), ("Código", '<a href="https://github.com/Bruno-LSo/DashCovid19">github.com/Bruno-LSo/DashCovid19</a>')],
        numeros=[("39.253.864", "casos acumulados no Brasil"), ("716.029", "óbitos acumulados"), ("1.887", "dias na série")],
        blocos=[("Casos novos por ano", M.painel("", '<div id="g-covid"></div>', "2025 até abril.")),
                ("Funcionalidades", M.lista([("Mapa", "Mapa por UF; o clique filtra os gráficos."),
                                              ("Período", "Filtro de ano e seletor de data."),
                                              ("Indicadores", "Casos, óbitos, recuperados e em acompanhamento."),
                                              ("Comparação", "Dois estados lado a lado, com picos diário e mensal.")]))],
        stack=["Python", "pandas", "Dash", "Plotly"],
        link=("Ver o código", "https://github.com/Bruno-LSo/DashCovid19"),
        script="""<script>
G.colunas(document.getElementById('g-covid'),[['2020',7.68],['2021',14.61],['2022',14.04],['2023',1.91],['2024',.86],['2025',.18]].map(([r,v])=>({rotulo:r,valores:[v]})),[{nome:'Casos novos (milhões)',cor:'#4FD1D4'}],{formatoY:v=>G.fmt(v,0)+' mi',formato:v=>G.fmt(v,2)+' mi',titulo:'Casos novos por ano, em milhões'});
</script>""")

projeto(slug="formatador", area="saude", nome="Formatador de pareceres técnicos",
        resumo="Consolida pareceres de revisores e destaca o conteúdo novo num Word padronizado.",
        tec="Python · Docling · python-docx",
        lead="Ferramenta para a revisão de capítulos de vigilância em saúde: converte os documentos, compara o parecer com o modelo e com o de outro revisor e monta um Word em que só o conteúdo novo fica destacado.",
        ficha=[("Contexto", "Revisão técnica para o Ministério da Saúde"), ("Entradas", ".doc, .docx e .pdf"), ("Comparação", "difflib"), ("Saída", "Dois documentos Word")],
        blocos=[("Saídas", M.lista([("Parecer formatado", "Formatação do documento base, com o texto novo destacado."),
                                     ("Revisão consolidada", "Blocos novos agrupados e identificados por revisor.")]))],
        stack=["Python", "Docling", "python-docx", "difflib"])

# ================================================================ produtos
projeto(slug="pomap", area="produtos", nome="PoMap",
        resumo="Aplicativo para encontrar e cadastrar árvores frutíferas em espaço público.",
        tec="Flutter · Firebase · Google Maps",
        lead="Aplicativo de celular para encontrar e compartilhar árvores frutíferas em espaço público, com mapa, cadastro por foto e localização, rotas e alertas de proximidade.",
        ficha=[("Tipo", "Produto próprio"), ("Plataformas", "Android e iOS"), ("Idiomas", "Português e inglês"), ("Modelo", "Gratuito e assinatura")],
        numeros=[("26", "telas"), ("45", "tipos de árvore e 51 subtipos"), ("16", "funções na nuvem")],
        blocos=[("Funcionalidades", M.lista([("Mapa", "Árvores próximas, filtro por tipo, fotos e avaliações."),
                                              ("Cadastro", "Foto, localização e tipo, com votação e aprovação de tipos novos."),
                                              ("Rotas", "Roteiro entre árvores."),
                                              ("Alertas", "Aviso de proximidade no plano pago."),
                                              ("Custos", "Modo econômico a 80% e modo de emergência a 95% dos limites diários."),
                                              ("Administração", "Usuários, tipos pendentes e monitor de custos.")]))],
        stack=["Flutter", "Dart", "Riverpod", "Firebase", "Cloud Functions", "Google Maps", "RevenueCat", "AdMob"])

projeto(slug="warncare", area="produtos", nome="WarnCare",
        resumo="Aplicativo de controle de medicamentos com leitura de receita por foto.",
        tec="Flutter · Firebase · Vision · Gemini",
        lead="Protótipo de aplicativo para controle de medicamentos. A receita ou a embalagem é fotografada, o texto é lido e organizado em nome, dose, frequência e duração, e o app calcula quando o remédio vai acabar.",
        ficha=[("Tipo", "Protótipo"), ("Plataformas", "Android e iOS"), ("Leitura", "Google Cloud Vision e Gemini"), ("Backend", "Firebase")],
        blocos=[("Estoque", M.texto(["Dias restantes = estoque dividido pelas doses diárias. Situação vazia com zero dias, crítica até 3, baixa até 7."]))],
        stack=["Flutter", "Dart", "BLoC", "Firebase", "Cloud Functions", "Google Cloud Vision", "Gemini"])

projeto(slug="alien-crue", area="produtos", nome="GXxT",
        resumo="Jogo online em tempo real sobre o mapa real, com território, gangues e economia.",
        tec="TypeScript · Three.js · WebSocket",
        lead="Jogo online em tempo real sobre o mapa do mundo. O jogador entra pela própria localização, coleta recursos, constrói e disputa território. Dia e noite seguem a posição do sol na localização do jogador.",
        ficha=[("Tipo", "Produto próprio"), ("Plataforma", "Navegador, com empacotamento para celular"), ("Servidor", "Autoritativo, WebSocket"), ("Monetização", "Somente itens visuais")],
        numeros=[("8", "tipos de personagem"), ("24", "habilidades"), ("200", "níveis"), ("10", "tabelas")],
        blocos=[("Funcionalidades", M.lista([("Mapa", "Mapa vetorial escuro e imagens de satélite."),
                                              ("Ciclo solar", "Dia e noite pela elevação do sol na posição do jogador."),
                                              ("Servidor", "Habilidades, dano e recarga calculados no servidor."),
                                              ("Construção", "Construções persistidas para todos os jogadores."),
                                              ("Gangues", "Território, relações e economia com registro de transações.")]))],
        stack=["TypeScript", "Three.js", "PixiJS", "WebSocket", "Node.js", "Supabase", "Vite", "Capacitor"])

projeto(slug="nucleo-dados", area="produtos", nome="Núcleo de dados",
        resumo="Pacote comum que guarda e recupera os arquivos de dados de todos os projetos.",
        tec="Python · Supabase Storage · zstd",
        lead="Pacote Python usado pelos demais projetos para ler arquivos de dados do disco ou baixá-los de um armazenamento central, idênticos ao original, e para guardar novos arquivos com catálogo.",
        ficha=[("Tipo", "Infraestrutura interna"), ("Armazenamento", "Supabase Storage"), ("Conferência", "sha1"), ("Compressão", "zstd")],
        stack=["Python", "Supabase", "PostgreSQL", "zstd"])

projeto(slug="transcritor", area="produtos", nome="Transcritor de áudio",
        resumo="Transcrição em lote de áudios e vídeos, com tempo por palavra.",
        tec="Python · faster-whisper",
        lead="Transcrição de áudios e vídeos em português, em lote, com marcação de tempo por palavra e uso da placa de vídeo.",
        ficha=[("Modelo", "Whisper large-v3"), ("Saída", "Texto e JSON"), ("Execução", "Local"), ("Aceleração", "GPU")],
        stack=["Python", "faster-whisper", "CUDA"])

projeto(slug="american-legends", area="produtos", nome="American Legends",
        resumo="Produção de vídeos narrados a partir de roteiro: voz, som, legendas e montagem.",
        tec="Python · TTS · Whisper · FFmpeg",
        lead="Fluxo de produção de vídeos de folclore para um canal no YouTube: a partir do roteiro saem narração, efeitos, ambiência, legendas sincronizadas e o vídeo montado.",
        ficha=[("Tipo", "Canal próprio"), ("Narração", "Síntese de voz"), ("Legendas", "SRT sincronizado"), ("Montagem", "FFmpeg")],
        numeros=[("41", "cenas no episódio piloto"), ("568", "legendas"), ("~18 min", "de duração")],
        stack=["Python", "TTS", "faster-whisper", "pyloudnorm", "FFmpeg"])

projeto(slug="mr-yalc", area="produtos", nome="Mr. Yalc",
        resumo="Separação de voz e instrumentos com análise de andamento, tom e acordes.",
        tec="Python · Demucs · librosa · PyQt5",
        lead="Programa de computador que separa voz e instrumentos de uma música, identifica andamento, tom e acordes e permite mixar, mudar tom e velocidade e exportar. Tem uma versão dedicada a guitarras.",
        ficha=[("Tipo", "Uso próprio"), ("Separação", "Demucs"), ("Análise", "librosa"), ("Interface", "PyQt5 e tkinter")],
        stack=["Python", "PyTorch", "Demucs", "librosa", "rubberband", "PyQt5"])

projeto(slug="elicitador", area="produtos", nome="Elicitador de requisitos",
        resumo="Roteiro de levantamento de requisitos em fases, com conferência e diagramas.",
        tec="Python · YAML · Mermaid",
        lead="Roteiro de levantamento de requisitos descrito em YAML, com um script que confere a consistência entre fases e gera os diagramas.",
        ficha=[("Tipo", "Método"), ("Formato", "YAML"), ("Diagramas", "Mermaid"), ("Conferência", "Script em Python")],
        stack=["Python", "YAML", "Mermaid"])


# ================================================================ casos detalhados
# Cada arquivo ferramentas/casos/<slug>.py define CASO = {...}.
# Projeto já listado acima: as chaves de CASO substituem as do registro (lead, ficha, numeros, blocos, stack, link...).
# Projeto novo: CASO traz também nome, resumo, tec e area.
def _carregar_casos():
    import importlib.util
    from pathlib import Path
    pasta = Path(__file__).parent / "casos"
    por_slug = {p["slug"]: p for p in P}
    for arq in sorted(pasta.glob("*.py")):
        if arq.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"casos.{arq.stem}", arq)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        caso = dict(mod.CASO)
        slug = caso.setdefault("slug", arq.stem)
        if slug in por_slug:
            por_slug[slug].update(caso)
        else:
            faltam = [k for k in ("nome", "resumo", "tec", "area") if k not in caso]
            assert not faltam, f"{arq.name}: faltam {faltam}"
            caso.setdefault("stack", [])
            P.append(caso)
            por_slug[slug] = caso


_carregar_casos()
