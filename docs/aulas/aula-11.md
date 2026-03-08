---
tags: [API, Backend, Módulo 07]
---

# 🌐 Aula 11 - Testes de Backend

!!! tip "Objetivo"
    **Objetivo:** Explorar a fundo os conceitos de Testes de Backend, abordando Testes Unitários, Postman, Pact e K6. Construiremos uma base teórica e prática com diagramas, comandos interativos e matemática aplicada à ciência da computação.

---

## 1. Visão Geral Teórica 🧠

O estudo de **Testes Unitários** e **Postman** é fundamental para sistemas de alta disponibilidade.

!!! info "Definição Técnica"
    Aplicações cloud-native exigem tolerância a falhas. Segundo o Teorema CAP, não podemos ter Consistência, Disponibilidade e Partição simultaneamente em sistemas distribuídos.

Quando lidamos com *Testes de Backend*, a performance pode ser modelada através da Lei de Amdahl:
$$ S_{latency}(s) = \frac{1}{(1 - p) + \frac{p}{s}} $$
Onde $p$ é a porção paralelizável.

---

## 2. Arquitetura e Modelagem 📊

Abaixo, a representação de como Testes Unitários é adotado em escala industrial.

```mermaid
graph TD
    Client[Cliente API] -->|Requisita| GW[API Gateway]
    GW --> S1[Testes Unitários]
    GW --> S2[Postman]
    S1 -.->|Consistência| DB1[(Banco Y)]
    S2 -.->|Mensageria| B[Broker Kafka]
```

### 2.1 Comparativo de Tecnologias

=== "Abordagem A"
    Focada em **Pact**. Maior curva de aprendizado, porém mais controle sobre o I/O.
=== "Abordagem B"
    Focada em **K6**. Mais rápida para o mercado (Time-to-Market).

---

## 3. Prática: Hands-on em `Pact` 💻

Vamos subir nosso ambiente local para explorar as particularidades tecnológicas de `Testes de Backend`.

```termynal
$ docker network create backend_net
$ docker run -d --name pact_svc -p 8080:8080 my-backend-image
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

    [:octicons-arrow-right-24: Slide 11](../slides/slide-11.html)

- :material-help-circle: **Quiz**

    ---

    Teste seu conhecimento com 10 questões interativas.

    [:octicons-arrow-right-24: Quiz 11](../quizzes/quiz-11.md)

- :fontawesome-solid-pencil: **Exercícios**

    ---

    5 exercícios progressivos (básico → desafio).

    [:octicons-arrow-right-24: Exercício 11](../exercicios/exercicio-11.md)

- :material-briefcase-outline: **Projeto**

    ---

    Aplicação prática dos conceitos da aula.

    [:octicons-arrow-right-24: Projeto 11](../projetos/projeto-11.md)

</div>

---

[➡️ Próxima Aula: Deploy e DevOps](./aula-12.md){ .md-button .md-button--primary }