"""Gera as páginas de caso em casos/ a partir do conteúdo abaixo.

Uso: python ferramentas/gerar_casos.py
As páginas feitas à mão (risco-cardiovascular, calculadora-avc, telemedicina-avc,
canteiros-urbanos, pesca-artesanal) não são tocadas.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import modelo as M  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
AREAS = {
    "saude": "Saúde e aprendizado de máquina", "campo": "Campo, território e infraestrutura",
    "comercio": "Lojas virtuais e marketplaces", "gestao": "Sistemas de gestão e plataformas",
    "dados": "Dados públicos e inteligência", "produtos": "Aplicativos, jogos e IA",
}
CASOS = []


def caso(**c):
    CASOS.append(c)


# ---------------------------------------------------------------- saúde
caso(
    slug="estatistica-avc", area="saude", acento="#4FD1D4", aba="Estrutura de saúde e letalidade do AVC",
    descricao="Testes estatísticos nas 27 UFs para saber se tomógrafos, neurologistas e trombólise acompanham menor letalidade do AVC.",
    h1="Mais tomógrafo, menos morte? <em>A estatística responde</em>",
    lead="Uma pesquisadora em saúde pública precisava saber, com rigor, se a estrutura de atendimento de cada estado explica as diferenças de letalidade do AVC. Apliquei correlação de Spearman, Kruskal-Wallis e Mann-Whitney nas 27 UFs e entreguei relatórios em texto e Excel prontos para o artigo.",
    ficha=[("Cliente", "Pesquisa em saúde pública"), ("Unidade", "27 unidades da federação"), ("Testes", "Spearman, Kruskal-Wallis, Mann-Whitney, t, Shapiro-Wilk"), ("Entrega", "Relatórios em texto e Excel com 7 abas")],
    kpis=[("−0,566", "correlação entre taxa de trombólise e letalidade (p = 0,002)"), ("16,6%", "letalidade média do AVC entre as UFs, de 12,2% a 26,2%"), ("12,9% × 17,9%", "letalidade média no Sul contra o Norte"), ("p = 0,26", "centros habilitados sozinhos não mostraram diferença significativa")],
    blocos=[
        ("Resultados", "Quem anda junto com a letalidade", "Correlação de Spearman de cada indicador com a letalidade do AVC. Quanto mais negativa, mais o indicador alto acompanha letalidade baixa. As três são significativas a 5%.",
         M.painel("spearman.py", '<div id="g-sp"></div>', "ρ de Spearman em 27 UFs. Trombólise p = 0,0021; tomógrafos p = 0,0047; neurologistas p = 0,0129.")),
        ("Diferença regional", "Letalidade média por região", "Kruskal-Wallis confirma que as regiões são diferentes (H = 10,43, p = 0,034), assim como a oferta de tomógrafos e de neurologistas.",
         M.painel("", '<div id="g-reg"></div>')),
        ("Escopo", "O que foi entregue", "", M.lista([
            ("Correlações", "Spearman entre letalidade, tomógrafos, neurologistas e trombólise, e entre os próprios indicadores."),
            ("Comparação regional", "Kruskal-Wallis entre as cinco regiões para cada indicador."),
            ("Centros habilitados", "Mann-Whitney, teste t, tamanho de efeito e correlação ponto-bisserial entre UFs com e sem centro."),
            ("Pressupostos conferidos", "Normalidade por Shapiro-Wilk e variância por Levene antes de escolher o teste."),
            ("Excel com 7 abas", "Resumo, estatísticas, dados, normalidade, testes, regional e interpretações em linguagem simples."),
            ("Leitura honesta", "O resultado que não deu diferença também está lá, explicado, em vez de escondido."),
        ])),
    ],
    stack=["Python", "pandas", "NumPy", "SciPy", "openpyxl"],
    script="""<script>
