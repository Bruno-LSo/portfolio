"""Caso detalhado: Mr. Yalc (repositórios mr-yalc e mryalc-guitars)."""
import modelo as M

SLUG = "mr-yalc"

CASO = dict(
    lead="Programa de computador que recebe uma música (arquivo, YouTube ou Spotify), separa voz e instrumentos, identifica andamento, tom e acordes e permite mixar, mudar tom e velocidade e exportar. Uma segunda versão é dedicada à guitarra.",
    ficha=[("Tipo", "Uso próprio"), ("Separação", "Demucs (Spleeter como alternativa)"),
           ("Análise", "librosa"), ("Interface", "PyQt5 e, na versão de guitarra, tkinter")],
    numeros=[("4", "faixas na versão principal: voz, bateria, baixo e outros"), ("6", "faixas na versão de guitarra"), ("±12", "semitons de mudança de tom"), ("0,5x a 2x", "de velocidade")],
    blocos=[
        ("Telas", M.telas(SLUG, [
            ("01-mixer.webp", "Reprodutor e mixer: cada faixa com pan, volume, mudo e solo, e presets como Karaoke. Dados fictícios."),
            ("02-analise.webp", "Análise musical: acorde atual, próximo acorde, linha de acordes com tempo, BPM, tom e compasso. Dados fictícios."),
            ("03-guitarras.webp", "Versão de guitarra: guitarras separadas por canal, metrônomo no BPM detectado e forma de onda de cada faixa. Dados fictícios."),
        ]), "Telas reproduzidas a partir do código das interfaces (mesmo layout, cores e textos).", "larga"),
        ("Processo", M.fluxograma([
            ("Entrada", [("Arquivo local", "mp3, wav, flac, ogg..."), ("YouTube", "yt-dlp"), ("Spotify", "spotdl")]),
            ("Separação", [("Demucs", "4 faixas"), ("Versão de guitarra", "htdemucs_6s + mdx_extra, média dos dois")]),
            ("Análise", [("BPM", ""), ("Tom", ""), ("Acordes", "croma e modelos de acorde"), ("Energia e dançabilidade", "")]),
            ("Mixagem", [("Volume e pan", "por faixa"), ("Tom e velocidade", "rubberband, sem distorção"), ("Loop A-B", "")]),
            ("Saída", [("Faixas em WAV", ""), ("Mix exportado", "WAV, FLAC ou MP3 320k")]),
        ]), "", "larga"),
        ("Funcionalidades", M.lista([
            ("Presets do mixer", "Personalizado, Karaoke (sem voz), Acapella (só voz), Instrumental e Drums & Bass."),
            ("Reprodutor", "Velocidade de 0,5x a 2x, tom de -12 a +12 semitons, loop inteiro ou entre os pontos A e B."),
            ("Acordes", "Acorde atual em destaque, próximo acorde e contagem de acordes únicos."),
            ("Cache", "Faixas já separadas ficam guardadas e não são processadas de novo."),
        ])),
        ("Versão de guitarra", M.lista([
            ("Dois modelos", "Roda htdemucs_6s (6 faixas) e mdx_extra (4 faixas) e faz a média, com 10 passadas e 50% de sobreposição."),
            ("Várias guitarras", "Separa até 4 guitarras: pelo canal esquerdo e direito ou por faixa de frequência (80 a 250 Hz, 250 a 2.000 Hz, 2.000 a 8.000 Hz)."),
            ("Metrônomo", "Gera metronome.wav no BPM detectado, alinhado à música."),
            ("Limites", "Músicas de até 10 minutos e arquivos de até 100 MB."),
        ]), "Repositório mryalc-guitars."),
    ],
    stack=["Python", "PyTorch", "Demucs", "librosa", "rubberband", "PyQt5", "tkinter", "yt-dlp"],
)
