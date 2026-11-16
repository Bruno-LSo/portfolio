"""Previsão de cancelamento de clientes de telecomunicações (churn). Bootcamp TripleTen, Sprint 17 (projeto final).
Fonte: Sprint_17/Projeto_Final.ipynb (repositório privado; sem link)."""
import modelo as M

SLUG = "previsao-cancelamento-clientes"


def _juncao():
    tabelas = [("Contratos", "7.043 clientes", "#4FD1D4"), ("Dados pessoais", "7.043 clientes", "#4FB3E8"),
               ("Internet", "5.517 clientes", "#FFD25E"), ("Telefone", "6.361 clientes", "#5CC98A")]
    p = ['<svg viewBox="0 0 960 360" role="img" aria-label="Junção das quatro tabelas pelo código do cliente">',
         '<defs><marker id="churn-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>']
    for i, (t, d, cor) in enumerate(tabelas):
        y = 12 + i * 86
        p.append(f'<rect x="10" y="{y}" width="200" height="66" rx="12" fill="#162A37" stroke="{cor}"/>')
        p.append(f'<text x="110" y="{y + 29}" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{t}</text>')
        p.append(f'<text x="110" y="{y + 52}" fill="#A9B8C6" font-family="JetBrains Mono" font-size="13" text-anchor="middle">{d}</text>')
        p.append(f'<path d="M210 {y + 33} C260 {y + 33} 260 180 300 180" stroke="#4FD1D4" stroke-width="2" fill="none"/>')
    p.append('<path d="M300 180 H330" stroke="#4FD1D4" stroke-width="2" marker-end="url(#churn-seta)"/>')
    caixas = [(330, "Junção", "pelo código do cliente", "#4FD1D4"), (520, "Tabela única", "7.043 x 20 variáveis", "#4FB3E8"),
              (710, "Random Forest", "chance de cancelar", "#F08A7E")]
    for j, (x, t, d, cor) in enumerate(caixas):
        p.append(f'<rect x="{x}" y="140" width="170" height="80" rx="12" fill="#162A37" stroke="{cor}"/>')
        p.append(f'<text x="{x + 85}" y="173" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">{t}</text>')
        p.append(f'<text x="{x + 85}" y="198" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">{d}</text>')
        if j < 2:
            p.append(f'<path d="M{x + 170} 180 H{x + 190}" stroke="#4FD1D4" stroke-width="2" marker-end="url(#churn-seta)"/>')
    p.append('<text x="330" y="262" fill="#A9B8C6" font-family="Sora" font-size="13">Cliente sem internet ou sem telefone: serviço marcado como ausente (0).</text>')
    p.append('<text x="330" y="284" fill="#A9B8C6" font-family="Sora" font-size="13">Alvo: data de saída preenchida = cancelou (1).</text>')
    p.append("</svg>")
    return "".join(p)


