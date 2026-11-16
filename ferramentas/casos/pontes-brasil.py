"""Pontes do Brasil: telas do painel, fluxo de páginas, pipeline e números do levantamento."""
import modelo as M

SLUG = "pontes-brasil"

CASO = dict(
    ficha=[("Instituição", "CONFEA"), ("Fontes", "OpenStreetMap e malhas do IBGE 2022"),
           ("Cobertura", "27 UFs e 5.293 municípios"), ("Saída", "Painel e 8 formatos de arquivo")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-painel.webp", "Painel com as 147.327 estruturas no mapa, indicadores e gráficos por estado, tipo e região."),
            ("02-mapa-calor.webp", "Mapa de calor da densidade de pontes no país."),
            ("03-filtro-sp.webp", "Filtro por estado: São Paulo, com 24.589 estruturas e contorno dos municípios."),
            ("04-municipio.webp", "Filtro por município sobre imagem de satélite: Recife, com 976 estruturas."),
            ("05-metodologia.webp", "Página de metodologia, com as etapas, as fontes e os limites do levantamento."),
        ]), "Capturas do painel gerado pelo pipeline.", "larga"),
        ("Fluxo de páginas", M.fluxograma([
            ("Páginas", [("Painel", "mapa, indicadores, gráficos e tabela"), ("Metodologia", "10 seções de documentação")]),
            ("Mapa", [("Todas as pontes", "um ponto por estrutura"), ("Mapa de calor", "densidade"),
                      ("Contornos", "estados e municípios"), ("Base", "claro, escuro, OSM ou satélite")], "filtra"),
            ("Filtros", [("Região", "5 regiões"), ("Estado", "27 UFs"), ("Município", "lista da UF escolhida"), ("Tipo", "7 tipos")], "recalcula"),
            ("Resultado", [("Indicadores", "total, km, municípios, com nome"), ("Gráficos", "por estado, tipo e região"), ("Tabela", "busca por nome")]),
        ]), "", "larga"),
        ("Processamento", M.fluxograma([
            ("01 Download", [("OpenStreetMap", "arquivo do Brasil, 1,96 GB"), ("IBGE 2022", "malhas de municípios e UFs")]),
            ("02 Extração", [("osmium", "tags bridge, man_made e building"), ("147.357", "elementos extraídos")]),
            ("03 Cálculo", [("Geometria", "centroide, comprimento e área"), ("Classes", "tipo e faixa de tamanho"), ("147.327", "estruturas válidas")]),
            ("04 Localização", [("Junção espacial", "município e UF"), ("100%", "estruturas localizadas")]),
            ("05 a 07 Saída", [("Painel HTML", "Leaflet e Chart.js"), ("Arquivos", "KML, KMZ, GeoJSON, Shapefile, GeoPackage, GPX, Excel, CSV")]),
        ], "Cada etapa é um script e grava os arquivos da etapa seguinte. A etapa 5 cruza com a base do DNIT quando o arquivo existe."), "", "larga"),
        ("Estruturas por tipo", M.painel("", '<div id="g-tipo"></div>')),
        ("Por tamanho", M.barras([("Até 10 m", 33279), ("10 a 50 m", 89095, True), ("50 a 200 m", 20659),
                                  ("200 m a 1 km", 4014), ("Acima de 1 km", 280)],
                                 titulo="Estruturas por faixa de comprimento"),
         "Mediana de 18,6 m e média de 41,9 m. A maior estrutura mede 15,3 km."),
        ("Por estado", M.painel("", '<div id="g-uf"></div>'), "São Paulo e Minas Gerais concentram 31% das estruturas."),
        ("Achados", M.achados([("147.327", "estruturas localizadas em 27 UFs"),
                               ("6.177 km", "de extensão somada"),
                               ("50.428", "estruturas com nome no OpenStreetMap (34%)"),
                               ("3.045", "estruturas no município do Rio de Janeiro, o 1º em número")])),
        ("Funcionalidades", M.lista([
            ("Mapa", "Um ponto por estrutura, com cor por tipo. O clique mostra nome, tipo, comprimento e município."),
            ("Densidade", "Mapa de calor e índice do vizinho mais próximo para medir a concentração."),
            ("Filtros encadeados", "Região, estado, município e tipo. Indicadores, gráficos e tabela seguem o filtro."),
            ("Arquivos", "Exportação nacional e por estado em 8 formatos, com dicionário de dados."),
        ])),
        ("Limites", M.lista([
            ("Cobertura do OpenStreetMap", "A base depende do mapeamento colaborativo. Estruturas não mapeadas ficam de fora."),
            ("DNIT", "Os 4 endereços das Obras de Arte Especiais não responderam na execução. O cruzamento ficou só com o OpenStreetMap."),
            ("Duplicidade", "A busca de estruturas sobrepostas existe no código, mas fica desligada por custo de processamento."),
        ])),
    ],
)