G.barrasH(document.getElementById('g-sp'),[{rotulo:'Taxa de trombólise',valor:.566,destaque:true},{rotulo:'Tomógrafos / 100 mil',valor:.527,cor:'#4FB3E8'},{rotulo:'Neurologistas / 100 mil',valor:.472,cor:'#3B5566'}],{max:.7,esquerda:180,formato:v=>'−'+G.fmt(v,3),titulo:'Correlação com a letalidade'});
G.barrasH(document.getElementById('g-reg'),[{rotulo:'Norte',valor:17.95,cor:'#F08A7E'},{rotulo:'Nordeste',valor:17.88,cor:'#F08A7E'},{rotulo:'Sudeste',valor:15.79,cor:'#3B5566'},{rotulo:'Centro-Oeste',valor:14.73,cor:'#3B5566'},{rotulo:'Sul',valor:12.91,destaque:true}],{min:8,max:20,esquerda:120,formato:v=>G.fmt(v,1)+'%',titulo:'Letalidade média por região'});
</script>""",
)

# ---------------------------------------------------------------- campo
caso(
    slug="pontes-brasil", area="campo", acento="#5CC98A", aba="Pontes do Brasil",
    descricao="Levantamento nacional de 147.327 pontes, viadutos e passarelas a partir do OpenStreetMap e das malhas do IBGE, com mapa, mapa de calor e exportação em oito formatos.",
    h1="Todas as pontes do país <em>num mapa só</em>",
    lead="Não existia uma base nacional aberta, localizada por município, das pontes e viadutos do Brasil, e a fonte oficial não respondeu. Montei a base do zero a partir do OpenStreetMap: 1,96 GB de mapa processados, cada estrutura classificada, medida e ligada ao seu município pelas malhas do IBGE.",
    ficha=[("Instituição", "CONFEA"), ("Fontes", "OpenStreetMap e IBGE (malhas 2022)"), ("Entrega", "Painel com mapa, base e 8 formatos de arquivo"), ("Cobertura", "27 UFs e 5.051 municípios")],
    kpis=[("147.327", "pontes, viadutos, passarelas e aquedutos mapeados"), ("6.177 km", "de estruturas somadas, média de 41,9 m cada"), ("100%", "localizadas no município pela junção espacial"), ("8", "formatos de saída: KML, KMZ, GeoJSON, Shapefile, GeoPackage, GPX, Excel e CSV")],
    blocos=[
        ("Por tipo", "O que foi encontrado", "Classificação automática pelas marcações do OpenStreetMap.",
         M.painel("pontes_brasil_metadata.json", '<div id="g-tipo"></div>')),
        ("Pipeline", "Sete etapas, do arquivo bruto ao mapa", "",
         M.fluxo([("01", "Download", "Arquivo do Brasil inteiro e malhas municipais do IBGE."),
                  ("02", "Extração", "Leitura com osmium de tudo que é ponte, viaduto ou passarela."),
                  ("03", "Processamento", "Comprimento por Haversine, área estimada e remoção de duplicadas."),
                  ("04", "Geocodificação", "Junção espacial com município e UF."),
                  ("05", "Cruzamento", "Totais por estado e município, com as maiores estruturas."),
                  ("06", "Visualização", "Painel com mapa, mapa de calor e indicadores."),
                  ("07", "Exportação", "Um arquivo por estado em cada formato.")])),
        ("Estados", "Onde estão as pontes", "São Paulo e Minas Gerais somam 31% das estruturas. Entre os municípios, Rio de Janeiro lidera com 3.045 e São Paulo vem em seguida com 2.790.",
         M.painel("", '<div id="g-uf"></div>')),
    ],
    stack=["Python", "osmium", "geopandas", "shapely", "pyproj", "Leaflet", "leaflet.heat", "Chart.js"],
    script="""<script>
