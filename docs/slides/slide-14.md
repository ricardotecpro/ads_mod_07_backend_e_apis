# Módulo 14
## API Gateways
<br>
Aprofundamento na Engenharia Cloud-Native

---

## A Importância de API Gateways 📈

- Base para sistemas de milhões de acessos. <!-- .element: class="fragment" -->
- Substitui práticas engessadas do legado. <!-- .element: class="fragment" -->
- Padroniza o fluxo de entrega. <!-- .element: class="fragment" -->

---

## 1. O que é Kong? 🧩

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

## 2. Abordando Apigee 📊

```mermaid
graph LR
    User -->|Call| Server[API Gateways]
    Server -->|Parse| Data[(Database)]
```

---

## Matemática Aplicada 🔢

As métricas de resposta provam que:
$$ O(log N) $$
Traz mais consistência do que buscas lineares sob estresse da rede.

---

## Aprofundando em Rate Limiting e Load Balancing 🚢

- **Rate Limiting**: <span class="fragment">Reduz o acoplamento temporal. <!-- .element: class="fragment" --></span>
- **Load Balancing**: <span class="fragment">Garante que o estado seja imutável a longo prazo. <!-- .element: class="fragment" --></span>

---

## Resumo e Próximos Passos ✅

- A base de **API Gateways** é sólida. <!-- .element: class="fragment" -->
- Apliquem este fluxo aos **Projetos Práticos**. <!-- .element: class="fragment" -->

> "O código que você escreve hoje moldará o sistema de amanhã."