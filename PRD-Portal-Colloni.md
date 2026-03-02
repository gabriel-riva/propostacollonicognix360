# Portal Colloni — PRD (Product Requirements Document)

| | |
|---|---|
| **Documento** | PRD — Portal de Conhecimento do Grupo Colloni |
| **Versão** | 1.0 |
| **Data** | 02 de março de 2026 |
| **Autor** | Cognix360 — Consultoria em IA e Automação para Negócios |
| **Cliente** | Grupo Colloni (Colloni Participações) |
| **Status** | Rascunho para validação interna |

---

## 1. Visão do Produto

### 1.1 O que é o Portal Colloni

O **Portal Colloni** é uma plataforma web exclusiva do Grupo Colloni, desenvolvida pela Cognix360, que centraliza todo o conhecimento, acompanhamento e evolução do programa de IA dentro do grupo.

O portal funciona como o **espaço digital oficial** onde gestores, equipes de TI e champions das 13 empresas do grupo acessam materiais, acompanham projetos, entregam tarefas e evoluem no uso estratégico de inteligência artificial.

### 1.2 Por que existe

O programa de acompanhamento contínuo da Cognix360 com o Grupo Colloni gera um volume significativo de conteúdo: gravações de encontros, tutoriais, templates, projetos identificados, mini tarefas e evolução de champions. Sem um espaço centralizado, esse conhecimento se perde em e-mails, drives e conversas.

O portal resolve isso ao:

- **Centralizar** todo o conteúdo do programa em um único lugar acessível
- **Organizar** o conhecimento por fase, empresa e tipo de material
- **Acompanhar** o progresso de projetos, tarefas e champions de forma visual
- **Empoderar** gestores com visão clara do que está acontecendo sem precisar executar
- **Manter o engajamento** entre encontros com tarefas e notificações

### 1.3 Objetivos Estratégicos

| Objetivo | Descrição |
|----------|-----------|
| Acesso organizado | Todo participante encontra qualquer material em menos de 3 cliques |
| Visibilidade do progresso | Gestores veem o status geral do programa sem pedir relatórios |
| Engajamento contínuo | Mini tarefas e notificações mantêm o grupo ativo entre encontros |
| Escala de conhecimento | Champions replicam conhecimento nas empresas com base nos materiais |
| Registro institucional | Tudo que foi criado, discutido e implementado fica registrado permanentemente |

---

## 2. Personas

### 2.1 Gestor — Diretor ou Gerente de empresa do grupo

**Perfil:** Diretor, gerente ou sócio de uma das 13 empresas. Não vai executar soluções de IA, mas precisa entender o que pode ser feito para cobrar, delegar e direcionar. Conforme Márcia Rigo definiu: *"Nós queremos que eles entendam o que pode ser feito."*

**Necessidades:**
- Visão rápida do progresso geral do programa
- Acesso a gravações e resumos dos encontros
- Acompanhamento dos projetos da sua empresa no kanban
- Saber quem são os champions e o que estão produzindo
- Receber notificações sobre novos materiais relevantes

**Comportamento esperado:** Acessa o portal 1-2 vezes por semana, principalmente para ver o dashboard, assistir gravações e acompanhar projetos. Não navega profundamente — precisa de informação na superfície.

**Frustração a evitar:** Portal complexo demais, muitos cliques para encontrar algo, visual confuso.

---

### 2.2 TI — Analista ou Coordenador de TI

**Perfil:** Profissional de tecnologia que participa dos encontros junto com os gestores. Tem papel de disseminador: sabe quem tem a "dor" dentro da empresa e pode conectar as soluções às pessoas certas.

**Necessidades:**
- Acesso a materiais técnicos (tutoriais, documentação, templates)
- Busca eficiente por tipo de conteúdo e empresa
- Visualização dos champions para saber quem está evoluindo
- Acesso a templates de automação e prompts reutilizáveis
- Possibilidade de comentar e interagir com o conteúdo

**Comportamento esperado:** Acessa com mais frequência que o gestor, busca materiais específicos, faz download de templates e repassa para colegas.

**Frustração a evitar:** Materiais desorganizados, sem filtros funcionais, difícil encontrar algo específico.

---

### 2.3 Champion — Colaborador facilitador

**Perfil:** Pessoa identificada dentro de uma empresa como alguém com facilidade ou abertura para IA. Não é necessariamente de TI — pode ser de qualquer área. Vai criar soluções, aplicar templates e ser referência na empresa.

