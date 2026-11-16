"""Caso detalhado: Transcritor de áudio (repositório transcritor-whisper)."""
import modelo as M

SLUG = "transcritor"

JSON = """<pre style="margin:0;white-space:pre-wrap;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.5">{
  "source_file": "reuniao-exemplo.ogg",
  "language": "pt",
  "duration_ms": 402300,
  "model": "large-v3",
  "word_timestamps": true,
  "segments": [
    { "id": 0, "start_ms": 0, "end_ms": 4120,
      "start": "00:00:00", "end": "00:00:04",
      "text": "Bom dia, vamos começar pela pauta de hoje.",
      "words": [
        { "word": "Bom", "start_ms": 0, "end_ms": 260, "probability": 0.991 },
        { "word": "dia,", "start_ms": 260, "end_ms": 610, "probability": 0.987 }
      ] }
  ]
}</pre>"""

CASO = dict(
    lead="Transcrição de áudios e vídeos em português, um arquivo ou uma pasta inteira, com o modelo Whisper large-v3 rodando no próprio computador. Tem proteção contra laço de repetição e gera texto, texto com tempo e JSON com tempo por palavra.",
    ficha=[("Modelo", "Whisper large-v3 (faster-whisper)"), ("Saída", "TXT, TXT com tempo e JSON"),
           ("Execução", "Local, sem envio do áudio"), ("Aceleração", "GPU com volta automática para CPU")],
    numeros=[("8", "formatos aceitos: mp4, wav, mp3, m4a, ogg, opus, mkv, webm"), ("16", "trechos de 30 s por lote na GPU"), ("3", "arquivos de saída por áudio")],
    blocos=[
        ("Tela", M.telas(SLUG, [("01-terminal.webp", "Execução no terminal: modelo na GPU, falas com tempo, um trecho reparado e os arquivos gravados. Dados fictícios.")]),
         "O programa roda no terminal. A tela reproduz as mensagens que o script imprime.", "larga"),
        ("Processo", M.fluxograma([
            ("Entrada", [("Arquivo ou pasta", "8 extensões")]),
            ("Modelo", [("GPU", "CUDA, float16, lote de 16"), ("CPU", "int8, lote de 4, se a GPU falhar")], "carrega"),
            ("Transcrição", [("Corte de silêncio", "pausas acima de 500 ms"), ("Busca em feixe", "5 hipóteses"), ("Dicionário", "termos do projeto, opcional")]),
            ("Conferência", [("Trecho repetitivo?", "palavras iguais ou texto que comprime demais")], "sim"),
            ("Reparo", [("Retranscreve o trecho", "sem contexto anterior, 6 temperaturas"), ("Último recurso", "limita a 3 repetições")]),
            ("Saída", [("nome.txt", "texto corrido"), ("nome_com_timestamps.txt", "[HH:MM:SS --> HH:MM:SS]"), ("nome.json", "tempo por palavra, em ms")]),
        ]), "", "larga"),
        ("Proteção contra repetição", M.lista([
            ("Mesma palavra", "4 palavras ou mais, todas iguais."),
            ("Pouca variedade", "Menos de 30% de palavras diferentes num trecho de 8 palavras ou mais."),
            ("Compressão", "Texto que fica mais de 2,4 vezes menor no zlib."),
            ("Reparo", "O trecho volta ao modelo com penalidade de repetição 1,1 e bloqueio de sequências de 4 palavras."),
        ])),
        ("Saída em JSON", M.painel("nome.json", JSON, "Estrutura do arquivo gerado por transcrever_json.py. Dados fictícios."), "Usada para sincronizar legendas e cortes de vídeo."),
        ("Uso em outros projetos", M.texto(["A versão com JSON alimenta as legendas do projeto American Legends. A mesma base, com o idioma trocado para inglês, transcreve a narração dos episódios."])),
    ],
    stack=["Python", "faster-whisper", "CTranslate2", "CUDA"],
)
