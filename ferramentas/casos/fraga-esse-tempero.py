import modelo as M

SLUG = "fraga-esse-tempero"

_m = ('<defs><marker id="fet-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>')


def _cx(x, y, w, t, s, cor="#4FD1D4"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="64" rx="10" fill="#162A37" stroke="{cor}"/>'
            f'<text x="{x + w / 2}" y="{y + 28}" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{t}</text>'
            f'<text x="{x + w / 2}" y="{y + 48}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{s}</text>')


def _ln(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#fet-s)"/>'


_svg = ('<svg viewBox="0 0 960 250" role="img" aria-label="Arquitetura: loja em React, API Node.js e Express, MongoDB e serviços de pagamento e e-mail">' + _m
        + _cx(10, 90, 180, "Loja (React)", "Ant Design, axios", "#4FB3E8")
        + _cx(250, 90, 220, "API Node.js + Express", "31 rotas, JWT")
        + _cx(530, 90, 180, "MongoDB", "4 coleções", "#5CC98A")
        + _cx(770, 10, 180, "Braintree", "pagamento", "#FFD25E")
        + _cx(770, 170, 180, "SendGrid", "recuperar senha", "#FFD25E")
        + _ln(190, 122, 248, 122) + _ln(470, 122, 528, 122)
        + '<path d="M470 105 L620 42 L768 42" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#fet-s)"/>'
        + '<path d="M470 140 L620 202 L768 202" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#fet-s)"/>'
        + '</svg>')

CASO = dict(
    nome="Fraga esse Tempero",
    area="comercio",
    resumo="Loja virtual de temperos com carrinho, pagamento, pedidos e painel do administrador.",
    tec="React · Node.js · MongoDB · Braintree",
    lead="Loja virtual de temperos. O cliente navega por categoria, filtra por preço, compra e acompanha o pedido. O administrador cadastra categorias e produtos e muda a situação dos pedidos.",
    ficha=[("Tipo", "Projeto acadêmico em grupo"), ("Ano", "2024"), ("Pagamento", "Braintree"), ("Testes", "Vitest e Cypress")],
    numeros=[("31", "rotas na API"), ("4", "coleções no banco"), ("37", "testes unitários"), ("62", "testes de integração da API")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-wireframe-home.webp", "Página inicial: novidades e mais vendidos, menu de categorias, busca e carrinho."),
            ("02-wireframe-produto-carrinho.webp", "Detalhe do produto com relacionados e carrinho com resumo e pagamento."),
            ("03-wireframe-admin.webp", "Administração: criar categoria, criar produto, lista de produtos e pedidos."),
        ]), "Wireframes do projeto de interface. As telas da loja carregam fotos e produtos da API, que não está publicada.", "larga"),
        ("Fluxo de páginas", M.fluxograma([
            ("Entrada", [("Início", "novidades e mais vendidos"), ("Loja", "filtro por categoria e preço"), ("Busca", "por palavra")]),
            ("Produto", [("Detalhe", "foto, preço, estoque"), ("Relacionados", "mesma categoria")], "selecionar"),
            ("Compra", [("Carrinho", "guardado no navegador"), ("Login ou cadastro", "com recuperação de senha"), ("Pagamento", "cartão via Braintree")], "adicionar"),
            ("Depois", [("Meus pedidos", "situação do pedido"), ("Perfil", "nome e endereço")]),
        ]), "O fluxo segue o fluxograma da documentação do projeto.", "larga"),
        ("Funcionalidades", M.lista([
            ("Catálogo", "Página com 6 produtos por vez e botão para ver mais; selo com o número de vendidos."),
            ("Filtros", "Categorias marcadas e faixas de preço de R$ 0 a R$ 19, R$ 20 a R$ 39 e acima."),
            ("Contas", "Senha com bcrypt, token JWT e e-mail de recuperação de senha."),
            ("Pedidos", "5 situações: não processado, processando, enviado, entregue e cancelado."),
            ("Administração", "Categorias, produtos com foto e mudança de situação dos pedidos."),
            ("Testes", "Testes unitários dos serviços com Vitest e testes da API com Cypress."),
        ])),
        ("Arquitetura", M.diagrama(_svg, "A loja chama a API; a API grava no MongoDB e usa serviços externos para pagamento e e-mail."), "", "larga"),
    ],
    stack=["React 18", "Ant Design", "Node.js", "Express", "MongoDB", "Mongoose", "JWT", "Braintree", "SendGrid", "Vitest", "Cypress"],
)
