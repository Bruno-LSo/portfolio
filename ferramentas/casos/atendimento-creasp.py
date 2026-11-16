"""Caso novo: consulta que alimenta o painel de Atendimento do Crea-SP."""
import modelo as M

SLUG = "atendimento-creasp"

_F = 'font-family="Sora" font-size="14" fill="#EAF1F6" text-anchor="middle"'


def _cx(x, y, w, h, cor, t1, t2=""):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#162A37" stroke="{cor}"/>'
    if t2:
        s += f'<text x="{x + w / 2}" y="{y + h / 2 - 4}">{t1}</text><text x="{x + w / 2}" y="{y + h / 2 + 16}" fill="#A9B8C6" font-size="13">{t2}</text>'
    else:
        s += f'<text x="{x + w / 2}" y="{y + h / 2 + 5}">{t1}</text>'
    return s


_SETA = ('<defs><marker id="at-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>')

# Árvore da CATEGORIA_STATUS
_SVG_STATUS = (
    f'<svg viewBox="0 0 960 400" role="img" aria-label="Classificação do protocolo">{_SETA}<g {_F}>'
    + _cx(360, 16, 240, 56, "#4FD1D4", "Último status do protocolo", "registro mais recente")
    + _cx(20, 150, 200, 64, "#FFD25E", "Documentação pendente", "")
    + _cx(250, 150, 200, 64, "#4FB3E8", "Em andamento", "não finalizado")
    + _cx(480, 150, 200, 64, "#4FB3E8", "Finalizado", "sem cancelamento")
    + _cx(710, 150, 230, 64, "#F08A7E", "Solicitação cancelada", "")
    + _cx(20, 300, 200, 64, "#FFD25E", "Exigência", "")
    + _cx(250, 300, 200, 64, "#4FB3E8", "Aberto", "inclui exigência atendida")
    + _cx(480, 300, 140, 64, "#5CC98A", "Fechado", "")
    + _cx(650, 300, 135, 64, "#F08A7E", "Cancelado", "outro motivo")
    + _cx(805, 300, 135, 64, "#F08A7E", "Sem pagamento", "boleto vencido")
    + '</g><g stroke="#4FD1D4" stroke-width="2" fill="none">'
    '<path d="M480 72 V110 H120 V146" marker-end="url(#at-seta)"/><path d="M350 110 V146" marker-end="url(#at-seta)"/>'
    '<path d="M580 110 V146" marker-end="url(#at-seta)"/><path d="M480 110 H825 V146" marker-end="url(#at-seta)"/>'
    '<path d="M120 214 V296" marker-end="url(#at-seta)"/><path d="M350 214 V296" marker-end="url(#at-seta)"/>'
    '<path d="M580 214 V296" marker-end="url(#at-seta)"/>'
    '<path d="M825 214 V260 H717 V296" marker-end="url(#at-seta)"/><path d="M825 260 H872 V296" marker-end="url(#at-seta)"/>'
    '</g></svg>')

# Cálculo do SLA
_SVG_SLA = (
    f'<svg viewBox="0 0 960 330" role="img" aria-label="Cálculo do prazo de atendimento">{_SETA}<g {_F}>'
    + _cx(20, 20, 260, 64, "#F08A7E", "Cancelado por boleto vencido", "prazo = 0")
    + _cx(20, 100, 260, 64, "#F08A7E", "Finalizado antes do pagamento", "prazo = 0")
    + _cx(20, 180, 260, 64, "#F08A7E", "Registro de empresa deferido", "prazo = 0")
    + _cx(20, 260, 260, 56, "#4FB3E8", "Demais protocolos", "")
    + _cx(360, 210, 260, 100, "#4FD1D4", "Dias corridos", "do pagamento, ou da abertura,")
    + '<text x="490" y="290" fill="#A9B8C6" font-size="13">até o último status ou hoje</text>'
    + _cx(700, 60, 240, 80, "#FFD25E", "Prazo oficial do subtipo", "10, 15 ou 20 dias")
    + _cx(700, 220, 240, 40, "#5CC98A", "Dentro do prazo", "")
    + _cx(700, 270, 240, 40, "#F08A7E", "Fora do prazo", "")
    + '</g><g stroke="#4FD1D4" stroke-width="2" fill="none">'
    '<path d="M280 288 H320 V260 H356" marker-end="url(#at-seta)"/>'
    '<path d="M620 260 H660 V240 H696" marker-end="url(#at-seta)"/><path d="M660 260 V290 H696" marker-end="url(#at-seta)"/>'
    '<path d="M820 140 V180 H660 V240" stroke-dasharray="6 5"/>'
    '</g><text x="740" y="172" font-family="Sora" font-size="13" fill="#A9B8C6" text-anchor="middle">compara</text></svg>')

