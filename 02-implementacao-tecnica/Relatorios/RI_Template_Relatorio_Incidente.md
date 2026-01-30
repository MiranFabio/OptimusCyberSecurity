# Relatório de Incidente de Segurança (RI) - Template

**ID do Incidente:** INC-AAAA-NNN
**Data do Relatório:** DD/MM/AAAA
**Autor:** [Seu Nome]
**Classificação:** INTERNO

---
## 1. Resumo Executivo (Para a Gestão)
_Esta seção deve ser lida em 60 segundos e focar no impacto para o negócio._

No dia [Data do Incidente], às [Hora UTC], foi detectada uma tentativa de [Tipo de Ataque] contra [Ativo/Usuário Afetado]. A resposta foi iniciada seguindo o protocolo [ID do PRIO].

- **Impacto no Negócio:** [Nenhum / Baixo / Médio / Alto]. [Descrever o impacto: Ex: Nenhum acesso não autorizado foi bem-sucedido. Não houve comprometimento de dados ou indisponibilidade de serviços.]
- **Ações de Contenção:** [Descrever as ações principais: Ex: O IP do atacante foi bloqueado e a conta-alvo foi temporariamente desabilitada.]
- **Próximos Passos:** [Descrever as recomendações principais: Ex: Recomenda-se a implementação de uma política de lockout de contas.]

## 2. Linha do Tempo Detalhada (Para o Time Técnico e Auditoria)
_Fatos, e nada mais que fatos, com data e hora (UTC)._

| Data/Hora (UTC) | Evento |
| :--- | :--- |
| AAAA-MM-DD HH:MM:SS | **Detecção:** Primeiro evento suspeito. |
| AAAA-MM-DD HH:MM:SS | **Alerta:** Sistema de monitoramento dispara o alerta. |
| AAAA-MM-DD HH:MM:SS | **Análise:** Analista confirma a natureza do incidente. |
| AAAA-MM-DD HH:MM:SS | **Contenção:** Primeira ação de contenção é aplicada. |
| AAAA-MM-DD HH:MM:SS | **Erradicação:** Causa raiz é removida. |
| AAAA-MM-DD HH:MM:SS | **Recuperação:** Sistemas voltam à operação normal. |
| AAAA-MM-DD HH:MM:SS | **Pós-Incidente:** Início da elaboração deste relatório. |

## 3. Análise da Causa Raiz (Root Cause Analysis)
_Por que isso aconteceu e como podemos evitar que se repita?_

O incidente foi possível devido a uma combinação de fatores:
1.  **Fator 1:** [Ex: Ausência de Política de Lockout de Contas.]
2.  **Fator 2:** [Ex: Senha do usuário considerada fraca.]
3.  **Fator 3:** [Ex: Falta de Autenticação Multifator (MFA).]

## 4. Recomendações (Plano de Ação)
_Ações acionáveis para fortalecer nossas defesas._

| Prioridade | Recomendação | Responsável Sugerido | Justificativa |
| :--- | :--- | :--- | :--- |
| **Alta** | Implementar política de lockout de contas. | Time de Infraestrutura | Mitiga a eficácia de ataques de força bruta. |
| **Média** | Forçar o uso de MFA em aplicações externas. | Time de Aplicações | Adiciona uma camada crítica de segurança. |
| **Baixa** | Realizar campanha de conscientização sobre senhas. | Time de Segurança | Melhora a postura de segurança geral. |

---