G.barrasH(document.getElementById('g-tipo'),[{rotulo:'Rodoviárias',valor:114565,destaque:true},{rotulo:'Passarelas',valor:15564,cor:'#9CC43B'},{rotulo:'Sem tipo definido',valor:7215,cor:'#3B5566'},{rotulo:'Viadutos',valor:5640,cor:'#1FA5A8'},{rotulo:'Ferroviárias',valor:4236,cor:'#D3A574'},{rotulo:'Aquedutos',valor:106,cor:'#4FB3E8'}],{esquerda:150,formato:v=>G.fmt(v),titulo:'Pontes por tipo'});
G.barrasH(document.getElementById('g-uf'),[{rotulo:'São Paulo',valor:24589,destaque:true},{rotulo:'Minas Gerais',valor:21605,destaque:true},{rotulo:'Outras 25 UFs',valor:101133,cor:'#3B5566'}],{esquerda:130,formato:v=>G.fmt(v),titulo:'Pontes por estado'});
</script>""",
)

caso(
    slug="pomap", area="campo", acento="#9CC43B", aba="PoMap",
    descricao="Aplicativo de celular para encontrar e compartilhar árvores frutíferas: mapa, cadastro com foto, rotas, alertas de proximidade e plano premium.",
    h1="O pomar da cidade <em>no bolso</em>",
    lead="Aplicativo para achar e compartilhar árvores frutíferas em espaço público: mangueira na praça, pitangueira na calçada, jabuticabeira no parque. O usuário vê as árvores perto dele, cadastra novas com foto e localização, monta rotas e recebe aviso quando passa perto de uma.",
    ficha=[("Tipo", "Produto próprio"), ("Plataformas", "Android e iOS"), ("Idiomas", "Português e inglês"), ("Modelo", "Gratuito com anúncio e plano premium")],
    kpis=[("26", "telas, incluindo área administrativa"), ("45", "tipos de árvore em 5 categorias e 51 subtipos"), ("16", "funções na nuvem: votos, aprovação, assinatura, custo e imagem"), ("~27.900", "linhas de código no aplicativo")],
    blocos=[
        ("Escopo", "O que o app faz", "", M.lista([
            ("Mapa de árvores próximas", "Google Maps com as árvores cadastradas, filtro por tipo e detalhe com fotos e avaliações."),
            ("Cadastro colaborativo", "Foto, localização e tipo; quem usa vota e avalia, e tipos novos passam por aprovação."),
            ("Rotas", "Monte um passeio de coleta e veja o caminho entre as árvores."),
            ("Alerta de proximidade", "Aviso quando você passa perto de uma árvore com fruta, no plano premium."),
            ("Assinatura e anúncio", "Plano mensal ou anual e anúncios para quem usa grátis."),
            ("Custo sob controle", "Monitor de uso: o app entra em modo econômico a 80% do limite diário e em modo de emergência a 95%."),
        ])),
        ("Por que importa", "Feito para crescer sem susto na conta", "",
         M.texto(["App colaborativo costuma morrer de dois jeitos: sem gente cadastrando ou com conta de servidor alta demais. Aqui as duas pontas foram pensadas desde o começo. <strong>Votos e aprovação</strong> mantêm a qualidade do cadastro, e o <strong>monitor de custo</strong> corta o que é caro antes de o limite estourar, com relatório diário de uso."])),
    ],
    stack=["Flutter", "Dart", "Riverpod", "Firebase", "Cloud Functions", "Google Maps e Places", "RevenueCat", "AdMob"],
)

# ---------------------------------------------------------------- comércio
caso(
    slug="emede", area="comercio", acento="#C9E36A", aba="EMEDE",
    descricao="Especificação e arquitetura de loja virtual de moda com estoque em tempo real vindo do Bling, pagamento pelo Mercado Pago e frete pelo Melhor Envio.",
    h1="Moda com o estoque da loja física <em>em tempo real</em>",
    lead="A marca vendia no Instagram e na loja física, com o site parado e o estoque no ERP. Antes de escrever a loja, inspecionei os dados reais: 3.743 cadastros, cores e tamanhos escritos de 12 jeitos diferentes, nenhuma logística integrada. A partir disso especifiquei uma loja leve para celular, ligada ao Bling, ao Mercado Pago e ao Melhor Envio.",
    ficha=[("Cliente", "EMEDE, moda feminina fitness e casual"), ("Integrações", "Bling, Mercado Pago, Melhor Envio"), ("Fase", "Especificada e testada no banco"), ("Base", "Supabase com regras por linha e 2FA")],
    kpis=[("3.743", "cadastros ativos no ERP: 393 produtos pai e 3.326 variações"), ("12", "grafias diferentes de cor e tamanho a padronizar"), ("42", "regras de negócio e 28 requisitos funcionais"), ("29", "cenários de segurança testados no banco antes do código")],
    blocos=[
        ("Diagnóstico", "O que os dados mostraram", "Uma semana de pedidos, lida direto do ERP, virou a base do desenho.",
         M.painel("diagnostico_bling", '<div class="kpis"><div class="kpi"><strong class="num">41</strong><span>pedidos em 7 dias</span></div><div class="kpi"><strong class="num">R$ 283,48</strong><span>ticket médio</span></div><div class="kpi"><strong class="num">2.335</strong><span>peças em estoque em 1.164 variações</span></div><div class="kpi"><strong class="num">22 de 25</strong><span>fretes do ano para o próprio estado</span></div></div>')),
        ("Integração", "Como o estoque chega na vitrine", "",
         M.fluxo([("bling", "ERP é a fonte", "Produto, variação, estoque e nota fiscal vêm do Bling, pela API v3."),
                  ("banco", "Cópia normalizada", "Cor e tamanho padronizados numa tabela única, com trava contra venda sem estoque."),
                  ("vitrine", "Loja no celular", "Vitrines por coleção, compra direta pelo tamanho e sacola lateral."),
                  ("checkout", "Três passos", "Pix ou cartão sem criar conta; frete cotado na hora e etiqueta gerada."),
                  ("painel", "Painel escondido", "Fotos tratadas no navegador, pedidos, etiquetas e permissão de preço por pessoa.")])),
        ("Escopo", "O que foi entregue", "", M.lista([
            ("Visão, escopo e regras", "42 regras de negócio, 28 requisitos funcionais e os não funcionais."),
            ("Oito decisões de arquitetura", "Cada escolha registrada com motivo e alternativa descartada."),
            ("Modelo de dados testado", "Regras de acesso e travas conferidas em 29 cenários automatizados."),
            ("Backlog em 6 fases", "25 tarefas com ordem de entrega e critério de pronto."),
            ("Protótipo visual", "Vitrine, card com bolinhas de cor e compra direta pelo tamanho."),
            ("Operação", "Roteiros de publicação, varredura de segredos no repositório e fluxograma do pedido."),
        ])),
    ],
    stack=["HTML, CSS e JavaScript", "Cloudflare Pages", "Supabase", "Edge Functions", "pg_cron", "Bling API v3", "Mercado Pago", "Melhor Envio", "pgTAP", "Playwright"],
)

caso(
    slug="curae", area="comercio", acento="#FFD25E", aba="CurAê",
    descricao="Site de compra coletiva e vitrine de queijos artesanais com cupons, revenda, rateio de frete, cobrança por Pix e painel do administrador.",
    h1="Do grupo de amigos à <em>vitrine do queijo artesanal</em>",
    lead="Começou como compra coletiva de queijo de um produtor da Serra da Mantiqueira, organizada em planilha. Virou um site com catálogo por categoria, selo de origem, cupons e comissão de revenda, e um painel que fecha a data-limite, rateia o frete e cobra cada pessoa por Pix.",
    ficha=[("Cliente", "Queijaria artesanal de Alagoa, MG"), ("Modelo", "Compra coletiva e revenda"), ("Entrega", "Site, painel e e-mails automáticos"), ("Destaque", "Mapa com o contorno real do município")],
    kpis=[("5", "versões, da planilha à vitrine com várias categorias"), ("~15", "tabelas no banco, com regras por linha"), ("R$ 4,00", "frete estimado por queijo até o rateio real"), ("1", "arquivo de página que roda até sem servidor, no modo demonstração")],
    blocos=[
        ("Escopo", "O que o site resolve", "", M.lista([
            ("Catálogo com origem", "Categorias, selo de origem e a quantidade disponível travada no banco."),
            ("Cupons e figurinhas", "Desconto por código e programa de figurinhas para quem compra sempre."),
            ("Revenda com comissão", "Quem revende ganha comissão calculada pelo sistema."),
            ("Frete justo", "Estimativa por unidade e, depois, rateio do frete real entre os pedidos."),
            ("Data-limite e aviso", "Pedido fecha na data; só quem teve item alterado recebe o aviso."),
            ("Cobrança por Pix", "Cada pessoa vê quanto deve e paga pela chave do produtor."),
        ])),
        ("Identidade", "Um site com cara de queijo", "",
         M.texto(["O visual saiu da própria embalagem: amarelo de casca, marrom de madeira, letras arredondadas. Um queijo em 3D gira na abertura e o mapa mostra o <strong>contorno real do município</strong>, desenhado a partir da malha do IBGE, para dizer de onde o produto vem sem precisar de texto."])),
    ],
    stack=["Python", "JavaScript", "Supabase", "Edge Functions", "Resend", "Three.js"],
)

# ---------------------------------------------------------------- gestão
caso(
    slug="plataforma-inspetores", area="gestao", acento="#4FB3E8", aba="Plataforma de Inspetores",
    descricao="Plataforma web e aplicativo que levam a indicação, validação, nomeação, mandato e encerramento dos inspetores do Crea-SP para um sistema só, com assinatura gov.br.",
    h1="Da indicação à posse, <em>sem planilha e sem e-mail</em>",
    lead="O Crea-SP tem cerca de 2.600 inspetores em 194 unidades. A indicação de cada um passava por planilha, e-mail, conferência manual em três ou quatro sistemas, certidões checadas uma a uma e um dossiê montado à mão. A plataforma leva o processo inteiro para a web e o celular, confere os requisitos na fonte e entrega o dossiê pronto para o processo eletrônico.",
    ficha=[("Instituição", "Crea-SP"), ("Entrega", "Web, aplicativo iOS e Android, banco e integrações"), ("Regras", "Regulamento das Inspetorias 2026"), ("Assinatura", "gov.br")],
    kpis=[("~2.600", "inspetores em 194 unidades com comissão"), ("82", "tabelas, todas com regra de acesso por linha"), ("111", "funções no banco: toda gravação passa por elas"), ("81", "requisitos funcionais, de 55 na primeira versão"), ("61 + 20", "páginas na web e telas no aplicativo")],
    blocos=[
        ("Telas", "Como ficou", "Protótipo navegável, com dados fictícios.",
         '<div style="display:grid;gap:14px"><div class="fig"><img src="../assets/img/casos/inspetores-painel-gerencial.webp" alt="Painel gerencial com nomeados no ano, tempo médio de validação, validados automaticamente e cadeiras livres" width="1400" height="612" loading="lazy"></div><div class="fig"><img src="../assets/img/casos/inspetores-painel-vagas.webp" alt="Painel de vagas de uma regional com unidades, cadeiras ocupadas e situação das cotas" width="1400" height="620" loading="lazy"></div></div><p class="legenda">Painel gerencial e painel de vagas da regional. Nomes e números fictícios do protótipo.</p>'),
        ("No celular", "O indicado resolve tudo pelo aplicativo", "Envio de documentos com link de emissão de cada certidão, e check-in de presença na reunião pelo GPS ou por QR quando não há sinal.",
         '<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;max-width:560px"><div class="fig" style="background:none;box-shadow:none"><img src="../assets/img/casos/inspetores-documentos.webp" alt="Tela de envio de documentos com certidões e status" width="836" height="1612" loading="lazy"></div><div class="fig" style="background:none;box-shadow:none"><img src="../assets/img/casos/inspetores-checkin.webp" alt="Tela de check-in na reunião com distância até a unidade e horário" width="520" height="896" loading="lazy"></div></div>'),
        ("Fluxo", "Sete fases, um processo", "",
         M.fluxo([("01", "Vaga e indicação", "A regional vê as cadeiras livres e as cotas, e indica pelo sistema."),
                  ("02", "Pré-validação", "Pelo CPF, o sistema confere registro, débitos e impedimentos antes de seguir."),
                  ("03", "Documentos", "O indicado envia pelo celular; cada certidão é conferida na fonte oficial."),
                  ("04", "Análise", "Fila do Gabinete com o resumo do currículo e os sinais de atenção."),
                  ("05", "Assinaturas", "Formulário, termo de posse e declarações assinados com gov.br."),
                  ("06", "Dossiê", "PDF único com todos os documentos e o histórico, pronto para o processo eletrônico."),
                  ("07", "Mandato", "Reuniões, presença, faltas, justificativas, regularidade mensal e encerramento.")])),
        ("Engenharia", "Construído para ser auditado", "", M.lista([
            ("Regra no banco, não na tela", "Toda gravação passa por funções do banco, e todas as 82 tabelas têm regra de acesso por linha."),
            ("Regras de negócio testadas", "O regulamento virou um pacote de domínio com testes automatizados."),
            ("Integração simulada e real", "Cada integração tem versão simulada para desenvolver e testar sem depender do sistema externo."),
            ("Acessibilidade conferida", "Testes de ponta a ponta e auditoria de acessibilidade em 6 larguras de tela, nos temas claro e escuro."),
            ("Migrações versionadas", "32 migrações aplicadas só pelo pipeline, nunca à mão."),
            ("Documentação completa", "13 documentos: contexto, especificação, interface, arquitetura, testes e decisões técnicas."),
        ])),
    ],
    stack=["Next.js", "Expo", "TypeScript", "Supabase", "PostgreSQL com RLS", "gov.br", "Playwright", "axe", "GitHub Actions", "Python"],
)

caso(
    slug="pericias", area="gestao", acento="#4FB3E8", aba="Plataforma de perícias",
    descricao="Especificação de plataforma para peritos judiciais: leitura diária dos tribunais, prazos, honorários, modelos de laudo e um robô que só lê.",
    h1="O perito judicial <em>sem perder prazo</em> em nenhum tribunal",
    lead="Um perito de engenharia acompanha processos em vários sistemas de tribunal, cada um com login e jeito próprio, redige peças à mão e controla honorários de forma espalhada. A plataforma lê os tribunais uma vez por dia, transforma cada movimentação em etapa, prazo e tarefa, e prepara os documentos a partir de modelos.",
    ficha=[("Cliente", "Perita judicial de engenharia civil"), ("Fase", "Especificação completa, versão 5.1"), ("Tribunais", "57 levantados"), ("Princípio", "Nada sem fonte")],
    kpis=[("57", "tribunais levantados; um único tradutor atende 15 deles"), ("14", "etapas do ciclo da perícia, da nomeação ao pagamento"), ("620", "documentos de 50 processos analisados para desenhar o fluxo"), ("25", "tabelas no modelo de dados")],
    blocos=[
        ("Arquitetura", "Como a plataforma funciona", "",
         M.fluxo([("cofre", "Credenciais protegidas", "Senhas dos tribunais cifradas e guardadas separadas do banco."),
                  ("robô", "Leitura somente", "Uma vez por dia, só os processos do perito, sem nunca protocolar nada."),
                  ("2FA", "Código pelo WhatsApp", "Quando o tribunal pede código de segurança, a plataforma pergunta ao perito."),
                  ("eventos", "Motor de prazos", "Cada movimentação vira etapa, prazo e tarefa, com aviso."),
                  ("documentos", "Modelos por tipo", "11 modelos de laudo e petições, preenchidos com o que está no processo.")])),
        ("Rigor", "Nada sem fonte", "", M.lista([
            ("Cada campo com origem", "A leitura de decisões cita de qual documento e trecho veio cada informação."),
            ("Conta é código", "Honorários e avaliações são calculados por programa testado, em centavos, nunca estimados."),
            ("Honorários pela tabela", "Hora técnica do IBAPE de cada estado aplicada automaticamente."),
            ("Livro financeiro", "Depósitos, levantamentos e repasses registrados por processo."),
            ("Funciona em campo", "Aplicativo de vistoria que trabalha sem internet."),
            ("Custo previsível", "Estimado em cerca de R$ 6 por mês por perito, além da base fixa."),
        ])),
    ],
    stack=["Supabase", "Playwright", "WhatsApp Business", "Resend", "Python", "ReportLab", "Mermaid"],
)

caso(
    slug="advinhae", area="gestao", acento="#4FB3E8", aba="AdvinhAê",
    descricao="Site de bolão entre amigos com sete esportes, placar atualizado por robô, palpite travado no banco, ranking e convites por e-mail.",
    h1="Bolão entre amigos <em>sem planilha e sem briga</em>",
    lead="Os participantes criam bolões, convidam amigos por e-mail, dão palpites e acompanham o ranking. Os jogos e placares chegam sozinhos de uma base esportiva, e as regras que geram discussão, como palpite fora de hora, ficam travadas no banco.",
    ficha=[("Cliente", "Empreendedor com produto próprio"), ("Esportes", "7, em 3 formatos de campeonato"), ("Entrega", "Site, banco, robô e guia de implantação"), ("Login", "E-mail ou conta Google")],
    kpis=[("5 min", "intervalo do robô que atualiza jogos e placares"), ("10 min", "antes do jogo o palpite trava, e a trava está no banco"), ("13", "tabelas com pontuação, auditoria e ranking"), ("20 · 10 · 0", "pontos para placar exato, acerto do vencedor ou erro")],
    blocos=[
        ("Experimente", "Calcule a pontuação", "A mesma regra do banco: placar exato vale 20, acertar quem vence ou o empate vale 10.",
         M.painel("pontuacao", '<div class="controles"><div class="campo"><label for="pa">Seu palpite: casa <output id="pa-o">2</output></label><input id="pa" type="range" min="0" max="6" value="2"></div><div class="campo"><label for="pb">Seu palpite: visitante <output id="pb-o">1</output></label><input id="pb" type="range" min="0" max="6" value="1"></div><div class="campo"><label for="ra">Resultado: casa <output id="ra-o">2</output></label><input id="ra" type="range" min="0" max="6" value="2"></div><div class="campo"><label for="rb">Resultado: visitante <output id="rb-o">0</output></label><input id="rb" type="range" min="0" max="6" value="0"></div></div><div class="kpi" style="margin-top:16px"><strong class="num" id="pts">10</strong><span id="pts-t" role="status">pontos: acertou quem venceu</span></div>')),
        ("Escopo", "O que foi construído", "", M.lista([
            ("Bolões e convites", "Criação de bolão, convite por e-mail e fuso horário de cada participante."),
            ("Robô de resultados", "Ligas, times e partidas atualizados automaticamente a cada 5 minutos."),
            ("Intra bolão", "Rodadas durante a partida, valendo um décimo dos pontos, quando o grupo quiser."),
            ("Ranking por e-mail", "Classificação atualizada e enviada sozinha ao grupo."),
            ("Pronto para anúncio", "Espaço de anúncio previsto e página de privacidade."),
            ("Guia de implantação", "Banco, e-mail, domínio e login com Google, passo a passo."),
        ])),
    ],
    stack=["React 18", "Supabase", "PostgreSQL", "pg_cron", "Edge Functions", "TheSportsDB", "Resend", "Google OAuth"],
    script="""<script>