CASO = dict(
    nome="Consulta do painel de Atendimento",
    resumo="Consulta SQL que alimenta o Power BI de Atendimento do Crea-SP, com regras de situação, prazo e regional.",
    tec="DB2 · SQL · Power BI · DAX",
    area="dados",
    lead="Consulta no banco DB2 do Crea-SP que entrega uma linha por protocolo de atendimento, com situação, prazo oficial, prazo real e regional. "
         "Alimenta o painel de Atendimento em Power BI e tem cada coluna documentada para as áreas usuárias.",
    ficha=[("Instituição", "Crea-SP"), ("Banco", "DB2"), ("Painel", "Power BI"), ("Documentação", "23 colunas, em Markdown e HTML")],
    numeros=[("7", "etapas na consulta (CTE)"), ("23", "colunas documentadas"), ("141.332", "protocolos depois da remoção de duplicatas"),
             ("30.148", "linhas repetidas removidas")],
    blocos=[
        ("Etapas da consulta", M.fluxograma([
            ("Leitura", [("Último status", "por protocolo"), ("Unidades", "unidade e localidade"), ("Regionais", "mapa de GRE"),
                         ("Funcionários", "responsáveis por acervo")]),
            ("Junção", [("Protocolo completo", "tipo, subtipo, boleto, pagamento, observações")], "combina"),
            ("Regras", [("Situação", "status simplificado e classificação"), ("Regional", "GRE ou sem distribuição"),
                        ("Prazo", "dias reais e prazo oficial")], "calcula"),
            ("Limpeza", [("Uma linha por protocolo", "com pagamento e mais recente primeiro")], "remove duplicatas"),
            ("Saída", [("Power BI", "medidas DAX de prazo e exigência")]),
        ]), "", "larga"),
        ("Classificação do protocolo", M.diagrama(_SVG_STATUS, "A regra mais específica vem primeiro. Desde 24/09/2025, a exigência atendida volta para a categoria Aberto."), "", "larga"),
        ("Cálculo do prazo", M.diagrama(_SVG_SLA, "O prazo real conta a partir do pagamento quando ele existe. Três casos não contam prazo."), "", "larga"),
        ("Duplicatas", M.colunas(
            M.achados([("171.480", "linhas na extração de 24/09/2025"), ("141.332", "protocolos distintos"),
                       ("13.584", "protocolos com mais de uma linha"), ("86,3%", "desses aparecem só 2 vezes")]),
            M.texto(["A junção com os boletos repetia o protocolo quando havia mais de um boleto.",
                     "A última etapa numera as linhas de cada protocolo e fica com a primeira: com pagamento, a mais recente; sem pagamento, o boleto mais antigo."]))),
        ("Prazos oficiais por subtipo", M.barras([
            ("Alteração de registro", 20), ("Cancelamento de registro", 20), ("Certidão de acervo", 20),
            ("Responsável de escola", 20), ("Cadastro de escola", 15),
            ("Baixa de ART", 10), ("Cancelamento de ART", 10)],
            titulo="Dias para concluir o protocolo", casas=0, nota="Registro de empresa, certidão de acervo técnico e cadastro de instituição de ensino. Tabela da área de atendimento.")),
        ("Documentação", M.lista([
            ("Por coluna", "Origem, regra de cálculo e exemplo para cada uma das 23 colunas."),
            ("Regras de negócio", "Cada pedido da área usuária ligado à linha da consulta que o atende."),
            ("Tabelas", "Lista das 11 tabelas e visões do DB2 usadas."),
            ("Medidas DAX", "Contagem de protocolos dentro e fora do prazo e de exigências no Power BI."),
            ("Página HTML", "Um script em Python junta os textos numa página navegável."),
        ])),
    ],
    stack=["DB2", "SQL", "Power BI", "DAX", "Python", "Dash", "markdown2"],
)
