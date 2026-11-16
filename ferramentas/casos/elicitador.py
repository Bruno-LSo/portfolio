"""Caso detalhado: Elicitador de requisitos (repositório elicitador-requisitos)."""
import modelo as M

SLUG = "elicitador"

YAML = """<pre style="margin:0;white-space:pre-wrap;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.55">- id: "1.2"
  tipo: decisao
  titulo: Óculos conectado?
  descricao: O app verifica se os óculos estão pareados e com bateria.
  ator: app
  ramos: {"Sim": "1.2a", "Não": "1.2b"}
- id: "1.2a"
  tipo: acao
  titulo: Modo áudio e vídeo
  descricao: Áudio principal do microfone de lapela (melhor qualidade)
    e vídeo dos óculos. O áudio dos óculos fica como reserva.
  ator: app
  proximo: "1.3"</pre>"""

CASO = dict(
    lead="Especificação de um produto que grava reuniões, levanta requisitos com IA e executa a demanda com segurança. O processo está escrito em YAML, para pessoas e para IA. Um script confere a consistência e gera os diagramas de cada fase.",
    ficha=[("Tipo", "Método e especificação de produto"), ("Formato", "YAML, JSON e Mermaid"),
           ("Conferência", "Script em Python"), ("Versão", "1.0, outubro de 2026")],
    numeros=[("10", "fases"), ("71", "passos"), ("12", "decisões"), ("5", "controles permanentes")],
    blocos=[
        ("Diagramas gerados", M.telas(SLUG, [
            ("01-visao-geral.webp", "Visão geral: as 10 fases e os retornos entre elas."),
            ("02-fase-3.webp", "Fase 3, processamento na nuvem: transcrição, identificação de quem falou e linha do tempo de evidências."),
            ("03-fase-8.webp", "Fase 8, execução segura: backup, ambiente isolado, testes com limite de tentativas e revisão humana."),
        ], celular=True), "Diagramas Mermaid gerados pelo gerar.py a partir do processo.yaml.", "larga"),
        ("As 10 fases", M.fluxograma([
            ("Preparo", [("F0 Cadastro", "conta, biometria, aparelhos, cofre"), ("F1 Preparação", "pauta e consentimento"), ("F2 Captura", "áudio e vídeo em blocos")]),
            ("Entendimento", [("F3 Processamento", "transcrição e falantes"), ("F4 Elicitação", "IA como especialista"), ("F5 Esclarecimento", "perguntas ao responsável"), ("F6 Artefatos", "documento e fluxograma")]),
            ("Execução", [("F7 Viabilidade", "cruza com os sistemas do usuário"), ("F8 Execução segura", "homologação e revisão"), ("F9 Entrega", "curso em vídeo e manutenção")]),
        ], "F4 e F5 se repetem até não sobrar pendência. F6 volta a F4 se a revisão não aprovar."), "", "larga"),
        ("Passos por fase", M.barras([("F0 Cadastro", 7), ("F1 Preparação", 8), ("F2 Captura", 6), ("F3 Processamento", 9), ("F4 Elicitação", 5),
                                      ("F5 Esclarecimento", 5), ("F6 Artefatos", 6), ("F7 Viabilidade", 8), ("F8 Execução segura", 12, True), ("F9 Entrega", 5)],
                                     titulo="71 passos: 51 ações, 12 decisões, 6 exceções, início e fim")),
        ("Formato do passo", M.painel("processo.yaml", YAML, "Cada passo tem tipo, ator, entradas, saídas, critério de conclusão e o passo seguinte."),
         "Tipos: ação, decisão, exceção, início e fim. Atores: usuário, participante, app, nuvem, agente de IA, agente conector e revisor humano."),
        ("Conferência automática", M.lista([
            ("Identificador repetido", "Interrompe com [PAREI]."),
            ("Decisão incompleta", "Toda decisão precisa de 2 ramos ou mais."),
            ("Destino inexistente", "Todo próximo passo precisa existir."),
            ("Ator", "Toda ação, decisão e exceção precisa de ator."),
            ("Alcance", "Todo passo é alcançável a partir do início e chega ao fim."),
        ]), "Resultado atual: 71 passos, 12 decisões, todos alcançáveis e todos chegam ao fim."),
        ("Controles permanentes", M.lista([
            ("C1 Criptografia", "TLS 1.2 ou superior e dado cifrado em repouso."),
            ("C2 Perfis e auditoria", "Dono, gestor, analista e convidado; log imutável."),
            ("C3 LGPD", "Biometria com consentimento específico e relatório de impacto."),
            ("C4 Orçamento de IA", "Teto por projeto e escolha do modelo mais barato que atende."),
            ("C5 Cronograma", "Marcos, percentual concluído e alerta de atraso."),
        ])),
    ],
    stack=["Python", "YAML", "JSON", "Mermaid"],
)