**Necessidades:**
- Templates e tutoriais passo-a-passo acessíveis
- Acompanhamento da sua própria evolução (nível, soluções criadas)
- Área para responder mini tarefas e registrar o que aplicou
- Contato com outros champions para trocar experiências
- Visibilidade do que outros champions estão fazendo (inspiração)

**Comportamento esperado:** Usuário mais ativo do portal. Acessa após cada encontro para entregar tarefas, consultar templates e registrar soluções.

**Frustração a evitar:** Não saber onde está, não entender seu progresso, tarefas confusas.

---

### 2.4 Administrador — Cognix360

**Perfil:** Gabriel Riva ou equipe da Cognix360. Gerencia todo o conteúdo do portal, cria tarefas, atualiza projetos, publica gravações e acompanha engajamento.

**Necessidades:**
- Upload rápido de gravações e materiais pós-encontro
- Criação e atribuição de mini tarefas com poucos cliques
- Gestão de champions (níveis, status, empresa)
- Gestão do kanban de projetos
- Relatórios de engajamento (quem acessou, quem entregou)
- Controle de agenda e encontros

**Comportamento esperado:** Acessa após cada encontro para publicar materiais e criar tarefas. Semanalmente para acompanhar engajamento e atualizar projetos.

**Frustração a evitar:** Processo lento de publicação, muitos passos para uma tarefa simples.

---

## 3. Funcionalidades Core

### 3.1 Dashboard Principal

O dashboard é a tela inicial após o login. Deve oferecer uma visão panorâmica do programa sem exigir navegação adicional.

**Componentes do Dashboard:**

| Componente | Descrição | Posição |
|-----------|-----------|---------|
| Barra de progresso do programa | Indica a fase atual (1, 2 ou 3) e percentual de avanço | Topo da área principal |
| Card "Próximo Encontro" | Data, horário, tema previsto e botão de acesso ao link Meet/Zoom | Destaque lateral direito |
| Mini tarefas pendentes | Lista das tarefas atribuídas ao usuário com status e prazo | Centro-esquerda |
| Mini tarefas concluídas (resumo) | Contador de tarefas concluídas no ciclo atual | Abaixo das pendentes |
| Métricas do programa | Horas utilizadas vs. contratadas; projetos em andamento; champions ativos | Cards horizontais |
| Notificações recentes | Novos materiais publicados, lembretes de tarefas, atualizações de projetos | Lista lateral ou topo |
| Acesso rápido | Atalhos para "Última gravação", "Materiais recentes", "Meus projetos" | Cards de atalho |

**Regras de comportamento:**
- O dashboard se adapta à persona: gestor vê métricas e progresso, champion vê tarefas e templates recentes
- Notificações não lidas aparecem com badge numérico
- Card "Próximo Encontro" pisca suavemente 24h antes do evento

---

### 3.2 Biblioteca de Conhecimento

A biblioteca é o repositório central de todo o conteúdo gerado no programa.

**Tipos de conteúdo:**

| Tipo | Ícone | Descrição |
|------|-------|-----------|
| Gravação | Play circle | Vídeo do encontro (embed ou link externo) |
| Tutorial | Book open | Guia passo-a-passo com texto e imagens |
| Template | File text | Prompt, workflow ou automação reutilizável |
| Apresentação | Monitor | Slides usados em encontros |
| Documento | File | PDFs, planilhas ou materiais complementares |

**Organização hierárquica:**
```
Fase do Programa
  └── Encontro (data + tema)
       └── Tipo de material
```

**Filtros disponíveis:**
- Por fase (1, 2 ou 3)
- Por empresa do grupo
- Por tipo de conteúdo (gravação, tutorial, template, etc.)
- Por data (mais recente primeiro)
- Busca textual por palavras-chave

**Funcionalidades adicionais:**
- **Favoritos pessoais:** cada usuário pode marcar materiais como favorito (estrela) para acesso rápido
- **Visualização em grade ou lista:** toggle para alternar entre cards visuais e listagem compacta
- **Indicador de "novo":** badge em materiais publicados nos últimos 7 dias
- **Contador de visualizações:** mostra quantas vezes o material foi acessado (visível para admin)

---

### 3.3 Mapa de Champions

Visualização que mostra os champions identificados em cada empresa do grupo, seu nível de evolução e contribuições.

**Visualização principal — Grid de empresas:**

Cada empresa do grupo aparece como um card com:
- Logo da empresa (ou ícone genérico se não disponível)
- Nome da empresa
- Quantidade de champions
- Status geral (indicador visual)

**Ao clicar em uma empresa, expande para mostrar os champions:**

