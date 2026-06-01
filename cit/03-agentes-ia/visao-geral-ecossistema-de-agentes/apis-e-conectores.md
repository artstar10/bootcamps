# 🔌 Aula 04 - APIs, Segurança e Governança

---

## 🔄 Arquitetura de Integração: O Papel das APIs

Agentes de IA ganham "vida" no mundo real através de APIs e Conectores. 

**Caso de Uso Prático (Suporte ao Cliente):**
1. **Trigger (Gmail API):** O agente recebe um email do cliente.
2. **Processamento (LLM):** O cérebro analisa o texto e extrai a intenção (ex: "Onde está meu pedido?").
3. **Consulta (Shopify API):** O agente faz um `GET /orders` para buscar o status da entrega.
4. **Ação (Zendesk API):** Se o pedido estiver muito atrasado, o agente faz um `POST /tickets` para escalar para um humano.
5. **Resposta (Gmail API):** O agente formula a resposta e faz um `POST /send` para o cliente.

⚠️ **Pontos Críticos na Integração:**
- **Rate Limits:** O LLM pode fazer requisições mais rápido do que a API de destino suporta. É preciso gerenciar filas.
- **Autenticação:** Decidir entre usar OAuth 2.0 (ações em nome do usuário) vs API Keys (ações em nome do sistema).

---

## 🚨 Segurança: Onde Projetos Morrem

O vazamento de chaves de API é um dos erros mais comuns e perigosos, podendo causar prejuízo financeiro imediato.

❌ **Bad Practice (RISCO):**
```python
# NUNCA faça hardcode de credenciais no código
api_key = 'chave_ficticia_exemplo...' 
```
*Problema:* Se esse código for para o GitHub (commit), bots maliciosos roubam a chave em segundos.

✅ **Good Practice (SEGURO):**
```python
import os
# Use Variáveis de Ambiente
api_key = os.getenv('OPENAI_API_KEY')
```
*Solução:* Gerenciamento via arquivo `.env` (desenvolvimento local) ou uso de *Secret Managers* como AWS Secrets Manager ou Azure Key Vault (em Produção).

---

## 🏢 Compliance e Governança Enterprise

Para levar agentes para o nível corporativo (Enterprise), é obrigatório lidar com governança e requisitos como o **SOC 2** (Disponibilidade, Integridade e Confidencialidade).

Os 3 pilares fundamentais são:

### 1. Privacidade (GDPR / LGPD)
- O sistema deve respeitar o **Direito ao Esquecimento** (capacidade de apagar dados do usuário se solicitado).
- É necessário ter consentimento explícito e garantir a proteção dos dados em trânsito e em repouso.

### 2. Sanitization (PII - Personally Identifiable Information)
- É proibido vazar dados de clientes para modelos de terceiros (como OpenAI ou Anthropic).
- **Regra de Ouro:** Mascarar dados sensíveis (CPFs, Cartões de Crédito, Emails, Telefones) **ANTES** de enviá-los ao LLM ou salvá-los nos logs.

### 3. Auditabilidade
- Sistemas autônomos precisam de rastreabilidade total (Logs detalhados).
- Se algo der errado, você precisa saber responder:
  - *Quem (ou o quê) ordenou a ação?*
  - *Por que o agente tomou essa decisão específica?*