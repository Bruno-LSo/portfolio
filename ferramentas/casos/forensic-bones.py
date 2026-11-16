import modelo as M

SLUG = "forensic-bones"


def _tab(x, y, w, titulo, campos, cor="#4FD1D4"):
    h = 40 + 24 * len(campos)
    r = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#162A37" stroke="{cor}"/>'
         f'<text x="{x + 14}" y="{y + 26}" fill="#EAF1F6" font-family="Sora" font-size="14" font-weight="600">{titulo}</text>')
    for i, c in enumerate(campos):
        r += f'<text x="{x + 14}" y="{y + 52 + 24 * i}" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13">{c}</text>'
    return r


def _ln(x1, y1, x2, y2, t):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#4FD1D4" stroke-width="2" fill="none"/>'
            f'<text x="{(x1 + x2) / 2}" y="{(y1 + y2) / 2 - 8}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{t}</text>')


_svg = ('<svg viewBox="0 0 960 330" role="img" aria-label="Modelo de dados: usuário, relatório e três registros ligados ao relatório">'
        + _tab(10, 110, 170, "Usuario", ["Nome, E-mail", "Senha (bcrypt)", "Perfil: Admin, User"], "#4FB3E8")
        + _tab(260, 110, 190, "Relatorio", ["Codigo", "Data", "Observacoes"], "#FFD25E")
        + _tab(560, 10, 390, "InventarioCranio", ["21 ossos: quantidade e descrição", "Frontal, Occipital, Mandíbula ..."], "#5CC98A")
        + _tab(560, 120, 390, "InventarioEsqueleto", ["fotos do esqueleto", "observações"], "#5CC98A")
        + _tab(560, 230, 390, "MarcadoresCranio", ["5 marcadores: M, F ou I", "CalculoEstimativaSexo"], "#5CC98A")
        + _ln(180, 150, 260, 150, "1 : N")
        + '<path d="M450 160 L505 160 L505 50 L558 50 M505 160 L558 160 M505 160 L505 270 L558 270" stroke="#4FD1D4" stroke-width="2" fill="none"/>'
        + '<text x="505" y="300" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">1 : N</text>'
        + '</svg>')

CASO = dict(
    nome="Forensic Bones",
    area="gestao",
    resumo="Relatório de antropologia forense com inventário ósseo e estimativa de sexo pelo crânio.",
    tec="ASP.NET Core · Entity Framework · SQL Server",
    lead="Aplicação web para o laboratório de antropologia forense. O perito abre um relatório, faz o inventário dos ossos, registra fotos dos achados e estima o sexo a partir de 5 marcadores do crânio.",
    ficha=[("Tipo", "Projeto acadêmico em grupo"), ("Ano", "2023"), ("Usuários", "Peritos e administrador"), ("Hospedagem", "Azure App Service (desativada)")],
    numeros=[("21", "ossos no inventário do crânio"), ("5", "marcadores para estimar o sexo"), ("11", "requisitos funcionais"), ("8", "casos de teste")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-inventario-cranio.webp", "Inventário do crânio: quantidade e descrição de cada osso. Captura do sistema em teste."),
            ("02-estimativa-sexo.webp", "Estimativa de sexo: cada marcador recebe masculino, feminino ou inconclusivo. Tela reproduzida do código, dados fictícios."),
            ("03-wireframe-inventario.webp", "Protótipo da tela de inventário, feito antes da programação."),
        ]), "", "larga"),
        ("Fluxo do exame", M.fluxograma([
            ("Acesso", [("Login", "e-mail e senha"), ("Cadastro", "na página inicial")]),
            ("Relatório", [("Novo relatório", "código, data, responsável"), ("Buscar relatório", "lista por data")]),
            ("Registros do relatório", [("Inventário do crânio", "21 ossos"), ("Inventário do esqueleto", "fotos e observações"),
                                        ("Achados patológicos", "fotos"), ("Estimativa de sexo", "5 marcadores")]),
            ("Consulta", [("Detalhar", "relatório e registros"), ("Alterar", "qualquer registro"), ("Excluir", "com confirmação")]),
        ]), "Fluxo da documentação do projeto: primeiro o relatório, depois os registros ligados a ele.", "larga"),
        ("Estimativa de sexo", M.fluxo([
            ("1", "Crista nucal", "Masculino, feminino ou inconclusivo."),
            ("2", "Processo mastoide", "Idem, com observação livre."),
            ("3", "Eminência mentoniana", "Idem."),
            ("4", "Margem supra-orbital", "Idem."),
            ("5", "Área da glabela", "Idem."),
            ("=", "Resultado", "A resposta mais frequente. Empate entre masculino e feminino dá inconclusivo."),
        ]), "Cada marcador abre a figura de referência. Na tela de exemplo: 3 masculino, 1 feminino e 1 inconclusivo dão M."),
        ("Funcionalidades", M.lista([
            ("Perfis", "Administrador gerencia usuários; perito vê relatórios, inventários e estimativas."),
            ("Acesso", "Login por cookie e senha com bcrypt; páginas de exame exigem login."),
            ("Relatórios", "Criar, consultar, alterar e excluir, do mais recente para o mais antigo."),
            ("Inventários", "Quantidade e descrição por osso, com fotos do esqueleto e dos achados."),
            ("Documentação", "Contexto, requisitos, wireframes, diagramas, plano e registro de testes."),
        ])),
        ("Modelo de dados", M.diagrama(_svg, "Cada relatório pertence a um usuário e reúne os inventários e a estimativa de sexo. Esquema criado por migrações do Entity Framework."), "", "larga"),
    ],
    stack=["C#", ".NET 8", "ASP.NET Core MVC", "Entity Framework Core", "SQL Server", "Bootstrap", "BCrypt", "Docker", "Azure"],
)