CASO = dict(
    nome="Previsão de cancelamento de clientes",
    resumo="Modelo que aponta clientes de telecomunicações com maior chance de cancelar o contrato.",
    tec="Python · pandas · scikit-learn",
    area="modelos",
    lead="Modelo que estima a chance de um cliente de operadora de telefonia e internet cancelar o contrato. "
         "A lista de clientes em risco permite oferecer planos de retenção antes da saída. "
         "Meta: AUC-ROC de 0,75. O Random Forest chegou a 0,838 no teste.",
    ficha=[("Contexto", "Bootcamp de Ciência de Dados, TripleTen, projeto final"), ("Problema", "Classificação binária: cancela ou não cancela"),
           ("Dados", "4 tabelas de uma operadora, 7.043 clientes"), ("Métrica", "AUC-ROC, meta de 0,75")],
    numeros=[("7.043", "clientes em 4 tabelas unidas"), ("26,5%", "dos clientes cancelaram (1.869)"),
             ("0,838", "AUC-ROC no teste do Random Forest"), ("73%", "dos cancelamentos do teste encontrados pelo modelo")],
    blocos=[
        ("Objetivo", M.texto([
            "Identificar os clientes com maior chance de cancelar, para a operadora oferecer promoções e planos antes da saída.",
            "Critério de aceite: AUC-ROC de pelo menos 0,75 no conjunto de teste."])),
        ("Dados", M.lista([
            ("Origem", "Quatro arquivos CSV de uma operadora, fornecidos pelo curso: contratos, dados pessoais, internet e telefone."),
            ("Tamanho", "7.043 clientes. 1.526 sem internet e 682 sem telefone."),
            ("Alvo", "Data de saída preenchida = cancelou. 5.174 ativos (73,5%) e 1.869 cancelados (26,5%)."),
            ("Variáveis", "20 depois da codificação: valores cobrados, tipo de contrato, forma de pagamento, serviços e perfil.")])),
        ("Junção das tabelas", M.diagrama(_juncao(), "As quatro tabelas viram uma linha por cliente."), "", "larga"),
        ("Organização", M.fluxograma([
            ("Dados", [("4 CSV", "contratos, pessoal, internet, telefone"), ("Conferência", "tipos, ausentes, duplicadas")], "análise"),
            ("Análise", [("Cancelamento", "26,5% dos clientes"), ("Fibra x DSL", "mais cancelamento na fibra"), ("Perfil", "idoso, parceiro, dependentes")], "preparo"),
            ("Preparo", [("Alvo", "a partir da data de saída"), ("Codificação", "one-hot nas categóricas"), ("Padronização", "valores mensal e total")], "junção"),
            ("Junção", [("Tabela única", "7.043 x 20"), ("Divisão 80/20", "estratificada: 5.634 e 1.409")], "treino"),
            ("Modelos", [("Regressão Logística", "busca em grade, 20 combinações"), ("Árvore de Decisão", "busca em grade"), ("Random Forest", "busca em grade, 24 combinações")], "validação cruzada de 5 partes"),
            ("Resultado", [("AUC-ROC no teste", "meta de 0,75"), ("Importância", "10 variáveis principais")]),
        ]), "", "larga"),
        ("Modelos e métricas", M.colunas(
            M.barras([("Random Forest", 0.838, True), ("Regressão Logística", 0.826), ("Árvore de Decisão", 0.823)],
                     titulo="AUC-ROC no teste", casas=3, nota="Meta: 0,75. Na validação cruzada: 0,842; 0,836 e 0,823."),
            M.barras([("Random Forest", 0.73, True), ("Regressão Logística", 0.50), ("Árvore de Decisão", 0.46)],
                     titulo="Recall dos cancelados no teste", casas=2, nota="374 cancelados no teste. O Random Forest usou pesos para equilibrar as classes."))),
        ("O que mais pesa", M.barras([("Valor total cobrado", 19.3, True), ("Valor mensal", 15.6, True), ("Contrato de 2 anos", 15.1, True),
                                      ("Internet por fibra", 9.2), ("Pagamento por cheque eletrônico", 7.2), ("Contrato de 1 ano", 6.5),
                                      ("Segurança on-line", 3.2), ("Fatura sem papel", 3.1), ("Suporte técnico", 2.6), ("Backup on-line", 2.2)],
                                     titulo="Importância das variáveis no Random Forest", casas=1, sufixo="%",
                                     nota="Soma das 10 primeiras: 84,0%.")),
        ("Achados", M.achados([
            ("0,838", "AUC-ROC do Random Forest no teste, 0,088 acima da meta."),
            ("73%", "dos clientes que cancelaram foram apontados pelo Random Forest. A Regressão Logística achou 50%."),
            ("15,1%", "da importância vem do contrato de 2 anos: contrato longo segura o cliente."),
            ("Fibra", "Clientes com fibra cancelam mais que os de DSL. A fibra soma 9,2% da importância.")])),
        ("Limites", M.lista([
            ("Alarmes falsos", "Precisão de 0,56 nos cancelados: de cada 100 clientes apontados, 44 não iam cancelar."),
            ("Tempo de casa", "A data de início saiu do modelo. O tempo de casa entra só pelo valor total cobrado."),
            ("Limiar fixo", "O corte de 0,5 não foi ajustado ao custo da oferta de retenção."),
            ("Foto do momento", "Os dados são de um único corte. O modelo precisa de novo treino com dados recentes.")])),
        ("Gráficos do notebook", M.telas(SLUG, [
            ("01-mensal-vs-total.webp", "Valor mensal contra valor total por cliente. As faixas verticais são os planos de preço fixo."),
            ("02-cancelamento-por-internet.webp", "Ativos e cancelados por tipo de internet: DSL e fibra."),
            ("03-cancelamento-por-perfil.webp", "Proporção de ativos e cancelados por idoso, parceiro e dependentes.")]),
         "Imagens geradas pelo notebook do projeto.", "larga"),
    ],
    stack=["Python", "Jupyter", "pandas", "NumPy", "scikit-learn", "Matplotlib", "seaborn"],
)
