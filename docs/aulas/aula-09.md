---
tags: [API, Backend, Módulo 07]
---

# 🌐 Aula 09 - Infraestrutura Cloud Native

!!! tip "Objetivo"
    **Objetivo:** Explorar a fundo os conceitos de Infra. Cloud Native, abordando Docker, Kubernetes, Service Discovery e Autoscaling. Construiremos uma base teórica e prática com diagramas, comandos interativos e matemática aplicada à ciência da computação.

---

## 1. Visão Geral Teórica 🧠

O estudo de **Docker** e **Kubernetes** é fundamental para sistemas de alta disponibilidade.

!!! info "Definição Técnica"
    Aplicações cloud-native exigem tolerância a falhas. Segundo o Teorema CAP, não podemos ter Consistência, Disponibilidade e Partição simultaneamente em sistemas distribuídos.

Quando lidamos com *Infra. Cloud Native*, a performance pode ser modelada através da Lei de Amdahl:
$$ S_{latency}(s) = \frac{1}{(1 - p) + \frac{p}{s}} $$
Onde $p$ é a porção paralelizável.

---

## 2. Arquitetura e Modelagem 📊

Abaixo, a representação de como Docker é adotado em escala industrial.

```mermaid
graph TD
    Client[Cliente API] -->|Requisita| GW[API Gateway]
    GW --> S1[Docker]
    GW --> S2[Kubernetes]
    S1 -.->|Consistência| DB1[(Banco Y)]
    S2 -.->|Mensageria| B[Broker Kafka]
```

### 2.1 Comparativo de Tecnologias

=== "Abordagem A"
    Focada em **Service Discovery**. Maior curva de aprendizado, porém mais controle sobre o I/O.
=== "Abordagem B"
    Focada em **Autoscaling**. Mais rápida para o mercado (Time-to-Market).

---

## 3. Prática: Hands-on em `Service Discovery` 💻

Vamos subir nosso ambiente local para explorar as particularidades tecnológicas de `Infra. Cloud Native`.

```termynal
$ docker network create backend_net
$ docker run -d --name service_discovery_svc -p 8080:8080 my-backend-image
# Inicializando o servidor...
[OK] Service started on port 8080.
```

### Analisando o Código fonte

```python title="main.py"
def processar_requisicao(payload):
    # (1) Validar contrato da API
    if not isinstance(payload, dict):
        raise ValueError("Invalid format")  
    return {"status": "success", "data": payload}
```

1.  A validação antecipada (*fail-fast*) evita perda de processamento em camadas mais profundas.

---

## 🔗 Materiais da Aula

<div class="grid cards" markdown>
- :material-presentation: **Slides**

    ---

    Material visual com diagramas e conceitos-chave.

    [:octicons-arrow-right-24: Slide 09](../slides/slide-09.html)

- :material-help-circle: **Quiz**

    ---

    Teste seu conhecimento com 10 questões interativas.

    [:octicons-arrow-right-24: Quiz 09](../quizzes/quiz-09.md)

- :fontawesome-solid-pencil: **Exercícios**

    ---

    5 exercícios progressivos (básico → desafio).

    [:octicons-arrow-right-24: Exercício 09](../exercicios/exercicio-09.md)

- :material-briefcase-outline: **Projeto**

    ---

    Aplicação prática dos conceitos da aula.

    [:octicons-arrow-right-24: Projeto 09](../projetos/projeto-09.md)

</div>

---

[➡️ Próxima Aula: Observabilidade](./aula-10.md){ .md-button .md-button--primary }