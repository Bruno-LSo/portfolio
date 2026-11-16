"""Captura de tela para o portfólio.

Uso:
  py -3.12 -X utf8 ferramentas/capturar.py <url ou arquivo .html> <saida.webp> [largura] [altura] [escala] [espera_ms]

Abre a página num Chromium sem janela (Playwright), espera a rede parar, captura a área
visível e grava em WEBP (qualidade 82, no máximo 1600 px de largura).
Padrão 1440 x 900 (computador). Celular: 390 844 2.
Use só páginas com dados públicos ou fictícios.
"""
import io
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def capturar(origem, saida, largura=1440, altura=900, escala=1, espera=1200):
    url = origem if origem.startswith(("http://", "https://", "file:")) else Path(origem).resolve().as_uri()
    saida = Path(saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        try:
            nav = pw.chromium.launch()
        except Exception:
            nav = pw.chromium.launch(executable_path=CHROME)
        pag = nav.new_page(viewport={"width": largura, "height": altura}, device_scale_factor=escala)
        pag.goto(url, wait_until="networkidle", timeout=90000)
        pag.wait_for_timeout(espera)
        png = pag.screenshot()
        nav.close()
    img = Image.open(io.BytesIO(png)).convert("RGB")
    if img.width > 1600:
        img = img.resize((1600, round(img.height * 1600 / img.width)), Image.LANCZOS)
    img.save(saida, "WEBP", quality=82, method=6)
    print(saida, img.size)


if __name__ == "__main__":
    a = sys.argv[1:]
    capturar(a[0], a[1], *(int(x) for x in a[2:6]))
