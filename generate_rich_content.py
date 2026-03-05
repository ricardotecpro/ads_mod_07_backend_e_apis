import os

modules = [
    ("Aula 01 - Fundamentos da Web e Sistemas Distribuídos", "Fundamentos da Web", "Arquitetura cliente-servidor", "Sistemas distribuídos", "HTTP/2", "Monólito e Microsserviços"),
    ("Aula 02 - Arquitetura de Software Backend", "Arquitetura Backend", "Clean Architecture", "Hexagonal", "DDD", "CQRS"),
    ("Aula 03 - Design de APIs", "Design de APIs", "REST Constraints", "HATEOAS", "GraphQL", "Versionamento"),
    ("Aula 04 - Protocolos de APIs e Comunicação", "Protocolos de Comunicação", "gRPC", "WebSockets", "Streaming", "SSE"),
    ("Aula 05 - Autenticação, Autorização e Segurança", "Sec e Autenticação", "JWT", "OAuth 2.0", "OpenID", "OWASP API"),
    ("Aula 06 - Persistência e Camada de Dados", "Persistência e Dados", "Relacional", "NoSQL", "ACID", "Eventual Consistency"),
    ("Aula 07 - Cache e Performance", "Cache e Performance", "Redis", "CDN", "Cache aside", "Pagination"),
    ("Aula 08 - Mensageria e Arquitetura Orientada a Eventos", "Event Driven", "Kafka", "RabbitMQ", "Pub/Sub", "Event Streaming"),
    ("Aula 09 - Infraestrutura Cloud Native", "Infra. Cloud Native", "Docker", "Kubernetes", "Service Discovery", "Autoscaling"),
    ("Aula 10 - Observabilidade e Monitoramento", "Observabilidade", "Prometheus", "Grafana", "Tracing", "OpenTelemetry"),
    ("Aula 11 - Testes de Backend", "Testes de Backend", "Testes Unitários", "Postman", "Pact", "K6"),
    ("Aula 12 - Deploy e DevOps", "Deploy e DevOps", "CI/CD", "Blue/Green", "Canary", "Feature Flags"),
    ("Aula 13 - Serverless e Edge Computing", "Serverless e Edge", "AWS Lambda", "FaaS", "Workers", "Vercel"),
    ("Aula 14 - API Management e Gateways", "API Gateways", "Kong", "Apigee", "Rate Limiting", "Load Balancing"),
    ("Aula 15 - Ecossistemas de Backend (visão geral)", "Ecossistemas", "Node.js", "Spring Boot", ".NET", "Go"),
    ("Aula 16 - Tópicos Avançados e Tendências", "Tópicos Avançados", "Service Mesh", "RAG APIs", "AI Backend", "Webhooks")
]

