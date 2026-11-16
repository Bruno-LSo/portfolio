# Portfólio · Bruno Lima · HoldUp

Site com os meus projetos, agrupados pelo tipo de problema que resolvem: saúde e aprendizado de máquina, campo e território, lojas virtuais e marketplaces, sistemas de gestão, dados públicos e aplicativos.

Site publicado: https://bruno-lso.github.io/portfolio/

## O que tem aqui

- `index.html`: abertura, áreas, casos em destaque, método e o catálogo completo com filtro e busca. O filtro fica no endereço (`?area=saude`, `?q=supabase`), para dar para mandar o link já filtrado.
- `casos/`: um estudo de caso por projeto, com problema, escopo, números reais e, quando faz sentido, uma demonstração que roda na própria página (montar uma cesta, enviar ficha sem sinal, simular a calculadora, comparar modelos).
- `assets/js/projetos.js`: o catálogo. Projeto novo entra aqui; se tiver estudo de caso, `caso: true`.
- `assets/js/graficos.js`: gráficos em SVG sem dependência.
- `assets/js/mosaico.js`: o mosaico animado da abertura, nas cores da marca. Pausa fora da tela e respeita quem prefere menos movimento.
- `ferramentas/gerar_casos.py`: gera as páginas de caso padronizadas a partir do conteúdo no próprio script.

## Como atualizar

```bash
python ferramentas/gerar_casos.py
```

As páginas `risco-cardiovascular`, `calculadora-avc`, `telemedicina-avc`, `canteiros-urbanos` e `pesca-artesanal` têm demonstração própria e são editadas direto no HTML.

## Cuidados com os dados

Os números vêm dos repositórios de cada projeto e das bases oficiais usadas neles. Dados de clientes aparecem só agregados; telas e demonstrações usam dados fictícios. Nenhum dado pessoal, chave ou endereço interno entra neste repositório.

## Identidade visual

Cores, fontes (Sora e JetBrains Mono) e logotipo da HoldUp.
