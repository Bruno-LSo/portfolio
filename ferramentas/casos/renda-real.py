"""Caso detalhado: Renda Real (calculadora de juros compostos e correção pelo IPCA)."""
import modelo as M

SLUG = "renda-real"

_SVG = (
    '<svg viewBox="0 0 960 300" role="img" aria-label="Origem das taxas da calculadora">'
    '<defs><marker id="rr-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker>'
    '<marker id="rr-seta2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0 0 L10 5 L0 10z" fill="#F08A7E"/></marker></defs>'
    # séries
    '<g font-family="Sora" font-size="14" fill="#EAF1F6">'
    '<rect x="20" y="30" width="200" height="56" rx="10" fill="#162A37" stroke="#4FB3E8"/>'
    '<text x="120" y="54" text-anchor="middle">Selic</text>'
    '<text x="120" y="74" text-anchor="middle" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13">série 432</text>'
    '<rect x="20" y="122" width="200" height="56" rx="10" fill="#162A37" stroke="#4FB3E8"/>'
    '<text x="120" y="146" text-anchor="middle">CDI</text>'
    '<text x="120" y="166" text-anchor="middle" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13">série 4389</text>'
    '<rect x="20" y="214" width="200" height="56" rx="10" fill="#162A37" stroke="#4FB3E8"/>'
    '<text x="120" y="238" text-anchor="middle">IPCA mensal</text>'
    '<text x="120" y="258" text-anchor="middle" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13">série 433</text>'
    # tentativas
    '<rect x="300" y="60" width="250" height="180" rx="12" fill="#162A37" stroke="#4FD1D4"/>'
    '<text x="425" y="88" text-anchor="middle">Leitura no navegador</text>'
    '<text x="425" y="124" text-anchor="middle" fill="#A9B8C6" font-size="13">1. API do Banco Central</text>'
    '<text x="425" y="150" text-anchor="middle" fill="#A9B8C6" font-size="13">2. intermediário corsproxy</text>'
    '<text x="425" y="176" text-anchor="middle" fill="#A9B8C6" font-size="13">3. intermediário allorigins</text>'
    '<text x="425" y="216" text-anchor="middle" fill="#A9B8C6" font-size="13">até 9 s por tentativa</text>'
    # saídas
    '<rect x="640" y="40" width="300" height="80" rx="12" fill="#162A37" stroke="#5CC98A"/>'
    '<text x="790" y="72" text-anchor="middle">Taxa ao vivo</text>'
    '<text x="790" y="96" text-anchor="middle" fill="#A9B8C6" font-size="13">indicador verde no topo</text>'
    '<rect x="640" y="180" width="300" height="80" rx="12" fill="#162A37" stroke="#F08A7E"/>'
    '<text x="790" y="212" text-anchor="middle">Valor de referência</text>'
    '<text x="790" y="236" text-anchor="middle" fill="#A9B8C6" font-size="13">gravado na geração da página</text>'
    '</g>'
    '<g stroke-width="2" fill="none">'
    '<path d="M220 58 H260 V150 H296" stroke="#4FD1D4" marker-end="url(#rr-seta)"/>'
    '<path d="M220 150 H296" stroke="#4FD1D4"/>'
    '<path d="M220 242 H260 V150" stroke="#4FD1D4"/>'
    '<path d="M550 110 H600 V80 H636" stroke="#4FD1D4" marker-end="url(#rr-seta)"/>'
    '<path d="M550 190 H600 V220 H636" stroke="#F08A7E" stroke-dasharray="6 5" marker-end="url(#rr-seta2)"/>'
    '</g>'
    '<text x="594" y="140" font-family="Sora" font-size="13" fill="#A9B8C6" text-anchor="middle">ok</text>'
    '<text x="594" y="176" font-family="Sora" font-size="13" fill="#A9B8C6" text-anchor="middle">falha</text>'
    '</svg>')

