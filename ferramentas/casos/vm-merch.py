import modelo as M

SLUG = "vm-merch"
F = "Dados fictícios."


def _cx(x, y, w, h, tit, sub, cor="#4FD1D4"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#162A37" stroke="{cor}"/>'
    if sub:
        s += f'<text x="{x + w / 2:.0f}" y="{y + h / 2 - 4:.0f}" fill="#EAF1F6">{tit}</text><text x="{x + w / 2:.0f}" y="{y + h / 2 + 16:.0f}" fill="#A9B8C6" font-size="13">{sub}</text>'
    else:
        s += f'<text x="{x + w / 2:.0f}" y="{y + h / 2 + 5:.0f}" fill="#EAF1F6">{tit}</text>'
    return s


_ARQ = ('<svg viewBox="0 0 960 400" role="img" aria-label="Arquitetura da loja: páginas estáticas na Hostinger, cinco funções no Supabase, Mercado Pago e Resend">'
        '<defs><marker id="vm-merch-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
        '<g font-family="Sora" font-size="14" text-anchor="middle">'
        + _cx(20, 40, 170, 64, "Loja /merch", "HTML e JS na Hostinger", "#4FB3E8")
        + _cx(20, 170, 170, 64, "Acompanhar pedido", "link do e-mail", "#4FB3E8")
        + _cx(20, 300, 170, 64, "Painel", "endereço secreto, 2FA", "#4FB3E8")
        + _cx(270, 20, 200, 56, "criar-pedido", "", "#4FD1D4")
        + _cx(270, 96, 200, 56, "webhook-mercadopago", "", "#4FD1D4")
        + _cx(270, 172, 200, 56, "acompanhar-pedido", "", "#4FD1D4")
        + _cx(270, 248, 200, 56, "enviar-emails", "", "#4FD1D4")
        + _cx(270, 324, 200, 56, "admin-acoes", "", "#4FD1D4")
        + '<rect x="540" y="120" width="190" height="170" rx="12" fill="#162A37" stroke="#4FD1D4" stroke-width="2"/>'
        '<text x="635" y="150" fill="#EAF1F6" font-size="15">Postgres</text>'
        '<text x="635" y="178" fill="#A9B8C6" font-size="13">produtos e variantes</text>'
        '<text x="635" y="200" fill="#A9B8C6" font-size="13">pedidos e histórico</text>'
        '<text x="635" y="222" fill="#A9B8C6" font-size="13">estoque e movimentos</text>'
        '<text x="635" y="244" fill="#A9B8C6" font-size="13">registro de atividades</text>'
        '<text x="635" y="266" fill="#A9B8C6" font-size="13">regras por linha</text>'
        + _cx(790, 40, 150, 64, "Mercado Pago", "Pix, boleto, cartão", "#5CC98A")
        + _cx(790, 170, 150, 64, "Resend", "e-mails do pedido", "#FFD25E")
        + _cx(790, 300, 150, 64, "Importador", "catálogo e fotos", "#F08A7E")
        + '<text x="230" y="14" fill="#A9B8C6" font-size="13">funções no Supabase</text>'
        '</g><g stroke="#4FD1D4" stroke-width="2" fill="none">'
        '<path d="M190 66 C230 66 240 48 266 48" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M190 202 H266" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M190 340 C230 340 240 352 266 352" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M470 48 C510 48 520 140 536 160" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M470 124 C505 124 515 170 536 180" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M470 200 H536" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M470 352 C510 352 520 280 536 262" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M470 40 C600 0 700 30 786 64" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M786 90 C700 110 560 112 474 120" stroke="#5CC98A" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M470 290 C600 340 830 330 860 238" marker-end="url(#vm-merch-seta)"/>'
        '<path d="M786 332 C770 320 750 300 734 280" stroke="#F08A7E" marker-end="url(#vm-merch-seta)"/>'
        '</g><text x="630" y="96" fill="#5CC98A" font-family="Sora" font-size="13" text-anchor="middle">aviso de pagamento</text></svg>')

CASO = dict(
    numeros=[("2", "produtos com variantes de cor: boné em 4 cores e caneca"), ("5", "funções no servidor"),
             ("9", "situações de pedido, do pagamento ao estorno"), ("8", "seções no painel do administrador")],
    blocos=[
        ("Telas da loja", M.telas(SLUG, [
            ("01-loja.webp", "Página da loja: chamada, formas de pagamento, frete e coleção."),
            ("02-produto.webp", "Produto: fotos, cor, aviso de últimas unidades, retirada e envio."),
            ("03-carrinho.webp", "Carrinho lateral com subtotal."),
            ("04-checkout.webp", "Finalizar compra, passo 1: dados do comprador."),
            ("05-entrega.webp", "Passo 2: retirada grátis ou envio, com endereço completado pelo CEP."),
            ("06-pagamento.webp", "Passo 3: Pix, boleto ou cartão, e aceite das condições."),
        ]), "Capturas da loja no ar em 16/11/2026, sem fazer pedido. Dados digitados fictícios.", "larga"),
        ("No celular", M.telas(SLUG, [("07-loja-celular.webp", "Loja em 390 px de largura.")], celular=True), "", "larga"),
        ("Painel do administrador", M.telas(SLUG, [
            ("08-painel-geral.webp", "Visão geral: faturamento, pedidos para despachar, vendas de 30 dias e alertas. " + F),
            ("09-painel-pedidos.webp", "Pedidos por situação, com busca por número, nome, e-mail ou CPF. " + F),
            ("10-painel-estoque.webp", "Estoque por variante, mínimo para alerta e últimas movimentações. " + F),
            ("11-painel-entregas.webp", "Entregas: retiradas, envios por estado e mapa das cidades. " + F),
        ]), "Telas reproduzidas com o código do painel e um banco simulado. O painel real exige login.", "larga"),
        ("Fluxo de compra", M.fluxograma([
            ("Loja", [("Coleção", "2 produtos"), ("Produto", "cor e quantidade")], "adiciona"),
            ("Carrinho", [("Carrinho lateral", "subtotal")], "finaliza"),
            ("Checkout", [("1. Seus dados", "nome, CPF, celular, e-mail"), ("2. Entrega", "retirada grátis ou R$ 20,00 SP e R$ 25,00 demais"), ("3. Pagamento", "Pix, boleto ou até 12x")], "cria o pedido"),
            ("Servidor", [("Recalcula", "preço, estoque e frete"), ("Mercado Pago", "página de pagamento")], "aviso de pagamento"),
            ("Depois", [("E-mail", "confirmação e link"), ("Acompanhamento", "página pública do pedido"), ("Painel", "despacho ou retirada")]),
        ]), "", "larga"),
        ("Situações do pedido", M.fluxo([
            ("1", "Aguardando pagamento", "Pedido criado; recusa leva a pagamento recusado."),
            ("2", "Para despachar", "Pagamento aprovado; alerta após 2 dias sem envio."),
            ("3", "Aguardando retirada", "Cliente recebe e-mail com o endereço da retirada."),
            ("4", "Enviado", "Registro do envio e e-mail ao cliente."),
            ("5", "Concluído", "Cliente com o produto."),
            ("6", "Problema, cancelado ou estornado", "Motivo obrigatório; o estoque reservado volta à venda."),
        ])),
        ("Painel", M.lista([
            ("Visão geral", "Faturamento do mês, ticket médio, vendas por dia e alertas de atraso, estoque e e-mail."),
            ("Pedidos", "Filtro por situação, detalhe, anotação, envio, retirada, estorno e reenvio de e-mail."),
            ("Estoque", "Reposição, retirada com motivo e estoque mínimo por variante."),
            ("Entregas", "Retiradas, envios por estado e mapa das cidades dos compradores."),
            ("Atividades", "Registro de cada ação, por categoria e por usuário."),
            ("Segurança", "Dois fatores configuráveis, sessão só na aba e saída após 30 minutos sem uso."),
        ])),
        ("Arquitetura", M.diagrama(_ARQ, "Scripts Python geram as páginas estáticas e o pacote para a Hostinger. A regra de negócio fica no Supabase."), "", "larga"),
    ],
)
