"""Caso detalhado: Emprego formal na engenharia (Novo CAGED x Sistema Confea/Crea)."""
import modelo as M

SLUG = "caged"


def _caixa(x, y, w, h, cor, t1, t2=""):
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#162A37" stroke="{cor}"/>'
         f'<text x="{x + w / 2}" y="{y + (h / 2 if not t2 else h / 2 - 6)}" text-anchor="middle" dominant-baseline="middle">{t1}</text>')
    if t2:
        s += f'<text x="{x + w / 2}" y="{y + h / 2 + 14}" text-anchor="middle" fill="#A9B8C6" font-size="13">{t2}</text>'
    return s


_FONTES = [("Novo CAGED", "FTP do Ministério do Trabalho", "#4FB3E8"),
           ("INEP", "Censo da Educação Superior", "#4FB3E8"),
           ("SIC do CONFEA", "registros e desligamentos", "#FFD25E"),
           ("Banco do Crea-SP", "registros ativos por município", "#FFD25E"),
           ("Banco Central", "salário mínimo, série 1619", "#4FB3E8"),
           ("Confea Valoriza", "editais abaixo do piso", "#FFD25E")]

_SVG = ('<svg viewBox="0 0 960 470" role="img" aria-label="Fontes e etapas do painel">'
        '<defs><marker id="cg-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
        '<g font-family="Sora" font-size="14" fill="#EAF1F6">'
        + "".join(_caixa(20, 20 + i * 74, 260, 58, c, a, b) for i, (a, b, c) in enumerate(_FONTES))
        + _caixa(360, 60, 260, 120, "#4FD1D4", "Filtro e ajuste", "13 famílias CBO, ajuste oficial")
        + _caixa(360, 230, 260, 120, "#4FD1D4", "Conjunto geral", "mesmo ajuste, sem filtro de CBO")
        + _caixa(700, 150, 240, 120, "#5CC98A", "index.html", "12 folhas, dados embutidos")
        + '<text x="490" y="400" text-anchor="middle" fill="#A9B8C6" font-size="13">Amarelo: base interna, só agregada.</text>'
        + '<text x="490" y="422" text-anchor="middle" fill="#A9B8C6" font-size="13">Azul: fonte pública.</text>'
        '</g><g stroke="#4FD1D4" stroke-width="2" fill="none">'
        '<path d="M280 49 H320 V120 H356" marker-end="url(#cg-seta)"/>'
        '<path d="M320 120 V290 H356" marker-end="url(#cg-seta)"/>'
        '<path d="M280 123 H320"/><path d="M280 197 H320"/><path d="M280 271 H320"/><path d="M280 345 H320"/><path d="M280 419 H320 V290"/>'
        '<path d="M620 120 H660 V210 H696" marker-end="url(#cg-seta)"/><path d="M620 290 H660 V210"/>'
        '</g></svg>')

