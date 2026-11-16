"""Cozinhas Solidárias (repositório kunha-conab). Números do relatório de consolidação de 30/08/2025."""
import modelo as M

SLUG = "cozinhas"


def _regra():
    caixa = ('<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#162A37" stroke="{c}" stroke-width="2"/>'
             '<text x="{tx}" y="{ty}" fill="#EAF1F6" font-family="Sora" font-size="15" font-weight="600" text-anchor="middle">{t1}</text>'
             '<text x="{tx}" y="{ty2}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{t2}</text>')
    p = ['<svg viewBox="0 0 960 300" role="img" aria-label="Regra de correspondência: código igual e município parecido">',
         '<defs><marker id="cozinhas-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>']
    topo = [("Resposta do estado", "código e município", "#4FB3E8"),
            ("Código igual?", "ao da base federal", "#FFD25E"),
            ("Município parecido?", "similaridade de 80% ou mais", "#FFD25E"),
            ("Casada", "entra na tabela única", "#5CC98A")]
    for i, (a, b, c) in enumerate(topo):
        x = 10 + i * 240
        p.append(caixa.format(x=x, y=30, w=200, h=84, c=c, tx=x + 100, ty=66, ty2=90, t1=a, t2=b))
        if i < 3:
            p.append(f'<path d="M{x + 204} 72 H{x + 236}" stroke="#4FD1D4" stroke-width="2" marker-end="url(#cozinhas-seta)"/>')
            if i:
                p.append(f'<text x="{x + 220}" y="62" fill="#5CC98A" font-family="Sora" font-size="13" text-anchor="middle">sim</text>')
    p.append(caixa.format(x=250, y=196, w=440, h=84, c="#F08A7E", tx=470, ty=232, ty2=256,
                          t1="Sem correspondência", t2="listada no relatório da consolidação"))
    for x in (350, 590):
        p.append(f'<path d="M{x} 118 V192" stroke="#F08A7E" stroke-width="2" marker-end="url(#cozinhas-seta)"/>')
        p.append(f'<text x="{x + 10}" y="160" fill="#F08A7E" font-family="Sora" font-size="13">não</text>')
    p.append("</svg>")
    return "".join(p)


CASO = dict(
    numeros=[("537", "cozinhas consolidadas"), ("26", "estados com respostas"), ("6.309", "cozinhas na base federal"),
             ("89,9%", "das respostas casadas (537 de 597)")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-consulta.webp", "Consulta: filtro por estado à esquerda e uma ficha por cozinha, agrupada por estado."),
            ("02-filtro-estados.webp", "Ceará e Rio de Janeiro marcados: 155 cozinhas. Dados fictícios."),
        ]), "Tela reproduzida a partir do painel gerado, com nomes, contatos e CNPJs trocados. Dados fictícios.", "larga"),

        ("Fluxo do processo", M.fluxograma([
            ("Entradas", [("26 planilhas estaduais", "respostas do levantamento 2025"),
                          ("Base federal", "6.309 cozinhas cadastradas")], "lê a primeira aba"),
            ("Leitura", [("Colunas-chave", "código, município e responsável achados pelo nome da coluna")], "compara"),
            ("Correspondência", [("Código", "igual, sem acento e sem caixa"), ("Município", "parecido, 80% ou mais")], "consolida"),
            ("Saídas", [("Tabela única", "537 cozinhas em Excel"), ("Relatório", "linhas casadas e não casadas"),
                        ("Painel HTML", "consulta por estado"), ("Word e PDF", "lista com capa e índice")]),
        ]), "", "larga"),

        ("Regra de correspondência", M.diagrama(_regra(), "O nome do município aceita grafias diferentes, como \"Maceió\", \"MACEIÓ\" e \"Maceió-AL\"."), "", "larga"),

        ("Cozinhas por estado", M.barras([
            ("RJ", 82, True), ("CE", 73), ("RS", 72), ("SP", 64), ("PE", 40), ("BA", 33),
            ("PI", 21), ("MG", 20), ("PR", 20), ("AL", 18)],
            titulo="Os 10 estados com mais cozinhas casadas", nota="Os outros 16 estados somam 94 cozinhas.")),

        ("Funcionalidades", M.lista([
            ("Painel", "Arquivo HTML único. Filtro por estado com contagem e ficha de cada cozinha com contato e CNPJ."),
            ("Documentos", "Word e PDF com capa, índice por estado e uma ficha por cozinha."),
            ("Relatório", "Texto com as colunas achadas, a taxa de correspondência e os códigos sem par em cada estado."),
        ])),
    ],
)
