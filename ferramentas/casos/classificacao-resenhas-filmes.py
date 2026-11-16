"""Classificação de resenhas de filmes (positiva ou negativa). Bootcamp TripleTen, Sprint 14.
Fonte: Sprint_14/Aprendizado-Automatico-Para-Textos.ipynb (repositório privado; sem link)."""
import modelo as M

SLUG = "classificacao-resenhas-filmes"


def _caixa(x, y, w, h, cor, titulo, detalhe=""):
    d = (f'<text x="{x + w / 2}" y="{y + h / 2 + 22}" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{detalhe}</text>'
         if detalhe else "")
    ty = y + h / 2 + (0 if detalhe else 5)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#162A37" stroke="{cor}"/>'
            f'<text x="{x + w / 2}" y="{ty}" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{titulo}</text>{d}')


def _seta(d):
    return f'<path d="{d}" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#res-seta)"/>'


_LINHAS = [
    # (texto da 2ª etapa, detalhe, vetor, detalhe, classificador, F1, destaque)
    ("NLTK", "lematização WordNet", "TF-IDF", "1.000 termos", "Regressão Logística", "F1 0,85", "#4FB3E8"),
    ("spaCy", "lematização", "TF-IDF", "1.000 termos", "Regressão Logística", "F1 0,86", "#5CC98A"),
    ("spaCy", "lematização", "TF-IDF", "1.000 termos", "LightGBM", "F1 0,82", "#4FB3E8"),
    ("BERT", "base, sem ajuste", "Vetor de 768", "por resenha", "Regressão Logística", "F1 0,67", "#F08A7E"),
]


def _diagrama():
    partes = ['<svg viewBox="0 0 960 400" role="img" aria-label="Quatro caminhos de processamento de texto testados">',
              '<defs><marker id="res-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
              '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>',
              _caixa(10, 160, 160, 80, "#4FD1D4", "Resenha", "minúsculas, só letras")]
    for i, (a, ad, b, bd, c, f1, cor) in enumerate(_LINHAS):
        y = 20 + i * 95
        meio = y + 32
        partes.append(_seta(f"M170 200 C200 200 200 {meio} 220 {meio}"))
        partes.append(_caixa(220, y, 180, 64, "#FFD25E", a, ad))
        partes.append(_seta(f"M400 {meio} H440"))
        partes.append(_caixa(440, y, 160, 64, "#FFD25E", b, bd))
        partes.append(_seta(f"M600 {meio} H640"))
        partes.append(_caixa(640, y, 190, 64, cor, c))
        partes.append(f'<text x="845" y="{meio + 5}" fill="{cor}" font-family="JetBrains Mono" font-size="15">{f1}</text>')
    partes.append("</svg>")
    return "".join(partes)