| Campo | Descrição |
|-------|-----------|
| Avatar | Foto ou iniciais do champion |
| Nome | Nome completo |
| Empresa | Empresa à qual pertence |
| Área | Departamento ou setor |
| Nível | "Em formação", "Ativo" ou "Referência" |
| Soluções criadas | Contador de soluções registradas |
| Última atividade | Data da última interação no portal |

**Níveis de evolução:**

| Nível | Critério | Badge visual |
|-------|----------|--------------|
| Em formação | Identificado, participando dos encontros | Cinza |
| Ativo | Entregou mini tarefas, criou pelo menos 1 solução | Dourado claro |
| Referência | Múltiplas soluções, engajamento consistente, ajuda outros | Marrom dourado |

**Funcionalidades:**
- Filtro por empresa
- Filtro por nível
- Perfil individual do champion com timeline de evolução
- Lista de soluções criadas por cada champion
- Botão de contato (abre e-mail ou chat) para comunicação entre champions

---

### 3.4 Projetos e Oportunidades

Área que acompanha projetos de IA identificados, em análise, em desenvolvimento ou já implementados.

**Kanban visual com 4 colunas:**

```
┌─────────────┬─────────────┬─────────────────┬──────────────┐
│ Identificado│ Em Análise  │ Em Desenvolvimento│ Implementado │
│             │             │                  │              │
│  [Card]     │  [Card]     │  [Card]          │  [Card]      │
│  [Card]     │             │  [Card]          │              │
│             │  [Card]     │                  │  [Card]      │
└─────────────┴─────────────┴─────────────────┴──────────────┘
```

**Cada card de projeto contém:**

| Campo | Descrição |
|-------|-----------|
| Título | Nome descritivo do projeto |
| Empresa | Qual empresa do grupo (com tag colorida) |
| Responsável | Champion ou pessoa designada |
| Descrição | Breve resumo do que o projeto resolve |
| Impacto esperado | Texto livre sobre o benefício previsto |
| Status | Coluna atual no kanban |
| Data de criação | Quando foi identificado |
| Última atualização | Quando foi movido ou editado |

**Visão detalhada do projeto (ao clicar):**
- Timeline de evolução (quando passou de cada fase)
- Descrição completa
- Comentários e notas de acompanhamento
- Indicadores de resultado pós-implementação (preenchidos após deploy)
- Materiais relacionados (links para biblioteca)

**Filtros:**
- Por empresa
- Por status (coluna do kanban)
- Por responsável
- Por período

---

### 3.5 Mini Tarefas (Entre Encontros)

Sistema de tarefas leves atribuídas após cada encontro para manter engajamento e gerar insumos para as sessões seguintes.

**Listagem de tarefas:**

Cada tarefa exibe:

| Campo | Descrição |
|-------|-----------|
| Título | Descrição curta da tarefa |
| Descrição | Detalhamento do que é esperado |
| Encontro de origem | A qual encontro a tarefa está vinculada |
| Prazo | Data limite (geralmente até o próximo encontro) |
| Status | Pendente → Em andamento → Concluída |
| Atribuído a | Pessoa responsável |

**Status e cores:**