CASO = dict(
    lead="Painel sobre emprego formal e salários nas profissões da engenharia, agronomia e geociências. "
         "Cruza o Novo CAGED com o Censo da Educação Superior, os registros do Sistema Confea/Crea e os concursos com salário abaixo do piso legal.",
    ficha=[("Instituição", "CONFEA e Crea-SP"), ("Demanda", "Comitê Gestor de Valorização Profissional do Crea-SP"),
           ("Período", "ago/2024 a ago/2026, 25 meses"), ("Saída", "Painel web de 12 folhas")],
    numeros=[("206.267", "movimentações nas 13 famílias de engenharia"), ("49,2%", "das admissões com salário abaixo do piso legal"),
             ("425", "vagas de concurso abaixo do piso"), ("13", "famílias de ocupação CBO")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-resumo.webp", "FL.01 Resumo: 101.001 admissões e 104.612 desligamentos no recorte, saldo de -3.611 e salário médio de admissão de R$ 9.673."),
            ("02-evolucao.webp", "FL.02 Evolução: admissões, desligamentos e saldo por mês, trimestre ou ano."),
            ("03-territorio.webp", "FL.03 Território: mapa e ranking por UF. Minas Gerais tem o menor saldo (-1.694)."),
            ("04-ocupacoes.webp", "FL.04 Ocupações: saldo e salário médio de admissão por família CBO."),
            ("05-piso-escuro.webp", "FL.04 em modo escuro, com a comparação com o conjunto geral ligada: 49.434 de 100.439 admissões abaixo do piso."),
            ("06-setores.webp", "FL.05 Setores: saldo por seção e subclasse da CNAE do empregador."),
            ("07-perfil.webp", "FL.06 Perfil: sexo, raça/cor, instrução, faixa etária e deficiência."),
            ("08-vinculos.webp", "FL.07 Vínculos: tipo de contrato, movimentação, porte, carga horária e faixa salarial."),
            ("09-formacao.webp", "FL.08 Formação: 6.670.760 ingressantes, 2.166.757 concluintes e 1.319.026 registros no Sistema."),
            ("10-valoriza.webp", "FL.12 Confea Valoriza: concursos públicos com salário abaixo do piso, por UF e por carga horária."),
        ]), "Capturas do painel gerado em 20/10/2026.", "larga"),
        ("Folhas do painel", M.fluxograma([
            ("Recorte", [("Período", "mês inicial e final"), ("Métrica", "saldo, admissões, desligamentos"),
                         ("Território", "UF e município"), ("Ocupação", "família CBO")], "vale para todas as folhas"),
            ("Medir", [("FL.01", "resumo"), ("FL.02", "evolução"), ("FL.03", "território"), ("FL.04", "ocupações e piso")]),
            ("Detalhar", [("FL.05", "setores"), ("FL.06", "perfil"), ("FL.07", "vínculos"), ("FL.08", "formação")]),
            ("Agir", [("FL.09", "cruzamentos"), ("FL.12", "concursos abaixo do piso")]),
            ("Referência", [("FL.10", "metodologia e limites"), ("FL.11", "links oficiais e guia")]),
        ], "A opção de comparar com o conjunto geral mostra o mesmo indicador para todas as ocupações do país."), "", "larga"),
        ("Fontes e etapas", M.diagrama(_SVG, "O painel junta seis fontes num arquivo único. Bases internas entram só como totais."), "", "larga"),
        ("Funcionalidades", M.lista([
            ("Recorte global", "Período, métrica, UF, município e família CBO valem para as 12 folhas."),
            ("Conjunto geral", "Cada indicador pode ser comparado com o total do mercado formal, tabulado no mesmo passo e com o mesmo ajuste."),
            ("Piso legal", "Compara o salário de admissão com o piso da Lei 4.950-A/66 para a carga horária diária: 6, 7,25 ou 8,5 salários mínimos."),
            ("Leitura guiada", "Cada gráfico tem botão de explicação com cálculo e fonte, e cada folha tem uma análise em texto."),
            ("Modos de tela", "Padrão, horizontal e tela cheia, em tema claro ou escuro."),
            ("Guia de extração", "Links oficiais dos microdados por mês e passo a passo para abrir os arquivos no Excel e no Python."),
        ])),
        ("Achados", M.achados([
            ("49,2%", "das 100.439 admissões com salário válido ficaram abaixo do piso legal da categoria."),
            ("-3.611", "saldo de empregos das 13 famílias de ago/2024 a ago/2026."),
            ("60,9%", "dos concluintes dos cursos do Sistema chegam ao registro profissional."),
            ("R$ 4.388", "de defasagem média mensal por vaga nos 370 editais de concurso abaixo do piso."),
            ("281", "dos 370 processos do Confea Valoriza foram judicializados (75,9%)."),
            ("0,2%", "das admissões do mercado formal são das 13 famílias de engenharia."),
        ])),
        ("Salário médio de admissão por família", M.barras([
            ("Engenheiros de minas", 13718), ("Engenheiros químicos", 11828), ("Geólogos e geofísicos", 11193),
            ("Engenheiros mecânicos", 11098), ("Engenheiros de produção", 9972), ("Média das 13 famílias", 9673, True),
            ("Engenheiros civis", 9103), ("Engenheiros agrônomos", 8747), ("Engenheiros ambientais", 7631),
            ("Engenheiros de alimentos", 4815)],
            titulo="R$ por mês, ago/2024 a ago/2026", casas=0,
            nota="Salário nominal declarado na admissão. Fonte: Novo CAGED.")),
        ("Regras de cálculo", M.fluxo([
            ("1", "Ajuste oficial", "Saldo = declarações no prazo, mais as fora do prazo, menos as exclusões, por mês de movimentação."),
            ("2", "Salário válido", "Só entram na média salários entre R$ 100 e R$ 300.000."),
            ("3", "Piso congelado", "Base de R$ 1.212, salário mínimo de 2022, conforme decisão do STF."),
            ("4", "Participação", "Percentuais usam admissões, nunca o saldo, que pode ser negativo."),
            ("5", "Privacidade", "Os microdados não identificam pessoa nem empresa; todo cruzamento é agregado."),
        ])),
    ],
    stack=["Python", "pandas", "pyarrow", "py7zr", "DB2", "SQL Server", "PostgreSQL", "API do Banco Central", "HTML e JavaScript"],
)
