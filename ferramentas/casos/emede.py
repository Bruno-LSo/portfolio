import modelo as M

SLUG = "emede"


def _cx(x, y, w, h, tit, sub, cor="#4FD1D4"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#162A37" stroke="{cor}"/>'
    if sub:
        s += f'<text x="{x + w / 2:.0f}" y="{y + h / 2 - 4:.0f}" fill="#EAF1F6">{tit}</text><text x="{x + w / 2:.0f}" y="{y + h / 2 + 16:.0f}" fill="#A9B8C6" font-size="13">{sub}</text>'
    else:
        s += f'<text x="{x + w / 2:.0f}" y="{y + h / 2 + 5:.0f}" fill="#EAF1F6">{tit}</text>'
    return s


_INTEG = ('<svg viewBox="0 0 960 380" role="img" aria-label="Integrações da loja: loja e painel na Cloudflare, Supabase no centro, Bling, Mercado Pago e Melhor Envio">'
          '<defs><marker id="emede-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
          '<g font-family="Sora" font-size="14" text-anchor="middle">'
          + _cx(10, 40, 150, 64, "Cliente", "navegador", "#A9B8C6")
          + _cx(10, 270, 150, 64, "Equipe", "login com 2 fatores", "#A9B8C6")
          + _cx(210, 40, 190, 64, "Loja", "Cloudflare Pages", "#4FB3E8")
          + _cx(210, 270, 190, 64, "Painel", "fotos, pedidos, etiquetas", "#4FB3E8")
          + '<rect x="430" y="96" width="210" height="190" rx="12" fill="#162A37" stroke="#4FD1D4" stroke-width="2"/>'
          '<text x="535" y="126" fill="#EAF1F6" font-size="15">Supabase</text>'
          '<text x="535" y="156" fill="#A9B8C6" font-size="13">Postgres com RLS</text>'
          '<text x="535" y="180" fill="#A9B8C6" font-size="13">Edge Functions</text>'
          '<text x="535" y="204" fill="#A9B8C6" font-size="13">fila e pg_cron</text>'
          '<text x="535" y="228" fill="#A9B8C6" font-size="13">Vault com os tokens</text>'
          '<text x="535" y="252" fill="#A9B8C6" font-size="13">Storage das fotos</text>'
          + _cx(700, 20, 240, 70, "Bling API v3", "estoque, preço, pedido, nota", "#FFD25E")
          + _cx(700, 156, 240, 70, "Mercado Pago", "Pix e cartão, aviso assinado", "#5CC98A")
          + _cx(700, 292, 240, 70, "Melhor Envio", "cotação, etiqueta, rastreio", "#F08A7E")
          + '<text x="820" y="118" fill="#A9B8C6" font-size="13">venda na loja física baixa o estoque</text>'
                    '</g>'
          '<g stroke="#4FD1D4" stroke-width="2" fill="none">'
          '<path d="M160 72 H206" marker-end="url(#emede-seta)"/>'
          '<path d="M160 302 H206" marker-end="url(#emede-seta)"/>'
          '<path d="M400 72 C415 72 420 110 428 130" marker-end="url(#emede-seta)"/>'
          '<path d="M400 302 C415 302 420 270 428 255" marker-end="url(#emede-seta)"/>'
          '<path d="M640 140 C670 120 680 70 696 60" marker-end="url(#emede-seta)"/>'
          '<path d="M640 191 H696" marker-end="url(#emede-seta)"/>'
          '<path d="M640 240 C670 260 680 310 696 322" marker-end="url(#emede-seta)"/>'
          '</g>'
          '<path d="M400 52 H650 C680 52 672 176 696 184" stroke="#5CC98A" stroke-width="1.5" stroke-dasharray="5 5" fill="none" marker-end="url(#emede-seta)"/>'
          '<text x="525" y="40" fill="#5CC98A" font-family="Sora" font-size="13" text-anchor="middle">pagamento do Mercado Pago dentro da loja</text>'
          '</svg>')

_ESTOQUE = ('<svg viewBox="0 0 960 200" role="img" aria-label="Sincronização do estoque: venda na loja física, aviso do Bling, caixa de entrada, fila e conferência periódica">'
            '<defs><marker id="emede-seta2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
            '<g font-family="Sora" font-size="14" text-anchor="middle">'
            + _cx(10, 50, 160, 70, "Loja física", "venda no Bling", "#FFD25E")
            + _cx(205, 50, 170, 70, "Aviso do Bling", "assinatura conferida", "#FFD25E")
            + _cx(410, 50, 170, 70, "Caixa de entrada", "resposta em até 5 s", "#4FD1D4")
            + _cx(615, 50, 150, 70, "Fila", "3 req/s no Bling", "#4FD1D4")
            + _cx(800, 50, 150, 70, "Site", "saldo atualizado", "#4FB3E8")
            + '<text x="560" y="168" fill="#A9B8C6" font-size="13">conferência completa a cada 15 min e de madrugada corrige avisos perdidos</text>'
            '</g><g stroke="#4FD1D4" stroke-width="2" fill="none">'
            '<path d="M170 85 H201" marker-end="url(#emede-seta2)"/><path d="M375 85 H406" marker-end="url(#emede-seta2)"/>'
            '<path d="M580 85 H611" marker-end="url(#emede-seta2)"/><path d="M765 85 H796" marker-end="url(#emede-seta2)"/>'
            '<path d="M875 120 V150 H690 V124" stroke-dasharray="5 5" marker-end="url(#emede-seta2)"/></g></svg>')

CASO = dict(
    numeros=[("73", "peças à venda na loja: 45 fitness e 28 casual"), ("3.326", "variações de cor e tamanho no Bling"),
             ("42", "regras de negócio"), ("29", "cenários de segurança testados no banco")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-vitrine.webp", "Vitrine: marca, novidades e faixas por coleção."),
            ("02-colecao.webp", "Coleção Fitness: 45 peças, grade de 2, 4 ou 6 colunas e cores de cada peça."),
            ("05-filtro.webp", "Filtrar e ordenar: preço, tamanho e cor, com a contagem de peças."),
            ("03-peca.webp", "Peça: fotos, cor, tamanho, guia de medidas e compra pelo WhatsApp."),
            ("04-sacola.webp", "Sacola lateral: cor, tamanho, quantidade e total."),
            ("06-checkout.webp", "Checkout em 3 passos, sem cadastro: identificação, entrega e pagamento."),
        ]), "Capturas da loja no ar em 16/11/2026, sem compra.", "larga"),
        ("No celular", M.telas(SLUG, [
            ("07-colecao-celular.webp", "Coleção com 2 colunas e filtro no topo."),
            ("08-peca-celular.webp", "Peça com fotos em carrossel."),
        ], celular=True), "Capturas em 390 px de largura.", "larga"),
        ("Fluxo de compra", M.fluxograma([
            ("Entrada", ["Vitrine", ("Coleções", "Fitness, Casual, Novidades"), "Busca"]),
            ("Escolha", [("Peça", "cor, tamanho, medidas"), ("Filtro", "preço, tamanho, cor"), "Favoritos"], "adiciona"),
            ("Sacola", [("Sacola lateral", "quantidade e total"), ("WhatsApp", "mensagem com peça, cor e tamanho")], "finaliza"),
            ("Checkout", [("1. Identificação", "e-mail, nome, CPF, celular"), ("2. Entrega", "CEP e cotação do frete"), ("3. Pagamento", "Pix ou cartão")], "reserva as peças"),
            ("Depois do pagamento", [("Confirmação", "e-mail com o link do pedido"), ("Bling", "pedido de venda e nota"), ("Etiqueta", "Melhor Envio e rastreio")]),
        ], "A peça fica reservada por 20 minutos no cartão e 30 minutos no Pix. Sem pagamento, ela volta ao site."), "", "larga"),
        ("Integrações", M.diagrama(_INTEG, "O Bling é o dono do estoque, do preço e da nota. A loja lê o catálogo e nunca grava estoque nem preço."), "", "larga"),
        ("Estoque em tempo real", M.diagrama(_ESTOQUE, "Toda escrita no Bling e no Melhor Envio passa por uma fila no banco, com nova tentativa em caso de falha."), "", "larga"),
        ("Regras do pedido", M.lista([
            ("Saldo no site", "Soma dos depósitos do Bling menos as peças reservadas em pagamentos em andamento."),
            ("Última peça", "Duas clientes não compram a mesma última peça. A segunda é avisada antes de pagar."),
            ("Pix atrasado", "Pix pago depois do prazo, com a peça já vendida, vai para Problemas com botão de reembolso."),
            ("Preço e frete", "Recalculados no servidor antes de criar o pagamento."),
            ("Avisos", "Assinatura conferida, gravação única por aviso e processamento fora da resposta."),
            ("Acesso", "Regras por linha em todas as tabelas e dois fatores para a equipe."),
        ])),
        ("Levantamento", M.painel("", '<div class="kpis"><div class="kpi"><strong class="num">41</strong><span>pedidos em 7 dias</span></div><div class="kpi"><strong class="num">R$ 283,48</strong><span>ticket médio</span></div><div class="kpi"><strong class="num">2.335</strong><span>peças em estoque</span></div><div class="kpi"><strong class="num">12</strong><span>grafias diferentes de cor e tamanho</span></div></div>'), "Dados lidos do Bling antes do desenho da loja."),
        ("Escopo", M.lista([("Documentação", "Visão, escopo, regras de negócio e requisitos funcionais e não funcionais."),
                            ("Arquitetura", "Oito registros de decisão técnica."),
                            ("Modelo de dados", "Regras de acesso por linha testadas com pgTAP."),
                            ("Planejamento", "Backlog em 6 fases com 25 tarefas."),
                            ("Fotos", "Recorte e conversão para AVIF e WebP no navegador do painel."),
                            ("Operação", "Roteiros de publicação e varredura de segredos no repositório.")])),
    ],
)