(function(){const ids=['pa','pb','ra','rb'],v=i=>+document.getElementById(i).value;
function calc(){ids.forEach(i=>document.getElementById(i+'-o').textContent=v(i));const s=Math.sign(v('pa')-v('pb')),r=Math.sign(v('ra')-v('rb'));let p=0,t='pontos: errou o resultado';
if(v('pa')===v('ra')&&v('pb')===v('rb')){p=20;t='pontos: placar exato'}else if(s===r){p=10;t=r===0?'pontos: acertou o empate':'pontos: acertou quem venceu'}
document.getElementById('pts').textContent=p;document.getElementById('pts-t').textContent=t}
ids.forEach(i=>document.getElementById(i).addEventListener('input',calc));calc()})();
</script>""",
)

# ---------------------------------------------------------------- dados
caso(
    slug="painel-confea", area="dados", acento="#FFD25E", aba="Painel do Sistema Confea/Crea",
    descricao="Painel com o retrato dos profissionais registrados no Sistema Confea/Crea: estoque por UF e sexo, idade, títulos, anuidades e fluxo de registros.",
    h1="O retrato de <em>1,2 milhão de profissionais</em>",
    lead="O painel antigo era uma planilha com gráficos colados. Passei a ler direto do banco nacional de registros, aplicando as regras oficiais de contagem, e a gerar o painel a partir de uma extração com data e hora, para que qualquer número possa ser refeito e conferido.",
    ficha=[("Instituição", "CONFEA, Presidência"), ("Fonte", "Banco nacional de registros"), ("Entrega", "Extração datada e painel web"), ("Período", "Fluxo de registros de 2010 a 2026")],
    kpis=[("1.222.610", "profissionais no estoque, nas 27 UFs"), ("248.033", "mulheres registradas"), ("417", "títulos profissionais diferentes"), ("1939", "ano do registro mais antigo ainda na base")],
    blocos=[
        ("Escopo", "O que o painel mostra", "", M.lista([
            ("Quem são", "Estoque por UF e sexo, pirâmide etária e títulos profissionais."),
            ("De onde vêm e para onde vão", "Coortes de registro e migração entre estados."),
            ("Entradas e saídas", "Ingressos, reingressos e desligamentos, com os últimos 12 meses."),
            ("Anuidades", "Série por ano e UF, ritmo de pagamento, parcelamento e inadimplência recorrente."),
            ("Número que se refaz", "Cada versão sai de um arquivo de extração com data e hora, guardado."),
            ("Regras oficiais", "Consultas validadas contra as regras de contagem do sistema."),
        ])),
        ("Antes e depois", "De planilha a fonte única", "",
         M.texto(["O ganho não é só visual. Antes, cada área tinha o seu número. Agora existe <strong>uma extração oficial com data</strong>, e o painel é só a leitura dela. O próximo passo, já planejado, é levar as regras dos indicadores para dentro do banco, com atualização diária e acesso por perfil."])),
    ],
    stack=["SQL Server", "Python", "pandas", "pymssql", "HTML e JavaScript"],
)

caso(
    slug="formados-registrados", area="dados", acento="#FFD25E", aba="Da faculdade ao registro",
    descricao="Painel que cruza o Censo da Educação Superior com os registros profissionais: ingressantes, concluintes e novos registros em engenharia de 2010 a 2024.",
    h1="De cada 100 que entram em engenharia, <em>17 chegam ao registro</em>",
    lead="Quantos estudantes de engenharia entram na faculdade, quantos se formam e quantos de fato se registram para trabalhar? Cruzei os microdados do INEP com a base de registros, por ano, estado, gênero e modalidade, e publiquei um painel aberto.",
    ficha=[("Instituição", "CONFEA"), ("Fontes", "INEP (Censo da Educação Superior) e registros profissionais"), ("Entrega", "Painel web e planilha Excel"), ("Painel", '<a href="https://bruno-lso.github.io/InepCNF/">Abrir o painel</a>')],
    kpis=[("503.025", "ingressantes em 2014, o pico da série"), ("219.192", "ingressantes em 2024, menos da metade do pico"), ("38 de 100", "concluem seis anos depois de entrar"), ("17 de 100", "chegam ao registro profissional")],
    blocos=[
        ("A série", "Entrar, formar, registrar", "Brasil, de 2010 a 2024.",
         M.painel("bruno-lso.github.io/InepCNF", '<div id="leg" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px"></div><div id="g-funil"></div>', "Brasil em 2010 e 2024, da série publicada. O pico de ingressantes foi em 2014, com 503.025.")),
        ("Escopo", "O que foi entregue", "", M.lista([
            ("Coleta automática", "Raspagem do portal de dados abertos do INEP e homologação dos arquivos."),
            ("Consultas documentadas", "Registros por ano, Crea, gênero e modalidade, com cada consulta explicada."),
            ("Indicador com defasagem", "De cada 100 ingressantes, quantos concluem e se registram seis anos depois."),
            ("Painel aberto", "Publicado na web, com exportação para Excel."),
        ])),
    ],
    stack=["Python", "pandas", "BeautifulSoup", "SQL Server", "Plotly"],
    script="""<script>
