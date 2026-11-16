"""Localizador por coordenadas: telas públicas, formatos aceitos e fluxo da planilha."""
import modelo as M

SLUG = "localizador"

CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-inicio.webp", "Tela inicial: campos de latitude e longitude, exemplos e mapa de satélite."),
            ("02-graus.webp", "Coordenada em graus, minutos e segundos, com N, S, L e O: o local e o endereço estimado."),
            ("03-decimal.webp", "Coordenada decimal com vírgula, no padrão brasileiro."),
        ]), "Capturas da página publicada.", "larga"),
        ("No celular", M.telas(SLUG, [("04-celular.webp", "Resultado no celular, com a coordenada em decimal e em graus.")], celular=True)),
        ("Fluxo da página", M.fluxograma([
            ("Entrada", [("Digitar", "latitude e longitude"), ("Colar o par", "no campo da latitude"), ("Clicar no mapa", "marca o ponto"), ("Exemplos", "5 locais prontos")]),
            ("Leitura", [("Formato", "decimal, vírgula, graus ou letras"), ("Faixa", "latitude de -90 a +90, longitude de -180 a +180")], "valida"),
            ("Resultado", [("Mapa", "marcador e aproximação"), ("Endereço", "continente, país, estado, cidade, bairro e rua"), ("Copiar", "coordenada em decimal e em graus")]),
        ]), "", "larga"),
        ("Formatos aceitos", M.lista([("Decimal", "-15.793889 , -47.882778"),
                                      ("Vírgula decimal", "-15,793889"),
                                      ("Letras de direção", "15.7939 S , 47.8828 O"),
                                      ("Graus, minutos e segundos", "15°47'38\"S 47°52'58\"O"),
                                      ("Par colado", "-15.7939, -47.8828 no campo da latitude")])),
        ("Planilhas", M.fluxograma([
            ("Entrada", [("Planilha Excel", "uma ou várias, sem alterar o original")]),
            ("Leitura", [("Colunas", "acha latitude e longitude pelos dados, não pelo cabeçalho")], "consulta"),
            ("Endereço", [("Nominatim", "1 consulta por segundo"), ("Cache", "pontos a 11 m de distância usam a mesma consulta")]),
            ("Saída", [("Nova planilha", "7 colunas ao lado da longitude, no mesmo estilo"), ("Link", "abre o ponto no Google Maps")]),
        ], "Colunas acrescentadas: continente, país, estado, cidade, bairro, rua e link."), "", "larga"),
        ("Funcionalidades", M.lista([
            ("Camadas", "Mapa, satélite e ruas."),
            ("Cursor", "Coordenada do ponteiro em tempo real."),
            ("Minha localização", "Centraliza o mapa na posição do aparelho."),
            ("Arquivo único", "Página em um HTML, publicada no GitHub Pages."),
        ])),
    ],
)
