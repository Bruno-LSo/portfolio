# Guia dos casos detalhados do portfólio HoldUp

Site: https://bruno-lso.github.io/portfolio/ (GitHub Pages). Código: D:\Repositorios\portfolio.
Modelo de arquivo: ferramentas/casos/_exemplo.py. Componentes: ferramentas/modelo.py (fim do arquivo).

## Objetivo

Cada projeto ganha uma página que mostra o trabalho de forma visual e fácil de percorrer:
- telas reais (capturas) ou reproduzidas;
- fluxo de páginas ou fluxo do processo (fluxograma);
- funcionalidades explicadas;
- em modelos preditivos e estatística: objetivo, dados, organização das etapas, modelos e métricas, achados e limites;
- diagramas que ajudam a entender o que foi feito.

## Arquivos que você pode criar ou alterar

- ferramentas/casos/<slug>.py (um por projeto, `CASO = dict(...)`).
- assets/telas/<slug>/NN-nome.webp (imagens).
- ferramentas/maquetes/<slug>/*.html (telas reproduzidas, quando precisar).
- projetos/<slug>.html, só para as 5 páginas manuais (manual=True em conteudo.py) do seu grupo.

Não altere conteudo.py, gerar.py, modelo.py, o CSS nem arquivos de outro grupo. Se faltar um componente, use
`M.diagrama` com SVG próprio ou relate a necessidade no relatório final. Não faça commit nem push.

## Formato do CASO

Projeto que já existe em conteudo.py: as chaves do CASO substituem as do registro. Leia o registro atual
e mantenha o que está certo (lead, ficha, numeros). Reescreva `blocos` completos, na ordem da página.

Projeto novo: inclua `nome`, `resumo` (uma frase, aparece no sumário da área), `tec` (3 a 4 itens com " · "),
`area`, `lead`, `ficha`, `stack` e, se houver página pública limpa, `link=("Abrir o painel", "https://...")`.
Áreas: comercio, campo (Território e infraestrutura), gestao (Sistemas e plataformas), dados (Dados e painéis),
saude (Saúde), modelos (Modelos preditivos e estatística), produtos (Aplicativos, jogos e automação).

Blocos: `(título, html, apoio opcional, "larga" opcional)`. Use "larga" para telas, fluxogramas, diagramas.

Componentes (import modelo as M):
- `M.telas(slug, [(arquivo, legenda)], celular=False)`: galeria; clique amplia. `celular=True` para telas de app.
- `M.fluxograma([(rótulo do nível, [caixa, ...], texto da seta opcional)], nota)`: caixa é "Título" ou ("Título", "detalhe").
- `M.achados([(valor, texto)])`: cartões de resultado.
- `M.barras([(rótulo, valor, destaque_bool)], titulo, casas, sufixo, nota)`: barras horizontais.
- `M.diagrama(svg, legenda)`: SVG inline. Cores: fundo das caixas #162A37, borda/acento #4FD1D4 (teal),
  #4FB3E8 (azul), #5CC98A (verde), #FFD25E (amarelo), #F08A7E (coral), texto #EAF1F6, texto suave #A9B8C6,
  fonte "Sora" (texto) e "JetBrains Mono" (números). viewBox largo (ex. 0 0 960 300), texto mínimo 13.
  Cada `id` de marker deve ser único na página (prefixe com o slug).
- `M.lista([(título, texto)])`, `M.fluxo([(etiqueta, título, texto)])`, `M.texto([parágrafos])`,
  `M.painel(barra, html, nota)`, `M.colunas(html1, html2, ...)`.

Ordem sugerida: Telas (larga) → Fluxo de páginas ou do processo (larga) → Funcionalidades → Arquitetura ou
Organização → Achados/Resultados → Diagrama (se ajudar). Em modelos: Objetivo → Dados → Organização
(fluxograma) → Modelos e métricas (barras) → Achados → Limites → Telas/gráficos do notebook.

## Telas

Captura: `py -3.12 -X utf8 ferramentas/capturar.py <url ou .html> assets/telas/<slug>/01-nome.webp [larg] [alt] [escala] [espera_ms]`
(computador 1440 900; celular 390 844 2). Rode sem `-I` (dependência na pasta do usuário).

De onde tirar a tela, nesta ordem:
1. Página pública do projeto (GitHub Pages bruno-lso.github.io/<repo>, site do cliente no ar).
2. HTML gerado que já está no repositório local D:\Repositorios\<repo> (abrir o arquivo, sem rodar código).
3. Tela reproduzida: monte um HTML em ferramentas/maquetes/<slug>/ fiel ao layout real (copie a estrutura e o
   CSS do código do projeto) com dados fictícios, e capture. A legenda termina com "Dados fictícios.".
   Para aplicativos Flutter (Dart), reproduza as telas a partir do código das telas.

Gráficos de notebook (.ipynb): extraia as imagens PNG das saídas (base64 em outputs[].data["image/png"]),
converta para WEBP com PIL e use em `M.telas`. Tabelas de métricas viram `M.barras` ou `M.achados`.

Privacidade, obrigatório: abra cada imagem (ferramenta Read) antes de usar. Não pode aparecer nome de pessoa
física (salvo autor de referência bibliográfica), CPF, e-mail, telefone, endereço, número de processo, dado
de paciente, senha, chave ou token, nem conteúdo de campanha eleitoral. Se aparecer, refaça com dados
fictícios ou não use. Não abra páginas que exijam login.

Não rode código dos projetos que escreva em banco, envie e-mail, chame API com credencial ou altere arquivos
do repositório. Ler arquivos e abrir HTML estático no navegador pode.

## Texto

- Português do Brasil, estilo ASD-STE100: frase curta (até 25 palavras), uma ideia por frase, voz ativa.
- Sóbrio e direto. Sem adjetivo de efeito, sem frase de abertura ou fechamento, sem "robusto", "inovador",
  "solução completa", "experiência", "jornada", "potencializar", "alavancar", "de ponta", "transformar".
- Toda afirmação diz a medida: "338 fichas", "AUC-ROC 0,788", "+76% trombólises (398 para 701 por ano)".
- Números no padrão brasileiro (1.234,5). Nunca travessão (— ou –) nem emoji. Hífen só em palavra composta.
- Nunca dizer "Bruno Lima"; o portfólio fala da HoldUp. Não citar ClickNow nem oportunidade comercial.
- Cliente: nome da organização só se já estiver em conteudo.py ou for órgão público. Pessoa física nunca.
- Nada inventado: todo número vem do código, do notebook, do banco local de exemplo ou do README do repositório.

## Repositórios

Locais em D:\Repositorios\<repo>. Os que não estão lá: `gh repo clone Bruno-LSo/<repo>` para uma pasta em
C:\Users\bruno\AppData\Local\Temp\claude\b0147d3e513e77ed\06d533f4-7760-4419-9574-2df6e564a8b1\scratchpad\repos\<repo>
(nunca dentro do portfolio). Lista completa com descrição: scratchpad\repos.tsv.

Fora do portfólio: campanha eleitoral (marchese-*, alisson-governador, confea-eleicoes-2026, emendas-parlamentares-sp,
InsightsCampanha, TerritorioSpProf, engaja-mapeador, vtracker-auditoria, fala-guacu-mogi, politica-one-laender,
Dashboard-Vinicius-Marchese, DashboardPython-EleicoesConfea, CNFCRDSHELECT, Vinicius-Varios-Dashs-Python),
creasp-gabinete-dashboard, creasp-portal-lucario, creasp-mapas-territoriais, confea-dri-sispad, confea-luana,
confea-organograma, gerente-de-portfolios, confea-comissoes, creasp-extracoes-db2, studytrack*, shawn*, utilitarios-dados.

## Conferência antes de terminar

1. `py -3.12 -I -X utf8 ferramentas/gerar.py` sem erro. Se falhar por arquivo de outro grupo, espere 1 minuto e repita.
2. Capture a sua página inteira (ex. 1440 x 4000) e a versão celular (390 x 3000 x 1) e abra as imagens:
   nada cortado, nada sobreposto, sem rolagem lateral.
3. `python -I -X utf8 D:\Claude\scripts\utilitarios\verificacao\verificar_saida.py projetos/<slug>.html`: saída 0.
   Avisos de hífen em código JavaScript podem ficar.
4. Páginas manuais: depois de rodar o gerador, confira se a sua edição continua no arquivo (outro gerador
   rodando ao mesmo tempo pode ter regravado). Inclua `<script src="../assets/js/telas.js"></script>` antes de
   `</body>` se usar `M.telas` ou `data-barras`.

## Relatório final (resposta ao coordenador)

Curto: slugs feitos; projetos novos com área; número de imagens por projeto; o que não foi possível e por quê;
qualquer dado sensível encontrado em repositório público.
