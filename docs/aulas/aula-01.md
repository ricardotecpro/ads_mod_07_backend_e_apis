# Aula 01 - Fundamentos da Web e Sistemas Distribuídos 🌐

!!! tip "Objetivo"
    **Objetivo:** Explorar a fundo os conceitos de Fundamentos da Web, abordando Arquitetura cliente-servidor, Sistemas distribuídos, HTTP/2 e Monólito e Microsserviços. Construiremos uma base teórica e prática com diagramas, comandos interativos e matemática aplicada à ciência da computação.

---

## 1. Visão Geral Teórica 🧠

O estudo de **Arquitetura cliente-servidor** e **Sistemas distribuídos** é fundamental para sistemas de alta disponibilidade.

!!! info "Definição Técnica"
    Aplicações cloud-native exigem tolerância a falhas. Segundo o Teorema CAP, não podemos ter Consistência, Disponibilidade e Partição simultaneamente em sistemas distribuídos.

Quando lidamos com *Fundamentos da Web*, a performance pode ser modelada através da Lei de Amdahl:
$$ S_{latency}(s) = \frac{1}{(1 - p) + \frac{p}{s}} $$
Onde $p$ é a porção paralelizável.

---

## 2. Arquitetura e Modelagem 📊

Abaixo, a representação de como Arquitetura cliente-servidor é adotado em escala industrial.

```mermaid
graph TD
    Client[Cliente API] -->|Requisita| GW[API Gateway]
    GW --> S1[Arquitetura cliente-servidor]
    GW --> S2[Sistemas distribuídos]
    S1 -.->|Consistência| DB1[(Banco Y)]
    S2 -.->|Mensageria| B[Broker Kafka]
```

### 2.1 Comparativo de Tecnologias

=== "Abordagem A"
    Focada em **HTTP/2**. Maior curva de aprendizado, porém mais controle sobre o I/O.
=== "Abordagem B"
    Focada em **Monólito e Microsserviços**. Mais rápida para o mercado (Time-to-Market).

---

## 3. Prática: Hands-on em `HTTP/2` 💻

Vamos subir nosso ambiente local para explorar as particularidades tecnológicas de `Fundamentos da Web`.

```termynal
$ docker network create backend_net
$ docker run -d --name http/2_svc -p 8080:8080 my-backend-image
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

    [:octicons-arrow-right-24: Slide 01](../slides/slide-01.html)

- :material-help-circle: **Quiz**

    ---

    Teste seu conhecimento com 10 questões interativas.

    [:octicons-arrow-right-24: Quiz 01](../quizzes/quiz-01.md)

- :fontawesome-solid-pencil: **Exercícios**

    ---

    5 exercícios progressivos (básico → desafio).

    [:octicons-arrow-right-24: Exercício 01](../exercicios/exercicio-01.md)

- :material-briefcase-outline: **Projeto**

    ---

    Aplicação prática dos conceitos da aula.

    [:octicons-arrow-right-24: Projeto 01](../projetos/projeto-01.md)

</div>

---

[➡️ Próxima Aula: Arquitetura Backend](./aula-02.md){ .md-button .md-button--primary }