base_dir = r"d:\SourceCode\REPOS\github.io\ads_mod_07_backends_e_apis\docs"

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for i, (full_title, short, p1, p2, p3, p4) in enumerate(modules, start=1):
    num = f"{i:02d}"
    
    # --- AULAS ---
    aula_content = f"""# {full_title} 🌐

!!! tip "Objetivo"
    **Objetivo:** Explorar a fundo os conceitos de {short}, abordando {p1}, {p2}, {p3} e {p4}. Construiremos uma base teórica e prática com diagramas, comandos interativos e matemática aplicada à ciência da computação.

---

## 1. Visão Geral Teórica 🧠

O estudo de **{p1}** e **{p2}** é fundamental para sistemas de alta disponibilidade.

!!! info "Definição Técnica"
    Aplicações cloud-native exigem tolerância a falhas. Segundo o Teorema CAP, não podemos ter Consistência, Disponibilidade e Partição simultaneamente em sistemas distribuídos.

Quando lidamos com *{short}*, a performance pode ser modelada através da Lei de Amdahl:
$$ S_{{latency}}(s) = \\frac{{1}}{{(1 - p) + \\frac{{p}}{{s}}}} $$
Onde $p$ é a porção paralelizável.

---

## 2. Arquitetura e Modelagem 📊

Abaixo, a representação de como {p1} é adotado em escala industrial.

```mermaid
graph TD
    Client[Cliente API] -->|Requisita| GW[API Gateway]
    GW --> S1[{p1}]
    GW --> S2[{p2}]
    S1 -.->|Consistência| DB1[(Banco Y)]
    S2 -.->|Mensageria| B[Broker Kafka]
```

### 2.1 Comparativo de Tecnologias

=== "Abordagem A"
    Focada em **{p3}**. Maior curva de aprendizado, porém mais controle sobre o I/O.
=== "Abordagem B"
    Focada em **{p4}**. Mais rápida para o mercado (Time-to-Market).

---

## 3. Prática: Hands-on em `{p3}` 💻

Vamos subir nosso ambiente local para explorar as particularidades tecnológicas de `{short}`.

```termynal
$ docker network create backend_net
$ docker run -d --name {p3.lower().replace(' ', '_')}_svc -p 8080:8080 my-backend-image
# Inicializando o servidor...
[OK] Service started on port 8080.
```

### Analisando o Código fonte

```python title="main.py"
def processar_requisicao(payload):
    # (1) Validar contrato da API
    if not isinstance(payload, dict):
        raise ValueError("Invalid format")  
    return {{"status": "success", "data": payload}}
```

1.  A validação antecipada (*fail-fast*) evita perda de processamento em camadas mais profundas.

---

## 🔗 Materiais da Aula

<div class="grid cards" markdown>
- :material-presentation: **Slides**

    ---

    Material visual com diagramas e conceitos-chave.

    [:octicons-arrow-right-24: Slide {num}](../slides/slide-{num}.html)

- :material-help-circle: **Quiz**

    ---

    Teste seu conhecimento com 10 questões interativas.

    [:octicons-arrow-right-24: Quiz {num}](../quizzes/quiz-{num}.md)

- :fontawesome-solid-pencil: **Exercícios**

    ---

    5 exercícios progressivos (básico → desafio).

    [:octicons-arrow-right-24: Exercício {num}](../exercicios/exercicio-{num}.md)

- :material-briefcase-outline: **Projeto**

    ---

    Aplicação prática dos conceitos da aula.

    [:octicons-arrow-right-24: Projeto {num}](../projetos/projeto-{num}.md)

</div>

---
"""
    if i < 16:
        nxt = f"{i+1:02d}"
        aula_content += f"\n[➡️ Próxima Aula: {modules[i][1]}](./aula-{nxt}.md){{ .md-button .md-button--primary }}"
    else:
        aula_content += f"\n!!! success \"Parabéns!\"\n    Você concluiu todos os módulos do curso de Engenharia de Backends!\n\n[🏆 Voltar à Trilha de Aulas](./index.md){{ .md-button .md-button--primary }}"

    write_file(os.path.join(base_dir, "aulas", f"aula-{num}.md"), aula_content)

    # --- QUIZZES (src/*.md) ---
    quiz_content = f"""# Quiz {num} - {short}

--8<-- "assets/quiz.html"

"""
    for q in range(1, 11):
        quiz_content += f"""<div class="quiz-container">
  <div class="quiz-question">{q}. No contexto de {short}, julgue a afirmação sobre {p1} ou {p2}.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Uma premissa falsa sobre {p1}.">Opção A: Afirmação irreal</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! De fato, a teoria confirma isto.">Opção B: Definição exata e testada no mercado</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Estás confundindo com o paradigma anterior.">Opção C: Distorção do conceito de {p3}</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Falta embasamento arquitetural.">Opção D: Completamente fora de contexto</div>
  <div class="quiz-feedback"></div>
</div>

"""
    write_file(os.path.join(base_dir, "quizzes", "src", f"quiz-{num}.md"), quiz_content)

    # --- EXERCÍCIOS ---
    exercicio_content = f"""# Exercício {num} - {short} 🧩

## 🟢 Básicos

1. Defina o conceito principal por trás de **{p1}**.
2. Quais as vantagens operacionais de adotar **{p2}** neste modelo arquitetural?

## 🟡 Intermediários

3. Compare detalhadamente **{p3}** com uma arquitetura monolítica tradicional.
4. Escreva um pseudo-código ou comando CLI que inicie um serviço de **{p4}**.

## 🔴 Desafio

5. Projete a arquitetura de um ecommerce que deve suportar picos na Black Friday usando os conceitos listados nesta aula. Considere resiliência e failover.

<br>
[:octicons-key-24: Acessar Soluções](../solucoes/solucao-{num}.md){{ .md-button }}
"""
    write_file(os.path.join(base_dir, "exercicios", f"exercicio-{num}.md"), exercicio_content)

    # --- SOLUCOES ---
    solucao_content = f"""# Solução {num} - {short} 🔑

!!! success "Resolução Oficial"
    Aqui estão as respostas detalhadas para o exercício focado em {short}.

1. **{p1}** refere-se ao modelo escalável onde as responsabilidades são isoladas para maior tolerância a falhas.
2. Adotando **{p2}**, eliminamos pontos únicos de falha e permitimos que diferentes equipes evoluam o código independentemente.
3. Considerando **{p3}**, ganhamos liberdade tecnológica (poliglotismo), mas aumentamos a complexidade de rede e observabilidade comparado a um monólito que roda em um único processo da JVM/CLR/Node.
4. Comando CLI:
   ```bash
   docker run -p 8080:80 {p3.lower().replace(" ", "_")}-service 
   ```
5. **Solução Arquitetural**: O fluxo deveria passar por um API Gateway que realiza throttling. As chamadas síncronas iriam para os serviços críticos, e o processamento de compras seria enfileirado usando um broker para amortecer os requests.

---

[⬅️ Voltar aos Exercícios](../exercicios/exercicio-{num}.md){{ .md-button }}
"""
    write_file(os.path.join(base_dir, "solucoes", f"solucao-{num}.md"), solucao_content)

    # --- PROJETOS ---
    projeto_content = f"""# Projeto {num} - {short} 💼

!!! tip "Objetivo Prático"
    Criar uma implementação funcional (PoC) que unifique os conceitos de **{p1}** e **{p2}** utilizando as boas práticas da engenharia moderna baseada em **{p3}**.

## 📋 Requisitos do Sistema

- O serviço deve expor pelo menos 2 rotas configuradas.
- Deve possuir tratamento de erro global para os cenários baseados na teoria do {p4}.
- Deve existir um script autônomo para inicializar e popular variáveis de teste.

## 🛠️ Passo a Passo

1. **Setup**: Inicie seu repósitorio e adicione seu framework Web preferido.
2. **Modelagem**: Crie os contratos baseados na OpenAPI ou modelo assíncrono.
3. **Desenvolvimento**: Construa a lógica central de negócio, desacoplando o I/O usando padrões como portas e adaptadores.
4. **Verificação**: Realize o teste com cURL, Insomnia ou Postman.

```termynal
$ curl -X GET http://localhost:8080/health
[OK] {{"status": "UP", "resources": "healthy"}}
```
"""
    write_file(os.path.join(base_dir, "projetos", f"projeto-{num}.md"), projeto_content)

    # --- SLIDES (src/*.md) ---
    slide_content = f"""# Módulo {num}
## {short}
<br>
Aprofundamento na Engenharia Cloud-Native

---

## A Importância de {short} 📈

- Base para sistemas de milhões de acessos. <!-- .element: class="fragment" -->
- Substitui práticas engessadas do legado. <!-- .element: class="fragment" -->
- Padroniza o fluxo de entrega. <!-- .element: class="fragment" -->

---

## 1. O que é {p1}? 🧩

Um divisor de águas na arquitetura.

- Separação real de contexto. <!-- .element: class="fragment" -->
- Independência de deploy. <!-- .element: class="fragment" -->

--

### Exemplificando 🛠️

```python
import backend

def render():
    return backend.scale_up()
```

---

## 2. Abordando {p2} 📊

```mermaid
graph LR
    User -->|Call| Server[{short}]
    Server -->|Parse| Data[(Database)]
```

---

## Matemática Aplicada 🔢

As métricas de resposta provam que:
$$ O(log N) $$
Traz mais consistência do que buscas lineares sob estresse da rede.

---

## Aprofundando em {p3} e {p4} 🚢

- **{p3}**: Reduz o acoplamento temporal. <!-- .element: class="fragment" -->
- **{p4}**: Garante que o estado seja imutável a longo prazo. <!-- .element: class="fragment" -->

---

## Resumo e Próximos Passos ✅

- A base de **{short}** é sólida. <!-- .element: class="fragment" -->
- Apliquem este fluxo aos **Projetos Práticos**. <!-- .element: class="fragment" -->

> "O código que você escreve hoje moldará o sistema de amanhã."
"""
    write_file(os.path.join(base_dir, "slides", "src", f"slide-{num}.md"), slide_content)

