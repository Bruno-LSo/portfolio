"""Formatador de pareceres técnicos (repositório formatador-pareceres)."""
import modelo as M

SLUG = "formatador"

_SVG = (
    '<svg viewBox="0 0 960 250" role="img" aria-label="Regra de comparação de cada parágrafo">'
    '<defs><marker id="formatador-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>'
    '<rect x="10" y="90" width="180" height="70" rx="10" fill="#162A37" stroke="#4FB3E8"/>'
    '<text x="100" y="120" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Parágrafo do</text>'
    '<text x="100" y="142" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">parecer</text>'
    '<path d="M190 125 H238" stroke="#4FD1D4" stroke-width="2" marker-end="url(#formatador-s)"/>'
    '<polygon points="340,60 440,125 340,190 240,125" fill="#162A37" stroke="#FFD25E"/>'
    '<text x="340" y="120" fill="#EAF1F6" font-family="Sora" font-size="13" text-anchor="middle">Existe no</text>'
    '<text x="340" y="138" fill="#EAF1F6" font-family="Sora" font-size="13" text-anchor="middle">modelo?</text>'
    '<path d="M440 125 H470 V45 H508" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#formatador-s)"/>'
    '<text x="478" y="80" fill="#A9B8C6" font-family="Sora" font-size="13">sim</text>'
    '<path d="M440 125 H470 V205 H508" stroke="#4FD1D4" stroke-width="2" fill="none" marker-end="url(#formatador-s)"/>'
    '<text x="478" y="178" fill="#A9B8C6" font-family="Sora" font-size="13">não</text>'
    '<rect x="510" y="10" width="440" height="70" rx="10" fill="#162A37" stroke="#5CC98A"/>'
    '<text x="730" y="40" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Copia a formatação do modelo, sem borda</text>'
    '<text x="730" y="62" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">pergunta e opções (X) com o X em negrito</text>'
    '<rect x="510" y="170" width="440" height="70" rx="10" fill="#162A37" stroke="#F08A7E"/>'
    '<text x="730" y="200" fill="#EAF1F6" font-family="Sora" font-size="14" text-anchor="middle">Conteúdo novo: Calibri 11, justificado, borda 1/2 pt</text>'
    '<text x="730" y="222" fill="#A9B8C6" font-family="Sora" font-size="13" text-anchor="middle">linhas novas seguidas viram um bloco só</text>'
    '</svg>')

CASO = dict(
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-terminal.webp", "Execução no terminal: três arquivos de entrada e o resumo do processamento. Dados fictícios."),
            ("02-documentos.webp", "Os dois documentos Word gerados: parecer formatado e revisão consolidada. Dados fictícios."),
        ]), "Telas reproduzidas a partir do código, com texto genérico.", "larga"),
        ("Fluxo do processo", M.fluxograma([
            ("Conversão", [("conversor_docling.py", ".doc, .docx e .pdf para Markdown")]),
            ("Entradas", [("Modelo", "Word com a formatação de referência"), ("Parecer", "texto do revisor 1"), ("Segundo parecer", "texto do revisor 2")], "compara com difflib"),
            ("Saídas", [("Parecer formatado", "texto novo com borda"), ("Revisão consolidada", "blocos novos por pergunta, dos dois revisores")]),
        ]), "", "larga"),
        ("Regra de comparação", M.diagrama(_SVG, "Cada parágrafo é comparado com o modelo; só o que não existe nele recebe destaque."), "", "larga"),
        ("Revisão consolidada", M.lista([
            ("Cabeçalho", "Ignora tudo antes de \"Identificação e estrutura geral\"."),
            ("Blocos", "Agrupa as linhas novas de cada revisor por pergunta, com uma borda por bloco."),
            ("Limpeza", "Tira do primeiro parecer a palavra OBSERVAÇÃO e as notas [Fonte: ...]; o segundo fica completo."),
            ("Respostas diferentes", "Quando as marcações (X) não batem, repete a pergunta em negrito com a resposta do segundo revisor."),
        ])),
        ("Saídas", M.lista([("Parecer formatado", "Formatação do documento base, com o texto novo destacado."),
                            ("Revisão consolidada", "Blocos novos agrupados e identificados por revisor.")])),
    ],
    stack=["Python", "Docling", "python-docx", "difflib", "markdown2", "pywin32"],
)
