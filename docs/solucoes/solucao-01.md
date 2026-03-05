# Solução 01 - Fundamentos da Web 🔑

!!! success "Resolução Oficial"
    Aqui estão as respostas detalhadas para o exercício focado em Fundamentos da Web.

1. **Arquitetura cliente-servidor** refere-se ao modelo escalável onde as responsabilidades são isoladas para maior tolerância a falhas.
2. Adotando **Sistemas distribuídos**, eliminamos pontos únicos de falha e permitimos que diferentes equipes evoluam o código independentemente.
3. Considerando **HTTP/2**, ganhamos liberdade tecnológica (poliglotismo), mas aumentamos a complexidade de rede e observabilidade comparado a um monólito que roda em um único processo da JVM/CLR/Node.
4. Comando CLI:
   ```bash
   docker run -p 8080:80 http/2-service 
   ```
5. **Solução Arquitetural**: O fluxo deveria passar por um API Gateway que realiza throttling. As chamadas síncronas iriam para os serviços críticos, e o processamento de compras seria enfileirado usando um broker para amortecer os requests.

---

[⬅️ Voltar aos Exercícios](../exercicios/exercicio-01.md){ .md-button }
