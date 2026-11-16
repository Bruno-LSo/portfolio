"""Caso novo: análises avulsas feitas para o CONFEA."""
import modelo as M

SLUG = "analises-confea"

CASO = dict(
    nome="Análises avulsas para o CONFEA",
    resumo="Painéis e extrações pontuais: pedidos de engenheiros a Portugal, quiz de palestra, orçamento federal e salários.",
    tec="Python · pandas · HTML · dados abertos",
    area="dados",
    lead="Quatro análises curtas feitas para o CONFEA, cada uma com o próprio script: um painel de pedidos de engenheiros brasileiros "
         "à Ordem dos Engenheiros de Portugal, um painel ao vivo para uma palestra, a conversão da Lei Orçamentária de 2026 e uma coleta "
         "de salários no Portal da Transparência.",
    ficha=[("Instituição", "CONFEA"), ("Formato", "Scripts independentes"), ("Saída", "HTML, CSV e Excel"), ("Período", "jan a mar/2026")],
    numeros=[("9.131", "pedidos de brasileiros à Ordem dos Engenheiros de Portugal, 2016 a 2026"), ("13", "perguntas no quiz da palestra"),
             ("4", "análises independentes")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-oep.webp", "Pedidos à Ordem dos Engenheiros de Portugal: 9.131 do Brasil para Portugal e 334 no sentido contrário, por sexo e UF."),
            ("02-oep-modalidades.webp", "Pedidos por ano e por modalidade. Engenharia civil soma 5.094 pedidos."),
            ("04-quiz.webp", "Painel da palestra: acertos por pergunta, atualizado durante a apresentação. Dados fictícios."),
            ("05-quiz-resumo.webp", "Segunda página: a plateia comparada com a pesquisa original de 2017 (12.000 pessoas em 14 países). Dados fictícios."),
        ]), "Capturas dos painéis gerados.", "larga"),
        ("Análises", M.lista([
            ("Ordem dos Engenheiros de Portugal", "Painel em arquivo único, para envio por e-mail. Filtra por UF e por intervalo de anos; mapa, tabela por sexo, série anual e modalidades."),
            ("Palestra sobre o método de Hans Rosling", "A plateia responde a 13 perguntas num formulário. Um script do Google Planilhas devolve os totais e o painel mostra o percentual de acerto de cada pergunta."),
            ("Lei Orçamentária de 2026", "Converte o arquivo RDF N-Triples do Portal de Dados Abertos em CSV e Excel, com leitor próprio, sem biblioteca de terceiros."),
            ("Salários de engenheiros públicos", "Consulta a API do Portal da Transparência pelas ocupações da família CBO 214 e grava a planilha formatada."),
        ])),
        ("Fluxo do painel da palestra", M.fluxograma([
            ("Plateia", [("Formulário", "13 perguntas de múltipla escolha")]),
            ("Planilha", [("Respostas", "uma linha por pessoa"), ("Apps Script", "compara com o gabarito e soma")], "publica JSON"),
            ("Painel", [("Página 1", "acerto por pergunta, em % ou absoluto"), ("Página 2", "comparação com a pesquisa de 2017")]),
        ]), "", "larga"),
        ("Pedidos por ano", M.barras([("2016", 346), ("2017", 762), ("2018", 1370, True), ("2019", 1113), ("2020", 558),
                                      ("2021", 764), ("2022", 1237), ("2023", 1054), ("2024", 879), ("2025", 965)],
                                     titulo="Pedidos de brasileiros à Ordem dos Engenheiros de Portugal", casas=0,
                                     nota="Pela data de solicitação. 2026 tem 83 pedidos até a data da extração.")),
        ("Pedidos por modalidade", M.achados([("5.094", "engenharia civil, 56% dos pedidos"), ("1.170", "engenharia elétrica"),
                                               ("908", "engenharia mecânica"), ("78%", "dos pedidos feitos por homens (7.096 de 9.131)")])),
    ],
    stack=["Python", "pandas", "openpyxl", "Google Apps Script", "API do Portal da Transparência", "HTML e JavaScript"],
)
