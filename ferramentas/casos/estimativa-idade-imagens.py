"""Estimativa de idade a partir de fotos de rosto (visão computacional). Bootcamp TripleTen, Sprint 15.
Fonte: Sprint_15/Visao_Computacional.ipynb (repositório privado; sem link).
As imagens de exemplo de rostos do notebook não foram usadas (pessoas reais)."""
import modelo as M

SLUG = "estimativa-idade-imagens"

# MAE por época, lido do registro de treino do notebook (20 épocas).
_MAE_TREINO = [14.2758, 13.7244, 13.6578, 13.6084, 13.5329, 13.5104, 13.5424, 13.5014, 13.4903, 13.4138,
               13.3730, 13.4655, 13.4250, 13.3183, 13.3855, 13.5136, 13.4378, 13.3539, 13.2879, 13.3009]
_MAE_VALID = [13.1055, 12.7812, 12.7486, 14.0748, 12.8440, 12.7087, 13.0666, 13.4036, 13.6471, 13.1633,
              12.7186, 13.1787, 13.0722, 13.0047, 13.8711, 12.6786, 12.5246, 13.2199, 12.8039, 12.9059]


def _curva():
    x0, x1, y0, y1 = 70, 930, 30, 250  # área do gráfico
    vmin, vmax = 12.0, 14.5

    def px(i):
        return x0 + (x1 - x0) * i / 19

    def py(v):
        return y1 - (y1 - y0) * (v - vmin) / (vmax - vmin)

    p = ['<svg viewBox="0 0 960 300" role="img" aria-label="Erro médio absoluto por época, treino e validação">']
    for v in (12.0, 12.5, 13.0, 13.5, 14.0, 14.5):
        y = py(v)
        p.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="#2A4252" stroke-width="1"/>')
        p.append(f'<text x="{x0 - 10}" y="{y + 4:.1f}" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13" text-anchor="end">{str(v).replace(".", ",")}</text>')
    for i in (0, 4, 9, 14, 19):
        p.append(f'<text x="{px(i):.1f}" y="275" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13" text-anchor="middle">{i + 1}</text>')
    p.append(f'<text x="{(x0 + x1) / 2}" y="296" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">época</text>')
    for serie, cor in ((_MAE_TREINO, "#4FB3E8"), (_MAE_VALID, "#4FD1D4")):
        pts = " ".join(f"{px(i):.1f},{py(v):.1f}" for i, v in enumerate(serie))
        p.append(f'<polyline points="{pts}" fill="none" stroke="{cor}" stroke-width="2.5"/>')
        p.extend(f'<circle cx="{px(i):.1f}" cy="{py(v):.1f}" r="3" fill="{cor}"/>' for i, v in enumerate(serie))
    p.append(f'<text x="{x1}" y="{py(_MAE_TREINO[-1]) - 10:.1f}" fill="#4FB3E8" font-family="Sora" font-size="13" text-anchor="end">treino 13,30</text>')
    p.append(f'<text x="{x1}" y="{py(_MAE_VALID[-1]) + 22:.1f}" fill="#4FD1D4" font-family="Sora" font-size="13" text-anchor="end">validação 12,91</text>')
    p.append("</svg>")
    return "".join(p)


def _arquitetura():
    caixas = [
        ("Foto", "224 x 224 x 3", "#4FD1D4"),
        ("ResNet50", "ImageNet, fixa", "#FFD25E"),
        ("Pooling global", "média por canal", "#4FB3E8"),
        ("Densa 512", "ReLU, descarte 30%", "#4FB3E8"),
        ("Densa 128", "ReLU, descarte 20%", "#4FB3E8"),
        ("Saída 1", "idade em anos", "#F08A7E"),
    ]
    w, h, gap, y = 146, 86, 14, 70
    p = ['<svg viewBox="0 0 960 230" role="img" aria-label="Arquitetura da rede: ResNet50 e camadas densas">',
         '<defs><marker id="idade-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>']
    for i, (t, d, cor) in enumerate(caixas):
        x = 7 + i * (w + gap)
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#162A37" stroke="{cor}"/>')
        p.append(f'<text x="{x + w / 2}" y="{y + 36}" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{t}</text>')
        p.append(f'<text x="{x + w / 2}" y="{y + 60}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{d}</text>')
        if i < len(caixas) - 1:
            p.append(f'<path d="M{x + w} {y + h / 2} H{x + w + gap}" stroke="#4FD1D4" stroke-width="2" marker-end="url(#idade-seta)"/>')
    p.append('<text x="12" y="40" fill="#A9B8C6" font-family="Sora" font-size="13">Treino: Adam, taxa 0,001, perda MSE, métrica MAE, lotes de 16, 20 épocas em GPU.</text>')
    p.append('<text x="12" y="200" fill="#A9B8C6" font-family="Sora" font-size="13">Aumento de dados no treino: espelhamento horizontal e rotação de até 10 graus.</text>')
    p.append("</svg>")
    return "".join(p)


