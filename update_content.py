import os

modules = [
    ("Aula 01 - Fundamentos da Web e Sistemas Distribuídos", "Fundamentos da Web", "Arquitetura cliente-servidor, Sistemas distribuídos, Escalabilidade, Latência, Consistência de dados, Alta disponibilidade, Protocolos Web (HTTP, HTTPS, HTTP/2 e 3, DNS, TLS), Padrões Monólitos e Microsserviços."),
    ("Aula 02 - Arquitetura de Software Backend", "Arquitetura Backend", "Arquiteturas modernas (Clean, Hexagonal, Onion, Layered), Domain Driven Design (DDD), Padrões arquiteturais (CQRS, Event Sourcing, Saga, BFF)."),
    ("Aula 03 - Design de APIs", "Design de APIs", "Princípios de design (API First, URI design), REST (maturity model, HATEOAS, Idempotência), GraphQL (Queries, Mutations)."),
    ("Aula 04 - Protocolos de APIs e Comunicação", "Protocolos de Comunicação", "Modelos de comunicação (REST, GraphQL, RPC, Streaming), Protocolos modernos (gRPC, WebSockets, SSE)."),
    ("Aula 05 - Autenticação, Autorização e Segurança", "Segurança em APIs", "Autenticação (JWT, OAuth 2.0, OpenID Connect), Segurança (CORS, CSRF, XSS, Rate limiting), OWASP API Security."),
    ("Aula 06 - Persistência e Camada de Dados", "Persistência e Bancos de Dados", "Modelos de bancos (Relacional, NoSQL, Graph), Estratégias (ORM, Repositórios), Transações ACID e Eventual consistency."),
    ("Aula 07 - Cache e Performance", "Cache e Performance", "Estratégias de cache (Cache aside, Write-through, CDN), Ferramentas (Redis), Otimização de APIs (Pagination, Filtering, Compression)."),
    ("Aula 08 - Mensageria e Arquitetura Orientada a Eventos", "Arquitetura Event Driven", "Comunicação assíncrona (Message queues, Pub/Sub), Event Driven Architecture, Ferramentas (Kafka, RabbitMQ)."),
    ("Aula 09 - Infraestrutura Cloud Native", "Cloud Native", "Containers (Docker), Orquestração (Kubernetes, clusters, service discovery, autoscaling)."),
    ("Aula 10 - Observabilidade e Monitoramento", "Observabilidade", "Logs estruturados, Métricas, Tracing distribuído (Prometheus, Grafana, OpenTelemetry), Health checks."),
    ("Aula 11 - Testes de Backend", "Testes de Software Backend", "Tipos de testes (Unitários, Integração, Contrato, E2E), Ferramentas (Postman, Pact), Testes de Performance (k6, JMeter)."),
    ("Aula 12 - Deploy e DevOps", "Deploy e DevOps", "CI/CD, Estratégias de deploy (Blue/Green, Canary, Rolling updates), Feature flags."),
    ("Aula 13 - Serverless e Edge Computing", "Serverless e Edge", "Serverless (FaaS, AWS Lambda, Vercel), Edge computing (Cloudflare Workers)."),
    ("Aula 14 - API Management e Gateways", "API Gateways", "Authentication, Rate limiting, Routing, Load balancing, Ferramentas (Kong, Nginx, Apigee)."),
    ("Aula 15 - Ecossistemas de Backend (visão geral)", "Ecossistemas de Backend", "Ecossistemas Node.js, Python (Django/FastAPI), JVM (Spring/Quarkus), .NET, Go, Rust."),
    ("Aula 16 - Tópicos Avançados e Tendências", "Tópicos Avançados", "Service mesh (Istio), Webhooks, Streaming APIs, Backend para IA (RAG APIs, LangChain, Bancos vetoriais).")
]

base_dir = r"d:\SourceCode\REPOS\github.io\ads_mod_07_backends_e_apis\docs"

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for i, (full_title, short_title, ementa) in enumerate(modules, start=1):
    num = f"{i:02d}"
    
    # Aula
    aula_content = f"""# {full_title} 🌐

!!! tip "Objetivo"
    **Objetivo**: Compreender os conceitos de {short_title} abordando as principais estratégias e ferramentas mercado.

---

## Ementa do Módulo

{chr(10).join(['- ' + item.strip() for item in ementa.split(',')])}

---

## Introdução

Conteúdo detalhado da aula em desenvolvimento...

---

**Próxima Aula**: Avançaremos para os próximos tópicos do currículo! 🚀
"""
    write_file(os.path.join(base_dir, "aulas", f"aula-{num}.md"), aula_content)

    # Slide
    slide_content = f"""# {full_title} 🌐
## {short_title}

---

## Agenda de Hoje 📅

1. Introdução <!-- .element: class="fragment" -->
2. Conceitos base <!-- .element: class="fragment" -->
3. Ferramentas <!-- .element: class="fragment" -->
4. Casos práticos <!-- .element: class="fragment" -->

---

## Tópicos do Módulo

{chr(10).join(['- ' + item.strip() + ' <!-- .element: class="fragment" -->' for item in ementa.split(',')])}

---

## Introdução 🚀

Conteúdo em desenvolvimento...

---

## Próxima Aula 🚀

Continuaremos explorando Engenharia de Backends!

---

## Dúvidas? 🤔

> "A arquitetura de hoje é o legado de amanhã. Escolha com sabedoria."
"""
    write_file(os.path.join(base_dir, "slides", f"slide-{num}.md"), slide_content)

    # Quiz
    quiz_content = f"""# Quiz {num} - {short_title} 🌐

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Pergunta em desenvolvimento sobre {short_title}?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto.">Opção A</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto!">Opção B</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto.">Opção C</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto.">Opção D</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Pergunta em desenvolvimento sobre {short_title}?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto!">Opção A</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto.">Opção B</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto.">Opção C</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto.">Opção D</div>
  <div class="quiz-feedback"></div>
</div>
"""
    write_file(os.path.join(base_dir, "quizzes", f"quiz-{num}.md"), quiz_content)

    # Exercicio
    exercicio_content = f"""# Exercícios {num} - {short_title} 🧩

## 🟢 Fáceis

1.  **Definição**: Explique com suas palavras os principais conceitos de {short_title}.
2.  **Diferenciação**: Descreva casos de uso para as tecnologias mencionadas neste módulo.

## 🟡 Médios

3.  **Cenário**: Dado o ecossistema atual de backends, como você aplicaria {short_title} para resolver um problema de negócio? Justifique.
4.  **Prática**: Pesquise uma ferramenta de mercado relacionada ao tema e descreva suas vantagens.

## 🔴 Desafio

5.  **Análise e Design**:
    Projete uma arquitetura ou solução simples focada em {short_title} que demonstre seu entendimento profundo do módulo.
"""
    write_file(os.path.join(base_dir, "exercicios", f"exercicio-{num}.md"), exercicio_content)

    # Projeto
    projeto_content = f"""# Projeto {num} - {short_title} 🛠️

**Objetivo**: Validar os conhecimentos em {short_title} aplicados em um cenário prático.

## O Desafio
1. Desenvolva um artefato ou configuração baseada em {short_title}.
2. Utilize as ferramentas introduzidas na aula correspondente.
3. Teste e valide sua solução em ambiente local.

## O que entregar?
- Código-fonte ou documentação em um repositório GitHub.
- Evidências (prints) da solução rodando.
"""
    write_file(os.path.join(base_dir, "projetos", f"projeto-{num}.md"), projeto_content)

print("Conteúdo gerado com sucesso!")
