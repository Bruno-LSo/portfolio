"""Caso detalhado: Núcleo de dados (repositório nucleo-dados)."""
import modelo as M

SLUG = "nucleo-dados"

GUARDA = '''<svg viewBox="0 0 960 300" role="img" aria-label="Como o núcleo de dados guarda um arquivo">
<defs><marker id="nd-seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#4FD1D4"/></marker></defs>
<g font-family="Sora" text-anchor="middle">
<rect x="20" y="100" width="170" height="90" rx="10" fill="#162A37" stroke="#4FB3E8"/>
<text x="105" y="135" fill="#EAF1F6" font-size="15">Arquivo original</text>
<text x="105" y="160" fill="#A9B8C6" font-size="13">.csv .xlsx .pdf .shp</text>
<rect x="250" y="100" width="170" height="90" rx="10" fill="#162A37" stroke="#4FD1D4"/>
<text x="335" y="135" fill="#EAF1F6" font-size="15">sha1 do conteúdo</text>
<text x="335" y="160" fill="#A9B8C6" font-size="13">vira o nome do objeto</text>
<rect x="480" y="30" width="200" height="80" rx="10" fill="#162A37" stroke="#FFD25E"/>
<text x="580" y="63" fill="#EAF1F6" font-size="15">Texto: zstd nível 19</text>
<text x="580" y="88" fill="#A9B8C6" font-size="13">CSV cerca de 30x menor</text>
<rect x="480" y="180" width="200" height="80" rx="10" fill="#162A37" stroke="#FFD25E"/>
<text x="580" y="213" fill="#EAF1F6" font-size="15">Binário: como está</text>
<text x="580" y="238" fill="#A9B8C6" font-size="13">xlsx, docx, imagem, zip</text>
<rect x="740" y="30" width="200" height="80" rx="10" fill="#162A37" stroke="#5CC98A"/>
<text x="840" y="63" fill="#EAF1F6" font-size="15">Bucket dados</text>
<text x="840" y="88" fill="#A9B8C6" font-size="13">privado</text>
<rect x="740" y="180" width="200" height="80" rx="10" fill="#162A37" stroke="#F08A7E"/>
<text x="840" y="213" fill="#EAF1F6" font-size="15">Bucket restrito</text>
<text x="840" y="238" fill="#A9B8C6" font-size="13">dados pessoais</text>
<path d="M190 145 H247" stroke="#4FD1D4" stroke-width="2" marker-end="url(#nd-seta)"/>
<path d="M420 135 L477 80" stroke="#4FD1D4" stroke-width="2" marker-end="url(#nd-seta)"/>
<path d="M420 155 L477 210" stroke="#4FD1D4" stroke-width="2" marker-end="url(#nd-seta)"/>
<path d="M680 70 H737" stroke="#4FD1D4" stroke-width="2" marker-end="url(#nd-seta)"/>
<path d="M680 220 H737" stroke="#4FD1D4" stroke-width="2" marker-end="url(#nd-seta)"/>
<path d="M680 95 L737 195" stroke="#4FD1D4" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#nd-seta)"/>
<path d="M680 195 L737 95" stroke="#4FD1D4" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#nd-seta)"/>

<text x="480" y="292" fill="#A9B8C6" font-size="13">Acima de 45 MB, o objeto é dividido em partes. Com pessoal=True, vai para o bucket restrito.</text>
</g></svg>'''

CASO = dict(
    lead="Pacote Python usado pelos demais projetos para abrir arquivos de dados. Se o arquivo está no disco, usa o do disco. Se não está, baixa a cópia guardada e confere que ela é idêntica ao original.",
    ficha=[("Tipo", "Infraestrutura interna"), ("Armazenamento", "Supabase Storage, 2 buckets privados"),
           ("Conferência", "sha1 no envio e em cada download"), ("Compressão", "zstd nível 19 para texto")],
    numeros=[("6", "funções de dados"), ("4", "funções de credenciais"), ("7", "tipos de arquivo público baixados da fonte"), ("45 MB", "limite de cada parte")],
    blocos=[
        ("Como o arquivo é encontrado", M.fluxograma([
            ("Pedido", [("nd.caminho(ref)", "caminho original ou só o nome")]),
            ("Fonte pública?", [("Sim", "baixa o zip da fonte oficial, confere ETag, data e tamanho"), ("Não", "segue")], "não"),
            ("No disco?", [("Sim", "usa o arquivo do disco"), ("Não", "procura no catálogo")], "não"),
            ("Catálogo", [("Baixa para o cache", "pasta local do usuário"), ("Descomprime", "se for texto"), ("Confere sha1", "idêntico byte a byte")]),
            ("Resultado", [("Caminho local", "o read_csv do projeto não muda")]),
        ], "Sem conexão, a cópia pública já baixada é usada, com aviso. Shapefile traz junto .dbf, .shx, .prj e .cpg."), "", "larga"),
        ("Como o arquivo é guardado", M.diagrama(GUARDA, "O mesmo conteúdo em duas pastas é guardado uma vez só, porque o nome do objeto é o sha1."), "", "larga"),
        ("Funções", M.lista([
            ("caminho(ref)", "Devolve um caminho local, do disco ou do cache."),
            ("ler(ref)", "O mesmo, já lido com pandas pela extensão."),
            ("guardar(arquivo)", "Envia e registra no catálogo, com os repositórios que leem o arquivo."),
            ("glob(padrão)", "Junta o que está no disco com o que está no catálogo."),
            ("existe(ref)", "Substitui os.path.exists para arquivos de dados."),
            ("listar(filtro)", "Consulta o catálogo."),
            ("credencial, segredo, preparar_env, preparar_arquivo", "Recriam .env e arquivos de chave a partir do cofre, sem guardar valor no repositório."),
        ])),
        ("Segurança", M.lista([
            ("Buckets privados", "Sem URL pública."),
            ("Catálogo fechado", "RLS ligado e forçado, sem política. Só a chave de serviço lê e escreve."),
            ("Teste com chave pública", "Catálogo, arquivos e segredos respondem bloqueado (401)."),
            ("Uso", "Só em scripts locais. Nunca em página ou aplicativo no navegador."),
        ])),
        ("Teste antes de apagar", M.texto(["A variável NUCLEO_DADOS_SEM_DISCO=1 faz o pacote ignorar o disco para tudo que está no catálogo. O projeto roda como se a pasta original já tivesse sido apagada."])),
    ],
    stack=["Python", "Supabase Storage", "PostgreSQL", "Supabase Vault", "zstd"],
)
