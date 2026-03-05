# � Curso: Engenharia de Backends e APIs Modernas

## Objetivo

Capacitar o aluno a **projetar, implementar, escalar e operar sistemas backend modernos**, incluindo APIs, arquiteturas distribuídas, observabilidade, segurança e infraestrutura cloud-native.

---

# Módulo 1 — Fundamentos da Web e Sistemas Distribuídos

### Conceitos fundamentais
* Arquitetura cliente-servidor
* Sistemas distribuídos
* Escalabilidade
* Latência
* Consistência de dados
* Alta disponibilidade
* Tolerância a falhas

### Protocolos Web
* HTTP
* HTTPS
* HTTP/2
* HTTP/3
* DNS
* TLS

### Modelo de comunicação
* Request / Response
* Streaming
* Push
* Long polling

### Padrões arquiteturais
* Monólitos
* Monólitos modulares
* Microserviços
* Serverless

---

# Módulo 2 — Arquitetura de Software Backend

### Arquiteturas modernas
* Clean Architecture
* Hexagonal Architecture (Ports & Adapters)
* Onion Architecture
* Layered Architecture

### Design orientado ao domínio
* Domain Driven Design (DDD)
* Bounded Contexts
* Aggregates
* Entities e Value Objects

### Padrões arquiteturais
* CQRS
* Event Sourcing
* Saga Pattern
* Backend for Frontend (BFF)

---

# Módulo 3 — Design de APIs

### Princípios de design
* API First
* Resource modeling
* URI design
* Naming conventions
* Versionamento de APIs
* Evolução de APIs

### REST
* REST constraints
* REST maturity model
* HATEOAS
* Idempotência
* Statelessness

### GraphQL
* Queries
* Mutations
* Subscriptions
* Schema design

Ferramenta padrão:
* GraphQL

---

# Módulo 4 — Protocolos de APIs e Comunicação

### Modelos de comunicação
* REST
* GraphQL
* RPC
* Streaming APIs

### Protocolos modernos
* gRPC
* WebSockets
* Server-Sent Events

Tecnologia:
* gRPC

---

# Módulo 5 — Autenticação, Autorização e Segurança

### Autenticação
* JWT
* OAuth 2.0
* OpenID Connect
* API Keys

Tecnologias:
* OAuth 2.0
* OpenID Connect

### Segurança de APIs
* CORS
* CSRF
* XSS
* Rate limiting
* API throttling

### OWASP API Security

Organização:
* OWASP

Principais riscos:
* Broken authentication
* Excessive data exposure
* Security misconfiguration

---

# Módulo 6 — Persistência e Camada de Dados

### Modelos de banco de dados
* Relacional
* NoSQL
* Key-value
* Document
* Column
* Graph

### Estratégias de acesso a dados
* ORM
* Query builders
* Repositórios

### Transações e consistência
* ACID
* BASE
* Eventual consistency

---

# Módulo 7 — Cache e Performance

### Estratégias de cache
* Cache aside
* Write-through
* Write-back
* CDN caching

Ferramenta principal:
* Redis

### Otimização de APIs
* Pagination
* Filtering
* Sorting
* Compression
* Response caching

---

# Módulo 8 — Mensageria e Arquitetura Orientada a Eventos

### Comunicação assíncrona
* Message queues
* Pub/Sub
* Event streaming

### Arquitetura Event Driven
* Event producers
* Event consumers
* Event brokers

Ferramentas:
* Apache Kafka
* RabbitMQ

---

# Módulo 9 — Infraestrutura Cloud Native

### Containers
* Containers
* Images
* Registries

Tecnologia:
* Docker

### Orquestração
* Clusters
* Service discovery
* Autoscaling

Tecnologia:
* Kubernetes

---

# Módulo 10 — Observabilidade e Monitoramento

### Observabilidade
* Logs estruturados
* Métricas
* Tracing distribuído

Tecnologias:
* Prometheus
* Grafana
* OpenTelemetry
* Jaeger

### Health checks
* Liveness probes
* Readiness probes

---

# Módulo 11 — Testes de Backend

### Tipos de testes
* Unit tests
* Integration tests
* Contract tests
* End-to-end tests

Ferramentas:
* Postman
* Pact

### Testes de performance
* Load testing
* Stress testing
* Spike testing

Ferramentas:
* k6
* Apache JMeter
* Gatling

---

# Módulo 12 — Deploy e DevOps

### CI/CD
* Continuous Integration
* Continuous Delivery
* Continuous Deployment

### Estratégias de deploy
* Blue/Green
* Canary
* Rolling updates

### Feature flags

Ferramenta:
* LaunchDarkly

---

# Módulo 13 — Serverless e Edge Computing

### Serverless
* Functions as a Service
* Event-driven functions

Plataformas:
* AWS Lambda
* Vercel

### Edge computing
* Edge APIs
* Edge functions

Plataforma:
* Cloudflare Workers

---

# Módulo 14 — API Management e Gateways

### API Gateways
* Authentication
* Rate limiting
* Routing
* Load balancing

Ferramentas comuns:
* Kong
* Nginx
* Apigee

---

# Módulo 15 — Ecossistemas de Backend (visão geral)

⚠️ Apenas **comparação de ecossistemas**, não aprofundamento.

---

## JavaScript / TypeScript
* Node.js
* Express
* NestJS

---

## Python
* Django
* FastAPI
* Flask

---

## JVM
* Java / Spring
* Quarkus
* Kotlin / Ktor

---

## .NET
* C# / ASP.NET

---

## Systems / Performance
* Go
* Rust
* C++

---

# Módulo 16 — Tópicos Avançados e Tendências

### Microservices avançados
* Service mesh

Tecnologias:
* Istio
* Linkerd

### APIs modernas
* Webhooks
* Streaming APIs

### Backend para IA
* AI APIs
* Vector databases
* RAG APIs

Ferramentas:
* LangChain
* Pinecone