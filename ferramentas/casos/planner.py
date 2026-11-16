import modelo as M

SLUG = "planner"

_m = ('<defs><marker id="pl-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>')


def _cx(x, y, w, t, s, cor="#4FD1D4"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="64" rx="10" fill="#162A37" stroke="{cor}"/>'
            f'<text x="{x + w / 2}" y="{y + 28}" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{t}</text>'
            f'<text x="{x + w / 2}" y="{y + 48}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{s}</text>')


def _ln(x1, y1, x2, y2, t=""):
    r = f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#pl-s)"/>'
    if t:
        r += f'<text x="{(x1 + x2) / 2}" y="{min(y1, y2) - 8}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{t}</text>'
    return r


_svg = ('<svg viewBox="0 0 960 260" role="img" aria-label="Fluxo de homologação: usuário pede, administrador aprova, gatilho registra">' + _m
        + _cx(10, 20, 190, "Usuário", "pede conclusão ou exclusão", "#4FB3E8")
        + _cx(260, 20, 200, "approval_requests", "pedido pendente", "#FFD25E")
        + _cx(520, 20, 200, "Administrador", "aprova ou rejeita", "#4FB3E8")
        + _cx(780, 20, 170, "apply_approval", "aplica no banco", "#5CC98A")
        + _cx(520, 170, 200, "Gatilhos", "7 tipos de registro", "#5CC98A")
        + _cx(780, 170, 170, "activity_logs", "tela Atividade", "#5CC98A")
        + _cx(260, 170, 200, "Notificação", "Realtime no navegador", "#FFD25E")
        + _ln(200, 52, 258, 52) + _ln(460, 52, 518, 52) + _ln(720, 52, 778, 52, "aprovado")
        + _ln(865, 84, 865, 168) + _ln(620, 202, 778, 202) + _ln(360, 84, 360, 168)
        + '</svg>')

CASO = dict(
    tec="Alpine.js · Supabase · SortableJS",
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-quadro.webp", "Quadro: uma coluna por projeto, com prioridade, prazo, equipe, anexos e ações."),
            ("02-acao.webp", "Edição de ação: prazo dentro da janela do projeto, situação, responsável e atribuídos."),
            ("03-prioridades.webp", "Prioridades: o usuário arrasta os projetos; o #1 é o mais importante."),
            ("04-dashboard.webp", "Dashboard: 6 indicadores, projetos com prazo em 14 dias e ações que vencem em 7 dias."),
            ("05-homologacoes.webp", "Homologações: pedidos dos usuários esperando a decisão do administrador."),
            ("06-atividade.webp", "Atividade: histórico com filtro por usuário, tipo de ação e período."),
            ("07-ferias.webp", "Férias e feriados: períodos sobrepostos entre pessoas aparecem como conflito."),
        ]), "Telas reproduzidas a partir do código da aplicação, com o banco trocado por dados fictícios. Dados fictícios.", "larga"),
        ("Fluxo de páginas", M.fluxograma([
            ("Acesso", [("Login", "usuário ou e-mail e senha")]),
            ("Trabalho", [("Quadro", "projetos e ações"), ("Prioridades", "ordem dos projetos e das ações"), ("Dashboard", "prazos e equipe"), ("Meu perfil", "dados e senha")]),
            ("Administração", [("Usuários", "perfis e férias"), ("Homologações", "aprovar ou rejeitar"), ("Atividade", "histórico"), ("Férias e feriados", "conflitos e datas")], "só administrador"),
        ]), "Página única. O usuário comum vê só os projetos e ações em que está atribuído.", "larga"),
        ("Funcionalidades", M.lista([
            ("Quadro", "Projetos em colunas e ações em cartões. Arrastar muda a ordem ou o projeto da ação."),
            ("Ações", "Situação pendente, em andamento ou concluída; prazo em vermelho quando vencido."),
            ("Prazos", "O formulário mostra a janela do projeto e avisa quando o prazo cai em feriado nacional."),
            ("Anexos", "Vários arquivos por projeto ou ação, até 10 MB cada, e imagem de capa."),
            ("Perfis", "Administrador vê tudo. Usuário vê o que é dele e pede aprovação para concluir ou excluir."),
            ("Tempo real", "Notificações, quadro, anexos e homologações se atualizam sem recarregar a página."),
        ])),
        ("Homologação e registro", M.diagrama(_svg, "Pedidos do usuário passam pelo administrador. Gatilhos no banco registram projetos, ações, anexos, capa, férias, feriados e homologações."), "", "larga"),
        ("Arquitetura", M.fluxo([
            ("gerador", "Python", "Um script gera o arquivo index.html com a aplicação inteira."),
            ("front", "Página única", "Alpine.js, Tailwind e SortableJS por CDN, sem etapa de build."),
            ("banco", "Supabase", "Tabelas com regras de acesso por linha, Storage para anexos e Realtime."),
            ("funcao", "Função no servidor", "Criar, editar e excluir usuário, com registro no histórico."),
        ])),
    ],
    stack=["Python", "Alpine.js 3", "Tailwind CSS", "SortableJS", "Supabase", "PostgreSQL", "Edge Functions", "Realtime"],
)
