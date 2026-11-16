/* Catálogo do portfólio: áreas, projetos e links.
   caso: página de estudo de caso neste portfólio; link: site ou código público. */
window.AREAS = [
  { id: 'saude', nome: 'Saúde e aprendizado de máquina', curto: 'Saúde e ML', cor: '#4FD1D4', texto: 'Modelos preditivos, economia da saúde e painéis para gestor público e indústria farmacêutica.' },
  { id: 'campo', nome: 'Campo, território e infraestrutura', curto: 'Campo e território', cor: '#5CC98A', texto: 'Coleta de dados onde não há sinal, mapas nacionais e bases municipais completas.' },
  { id: 'comercio', nome: 'Lojas virtuais e marketplaces', curto: 'Lojas e marketplaces', cor: '#C9E36A', texto: 'Catálogo, carrinho, pagamento, frete, estoque integrado e pedido pelo WhatsApp.' },
  { id: 'gestao', nome: 'Sistemas de gestão e plataformas', curto: 'Sistemas e plataformas', cor: '#4FB3E8', texto: 'Fluxos com aprovação, assinatura digital, perfis de acesso e regras de negócio no banco.' },
  { id: 'dados', nome: 'Dados públicos e inteligência', curto: 'Dados e inteligência', cor: '#FFD25E', texto: 'Extração, conferência e painéis com bases oficiais e sistemas internos de grande porte.' },
  { id: 'produtos', nome: 'Aplicativos, jogos e IA', curto: 'Apps, jogos e IA', cor: '#D3A574', texto: 'Produtos próprios: apps de celular, jogo em tempo real, áudio e vídeo com inteligência artificial.' }
];