CASO = dict(
    nome="Classificação de resenhas de filmes",
    resumo="Processamento de texto para separar resenhas positivas e negativas, com quatro abordagens comparadas.",
    tec="Python · NLTK · spaCy · BERT",
    area="modelos",
    lead="Classificador que identifica se uma resenha de filme é positiva ou negativa. "
         "Foram comparadas quatro formas de transformar o texto em números. "
         "A meta era F1 de 0,85. A combinação de spaCy, TF-IDF e Regressão Logística chegou a 0,86 em 23.483 resenhas de teste.",
    ficha=[("Contexto", "Bootcamp de Ciência de Dados, TripleTen"), ("Problema", "Classificação binária de texto em inglês"),
           ("Dados", "Resenhas do IMDb rotuladas por polaridade (Maas et al., 2011)"), ("Métrica", "F1, meta de 0,85")],
    numeros=[("47.242", "resenhas depois de remover duplicadas"), ("0,86", "F1 no teste com spaCy, TF-IDF e Regressão Logística"),
             ("0,93", "AUC-ROC no teste do mesmo modelo"), ("4", "abordagens de texto comparadas, mais 3 referências aleatórias")],
    blocos=[
        ("Objetivo", M.texto([
            "Separar resenhas de filmes em positivas e negativas sem leitura manual.",
            "Critério de aceite: F1 de pelo menos 0,85 no conjunto de teste."])),
        ("Dados", M.lista([
            ("Origem", "Base pública de resenhas do IMDb, com 17 colunas: texto, nota de 1 a 10, polaridade e dados do filme."),
            ("Tamanho", "47.331 resenhas. Ficam 47.242 depois de remover duplicadas."),
            ("Classes", "23.680 negativas e 23.562 positivas: classes equilibradas."),
            ("Divisão", "A própria base separa treino e teste: 23.759 e 23.483 resenhas. As notas 5 e 6 não aparecem.")])),
        ("Organização", M.fluxograma([
            ("Dados", [("Leitura do TSV", "17 colunas"), ("Limpeza", "duplicadas e valores \\N")], "análise"),
            ("Análise", [("Filmes por ano", "pico de produção em 2008"), ("Notas", "concentradas em 1 e 10"), ("Polaridade", "equilibrada no treino e no teste")], "texto"),
            ("Texto", [("Normalização", "minúsculas, só letras, sem palavras vazias"), ("Lematização", "NLTK ou spaCy")], "vetores"),
            ("Vetores", [("TF-IDF", "1.000 termos mais frequentes"), ("BERT", "vetor de 768 posições")], "treino"),
            ("Modelos", [("Referência", "3 classificadores aleatórios"), ("Regressão Logística", "2 versões"), ("LightGBM", "1 versão"), ("BERT + RL", "amostra de 100")], "avaliação"),
            ("Avaliação", [("F1 e acurácia", "no teste"), ("Curvas ROC e PR", "treino e teste"), ("Resenhas novas", "15 frases escritas à mão")]),
        ]), "", "larga"),
        ("Caminhos testados", M.diagrama(_diagrama(), "Quatro caminhos do texto ao rótulo. F1 no conjunto de teste."), "", "larga"),
        ("Modelos e métricas", M.colunas(
            M.barras([("spaCy + TF-IDF + RL", 0.86, True), ("NLTK + TF-IDF + RL", 0.85), ("spaCy + TF-IDF + LightGBM", 0.82),
                      ("BERT + RL (amostra)", 0.67), ("Aleatório estratificado", 0.50), ("Classe mais frequente", 0.34)],
                     titulo="F1 no teste", casas=2, nota="Meta: 0,85. BERT avaliado em 100 resenhas por causa do custo de processamento em CPU."),
            M.barras([("spaCy + TF-IDF + RL", 0.93, True), ("NLTK + TF-IDF + RL", 0.93), ("spaCy + TF-IDF + LightGBM", 0.91), ("BERT + RL (amostra)", 0.77)],
                     titulo="AUC-ROC no teste", casas=2, nota="No treino: 0,94; 0,94; 0,95 e 1,00. O BERT decorou as 100 resenhas de treino."))),
        ("Achados", M.achados([
            ("0,86", "F1 do melhor modelo: spaCy, TF-IDF e Regressão Logística. Passou a meta de 0,85."),
            ("+0,01", "de F1 do spaCy sobre o NLTK, com o mesmo vetor e o mesmo classificador."),
            ("−0,04", "de F1 do LightGBM em relação à Regressão Logística (0,82 contra 0,86), com o mesmo texto."),
            ("1,00 → 0,77", "AUC-ROC do BERT do treino para o teste: sobreajuste numa amostra de 100 resenhas.")])),
        ("Limites", M.lista([
            ("Vocabulário curto", "O TF-IDF usou só os 1.000 termos mais frequentes."),
            ("BERT incompleto", "O BERT rodou em CPU com 100 resenhas de treino e 100 de teste. O resultado não se compara aos outros."),
            ("Ironia e negação", "A limpeza remove palavras vazias como \"not\". Frases como \"I just didn't like it\" perdem a negação."),
            ("Idioma", "O modelo foi treinado em inglês. Não se aplica a resenhas em português sem novo treino.")])),
        ("Gráficos do notebook", M.telas(SLUG, [
            ("01-notas-treino-teste.webp", "Notas das resenhas no treino e no teste. As notas extremas (1 e 10) são as mais frequentes."),
            ("02-curvas-spacy-rl.webp", "Melhor modelo: F1 por limiar, curva ROC e curva de precisão e revocação. Treino e teste quase iguais."),
            ("03-curvas-lgbm.webp", "LightGBM: distância maior entre treino e teste nas três curvas."),
            ("04-curvas-bert.webp", "BERT em amostra de 100: treino perfeito e teste irregular.")]),
         "Imagens geradas pelo notebook do projeto.", "larga"),
    ],
    stack=["Python", "Jupyter", "pandas", "NLTK", "spaCy", "scikit-learn", "LightGBM", "PyTorch", "Transformers (BERT)"],
)