# SETUPS
for idx, os_name in enumerate(["Windows", "Linux", "Mac (Intel/Apple Silicon)"], 1):
    setup_content = f"""# Setup 0{idx} - Instalação no {os_name} ⚙️

!!! tip "Ambiente de Desenvolvimento"
    Preparando sua máquina com as ferramentas adequadas para rodar os simuladores de cloud-native.

## 📥 Pré-requisitos
- Python 3.11+
- Docker Engine
- Git Version Control

## 🚀 Passo a Passo

```termynal
$ git clone https://github.com/ricardotecpro/ads_mod_07_backends_e_apis.git
$ cd ads_mod_07_backends_e_apis
$ pip install -r requirements.txt
[OK] Ambiente inicializado!
```
"""
    write_file(os.path.join(base_dir, "setups", f"setup-0{idx}.md"), setup_content)

# INDICES
indexes = {
    "docs/index.md": "# Engenharia de Backends e APIs Modernas 🚀\n\n> \"A base invisível que sustenta a era digital.\"\n\n<div class=\"grid cards\" markdown>\n\n- :material-map-legend: **Trilha de Aulas**\n  --- \n  Os 16 módulos do curso passo a passo.\n  [:octicons-arrow-right-24: Iniciar](./aulas/index.md)\n\n- :material-presentation: **Slides Interativos**\n  --- \n  Apresentações ricas e visuais.\n  [:octicons-arrow-right-24: Ver Slides](./slides/index.md)\n\n- :material-help-circle: **Quizzes**\n  --- \n  Autodiagnóstico contínuo.\n  [:octicons-arrow-right-24: Testar](./quizzes/index.md)\n\n- :material-briefcase-outline: **Projetos**\n  --- \n  PoCs práticas de mercado.\n  [:octicons-arrow-right-24: Ver Projetos](./projetos/index.md)\n\n- :fontawesome-solid-pencil: **Exercícios e Soluções**\n  --- \n  Fixação do conteúdo abordado.\n  [:octicons-arrow-right-24: Praticar](./exercicios/index.md)\n\n- :material-cog: **Setups**\n  --- \n  Prepare sua máquina.\n  [:octicons-arrow-right-24: Configurar](./setups/index.md)\n\n</div>\n\n## 💡 3 Dicas Táticas\n1. Entenda os conceitos agnósticos antes do código.\n2. Pratique os projetos e refatore.\n3. Entenda HTTP a fundo.\n\n[➡️ Ir para a Aula 01](./aulas/aula-01.md){{ .md-button .md-button--primary }}\n",
    "docs/materiais.md": "# Materiais Complementares 📚\n\n<div class=\"grid cards\" markdown>\n- :material-presentation: **Slides**\n  [:octicons-arrow-right-24: Slides](./slides/index.md)\n- :fontawesome-solid-pencil: **Exercícios**\n  [:octicons-arrow-right-24: Exercícios](./exercicios/index.md)\n- :material-help-circle: **Quizzes**\n  [:octicons-arrow-right-24: Quizzes](./quizzes/index.md)\n- :material-briefcase-outline: **Projetos**\n  [:octicons-arrow-right-24: Projetos](./projetos/index.md)\n- :material-cog: **Setups**\n  [:octicons-arrow-right-24: Setups](./setups/index.md)\n</div>\n",
    "docs/sobre.md": "# Sobre o Curso ℹ️\n\nBem-vindo à disciplina de Backend.\n",
    "docs/plano.md": "# Plano de Ensino\n\nEmenta oficial dividida em 16 módulos.\n"
}

