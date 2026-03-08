---
tags: [API, Backend, Módulo 07]
---

# 🌐 Aula 06 - Persistência e Camada de Dados

!!! tip "Objetivo"
    **Objetivo:** Explorar a fundo os conceitos de Persistência e Dados, abordando Relacional, NoSQL, ACID e Eventual Consistency. Construiremos uma base teórica e prática com diagramas, comandos interativos e matemática aplicada à ciência da computação.

---

## 1. Visão Geral Teórica 🧠

O estudo de **Relacional** e **NoSQL** é fundamental para sistemas de alta disponibilidade.

!!! info "Definição Técnica"
    Aplicações cloud-native exigem tolerância a falhas. Segundo o Teorema CAP, não podemos ter Consistência, Disponibilidade e Partição simultaneamente em sistemas distribuídos.

Quando lidamos com *Persistência e Dados*, a performance pode ser modelada através da Lei de Amdahl:
$$ S_{latency}(s) = \frac{1}{(1 - p) + \frac{p}{s}} $$
Onde $p$ é a porção paralelizável.

---

## 2. Arquitetura e Modelagem 📊

Abaixo, a representação de como Relacional é adotado em escala industrial.

```mermaid
graph TD
    Client[Cliente API] -->|Requisita| GW[API Gateway]
    GW --> S1[Relacional]
    GW --> S2[NoSQL]
    S1 -.->|Consistência| DB1[(Banco Y)]
    S2 -.->|Mensageria| B[Broker Kafka]
```

### 2.1 Comparativo de Tecnologias

=== "Abordagem A"
    Focada em **ACID**. Maior curva de aprendizado, porém mais controle sobre o I/O.
=== "Abordagem B"
    Focada em **Eventual Consistency**. Mais rápida para o mercado (Time-to-Market).

---

## 3. Prática: Hands-on em `ACID` 💻

Vamos subir nosso ambiente local para explorar as particularidades tecnológicas de `Persistência e Dados`.

```termynal
$ docker network create backend_net
$ docker run -d --name acid_svc -p 8080:8080 my-backend-image
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

    [:octicons-arrow-right-24: Slide 06](../slides/slide-06.html)

- :material-help-circle: **Quiz**

    ---

    Teste seu conhecimento com 10 questões interativas.

    [:octicons-arrow-right-24: Quiz 06](../quizzes/quiz-06.md)

- :fontawesome-solid-pencil: **Exercícios**

    ---

    5 exercícios progressivos (básico → desafio).

    [:octicons-arrow-right-24: Exercício 06](../exercicios/exercicio-06.md)

- :material-briefcase-outline: **Projeto**

    ---

    Aplicação prática dos conceitos da aula.

    [:octicons-arrow-right-24: Projeto 06](../projetos/projeto-06.md)

</div>

---

[➡️ Próxima Aula: Cache e Performance](./aula-07.md){ .md-button .md-button--primary }