window.PROJETOS = [
  // saúde
  { id: 'risco-cardiovascular', area: 'saude', titulo: 'Risco cardiovascular com TabPFN', resumo: 'Cinco algoritmos comparados para prever doença cardiovascular depois dos 55 anos, com Boruta e SHAP.', tec: 'Python · TabPFN · CatBoost · SHAP', selo: 'Código aberto', caso: true, link: 'https://github.com/Bruno-LSo/ML-Health-TABPFN', destaque: true, ml: true },
  { id: 'calculadora-avc', area: 'saude', titulo: 'Calculadora de custos do AVC', resumo: 'Impacto orçamentário de tenecteplase e alteplase por território, com sequelas em 5 anos. Para a Boehringer Ingelheim.', tec: 'JavaScript · Supabase · PostgreSQL · Python', selo: 'Estudo de caso', caso: true, destaque: true },
  { id: 'telemedicina-avc', area: 'saude', titulo: 'Telemedicina no AVC em São Paulo', resumo: 'Custo de 16 plantões presenciais contra um por vídeo, recurso não captado e resultados de 2023 a 2025.', tec: 'Python · pandas · ReportLab · SVG', selo: 'Estudo de caso', caso: true },
  { id: 'estatistica-avc', area: 'saude', titulo: 'Estrutura de saúde e letalidade do AVC', resumo: 'Testes estatísticos nas 27 UFs: tomógrafos, neurologistas e trombólise contra a letalidade.', tec: 'Python · SciPy · Spearman · Kruskal-Wallis', selo: 'Estudo de caso', caso: true, ml: true },
  { id: 'covid', area: 'saude', titulo: 'Painel da COVID-19 no Brasil', resumo: 'Casos e óbitos por estado de 2020 a 2025, mapa clicável e comparação entre estados.', tec: 'Python · Dash · Plotly', selo: 'Código aberto', link: 'https://github.com/Bruno-LSo/DashCovid19' },
  { id: 'formatador', area: 'saude', titulo: 'Formatador de pareceres técnicos', resumo: 'Junta pareceres de revisores de capítulos de vigilância em saúde e destaca só o texto novo, num Word padronizado.', tec: 'Python · Docling · python-docx · difflib', selo: 'Ferramenta interna' },
  // campo
  { id: 'pesca-artesanal', area: 'campo', titulo: 'Monitoramento da pesca artesanal', resumo: 'Fichas de pesca registradas no celular sem sinal, painel por perfil e dado sensível protegido no banco.', tec: 'PWA · PostgreSQL · RLS · ECharts', selo: 'Painel no ar', caso: true, destaque: true },
  { id: 'pontes-brasil', area: 'campo', titulo: 'Pontes do Brasil', resumo: '147.327 pontes, viadutos e passarelas do OpenStreetMap localizados em 5.051 municípios.', tec: 'Python · geopandas · osmium · Leaflet', selo: 'Estudo de caso', caso: true },
  { id: 'saneamento', area: 'campo', titulo: 'Saneamento em todos os municípios', resumo: 'Água, esgoto, perdas e investimento de 5.570 municípios, de 2010 a 2024, em 419.850 linhas.', tec: 'Python · coleta paralela · Excel', selo: 'Base entregue' },
  { id: 'pomap', area: 'campo', titulo: 'PoMap, mapa de árvores frutíferas', resumo: 'App para achar e cadastrar árvores frutíferas perto de você, com 45 espécies, rotas e plano premium.', tec: 'Flutter · Firebase · Google Maps', selo: 'Estudo de caso', caso: true },
  { id: 'localizador', area: 'campo', titulo: 'Localizador por coordenadas', resumo: 'Cola uma coordenada em qualquer formato e vê o lugar no mapa; também completa planilhas com o endereço.', tec: 'JavaScript · Leaflet · OpenStreetMap', selo: 'Site no ar', link: 'https://bruno-lso.github.io/LocalizadorPorLongitudeELatitude/' },
  // comércio
  { id: 'canteiros-urbanos', area: 'comercio', titulo: 'Canteiros Urbanos', resumo: 'Loja de hortaliças e temperos com cesta recorrente, pedido pelo WhatsApp e métricas por bairro.', tec: 'React · Node.js · MongoDB · Redis', selo: 'Estudo de caso', caso: true, destaque: true },
  { id: 'emede', area: 'comercio', titulo: 'EMEDE, moda com estoque em tempo real', resumo: 'Loja integrada ao Bling, Mercado Pago e Melhor Envio, especificada a partir de 3.743 cadastros reais.', tec: 'Supabase · Edge Functions · Bling · Mercado Pago', selo: 'Estudo de caso', caso: true },
  { id: 'curae', area: 'comercio', titulo: 'CurAê, queijos da Mantiqueira', resumo: 'Compra coletiva de queijo artesanal que virou vitrine: cupons, revenda, rateio de frete e cobrança por Pix.', tec: 'Python · Supabase · Resend · Three.js', selo: 'Estudo de caso', caso: true },
  { id: 'vm-merch', area: 'comercio', titulo: 'Loja da VM Solutions', resumo: 'Loja de produtos da marca com pagamento, estorno, acompanhamento público do pedido e painel com 2FA.', tec: 'Supabase · Mercado Pago · Resend', selo: 'Site no ar', link: 'https://www.vmsolutions.tech/merch/' },
  // gestão
  { id: 'plataforma-inspetores', area: 'gestao', titulo: 'Plataforma de Inspetores do Crea-SP', resumo: 'Da indicação à posse e ao fim do mandato de cerca de 2.600 inspetores, na web e no celular, com assinatura gov.br.', tec: 'Next.js · Expo · Supabase · Playwright', selo: 'Estudo de caso', caso: true, destaque: true },
  { id: 'pericias', area: 'gestao', titulo: 'Plataforma de perícias judiciais', resumo: 'Acompanha processos em 57 tribunais, calcula honorários e monta laudos para peritos de engenharia.', tec: 'Supabase · Playwright · IA com fonte citada', selo: 'Estudo de caso', caso: true },
  { id: 'advinhae', area: 'gestao', titulo: 'AdvinhAê, bolão entre amigos', resumo: 'Bolões em 7 esportes com placar atualizado por robô a cada 5 minutos, trava no banco e ranking.', tec: 'React · Supabase · pg_cron · TheSportsDB', selo: 'Estudo de caso', caso: true },
  { id: 'conselheiros', area: 'gestao', titulo: 'Painel dos conselheiros do Crea-SP', resumo: 'Pauta, relatos e votos em 9 câmaras, com carga incremental de dois sistemas e conferência automática.', tec: 'SQL Server · Playwright · Supabase', selo: 'Em uso' },
  { id: 'programa-mulher', area: 'gestao', titulo: 'Programa Mulher 2026', resumo: 'Os 27 Creas planejam e acompanham as ações do programa num painel com metas, eixos e ranking.', tec: 'Alpine.js · Supabase · Python', selo: 'Em uso' },
  { id: 'homecook', area: 'gestao', titulo: 'HomeCook, gestão de cozinha', resumo: 'Produtos, estoque, clientes, vendas, cursos e eventos de um negócio de culinária, sobre planilha Google.', tec: 'Python · Dash · Flask · Google Sheets', selo: 'Sistema entregue' },
  { id: 'planner', area: 'gestao', titulo: 'Planner de projetos do Gabinete', resumo: 'Quadros, tarefas, anexos e registro de alterações no estilo Planner, para a equipe do Gabinete.', tec: 'HTML · Supabase', selo: 'Em uso' },
  // dados
  { id: 'painel-confea', area: 'dados', titulo: 'Painel do Sistema Confea/Crea', resumo: '1.222.610 profissionais por UF, sexo, idade, títulos, anuidades e fluxo de registros.', tec: 'SQL Server · Python · pandas', selo: 'Estudo de caso', caso: true },
  { id: 'formados-registrados', area: 'dados', titulo: 'Da faculdade ao registro', resumo: 'Ingressantes, concluintes e novos registros em engenharia de 2010 a 2024: de cada 100 que entram, 17 se registram.', tec: 'Python · INEP · Plotly', selo: 'Site no ar', caso: true, link: 'https://bruno-lso.github.io/InepCNF/', ml: false },
  { id: 'acervo-tecnico', area: 'dados', titulo: 'Prioridade no Acervo Técnico', resumo: 'Ordena 1.365 pedidos de certidão pelo valor do edital e pela data da licitação, com alerta de capital.', tec: 'DB2 · Python · Plotly', selo: 'Estudo de caso', caso: true },
  { id: 'mapa-profissoes', area: 'dados', titulo: 'Mapa das profissões', resumo: 'Cursos de engenharia, agronomia e geociências em 3.175 municípios, de 2010 a 2024, presencial e EaD.', tec: 'Python · INEP · IBGE', selo: 'Painel entregue' },
  { id: 'caged', area: 'dados', titulo: 'Emprego formal na engenharia', resumo: 'Novo CAGED cruzado com as profissões do sistema: 206.333 movimentações e vagas públicas abaixo do piso.', tec: 'Python · Parquet · CAGED', selo: 'Painel entregue' },
  { id: 'toshi-caged', area: 'dados', titulo: 'Extrator do Novo CAGED', resumo: 'Baixa e traduz os microdados oficiais de emprego e entrega um CSV único e um painel.', tec: 'Python · pandas · Parquet', selo: 'Site no ar', link: 'https://bruno-lso.github.io/ToshiCaged/' },
  { id: 'cozinhas', area: 'dados', titulo: 'Cozinhas Solidárias', resumo: 'Consolida 26 planilhas estaduais com a base federal e gera painel, Word e PDF com a lista das cozinhas.', tec: 'Python · pandas · ReportLab', selo: 'Entregue' },
  { id: 'renda-real', area: 'dados', titulo: 'Renda Real, calculadora com o Banco Central', resumo: 'Juros compostos, viver de renda e correção pela inflação com o IPCA atualizado ao vivo.', tec: 'JavaScript · API do Banco Central', selo: 'Site no ar', link: 'https://bruno-lso.github.io/PrevisaoOrcamentariaApiBacen/' },
  // produtos
  { id: 'alien-crue', area: 'produtos', titulo: 'GXxT, jogo no mapa real', resumo: 'Jogo online em tempo real em que se disputa território na própria cidade, com dia e noite reais.', tec: 'TypeScript · Three.js · WebSocket · Supabase', selo: 'Estudo de caso', caso: true },
  { id: 'warncare', area: 'produtos', titulo: 'WarnCare, controle de remédios', resumo: 'Lê receitas e caixas por foto com IA e avisa quando o remédio está acabando.', tec: 'Flutter · Firebase · Vision · Gemini', selo: 'Protótipo' },
  { id: 'american-legends', area: 'produtos', titulo: 'American Legends, vídeos narrados', resumo: 'Linha de produção que transforma roteiro em vídeo: narração, efeitos, legendas e montagem final.', tec: 'Python · TTS · Whisper · FFmpeg', selo: 'Canal próprio' },
  { id: 'mr-yalc', area: 'produtos', titulo: 'Mr. Yalc, separador de instrumentos', resumo: 'Separa voz e instrumentos de uma música e mostra andamento, tom e acordes; versão só para guitarras.', tec: 'Python · Demucs · librosa · PyQt5', selo: 'Uso próprio' },
  { id: 'transcritor', area: 'produtos', titulo: 'Transcritor de áudio', resumo: 'Áudios e reuniões em texto, em lote, com tempo por palavra, usando a placa de vídeo.', tec: 'Python · faster-whisper', selo: 'Uso próprio' },
  { id: 'nucleo-dados', area: 'produtos', titulo: 'Núcleo de dados', resumo: 'Pacote comum a todos os projetos: guarda e recupera arquivos num banco central, idênticos ao original.', tec: 'Python · Supabase Storage · zstd', selo: 'Infraestrutura' },
  { id: 'elicitador', area: 'produtos', titulo: 'Elicitador de requisitos', resumo: 'Roteiro de levantamento de requisitos em fases, conferido por script e com diagramas gerados.', tec: 'Python · YAML · Mermaid', selo: 'Método' }
];

