"""Saneamento por município: planilhas geradas, fluxo da coleta, conferências e números do Brasil."""
import modelo as M

SLUG = "saneamento"

CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-resumo.webp", "Excel de São Paulo, aba Resumo 2024: Brasil, o estado e os 645 municípios, um indicador por coluna."),
            ("02-serie.webp", "Aba Coleta de esgoto: série de 2024 para trás, um ano por coluna. Células sem dado aparecem como n/d."),
        ]), "Planilha gerada pela coleta, reproduzida em HTML com os dados públicos do arquivo.", "larga"),
        ("Fluxo da coleta", M.fluxograma([
            ("Lista", [("API do IBGE", "5.571 municípios, código de 7 dígitos"), ("Identificador", "código sem o dígito verificador")]),
            ("Coleta", [("Página da localidade", "valor do ano mais recente, com código do indicador"),
                        ("Página da série", "todos os anos, de 2010 a 2024")], "8 frentes em paralelo"),
            ("Conferência", [("Valores iguais", "o último ano das duas páginas tem de bater"), ("Tipo de localidade", "município e região metropolitana com o mesmo nome"),
                             ("Séries idênticas", "sinal de página errada")]),
            ("Saída", [("27 arquivos Excel", "um por UF, 8 abas"), ("CSV único", "419.850 linhas, formato longo"), ("Log", "avisos e erros por localidade")]),
        ], "Cada localidade coletada vai para um cache. Uma execução interrompida retoma do ponto em que parou."), "", "larga"),
        ("Indicadores", M.lista([("Acesso à água", "Percentual da população atendida."),
                                 ("Coleta de esgoto", "Percentual da população com coleta."),
                                 ("Esgoto tratado", "Percentual do esgoto tratado em relação à água consumida."),
                                 ("Perdas na distribuição", "Percentual da água perdida."),
                                 ("Investimento", "Investimento por habitante, em reais de 2024.")])),
        ("Brasil, 2010 e 2024", M.achados([("+11,3 p.p.", "na coleta de esgoto: 45,4% para 56,7% da população"),
                                           ("+15,6 p.p.", "no esgoto tratado: 36,2% para 51,8%"),
                                           ("+3,1 p.p.", "no acesso à água: 81,0% para 84,1%"),
                                           ("39,5%", "da água perdida na distribuição em 2024 (39,0% em 2010)")])),
        ("Coleta de esgoto por UF", M.barras([
            ("SP", 93.2, True), ("DF", 91.8), ("PR", 76.5), ("MG", 75.2), ("GO", 65.7), ("MS", 63.1), ("RR", 63.0),
            ("RJ", 60.4), ("ES", 56.9), ("PI", 45.1), ("BA", 42.3), ("MT", 39.9), ("PB", 37.7), ("RS", 34.7),
            ("SE", 33.9), ("TO", 32.7), ("CE", 31.9), ("SC", 30.7), ("PE", 28.9), ("RN", 25.0), ("AM", 20.2),
            ("AL", 19.9), ("MA", 13.1), ("AC", 11.0), ("RO", 10.6), ("PA", 10.0), ("AP", 9.3)],
            titulo="Parcela da população com coleta de esgoto, 2024", casas=1, sufixo="%",
            nota="Fonte: Painel Saneamento Brasil, com dados do SNIS/SINISA. Média do Brasil: 56,7%."), "", "larga"),
        ("Conferências da execução final", M.achados([("5.598", "localidades gravadas: Brasil, 27 UFs e 5.570 municípios"),
                                                      ("17", "municípios com séries idênticas, marcados para revisão"),
                                                      ("2", "grafias divergentes entre IBGE e site, mantidas pelo código"),
                                                      ("1", "município sem página no site, registrado no log")])),
        ("Processamento", M.texto(["A coleta lê duas páginas por localidade e compara o valor do ano mais recente. Se os valores divergem, a localidade sai do arquivo e o motivo vai para o log. Um erro em um município não interrompe a execução."])),
    ],
)
