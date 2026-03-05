# Projeto 11 - Testes de Backend 💼

!!! tip "Objetivo Prático"
    Criar uma implementação funcional (PoC) que unifique os conceitos de **Testes Unitários** e **Postman** utilizando as boas práticas da engenharia moderna baseada em **Pact**.

## 📋 Requisitos do Sistema

- O serviço deve expor pelo menos 2 rotas configuradas.
- Deve possuir tratamento de erro global para os cenários baseados na teoria do K6.
- Deve existir um script autônomo para inicializar e popular variáveis de teste.

## 🛠️ Passo a Passo

1. **Setup**: Inicie seu repósitorio e adicione seu framework Web preferido.
2. **Modelagem**: Crie os contratos baseados na OpenAPI ou modelo assíncrono.
3. **Desenvolvimento**: Construa a lógica central de negócio, desacoplando o I/O usando padrões como portas e adaptadores.
4. **Verificação**: Realize o teste com cURL, Insomnia ou Postman.

```termynal
$ curl -X GET http://localhost:8080/health
[OK] {"status": "UP", "resources": "healthy"}
```