(function () {
  const base = location.pathname.includes('/casos/') ? '' : 'casos/';
  const area = (id) => window.AREAS.find((a) => a.id === id);
  window.urlProjeto = (p) => (p.caso ? base + p.id + '.html' : p.link || null);
  window.cardProjeto = function (p) {
    const a = area(p.area), url = window.urlProjeto(p), ext = url && !p.caso;
    const tag = url ? 'a' : 'div';
    const attrs = url ? ` href="${url}"${ext ? ' rel="noopener"' : ''}` : '';
    const ir = url ? `<span class="card__ir">${p.caso ? 'Ver estudo de caso' : 'Abrir'} <span class="seta" aria-hidden="true">→</span></span>` : '';
    return `<${tag} class="card" style="--c:${a.cor}"${attrs}><div class="card__topo"><span class="card__area"><b></b>${a.curto}</span><span class="card__selo">${p.selo}</span></div><h3>${p.titulo}</h3><p>${p.resumo}</p><span class="card__tec">${p.tec}</span>${ir}</${tag}>`;
  };
  // "continue vendo" nas páginas de caso: outros casos da mesma área primeiro
  document.querySelectorAll('[data-proximos]').forEach((el) => {
    const atual = window.PROJETOS.find((p) => p.id === el.dataset.proximos);
    const casos = window.PROJETOS.filter((p) => p.caso && p.id !== atual.id);
    const lista = casos.filter((p) => p.area === atual.area).concat(casos.filter((p) => p.area !== atual.area && p.destaque)).slice(0, 3);
    el.innerHTML = lista.map(window.cardProjeto).join('');
  });
})();
