# Portfólio · HoldUp

Projetos organizados por área.

Site publicado: https://bruno-lso.github.io/portfolio/

## Estrutura

- `index.html`: áreas do portfólio.
- `areas/`: uma página por área, com o sumário dos projetos.
- `projetos/`: uma página por projeto.
- `ferramentas/conteudo.py`: conteúdo de todas as páginas e a ordem das áreas e dos projetos.
- `ferramentas/gerar.py`: gera `index.html`, `areas/`, `projetos/` e `assets/js/projetos.js`.
- `assets/js/graficos.js`: gráficos em SVG.
- `assets/js/mosaico.js`: mosaico animado da página inicial.

As páginas de Canteiros Urbanos, pesca artesanal, calculadora do AVC, risco cardiovascular e telemedicina têm demonstração própria e são editadas no HTML; o gerador atualiza apenas o cabeçalho, a migalha e a navegação delas.

## Como atualizar

```bash
python ferramentas/gerar.py
```

## Cuidados com os dados

Os números vêm dos repositórios de cada projeto e das bases oficiais usadas neles. Dados de clientes aparecem só agregados; telas e demonstrações usam dados fictícios. Nenhum dado pessoal, chave ou endereço interno entra neste repositório.

## Identidade visual

Cores, fontes (Sora e JetBrains Mono) e logotipo da HoldUp.
