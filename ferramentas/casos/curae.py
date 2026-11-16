import modelo as M

SLUG = "curae"
F = "Dados fictícios."


def _cx(x, y, w, h, tit, sub, cor="#4FD1D4"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#162A37" stroke="{cor}"/>'
    if sub:
        s += f'<text x="{x + w / 2:.0f}" y="{y + h / 2 - 4:.0f}" fill="#EAF1F6">{tit}</text><text x="{x + w / 2:.0f}" y="{y + h / 2 + 16:.0f}" fill="#A9B8C6" font-size="13">{sub}</text>'
    else:
        s += f'<text x="{x + w / 2:.0f}" y="{y + h / 2 + 5:.0f}" fill="#EAF1F6">{tit}</text>'
    return s


_ARQ = ('<svg viewBox="0 0 960 250" role="img" aria-label="Arquitetura: gerador Python, página única, Supabase e envio de e-mail pela Resend">'
        '<defs><marker id="curae-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
        '<g font-family="Sora" font-size="14" text-anchor="middle">'
        + _cx(10, 90, 160, 70, "Gerador Python", "um script", "#FFD25E")
        + _cx(215, 90, 170, 70, "index.html", "página única", "#4FB3E8")
        + '<rect x="430" y="30" width="230" height="190" rx="12" fill="#162A37" stroke="#4FD1D4" stroke-width="2"/>'
        '<text x="545" y="60" fill="#EAF1F6" font-size="15">Supabase</text>'
        '<text x="545" y="88" fill="#A9B8C6" font-size="13">login e perfis</text>'
        '<text x="545" y="110" fill="#A9B8C6" font-size="13">catálogo e categorias</text>'
        '<text x="545" y="132" fill="#A9B8C6" font-size="13">pedidos e vendas</text>'
        '<text x="545" y="154" fill="#A9B8C6" font-size="13">cupons e figurinhas</text>'
        '<text x="545" y="176" fill="#A9B8C6" font-size="13">validar cupom, comissão</text>'
        '<text x="545" y="198" fill="#A9B8C6" font-size="13">registro de alterações</text>'
        + _cx(705, 90, 110, 70, "mailer", "função", "#4FD1D4")
        + _cx(850, 90, 100, 70, "Resend", "e-mail", "#5CC98A")
        + '</g><g stroke="#4FD1D4" stroke-width="2" fill="none">'
        '<path d="M170 125 H211" marker-end="url(#curae-seta)"/><path d="M385 125 H426" marker-end="url(#curae-seta)"/>'
        '<path d="M660 125 H701" marker-end="url(#curae-seta)"/><path d="M815 125 H846" marker-end="url(#curae-seta)"/></g>'
        '<text x="190" y="190" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">sem servidor próprio: a página lê e grava direto no banco</text></svg>')

CASO = dict(
    numeros=[("5", "versões do gerador, de 13 a 30/06/2026"), ("R$ 4,00", "estimativa de frete por queijo até o pedido fechar"),
             ("4", "produtos comprados para ganhar uma figurinha"), ("7", "abas no painel: resumo, pedidos, produtos, categorias, cupons, figurinhas e configurações")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-inicio.webp", "Abertura com o queijo em 3D e os atalhos para o pedido e a origem. " + F),
            ("02-catalogo.webp", "Cardápio: aviso do frete estimado e os 3 passos do pedido. " + F),
            ("03-pedido.webp", "Pedido em montagem: 7 queijos de 4 tipos, frete estimado e total. " + F),
            ("05-cadastro.webp", "Cadastro com a escolha de quem convidou. " + F),
            ("06-conta.webp", "Minha conta: pedido atual, figurinha e troca de senha. " + F),
            ("04-origem.webp", "Origem: mapa de Minas Gerais com os 853 municípios. " + F),
        ]), "Telas capturadas no modo de demonstração da página, que funciona sem servidor.", "larga"),
        ("Painel dos organizadores", M.telas(SLUG, [
            ("07-painel-queijos.webp", "Queijos: preço, disponibilidade, quantidade e total pedido. " + F),
            ("08-painel-frete.webp", "Frete e datas: estimativa ou valor real rateado, data-limite e previsão. " + F),
            ("09-painel-pedidos.webp", "Pedidos por participante, com exportação em CSV. " + F),
        ]), "", "larga"),
        ("Fluxo da compra coletiva", M.fluxograma([
            ("Participante", [("Cardápio", "tipos e quantidades"), ("Cadastro", "nome, e-mail, convidado de quem")], "registra"),
            ("Pedido", [("Registrar interesse", "e-mail de confirmação"), ("Editar", "até a data-limite")]),
            ("Organizadores", [("Fecha o pedido", "data-limite"), ("Frete real", "rateado por queijo"), ("Ajustes", "aviso só a quem teve item alterado")], "dispara cobrança"),
            ("Cobrança", [("E-mail final", "total de cada participante"), ("Pix", "chave no e-mail")]),
        ], "O frete aparece como estimativa de R$ 4,00 por queijo até o organizador informar o valor real."), "", "larga"),
        ("Funcionalidades", M.lista([("Catálogo", "Categorias, selo de origem e quantidade disponível travada no banco."),
                                     ("Cupons", "Desconto por código, validado por função no banco."),
                                     ("Figurinhas", "A cada 4 produtos comprados, o participante cria uma figurinha."),
                                     ("Revenda", "Comissão calculada para revendedores."),
                                     ("Frete", "Estimativa por unidade e rateio do frete real entre os pedidos."),
                                     ("Fechamento", "Data-limite do pedido e aviso apenas a quem teve item alterado."),
                                     ("Cobrança", "Valor de cada participante e pagamento por Pix."),
                                     ("Demonstração", "Sem chave do banco, a página usa dados só do navegador.")])),
        ("Arquitetura", M.diagrama(_ARQ, "O gerador grava um único index.html. A chave escrita na página é a pública; a chave da Resend fica só na função."), "", "larga"),
    ],
)
