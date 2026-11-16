import modelo as M

SLUG = "homecook"

_m = ('<defs><marker id="hc-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>')


def _cx(x, y, w, t, s, cor="#4FD1D4"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="64" rx="10" fill="#162A37" stroke="{cor}"/>'
            f'<text x="{x + w / 2}" y="{y + 28}" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{t}</text>'
            f'<text x="{x + w / 2}" y="{y + 48}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{s}</text>')


def _ln(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#hc-s)"/>'


_abas = ["users", "inventory", "products", "courses", "course_products", "customers", "sales", "events"]
_svg_abas = "".join(
    f'<rect x="{700 + (i % 2) * 125}" y="{20 + (i // 2) * 52}" width="115" height="40" rx="8" fill="#162A37" stroke="#5CC98A"/>'
    f'<text x="{757 + (i % 2) * 125}" y="{45 + (i // 2) * 52}" fill="#EAF1F6" font-family="JetBrains Mono" font-size="13" text-anchor="middle">{a}</text>'
    for i, a in enumerate(_abas))

_svg = ('<svg viewBox="0 0 960 240" role="img" aria-label="Arquitetura: navegador, Dash e Flask, camada de acesso e planilha Google">' + _m
        + _cx(10, 80, 150, "Navegador", "localhost:8050", "#4FB3E8")
        + _cx(200, 80, 190, "Dash + Flask", "9 páginas, login")
        + _cx(430, 80, 220, "GoogleSheetsManager", "cache 60 s, nova tentativa", "#FFD25E")
        + _svg_abas
        + _ln(160, 112, 198, 112) + _ln(390, 112, 428, 112) + _ln(650, 112, 694, 112)
        + '<text x="575" y="200" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">até 60 leituras e 60 gravações por minuto por usuário</text>'
        + '<text x="825" y="232" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">uma aba por entidade</text>'
        + '</svg>')

CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-painel.webp", "Painel: vendas do mês, clientes, itens abaixo do mínimo e margem média dos cursos."),
            ("02-estoque.webp", "Estoque em gramas, com custo por grama, valor total e situação de cada item."),
            ("03-cursos.webp", "Cursos com preço, custo dos insumos e margem."),
            ("04-curso-insumos.webp", "Cadastro de curso: o custo e a margem saem dos insumos e das quantidades."),
            ("05-vendas.webp", "Vendas filtradas por período e cliente, com total, quantidade, ticket médio e brindes."),
            ("06-nova-venda.webp", "Registro de venda com forma de pagamento e brinde."),
        ]), "Telas reproduzidas a partir do layout do código (Dash e Bootstrap). Dados fictícios.", "larga"),
        ("Fluxo de páginas", M.fluxograma([
            ("Acesso", [("Login", "usuário e senha")]),
            ("Painel", [("Dashboard", "4 indicadores, 2 gráficos, 2 tabelas")]),
            ("Menus", [("Cadastros", "Estoque, Insumos, Cursos"), ("Operações", "Clientes, Vendas, Eventos"), ("Conta", "Minha conta, Usuários, Sistema, Backup")]),
            ("Em cada tela", [("Lista", "busca e filtros"), ("Formulário", "janela para criar e editar"), ("Indicadores", "cartões de resumo")]),
        ]), "9 páginas no total, contando o login.", "larga"),
        ("Do insumo à margem", M.fluxo([
            ("estoque", "Insumo", "Quantidade em gramas, custo por grama e estoque mínimo."),
            ("curso", "Ficha do curso", "Lista de insumos com a quantidade usada de cada um."),
            ("custo", "Custo", "Soma de quantidade vezes custo por grama."),
            ("margem", "Margem", "(preço menos custo) dividido pelo preço."),
            ("venda", "Venda", "Curso, quantidade, pagamento e brinde."),
            ("painel", "Painel", "Vendas do mês e alerta de estoque baixo."),
        ]), "Exemplo da tela: custo de R$ 56,48 e preço de R$ 220,00 dão margem de 74,33%."),
        ("Funcionalidades", M.lista([
            ("Perfis", "4 perfis: administrador, gerente, operador e leitura."),
            ("Login", "Senha com bcrypt; 3 tentativas erradas bloqueiam o usuário por 5 minutos."),
            ("Estoque", "Situação normal, baixo ou sem estoque, com filtro e busca."),
            ("Eventos", "Eventos e investimentos com custo, local e retorno (ROI)."),
            ("Validação", "Regras de entrada para usuário, insumo, estoque, cliente, venda, evento e curso."),
            ("Manutenção", "Scripts para criar o primeiro usuário, corrigir permissões e refazer a estrutura das abas com backup."),
        ])),
        ("Arquitetura", M.diagrama(_svg, "A aplicação roda no computador do negócio. A planilha Google guarda os dados em 8 abas."), "", "larga"),
    ],
)
