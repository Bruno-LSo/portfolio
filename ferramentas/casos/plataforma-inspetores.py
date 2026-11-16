import modelo as M

SLUG = "plataforma-inspetores"
F = "Protótipo com dados fictícios."

CASO = dict(
    blocos=[
        ("Fluxo completo", M.fluxograma([
            ("1. Indicar", [("Vagas e cotas", "cadeiras livres por CAF e câmara"),
                            ("Pré-validação", "registro, anuidade, empresa, endereço e título pelo CPF")], "link por e-mail"),
            ("2. Aceitar", [("Aceite", "o que é ser inspetor"), ("Currículo", "modelo único"),
                            ("Documentos", "4 certidões, comprovante e conta"), ("Assinatura", "3 documentos com gov.br")], "envio"),
            ("3. Validar", [("Agentes", "conferem cada item na fonte"), ("Devolução", "só o item com problema"),
                            ("Exceções", "Controle de Inspetoria decide")], "tudo validado"),
            ("4. Nomear", [("Gabinete", "aprova"), ("SUPFIS e Presidência", "assinam em lote"),
                           ("Dossiê", "PDF único para o SEI")], "nomeação"),
            ("5. Mandato", [("Carteira", "no aplicativo"), ("CAF", "calendário, convocação e check-in"),
                            ("Faltas", "justificativa assinada"), ("Monitoramento", "anuidade e processos, todo mês")], "fim"),
            ("6. Encerrar", [("Licença", "temporária"), ("Exoneração", "a pedido ou obrigatória"), "Fim do mandato"]),
        ], "Regulamento das Inspetorias 2026. Se a pré-validação falha, nenhuma indicação é criada e nenhum link sai."), "", "larga"),
        ("Indicação", M.telas(SLUG, [
            ("01-entrar.webp", "Login só com gov.br. CPF sem acesso recebe a mensagem única \"Acesso não liberado\"."),
            ("02-painel-vagas.webp", "Vagas da regional: cadeiras ocupadas, câmaras e cotas de cada CAF."),
            ("03-indicar.webp", "Indicação: 7 conferências feitas na hora, pelo registro no Crea-SP."),
        ]), F, "larga"),
        ("Aplicativo do indicado", M.telas(SLUG, [
            ("04-convite.webp", "E-mail com o link e o prazo."),
            ("05-aceitar.webp", "Aceite com as regras da função."),
            ("06-curriculo.webp", "Passo 1: currículo no modelo."),
            ("07-documentos.webp", "Passo 2: documentos com link de emissão."),
            ("08-assinar.webp", "Passo 3: termos e assinatura gov.br."),
            ("10-devolucao.webp", "Devolução de 1 documento; os outros 5 ficam validados."),
        ], celular=True), F, "larga"),
        ("Validação e nomeação", M.telas(SLUG, [
            ("09-agentes.webp", "Resultado dos agentes: 9 itens validados, 1 inconsistente, 1 inconclusivo."),
            ("11-assinaturas.webp", "Presidência assina as nomeações em lote, com a conferência do dia."),
        ]), F, "larga"),
        ("Mandato no aplicativo", M.telas(SLUG, [
            ("12-nomeado.webp", "Carteira de inspetor e próxima reunião."),
            ("14-convite-caf.webp", "Convocação da CAF com a pauta."),
            ("15-justificar.webp", "Justificativa de ausência com texto sugerido."),
            ("17-checkin.webp", "Check-in por localização, raio de 200 m."),
            ("20-licenca.webp", "Pedido de licença ou exoneração."),
            ("21-avisos.webp", "Central de avisos, também por e-mail e notificação."),
        ], celular=True), F, "larga"),
        ("Mandato e gestão na web", M.telas(SLUG, [
            ("13-calendario.webp", "Calendário anual da CAF: 6 reuniões."),
            ("16-justificativas.webp", "Inspetor-Chefe aceita ou recusa justificativas."),
            ("18-presenca.webp", "Presença gerada pelo check-in, com quórum."),
            ("19-monitoramento.webp", "Monitoramento mensal: anuidade, faltas e processos éticos."),
            ("22-admin.webp", "Estrutura, acessos com dupla aprovação e parâmetros."),
            ("23-painel-gerencial.webp", "Painel gerencial do estado e busca de currículos."),
        ]), F, "larga"),
        ("Perfis de acesso", M.lista([("Chefe de Equipe", "Indica; a indicação passa pelo Gerente Regional."),
                     ("Gerente Regional", "Indica e aprova na sua GRE."),
                     ("Gabinete da Presidência", "Indica e aprova os processos validados."),
                     ("Controle de Inspetoria", "Decide exceções e registra o SEI."),
                     ("SUPFIS e Presidência", "Assinam as nomeações."),
                     ("Chefe da UGI, Financeiro, Auditoria", "Consulta no seu escopo."),
                     ("Administrador", "Homologa acessos e altera parâmetros, com registro."),
                     ("Indicado", "Existe enquanto a indicação está aberta."),
                     ("Inspetor, Inspetor-Chefe, Inspetor Especial", "Vêm do mandato e da designação."),
                     ("Escopo", "GRE, municípios da divisão, CAF ou estado, conforme o perfil.")]),
         "10 perfis de funcionário e 4 papéis do profissional. Os perfis vêm do organograma, conferido 1 vez por mês."),
        ("Situações da indicação", M.fluxograma([
            ("Início", [("Em elaboração", "Gerente aprova em 3 dias úteis")]),
            ("Indicado", [("Aguardando ação", "30 dias, lembrete a cada 7"), ("Em correção", "15 dias")]),
            ("Validação", [("Em validação", "exceção em 2 dias úteis")]),
            ("Aprovação", [("Gabinete", "5 dias úteis"), ("Assinaturas", "5 + 5 dias úteis"), ("SEI", "2 dias úteis")]),
            ("Fim", ["Efetivada", ("Cancelada", "8 motivos")]),
        ], "9 situações. Prazos são parâmetros editáveis com dupla aprovação."), "", "larga"),
        ("Engenharia", M.lista([("Banco", "Toda gravação passa por funções do banco; todas as 82 tabelas têm regra de acesso por linha."),
                                ("Regras de negócio", "Regulamento implementado em pacote próprio, com testes. Tela não decide regra."),
                                ("Integrações", "Versões simulada e real para APIs internas, certidões e gov.br."),
                                ("Testes", "Ponta a ponta com Playwright e acessibilidade em 6 larguras de tela, temas claro e escuro."),
                                ("Migrações", "38 migrações aplicadas pelo GitHub Actions."),
                                ("Documentação", "13 documentos de contexto, especificação, arquitetura e testes.")])),
    ],
)