const S=[{nome:'Ingressantes',cor:'#FFD25E'},{nome:'Concluintes',cor:'#4FB3E8'},{nome:'Novos registros',cor:'#5CC98A'}];
G.legenda(document.getElementById('leg'),S);
G.colunas(document.getElementById('g-funil'),[{rotulo:'2010',valores:[281011,82936,43882]},{rotulo:'2024',valores:[219192,105064,64486]}],S,{esquerda:64,formatoY:v=>G.fmt(v/1000)+' mil',formato:v=>G.fmt(v),titulo:'Ingressantes, concluintes e novos registros'});
</script>""",
)

caso(
    slug="acervo-tecnico", area="dados", acento="#FFD25E", aba="Prioridade no Acervo Técnico",
    descricao="Painel que ordena os pedidos de certidão de acervo técnico pelo valor do edital e pela data da licitação, com alerta de capital social insuficiente.",
    h1="Analisar primeiro <em>o que vence primeiro</em>",
    lead="Empresas pedem certidão de acervo técnico para disputar licitações, e uma certidão que sai depois da sessão pública não serve para nada. O painel lê os pedidos direto do banco, cruza com o edital de cada um e mostra a fila na ordem que importa: data da sessão e valor em jogo.",
    ficha=[("Instituição", "Crea-SP, Acervo Técnico"), ("Fonte", "Banco DB2 e arquivos dos protocolos"), ("Entrega", "Painel web publicado no servidor interno"), ("Atualização", "Por rotina programada")],
    kpis=[("1.365", "pedidos em análise na data de referência"), ("R$ 25,8 bi", "em editais únicos, sem duplicados"), ("259", "sessões urgentes: vencidas ou em até 3 dias"), ("246", "alertas de capital social abaixo de 10% do edital")],
    blocos=[
        ("Regra", "Como a fila é montada", "",
         M.fluxo([("01", "Pedidos", "Protocolos de certidão de acervo lidos do banco, com o documento de cada um."),
                  ("02", "Edital", "Valor e data da sessão pública extraídos e duplicados removidos."),
                  ("03", "Urgência", "Dias até a sessão: vencidas, até 3 dias, até 7, depois."),
                  ("04", "Risco", "Capital social da empresa menor que 10% do edital acende alerta."),
                  ("05", "Fila", "Ordem final por urgência e valor, com o perfil da empresa e do profissional.")])),
    ],
    stack=["DB2", "Python", "pandas", "Plotly", "SFTP"],
)

# ---------------------------------------------------------------- produtos
caso(
    slug="alien-crue", area="produtos", acento="#D3A574", aba="GXxT, jogo no mapa real",
    descricao="Jogo online em tempo real sobre o mapa do mundo: o jogador usa a própria localização, disputa território e vive dia e noite reais.",
    h1="Um jogo em que o mapa <em>é a sua cidade</em>",
    lead="Jogo online em tempo real sobre o mapa real: o jogador entra pela própria localização, coleta recursos, constrói, enfrenta hordas e disputa território com gangues. O dia e a noite do jogo seguem o sol de verdade na latitude de quem está jogando.",
    ficha=[("Tipo", "Produto próprio"), ("Plataformas", "Navegador, com caminho para Android e iOS"), ("Servidor", "Autoritativo, em tempo real"), ("Modelo", "Só cosméticos pagos")],
    kpis=[("8", "tipos de personagem, cada um com 3 habilidades e árvore de 6 níveis"), ("24", "habilidades montadas com 18 peças reutilizáveis"), ("200", "níveis de progressão, com cerca de 129 milhões de pontos de experiência"), ("10", "tabelas: personagens, mundo, gangues, economia e loja")],
    blocos=[
        ("Escopo", "O que já roda", "", M.lista([
            ("Mapa real com estética própria", "Mapa vetorial escuro com visual neon e imagens de satélite."),
            ("Sol de verdade", "Dia e noite calculados pela elevação do sol na posição do jogador."),
            ("Servidor que manda", "Habilidades, dano e recarga calculados no servidor, para evitar trapaça."),
            ("Construção persistente", "O que se constrói no mapa fica salvo para todos."),
            ("Gangues e economia fechada", "Território, relações entre gangues e moeda com registro de cada movimento."),
            ("Justo para quem não paga", "Só itens visuais são vendidos; poder no jogo se conquista jogando."),
        ])),
    ],
    stack=["TypeScript", "Three.js", "PixiJS", "WebSocket", "Node.js", "Supabase", "Vite", "Capacitor"],
)


def gerar():
    for c in CASOS:
        partes = [M.TOPO.format(titulo_aba=c["aba"], descricao=c["descricao"], acento=c["acento"], css=c.get("css", "")),
                  M.hero(c, AREAS[c["area"]], c["area"]), M.kpis(c["kpis"])]
        for rot, tit, txt, corpo in c["blocos"]:
            partes.append(M.bloco(rot, tit, txt, corpo))
        partes += [M.stack(c["stack"]), M.proximos(c["slug"]), M.RODAPE.format(script=c.get("script", ""))]
        destino = RAIZ / "casos" / f"{c['slug']}.html"
        destino.write_text("".join(partes), encoding="utf-8")
        print("gerado", destino.name)


if __name__ == "__main__":
    gerar()