CASO = dict(
    nome="Estimativa de idade por foto",
    resumo="Rede neural convolucional que estima a idade de uma pessoa a partir da foto do rosto.",
    tec="Python · TensorFlow · Keras · ResNet50",
    area="modelos",
    lead="Rede neural que estima a idade a partir de uma foto de rosto, pensada para conferir idade na venda de bebida alcoólica. "
         "A ResNet50 pré-treinada foi usada sem ajuste dos pesos. O erro médio na validação ficou em 12,91 anos.",
    ficha=[("Contexto", "Bootcamp de Ciência de Dados, TripleTen"), ("Problema", "Regressão: idade em anos a partir da imagem"),
           ("Dados", "7.591 fotos de rosto com a idade real"), ("Métrica", "Erro médio absoluto (MAE), em anos")],
    numeros=[("7.591", "fotos: 5.694 para treino e 1.897 para validação"), ("12,91", "anos de erro médio na validação, depois de 20 épocas"),
             ("1.503", "fotos de menores de 18 anos (19,8%)"), ("~222 s", "por época de treino em GPU")],
    blocos=[
        ("Objetivo", M.texto([
            "Estimar a idade de um cliente pela foto do rosto, para apoiar a conferência de idade na venda de bebida alcoólica.",
            "Métrica: erro médio absoluto (MAE), em anos, no conjunto de validação."])),
        ("Dados", M.lista([
            ("Origem", "Pasta com fotos de rosto e um CSV com o nome do arquivo e a idade real, fornecidos pelo curso."),
            ("Tamanho", "7.591 fotos, sem valores ausentes. Divisão de 75% para treino (5.694) e 25% para validação (1.897)."),
            ("Idade", "De 1 a 100 anos. Média 31,2, mediana 29, desvio padrão 17,1. Concentração entre 20 e 40 anos."),
            ("Faixa crítica", "907 fotos entre 16 e 20 anos (11,9%). De 128 a 193 fotos por idade entre 15 e 22 anos.")])),
        ("Organização", M.fluxograma([
            ("Dados", [("CSV de rótulos", "nome do arquivo e idade"), ("Fotos", "carregadas em lotes de 16")], "análise"),
            ("Análise", [("Distribuição", "assimétrica, pico entre 20 e 30 anos"), ("Grupos etários", "6 faixas"), ("Faixa de 14 a 21 anos", "por idade")], "preparo"),
            ("Preparo", [("Redimensionamento", "224 x 224 pixels"), ("Normalização", "pixels de 0 a 1"), ("Aumento de dados", "espelho e rotação de 10 graus")], "modelo"),
            ("Modelo", [("ResNet50", "congelada"), ("Camadas densas", "512 e 128, com descarte"), ("Saída", "1 valor, ReLU")], "treino em GPU"),
            ("Treino", [("20 épocas", "~222 s cada"), ("Perda", "MSE"), ("Métrica", "MAE")], "avaliação"),
            ("Resultado", [("MAE na validação", "12,91 anos")]),
        ], "O notebook gera um script .py e o executa num servidor com GPU."), "", "larga"),
        ("Arquitetura da rede", M.diagrama(_arquitetura(), "Transferência de aprendizado: só as camadas densas são treinadas."), "", "larga"),
        ("Modelos e métricas", M.colunas(
            M.barras([("Treino, 1ª época", 14.28), ("Treino, 20ª época", 13.30), ("Validação, 1ª época", 13.11), ("Validação, 20ª época", 12.91, True)],
                     titulo="Erro médio absoluto (anos)", casas=2, nota="Queda de 0,20 ano na validação em 20 épocas."),
            M.barras([("Menor de 18", 1503), ("18 a 21", 694), ("22 a 25", 918), ("26 a 35", 1903, True), ("36 a 50", 1593), ("Acima de 50", 980)],
                     titulo="Fotos por grupo etário", nota="Total de 7.591 fotos."))),
        ("Curva de treino", M.diagrama(_curva(), "Erro médio absoluto por época. A validação oscila entre 12,52 e 14,07 anos sem tendência clara de queda."), "", "larga"),
        ("Achados", M.achados([
            ("12,91 anos", "de erro médio na validação: a estimativa erra, em média, 13 anos para mais ou para menos."),
            ("−0,20 ano", "de ganho na validação entre a 1ª e a 20ª época: o modelo parou de aprender cedo."),
            ("12,91 < 13,30", "validação abaixo do treino: não há sobreajuste. O limite está na capacidade do modelo."),
            ("19,8%", "das fotos são de menores de 18 anos: há exemplos suficientes da faixa crítica.")])),
        ("Limites", M.lista([
            ("Rede congelada", "A ResNet50 não foi ajustada às fotos de rosto. Só as camadas finais aprenderam."),
            ("Erro alto para o uso", "Com erro médio de 13 anos, o modelo não serve para decidir se a pessoa tem 18 anos."),
            ("Alternativa indicada", "Tratar o caso como classificação (menor ou maior de 18) e liberar o ajuste das últimas camadas."),
            ("Poucos idosos", "Há menos fotos acima de 60 anos. O erro tende a crescer nessa faixa.")])),
        ("Gráficos do notebook", M.telas(SLUG, [
            ("01-distribuicao-idades.webp", "Distribuição das 7.591 fotos por idade. Pico entre 20 e 30 anos."),
            ("02-idades-em-torno-de-18.webp", "Fotos por idade entre 14 e 21 anos. A linha marca os 18 anos.")]),
         "Imagens geradas pelo notebook. As fotos de exemplo do notebook não aparecem aqui porque mostram rostos de pessoas reais.", "larga"),
    ],
    stack=["Python", "Jupyter", "pandas", "TensorFlow", "Keras", "ResNet50", "Matplotlib"],
)
