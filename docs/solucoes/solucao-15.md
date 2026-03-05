# Solução 15 - Ecossistemas 🔑

!!! success "Resolução Oficial"
    Aqui estão as respostas detalhadas para o exercício focado em Ecossistemas.

1. **Node.js** refere-se ao modelo escalável onde as responsabilidades são isoladas para maior tolerância a falhas.
2. Adotando **Spring Boot**, eliminamos pontos únicos de falha e permitimos que diferentes equipes evoluam o código independentemente.
3. Considerando **.NET**, ganhamos liberdade tecnológica (poliglotismo), mas aumentamos a complexidade de rede e observabilidade comparado a um monólito que roda em um único processo da JVM/CLR/Node.
4. Comando CLI:
   ```bash
   docker run -p 8080:80 .net-service 
   ```
5. **Solução Arquitetural**: O fluxo deveria passar por um API Gateway que realiza throttling. As chamadas síncronas iriam para os serviços críticos, e o processamento de compras seria enfileirado usando um broker para amortecer os requests.

---

[⬅️ Voltar aos Exercícios](../exercicios/exercicio-15.md){ .md-button }