CASO = dict(
    lead="Calculadora pública de juros compostos, renda mensal sustentável e correção de valores pelo IPCA. "
         "As taxas Selic, CDI e IPCA são lidas da API do Banco Central quando a página abre.",
    numeros=[("3", "séries do Banco Central: 432, 4389 e 433"), ("2", "modos: projeção e correção pelo IPCA"),
             ("5 a 40", "anos de projeção"), ("1", "arquivo HTML, sem servidor")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-projecao.webp", "Projeção de R$ 1.000.000 por 20 anos com Selic de 13,75% e IPCA de 4,63%: R$ 13,2 milhões nominais e R$ 5,3 milhões em valor de hoje."),
            ("02-retirada.webp", "Mesmo capital com retirada de R$ 9.000 por mês: o painel avisa que a retirada passa da renda sustentável de R$ 6.988,70."),
            ("04-tabela.webp", "Tabela ano a ano com juros, saldo nominal e saldo real."),
            ("03-ipca.webp", "Correção pelo IPCA: R$ 1.000.000 de jan/1995 equivalem a R$ 7.455.184,57 em nov/2026 (inflação acumulada de 645,52% em 381 meses)."),
            ("05-metodo.webp", "Explicação dos cálculos, com as equações e um exemplo numérico."),
        ]), "Capturas da página publicada. Valores com as taxas lidas do Banco Central na data da captura.", "larga"),
        ("Fluxo de uso", M.fluxograma([
            ("Entrada", [("Página única", "taxas do Banco Central no topo")]),
            ("Modo", [("Projeção", "capital, aporte, retirada, juros, inflação, prazo"),
                      ("Inflação", "valor, mês e ano inicial e final")], "escolhe"),
            ("Cálculo", [("Mês a mês", "saldo nominal e saldo real"), ("Renda sustentável", "retirada que preserva o poder de compra"),
                         ("IPCA acumulado", "produto das variações mensais")], "calcula"),
            ("Saída", [("Cartões", "valor por extenso"), ("Gráfico", "linear ou logarítmico"), ("Tabela", "ano a ano")]),
        ]), "", "larga"),
        ("Funcionalidades", M.lista([
            ("Taxas ao vivo", "Selic, CDI e IPCA de 12 meses lidos da API SGS do Banco Central. Um botão aplica cada taxa ao campo de juros ou de inflação."),
            ("Retirada em R$ ou %", "A retirada mensal aceita valor fixo ou percentual do capital; o painel mostra a taxa anual equivalente."),
            ("Renda sustentável", "Calcula a retirada mensal que mantém o patrimônio em valor de hoje e avisa quando a retirada passa desse limite."),
            ("Valor por extenso", "Todo resultado em reais tem a escrita por extenso, para evitar erro de leitura de casas."),
            ("Correção pelo IPCA", "Multiplica a inflação de cada mês do período, em blocos de até 10 anos por consulta."),
            ("Método aberto", "Uma janela mostra as fórmulas com exemplo numérico."),
        ])),
        ("Cálculo", M.fluxo([
            ("1", "Taxa mensal", "Taxa equivalente composta: (1 + taxa anual) elevado a 1/12, menos 1."),
            ("2", "Saldo do mês", "Saldo anterior com juros, mais aporte, menos retirada."),
            ("3", "Valor real", "Saldo dividido pela inflação acumulada até o mês."),
            ("4", "Juro real", "Fórmula de Fisher: (1 + juro nominal) / (1 + inflação) menos 1."),
            ("5", "Renda sustentável", "Capital vezes a taxa real mensal equivalente."),
        ])),
        ("Exemplo", M.barras([("Valor final nominal", 13153099.53, True), ("Valor final em reais de hoje", 5319901.61),
                              ("Total em juros", 12153099.53), ("Capital inicial", 1000000)],
                             titulo="R$ 1.000.000 por 20 anos, Selic 13,75% e IPCA 4,63% ao ano", casas=0, sufixo="",
                             nota="Valores em R$, tirados da tela publicada.")),
        ("Origem das taxas", M.diagrama(_SVG, "Cada série tenta a API direta e dois intermediários. Se as três falharem, a página usa o valor gravado na geração."), "", "larga"),
        ("Geração", M.texto(["Um script em Python grava o HTML com o CSS, o JavaScript e as taxas de referência embutidos. "
                             "A página publicada não depende de servidor próprio: só lê a API pública do Banco Central."])),
    ],
    stack=["Python", "HTML, CSS e JavaScript", "API SGS do Banco Central", "KaTeX", "GitHub Pages"],
)