| Status | Cor | Comportamento |
|--------|-----|---------------|
| Pendente | Amarelo (#EAB308) | Tarefa criada, ainda não iniciada |
| Em andamento | Azul (#3B82F6) | Participante começou a trabalhar |
| Concluída | Verde (#22C55E) | Entregue com resposta preenchida |
| Atrasada | Vermelho (#EF4444) | Passou do prazo sem conclusão |

**Área de resposta:**
- Campo de texto rico para o participante descrever o que imaginou, aplicou ou descobriu
- Possibilidade de anexar arquivo (screenshot, documento)
- Botão "Enviar" que muda o status para "Concluída"
- Após envio, não pode ser editado (apenas visualizado)

**Histórico:**
- Aba "Anteriores" mostra entregas de ciclos passados
- Filtro por encontro de origem
- Estatísticas pessoais: tarefas concluídas vs. total atribuído

---

### 3.6 Agenda e Encontros

Calendário visual com todos os turnos agendados do programa.

**Visualização do calendário:**
- Vista mensal como padrão
- Cada encontro aparece como bloco colorido no dia correspondente
- Encontros passados em tom suave; futuros em destaque
- Hoje marcado com indicador visual

**Detalhes de cada encontro (ao clicar):**

| Campo | Descrição |
|-------|-----------|
| Data e horário | Início e fim do turno (formato 4h) |
| Tema previsto | Assunto principal a ser tratado |
| Fase | A qual fase do programa pertence |
| Participantes esperados | Lista de pessoas confirmadas |
| Link da reunião | Botão direto para Meet/Zoom |
| Status | Agendado / Realizado / Cancelado |

**Pós-encontro (após a sessão acontecer):**
- Gravação linkada automaticamente (ou manualmente pelo admin)
- Notas do encontro (resumo do que foi discutido)
- Materiais publicados vinculados
- Mini tarefas geradas a partir deste encontro
- Tudo acessível diretamente na ficha do encontro

---

### 3.7 Painel Administrativo (Cognix360)

Área exclusiva do administrador para gestão completa do portal.

**Módulos do painel:**

#### 3.7.1 Gestão de Conteúdo
- Upload de gravações (embed de YouTube/Vimeo ou upload direto)
- Upload de materiais (PDF, PPTX, templates)
- Categorização por fase, encontro e tipo
- Edição e exclusão de materiais publicados
- Vinculação de materiais a encontros específicos

#### 3.7.2 Gestão de Mini Tarefas
- Criação de tarefa com título, descrição e prazo
- Atribuição individual ou em grupo (por empresa, por tipo de persona)
- Visualização de todas as entregas recebidas
- Marcação de tarefas como "destaque" (para apresentar no próximo encontro)

#### 3.7.3 Gestão de Champions
- Cadastro de novos champions
- Atualização de nível (Em formação → Ativo → Referência)
- Registro de soluções criadas por cada champion
- Desativação de champions que saíram do programa

#### 3.7.4 Gestão de Projetos
- Criação de projetos no kanban
- Movimentação entre colunas
- Adição de comentários e notas de acompanhamento
- Registro de indicadores de resultado

#### 3.7.5 Gestão de Agenda
- Criação e edição de encontros no calendário
- Definição de tema, participantes e link da reunião
- Vinculação pós-encontro (gravação, notas, materiais, tarefas)

#### 3.7.6 Relatórios de Engajamento

| Métrica | Descrição |
|---------|-----------|
| Acessos ao portal | Quem acessou e quando (por período) |
| Materiais visualizados | Quais materiais foram mais acessados |
| Tarefas concluídas | Taxa de conclusão por pessoa e por empresa |
| Champions ativos | Quantos estão acessando e produzindo |
| Projetos em movimento | Quantos projetos avançaram no kanban no período |

Relatórios exportáveis em PDF para inclusão em reportes ao grupo.

---

## 4. Design UI/UX

### 4.1 Princípios de Design

| Princípio | Descrição | Aplicação Prática |
|-----------|-----------|-------------------|
| **Clareza** | Informação acessível em poucos cliques, sem complexidade desnecessária | Máximo 3 cliques para qualquer conteúdo. Dashboard mostra o essencial sem scroll |
| **Familiaridade** | Visual similar a ferramentas que gestores já usam diariamente | Padrões visuais de Google Workspace e Notion. Sidebar + canvas. Sem experimentalismos |
| **Progressividade** | Revela complexidade conforme o usuário avança | Tela inicial limpa; detalhes aparecem ao clicar. Filtros avançados em painel colapsável |
| **Identidade** | Marca do Grupo Colloni presente de forma elegante, sem ser pesada | Logo no topo da sidebar, cores institucionais nos elementos principais, sem excesso decorativo |
| **Consistência** | Mesmos padrões visuais em todas as telas | Cards com mesmo border-radius, mesma tipografia, mesma hierarquia de cores em todo o portal |

---

### 4.2 Layout Geral

```
┌───────────┬──────────────────────────────────────────────────┐
│           │  Header: Nome do usuário | Empresa | Notificações│
│  SIDEBAR  ├──────────────────────────────────────────────────┤
│  (fixa)   │                                                  │
│           │                                                  │
│  Logo     │              ÁREA PRINCIPAL                      │
│  Colloni  │              (Canvas)                            │
│           │              ~80% da tela                        │
│  Nav      │                                                  │
│  items    │                                                  │
│           │                                                  │
│  ───────  │                                                  │
│  Perfil   │                                                  │
│  Suporte  │                                                  │
└───────────┴──────────────────────────────────────────────────┘
```

**Sidebar (20% da largura, mínimo 240px):**
- Fundo: #472D07 (marrom dourado)
- Texto: #FFFFFF
- Logo Colloni no topo com espaçamento generoso
- Itens de navegação com ícone + texto
- Item ativo destacado com fundo rgba(255,255,255,0.15)
- Hover sutil em rgba(255,255,255,0.08)

**Área principal (80% da largura):**
- Fundo: #FAFAFA
- Padding interno: 32px
- Largura máxima do conteúdo: 1200px (centralizado se a tela for maior)

**Header:**
- Fundo: #FFFFFF com borda inferior sutil
- Altura: 64px
- Nome do usuário + empresa à direita
- Ícone de notificações com badge contador
- Breadcrumb opcional à esquerda (ex: "Biblioteca > Fase 1 > Encontro 3")

**Responsividade:**
- Em telas menores que 768px: sidebar colapsa para hamburger menu
- Cards empilham verticalmente
- Kanban permite scroll horizontal

---

### 4.3 Navegação (Sidebar)

Itens na ordem exata, com ícones sugeridos:

| Ordem | Item | Ícone | Rota |
|-------|------|-------|------|
| 1 | Dashboard | LayoutDashboard | /dashboard |
| 2 | Biblioteca | BookOpen | /biblioteca |
| 3 | Champions | Trophy | /champions |
| 4 | Projetos | Kanban | /projetos |
| 5 | Tarefas | CheckCircle | /tarefas |
| 6 | Agenda | Calendar | /agenda |
| — | *Separador visual* | — | — |
| 7 | Meu Perfil | User | /perfil |
| 8 | Suporte | Headphones | /suporte |
| — | *Apenas admin:* | — | — |
| 9 | Administração | Settings | /admin |

**Comportamento da navegação:**
- Item ativo com background claro e borda esquerda de 3px na cor accent (#C1B89A)
- Tooltip no hover com nome da seção (útil quando sidebar está minimizada)
- Badge de notificação ao lado de "Tarefas" (quantidade pendente) e "Biblioteca" (novos materiais)

---

### 4.4 Componentes Visuais

#### Cards
- Background: #FFFFFF
- Border-radius: 12px
- Sombra: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06)
- Hover: sombra aumenta sutilmente para 0 4px 6px rgba(0,0,0,0.1)
- Padding interno: 20px (desktop), 16px (mobile)

#### Status Badges
| Status | Cor de fundo | Cor do texto | Exemplo |
|--------|-------------|-------------|---------|
| Ativo / Concluída | #DCFCE7 | #166534 | Verde suave |
| Pendente | #FEF9C3 | #854D0E | Amarelo suave |
| Em andamento | #DBEAFE | #1E40AF | Azul suave |
| Atrasada / Alerta | #FEE2E2 | #991B1B | Vermelho suave |
| Referência | #F5F0E6 | #472D07 | Marrom dourado suave |

#### Progress Bars
- Height: 8px
- Border-radius: 4px (arredondadas)
- Background track: #E5E7EB
- Fill: gradiente de #C1B89A para #472D07 (do accent ao primary)
- Animação suave ao carregar

#### Avatares
- Formato: circular
- Tamanhos: 32px (listas), 48px (cards), 80px (perfil)
- Borda: 2px solid #E5E7EB
- Fallback: iniciais do nome em fundo #472D07 com texto #FFFFFF

#### Tags de Empresa
Cada empresa do grupo tem uma cor suave diferenciada:

| Empresa | Cor da tag |
|---------|-----------|
| Tecnotri | #DBEAFE (azul) |
| Robustec Componentes | #FEE2E2 (vermelho) |
| Robustec Implementos | #FCE7F3 (rosa) |
| LBF Industrial | #FEF3C7 (âmbar) |
| Gallus | #D1FAE5 (verde) |
| Movix | #E0E7FF (indigo) |
| Up Equipamentos | #F3E8FF (violeta) |
| Purificatta | #CCFBF1 (teal) |
| Innovar Urbanizadora | #FFF7ED (laranja) |
| Visione | #F0FDF4 (esmeralda) |
| Carbo Campers | #FEF2F2 (vermelho claro) |
| Granjas São João / Vila Carreiro | #ECFDF5 (verde claro) |
| Colloni Participações | #F5F0E6 (dourado) |

#### Ícones
- Biblioteca: Lucide Icons ou Phosphor Icons (outline, clean)
- Tamanho padrão: 20px na sidebar, 16px inline
- Cor na sidebar: #FFFFFF (opacidade 0.7 inativo, 1.0 ativo)
- Cor no conteúdo: #6B7280 (cinza muted)

#### Botões

| Tipo | Background | Texto | Border | Uso |
|------|-----------|-------|--------|-----|
| Primário | #472D07 | #FFFFFF | nenhuma | Ações principais (Enviar, Salvar) |
| Secundário | transparent | #472D07 | 1px solid #472D07 | Ações secundárias (Cancelar, Voltar) |
| Accent | #C1B89A | #472D07 | nenhuma | CTAs de destaque (Acessar Encontro) |
| Ghost | transparent | #6B7280 | nenhuma | Ações terciárias (Filtrar, Ordenar) |
| Destructive | #EF4444 | #FFFFFF | nenhuma | Ações de exclusão (apenas admin) |

Todos com border-radius: 8px, padding: 10px 20px, transição hover de 150ms.

---

### 4.5 Paleta de Cores do Portal

**Cores primárias:**

| Token | Hex | Uso |
|-------|-----|-----|
| primary | #472D07 | Sidebar, botões primários, headings em destaque |
| accent | #C1B89A | CTAs, progress bars, elementos de destaque |
| background | #FAFAFA | Fundo geral da área principal |
| surface | #FFFFFF | Cards, modais, header |
| text-primary | #1A1A1A | Texto principal, títulos |
| text-secondary | #6B7280 | Texto auxiliar, labels, timestamps |
| text-muted | #9CA3AF | Placeholders, texto desabilitado |
| border | #E5E7EB | Bordas de separação, dividers |

**Cores de status:**

| Token | Hex | Uso |
|-------|-----|-----|
| success | #22C55E | Concluído, ativo, positivo |
| warning | #EAB308 | Pendente, atenção |
| info | #3B82F6 | Em andamento, informativo |
| danger | #EF4444 | Atrasado, erro, exclusão |

**Cores de hover e interação:**

| Token | Valor | Uso |
|-------|-------|-----|
| sidebar-hover | rgba(255,255,255,0.08) | Hover em itens da sidebar |
| sidebar-active | rgba(255,255,255,0.15) | Item ativo na sidebar |
| card-hover-shadow | 0 4px 6px rgba(0,0,0,0.1) | Sombra ao passar o mouse em cards |
| primary-hover | #5A3A0E | Hover em botões primários |
| accent-hover | #B0A688 | Hover em botões accent |

---

### 4.6 Tipografia

| Elemento | Fonte | Peso | Tamanho | Line-height |
|----------|-------|------|---------|-------------|
| H1 (título de página) | Open Sans | Bold (700) | 28px | 36px |
| H2 (seção) | Open Sans | Bold (700) | 22px | 30px |
| H3 (subtítulo) | Open Sans | SemiBold (600) | 18px | 26px |
| Body | Open Sans | Regular (400) | 15px | 24px |
| Body small | Open Sans | Regular (400) | 13px | 20px |
| Label | Open Sans | Medium (500) | 13px | 18px |
| Caption | Open Sans | Regular (400) | 12px | 16px |
| Metric/Data | JetBrains Mono | Regular (400) | 14px | 20px |
| Metric grande | JetBrains Mono | Medium (500) | 24px | 32px |

**Regras tipográficas:**
- Cor padrão de texto: #1A1A1A
- Nunca usar mais de 2 tamanhos de heading na mesma tela
- Métricas numéricas (horas, contadores, percentuais) sempre em JetBrains Mono para alinhamento visual
- Máximo de 70 caracteres por linha em textos de parágrafo

---

## 5. User Flows Principais

### Flow 1: Gestor acessa o portal após encontro

```
Login
  → Dashboard
    → Vê card "Último encontro" com botão "Ver gravação"
      → Clica → Biblioteca → Player da gravação
        → Abaixo do player: notas do encontro + materiais publicados
          → Volta ao Dashboard (breadcrumb ou botão voltar)
```

**Pontos de atenção:**
- A gravação deve estar disponível em até 24h após o encontro
- Notas e materiais aparecem vinculados automaticamente
- O gestor não deve precisar procurar a gravação: ela aparece no dashboard

---

### Flow 2: Champion entrega mini tarefa

```
Login
  → Dashboard
    → Card "Tarefas Pendentes" mostra tarefa com prazo
      → Clica "Responder"
        → Abre modal/página com descrição da tarefa
          → Campo de texto para resposta
            → Escreve o que imaginou/aplicou
              → Botão "Enviar resposta"
                → Confirmação visual (checkmark animado)
                  → Status muda para "Concluída" no dashboard
```

**Pontos de atenção:**
- O campo de resposta deve suportar texto formatado (negrito, lista)
- Após envio, a resposta fica visível para o admin e para o próprio champion
- Notificação para o admin quando uma tarefa é concluída

---

### Flow 3: TI consulta templates na Biblioteca

```
Login
  → Sidebar: Biblioteca
    → Visualização padrão: todos os materiais (grid)
      → Clica no filtro "Tipo" → Seleciona "Templates"
        → Grid mostra apenas templates
          → Clica em um template
            → Visualização do template com descrição e preview
              → Botão "Copiar" ou "Download"
                → Template copiado/baixado para uso local
```

**Pontos de atenção:**
- Filtros devem ser persistentes (não resetar ao voltar)
- Templates devem ter descrição clara do caso de uso
- Indicação visual de quais templates são mais populares (contador de downloads)

---

### Flow 4: Gestor acompanha projetos da sua empresa

```
Login
  → Sidebar: Projetos
    → Kanban geral (todas as empresas)
      → Clica no filtro "Empresa" → Seleciona sua empresa
        → Kanban mostra apenas projetos da empresa
          → Clica em um card de projeto
            → Página detalhada com timeline, status, comentários
              → Vê evolução do projeto e impacto esperado
                → Volta ao kanban (botão voltar ou breadcrumb)
```

**Pontos de atenção:**
- O filtro por empresa deve lembrar a preferência do usuário
- Timeline visual mostra quando o projeto passou de cada fase
- Gestores podem ver projetos de outras empresas para inspiração

---

### Flow 5: Admin publica material pós-encontro

```
Login (admin)
  → Sidebar: Administração
    → Módulo: Gestão de Conteúdo
      → Botão "+ Publicar material"
        → Formulário: tipo, fase, encontro vinculado, upload
          → Publica gravação (embed YouTube/Vimeo URL)
          → Publica materiais complementares (upload PDF/PPTX)
    → Módulo: Gestão de Tarefas
      → Botão "+ Nova tarefa"
        → Formulário: título, descrição, prazo, atribuição
          → Atribui a participantes (individual ou por grupo)
            → Confirma → Notificação enviada aos participantes
```

**Pontos de atenção:**
- Fluxo de publicação deve ser completável em menos de 5 minutos
- Possibilidade de criar múltiplas tarefas de uma vez (batch)
- Preview do material antes de publicar
- Notificações automáticas aos participantes relevantes

---

### Flow 6: Champion explora Mapa de Champions

```
Login (champion)
  → Sidebar: Champions
    → Grid de empresas do grupo (cards com logo)
      → Clica na sua empresa
        → Vê lista de champions da empresa com perfil resumido
          → Clica em outro champion
            → Perfil detalhado: nível, soluções, atividade
              → Botão "Entrar em contato" (abre e-mail)
      → Clica em outra empresa (para ver champions de lá)
        → Vê soluções criadas por champions de outras empresas
          → Inspiração para aplicar algo similar
```

**Pontos de atenção:**
- A visualização deve incentivar a descoberta (mostrar soluções interessantes)
- Champions podem ver toda a rede, não apenas sua empresa
- Perfil mostra evolução temporal (timeline visual)

---

## 6. Informação Arquitetural

### 6.1 Estrutura de Conteúdo

```
Programa de IA — Grupo Colloni
├── Fase 1: Visão e Possibilidades
│   ├── Encontro 1 (data)
│   │   ├── Gravação
│   │   ├── Apresentação
│   │   ├── Notas
│   │   └── Mini Tarefas geradas
│   ├── Encontro 2 (data)
│   │   └── ...
│   └── Templates da Fase 1
├── Fase 2: Identificação e Empoderamento
│   ├── Encontro N (data)
│   │   └── ...
│   └── Templates da Fase 2
├── Fase 3: Aprofundamento e Projetos
│   ├── Encontro N (data)
│   │   └── ...
│   └── Templates da Fase 3
└── Materiais Gerais (sem fase específica)
```

### 6.2 Relações entre Entidades

| Entidade | Pertence a | Relaciona com |
|----------|-----------|---------------|
| Encontro | Fase do programa | Materiais, Tarefas, Gravação |
| Material | Encontro + Fase | Tags de empresa, Tipo de conteúdo |
| Tarefa | Encontro | Participante (atribuição) |
| Champion | Empresa | Soluções, Tarefas, Nível |
| Projeto | Empresa | Champion (responsável), Comentários |
| Empresa | Grupo Colloni | Champions, Projetos, Tags |

### 6.3 Modelo de Permissões

| Ação | Gestor | TI | Champion | Admin |
|------|--------|-----|----------|-------|
| Ver Dashboard | Sim | Sim | Sim | Sim |
| Ver Biblioteca | Sim | Sim | Sim | Sim |
| Download de templates | Sim | Sim | Sim | Sim |
| Favoritar materiais | Sim | Sim | Sim | Sim |
| Comentar conteúdo | Não | Sim | Sim | Sim |
| Responder mini tarefas | Não | Não | Sim | Sim |
| Atualizar seus projetos | Não | Não | Sim | Sim |
| Ver Mapa de Champions | Sim | Sim | Sim | Sim |
| Ver Painel Admin | Não | Não | Não | Sim |
| Upload de materiais | Não | Não | Não | Sim |
| Criar/atribuir tarefas | Não | Não | Não | Sim |
| Gerenciar champions | Não | Não | Não | Sim |
| Gerenciar projetos (kanban) | Não | Não | Não | Sim |
| Ver relatórios de engajamento | Não | Não | Não | Sim |

**Nota:** Gestores e TI podem ser promovidos a champions se identificados pelo programa. A mudança de papel é feita pelo admin.

---

## 7. Métricas de Sucesso

### 7.1 Métricas de Engajamento

| Métrica | Meta | Frequência de medição |
|---------|------|-----------------------|
| Taxa de acesso semanal ao portal | >60% dos participantes | Semanal |
| Tempo médio por sessão | >5 minutos | Mensal |
| Materiais visualizados por usuário/mês | >3 | Mensal |
| Templates baixados por mês | >5 (total) | Mensal |

### 7.2 Métricas de Produtividade

| Métrica | Meta | Frequência de medição |
|---------|------|-----------------------|
| Mini tarefas concluídas por ciclo | >70% do total atribuído | A cada encontro |
| Tarefas entregues no prazo | >80% | A cada encontro |
| Projetos movendo no kanban | ≥2 novos por mês | Mensal |
| Projetos implementados no trimestre | ≥3 | Trimestral |

### 7.3 Métricas de Evolução

| Métrica | Meta | Frequência de medição |
|---------|------|-----------------------|
| Champions ativos | ≥1 por empresa participante | Mensal |
| Champions nível "Referência" | ≥3 em 6 meses | Semestral |
| Soluções registradas por champions | ≥10 em 6 meses | Semestral |
| NPS do programa | >8 | Trimestral |

### 7.4 Métricas do Portal

| Métrica | Meta | Frequência de medição |
|---------|------|-----------------------|
| Tempo até encontrar conteúdo | <30 segundos | Teste de usabilidade |
| Satisfação com o portal (survey) | >4/5 | Trimestral |
| Taxa de retorno espontâneo | >40% dos acessos sem notificação | Mensal |
| Bugs reportados por mês | <2 | Mensal |

---

## 8. Fases de Implementação

### Fase 1 — MVP (Lançamento do programa)

**Escopo mínimo para o dia 1:**
- Login com autenticação
- Dashboard com próximo encontro e tarefas
- Biblioteca (upload e visualização de materiais)
- Mini Tarefas (criação, atribuição e resposta)
- Agenda (calendário de encontros)
- Painel Admin básico (upload, tarefas, agenda)

**Justificativa:** Estas funcionalidades cobrem o ciclo básico do programa: agendar → encontrar → publicar → atribuir tarefas → acompanhar.

### Fase 2 — Evolução (Após 1-2 meses de uso)

**Funcionalidades adicionais:**
- Mapa de Champions completo
- Projetos e Kanban
- Favoritos e busca avançada na Biblioteca
- Relatórios de engajamento
- Notificações por e-mail

**Justificativa:** Champions e projetos ganham corpo conforme o programa avança. Não são necessários no dia 1.

### Fase 3 — Maturidade (Após 3-4 meses de uso)

**Funcionalidades avançadas:**
- Dashboard personalizado por persona
- Indicadores de resultado pós-implementação nos projetos
- Contato e rede entre champions
- Exportação de relatórios em PDF
- Integrações (Google Calendar, notificações mobile)

**Justificativa:** Refinamentos baseados no feedback real dos usuários.

---

## 9. Considerações Finais

O Portal Colloni não é apenas uma ferramenta de gestão de conteúdo — é o **ativo digital** do programa de IA do grupo. Cada gravação, template, tarefa e projeto registrado no portal aumenta o valor acumulado do programa e facilita a escalabilidade.

O design prioriza **simplicidade para gestores** (que querem visão rápida) e **profundidade para champions** (que querem recursos para aplicar). A identidade visual do Grupo Colloni está presente de forma elegante, reforçando que este é um espaço exclusivo do grupo — não uma ferramenta genérica.

O sucesso do portal será medido não apenas por métricas de acesso, mas pela **evolução tangível** do grupo no uso de IA: projetos implementados, champions formados e processos melhorados.

---

*Documento produzido por Cognix360 — Consultoria em IA e Automação para Negócios*
*www.cognix360.com — Março de 2026*
