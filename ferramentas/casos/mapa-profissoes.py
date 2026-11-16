"""Mapa das profissões (repositório confea-mapa-profissoes). Números do registro do pipeline de 13/07/2026."""
import modelo as M

SLUG = "mapa-profissoes"

CASO = dict(
    numeros=[("3.175", "municípios com curso presencial de 2010 a 2024"), ("125", "cursos (códigos CINE)"),
             ("420", "combinações de ano e UF conferidas"), ("463.562", "ingressantes em 2024")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-brasil.webp", "Brasil, 2024: ingressantes presenciais por município e, ao lado, os números do EaD por estado."),
            ("02-estado.webp", "Recorte por estado: São Paulo, com os municípios coloridos pela quantidade de ingressantes."),
            ("03-municipio.webp", "Município: o mapa aproxima e os cartões mostram 956 ingressantes e 605 concluintes em 2024."),
            ("04-regiao-concluintes.webp", "Região Nordeste com a métrica trocada para concluintes: muda a escala de cores."),
            ("05-curso-intervalo.webp", "Um curso (Engenharia civil) em Minas Gerais, somando o intervalo de 2014 a 2024."),
        ]), "Painel gerado a partir dos dados salvos do pipeline, sem os dados de profissionais.", "larga"),

        ("No celular", M.telas(SLUG, [("06-celular.webp", "Os filtros abrem num painel inferior.")], celular=True)),

        ("Fluxo de páginas", M.fluxograma([
            ("Entrada", [("Mapa do Brasil", "ingressantes do último ano")], "escolhe"),
            ("Recorte", [("Busca", "região, estado ou município"), ("Lista", "Brasil, 5 regiões, 27 UFs"),
                         ("Clique no mapa", "aproxima o território")], "filtra"),
            ("Filtros", [("Curso", "125 cursos ou todos"), ("Período", "um ano ou intervalo"), ("Escala", "linear ou logarítmica")], "atualiza"),
            ("Saída", [("Mapa", "cor por município"), ("Cartões", "ingressantes, concluintes, matriculados"),
                       ("EaD", "por estado, separado do mapa")]),
        ], "Os cartões trocam a métrica do mapa."), "", "larga"),

        ("Fluxo do processo", M.fluxograma([
            ("Entrada", [("Microdados do INEP", "Censo da Educação Superior, 2010 a 2024"),
                         ("Filtro de cursos", "125 códigos CINE do Sistema Confea/Crea")], "exclui Arquitetura"),
            ("Agregação", [("Presencial", "por município"), ("EaD", "por UF de oferta")], "junta"),
            ("Malhas", [("IBGE", "5.570 municípios de referência")], "confere"),
            ("Conferência", [("Cursos = município", "3.175 municípios"), ("Municípios = UF", "420 combinações")], "gera"),
            ("Saída", [("HTML único", "18,8 MB, dados e malhas embutidos"), ("Excel", "mesmas tabelas")]),
        ]), "", "larga"),

        ("Presencial e EaD", M.barras([
            ("2010 presencial", 256668), ("2010 EaD", 16764),
            ("2016 presencial", 356534), ("2016 EaD", 56452),
            ("2020 presencial", 234212), ("2020 EaD", 135134),
            ("2024 presencial", 192791), ("2024 EaD", 270771, True)],
            titulo="Ingressantes nos cursos da área, Brasil",
            nota="O EaD passou o presencial em 2022 (233.054 contra 206.211).")),

        ("Achados", M.achados([
            ("6,1% para 58,4%", "parte do EaD nos ingressantes, de 2010 para 2024"),
            ("-24,9%", "ingressantes presenciais de 2010 para 2024 (256.668 para 192.791)"),
            ("869 para 2.940", "municípios com curso presencial, de 2010 para 2024"),
            ("98,73%", "dos profissionais casados a um município do IBGE (1.554.461 de 1.574.484)"),
        ])),

        ("Conferência", M.lista([
            ("Cursos e município", "A soma dos cursos é igual ao total do município em ingressantes, concluintes e matriculados."),
            ("Municípios e UF", "A soma dos municípios é igual ao total presencial da UF em cada ano."),
            ("Total oficial", "Presencial mais EaD é igual ao total oficial do INEP em cada ano e UF."),
            ("Profissionais", "Extraídos e casados por município, mas fora do painel publicado."),
        ])),
    ],
)
