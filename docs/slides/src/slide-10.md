# Módulo 10
## Observabilidade
<br>
Aprofundamento na Engenharia Cloud-Native

---

## A Importância de Observabilidade 📈

- Base para sistemas de milhões de acessos. <!-- .element: class="fragment" -->
- Substitui práticas engessadas do legado. <!-- .element: class="fragment" -->
- Padroniza o fluxo de entrega. <!-- .element: class="fragment" -->

---

## 1. O que é Prometheus? 🧩

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

## 2. Abordando Grafana 📊

```mermaid
graph LR
    User -->|Call| Server[Observabilidade]
    Server -->|Parse| Data[(Database)]
```

---

## Matemática Aplicada 🔢

As métricas de resposta provam que:
$$ O(log N) $$
Traz mais consistência do que buscas lineares sob estresse da rede.

---

## Aprofundando em Tracing e OpenTelemetry 🚢

- **Tracing**: Reduz o acoplamento temporal. <!-- .element: class="fragment" -->
- **OpenTelemetry**: Garante que o estado seja imutável a longo prazo. <!-- .element: class="fragment" -->

---

## Resumo e Próximos Passos ✅

- A base de **Observabilidade** é sólida. <!-- .element: class="fragment" -->
- Apliquem este fluxo aos **Projetos Práticos**. <!-- .element: class="fragment" -->

> "O código que você escreve hoje moldará o sistema de amanhã."
