"""Caso detalhado: American Legends (repositório dark-channel-horror)."""
import modelo as M

SLUG = "american-legends"

# Início (s), tipo e transição de cada uma das 41 imagens do piloto (episodios/01_bell_witch/shotlist.json).
CORTES = [(0, "ilu", "d"), (26, "out", "d"), (30, "ilu", "d"), (51, "out", "d"), (77, "ilu", "h"), (98, "foto", "d"),
          (129, "ret", "d"), (132, "out", "d"), (140, "foto", "d"), (158, "liv", "f"), (172, "liv", "d"), (199, "liv", "d"),
          (216, "liv", "d"), (264, "liv", "d"), (274, "liv", "d"), (300, "ilu", "d"), (330, "ret", "d"), (362, "liv", "d"),
          (384, "ret", "d"), (406, "liv", "d"), (430, "liv", "d"), (460, "ret", "d"), (492, "ilu", "f"), (541, "ilu", "d"),
          (553, "out", "d"), (593, "foto", "d"), (632, "foto", "h"), (651, "ret", "d"), (660, "liv", "d"), (677, "out", "d"),
          (754, "ret", "d"), (790, "foto", "d"), (834, "liv", "d"), (859, "ilu", "d"), (903, "ret", "d"), (926, "foto", "d"),
          (945, "ilu", "d"), (963, "foto", "f"), (995, "ret", "d"), (1038, "foto", "d"), (1066, "foto", "d")]
DUR = 1092.2
COR = {"ilu": "#F08A7E", "liv": "#FFD25E", "foto": "#5CC98A", "ret": "#4FB3E8", "out": "#4FD1D4"}
NOME = {"ilu": "Ilustração de época (8)", "liv": "Livro ou página digitalizada (11)", "foto": "Foto do local (9)",
        "ret": "Retrato (8)", "out": "Objeto ou imagem genérica (5)"}


def _linha_do_tempo():
    x0, x1, y = 40, 920, 70
    k = (x1 - x0) / DUR
    p = [f'<svg viewBox="0 0 960 250" role="img" aria-label="Linha do tempo das 41 imagens do episódio piloto">',
         '<g font-family="Sora">']
    for i, (t, tipo, tr) in enumerate(CORTES):
        fim = CORTES[i + 1][0] if i + 1 < len(CORTES) else DUR
        p.append(f'<rect x="{x0 + t * k:.1f}" y="{y}" width="{max((fim - t) * k - 1.5, 1):.1f}" height="44" fill="{COR[tipo]}" opacity=".85"/>')
        if tr == "f":
            p.append(f'<line x1="{x0 + t * k:.1f}" y1="{y - 22}" x2="{x0 + t * k:.1f}" y2="{y + 58}" stroke="#EAF1F6" stroke-width="2" stroke-dasharray="4 3"/>')
    for m in range(0, 19, 3):
        x = x0 + m * 60 * k
        p.append(f'<text x="{x:.1f}" y="{y + 76}" fill="#A9B8C6" font-size="13" font-family="JetBrains Mono" text-anchor="middle">{m} min</text>')
    p.append(f'<text x="{x0}" y="{y - 30}" fill="#EAF1F6" font-size="13">Linhas tracejadas: fade para preto (3 viradas de ato). As demais trocas usam dissolve ou corte seco.</text>')
    for j, (tipo, nome) in enumerate(NOME.items()):
        cx = x0 + (j % 3) * 300
        cy = 190 + (j // 3) * 28
        p.append(f'<rect x="{cx}" y="{cy - 12}" width="14" height="14" fill="{COR[tipo]}"/><text x="{cx + 22}" y="{cy}" fill="#EAF1F6" font-size="13">{nome}</text>')
    p.append("</g></svg>")
    return "".join(p)


ROTEIRO = """<pre style="margin:0;white-space:pre-wrap;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.55">[ambience id="spooky_night" gain="-30" fade="2500"]
[ambience id="horror_drone" gain="-28" fade="3000"]

[hook]
This is the only death in American legal history...
whose official cause was recorded as a supernatural force.
[/hook]

[normal]
No court ever overturned it. No coroner ever corrected it.
[/normal]

[sfx id="door_creak" pos="R" gain="-6" delay="200" move="R>L"]</pre>"""

CASO = dict(
    lead="Linha de produção de vídeos de folclore dos Estados Unidos para um canal no YouTube. O roteiro marcado gera a narração com efeitos e ambiência, as legendas sincronizadas, o catálogo de imagens com licença e o vídeo montado.",
    ficha=[("Tipo", "Canal próprio"), ("Narração", "Voz clonada (Chatterbox) ou Edge-TTS para teste"),
           ("Legendas", "SRT pelo tempo de cada palavra"), ("Montagem", "FFmpeg, 1920 x 1080, 30 quadros/s")],
    numeros=[("41", "imagens no episódio piloto"), ("568", "legendas"), ("18 min 12 s", "de duração"), ("-14 LUFS", "volume final, padrão do YouTube")],
    blocos=[
        ("Linha de produção", M.fluxograma([
            ("1. Roteiro", [("Blocos .txt", "6 partes e 3 teasers no piloto"), ("Marcações", "tom da voz, efeito, ambiência, música, silêncio")]),
            ("2. Áudio", [("Narração", "um tom por bloco: normal, hook, sussurro, grito..."), ("Teatro sonoro", "efeito com posição L/R e movimento"), ("Mixagem", "-14 LUFS e teto de pico")], "_FULL.wav"),
            ("3. Transcrição", [("faster-whisper", "tempo por palavra"), ("Legendas", "arquivo .srt")]),
            ("4. Imagens", [("Shot list", "segundo exato de cada imagem"), ("Planilha", "shot list, licenças e storyboard"), ("Download", "nome = segundo de entrada")]),
            ("5. Montagem", [("Ken Burns", "zoom e pan por imagem"), ("Transições", "dissolve, corte seco, fade"), ("Acabamento", "cor teal e âmbar, grão")], "MP4"),
            ("6. Publicação", [("Capa e título", ""), ("Descrição", "fontes, créditos e aviso de IA")]),
        ], "As etapas 1, 4, 5 e 6 são automatizadas por skills do Claude Code. O áudio é renderizado no Google Colab."), "", "larga"),
        ("Episódio piloto, imagem por imagem", M.diagrama(_linha_do_tempo(), "Fonte: shotlist.json do piloto (Bell Witch, Tennessee). Cada faixa é uma imagem, do segundo em que entra até a próxima."), "", "larga"),
        ("Roteiro marcado", M.painel("01_cold_open.txt", ROTEIRO, "Início do roteiro do piloto. O motor lê as marcações e posiciona cada som no tempo."),
         "A voz muda de tom pelo bloco. O efeito pode andar de um lado para o outro do ouvinte."),
        ("Movimento das imagens", M.barras([("push_in (aproxima)", 28, True), ("pan_down", 4), ("pull_out (afasta)", 4), ("pan_right", 2), ("pan_left", 1), ("pan_up", 1), ("static", 1)],
                                           titulo="Imagens por movimento, piloto (41)")),
        ("Licença das imagens", M.barras([("Domínio público", 20, True), ("Própria", 8), ("A verificar", 7), ("CC-BY-SA", 4), ("CC-BY", 2)],
                                         titulo="Imagens por licença, piloto (41)",
                                         nota="As 7 marcadas para verificar saem numa lista de ação manual, com o segundo, o que mostrar e onde procurar.")),
    ],
    stack=["Python", "PyTorch", "Chatterbox TTS", "Edge-TTS", "faster-whisper", "pydub", "pyloudnorm", "FFmpeg"],
)