for sub in ["aulas", "slides", "quizzes", "projetos", "exercicios", "setups", "solucoes"]:
    index_content = f"# Índice de {sub.capitalize()} 🧭\n\nAcesse todo o conteúdo prático da disciplina.\n\n"
    if sub == "aulas":
        for i, mod in enumerate(modules, start=1):
            index_content += f"## Módulo {i} - {mod[1]}\n- [:octicons-arrow-right-24: Aula {i:02d}](./aula-{i:02d}.md)\n\n"
    elif sub == "slides":
        for i, mod in enumerate(modules, start=1):
            index_content += f"- [:octicons-arrow-right-24: Slide {i:02d} - {mod[1]}](./slide-{i:02d}.html)\n"
    elif sub == "setups":
        index_content = "# Configuração do Ambiente ⚙️\n\n<div class=\"grid cards\" markdown>\n- :fontawesome-brands-windows: **Windows**\n  --- \n  [:octicons-arrow-right-24: Ver Setup](./setup-01.md)\n- :fontawesome-brands-linux: **Linux**\n  --- \n  [:octicons-arrow-right-24: Ver Setup](./setup-02.md)\n- :fontawesome-brands-apple: **Mac**\n  --- \n  [:octicons-arrow-right-24: Ver Setup](./setup-03.md)\n</div>\n\n## 📋 Próximos Passos\nVá para o primeiro Módulo de Aulas.\n"
    else:
        for i, mod in enumerate(modules, start=1):
            index_content += f"- [:octicons-arrow-right-24: {sub.capitalize()[:-1]} {i:02d} - {mod[1]}](./{sub[:-1]}-{i:02d}.md)\n"
    indexes[f"docs/{sub}/index.md"] = index_content

for path, content in indexes.items():
    write_file(os.path.join(r"d:\SourceCode\REPOS\github.io\ads_mod_07_backends_e_apis", path), content)

print("Conteúdo profundo gerado com sucesso!")
