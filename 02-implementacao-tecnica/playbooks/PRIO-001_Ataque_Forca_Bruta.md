# Protocolo de Resposta a Incidentes Optimus (PRIO) - 001

**ID do Protocolo:** PRIO-001
**Tipo de Incidente:** Acesso Não Autorizado - Tentativa de Força Bruta
**Severidade Inicial:** Média
**Proprietário:** Equipe de Segurança da Informação (SOC/CSIRT)
**Versão:** 1.0

---
## Objetivo (Para o Curso)
_Este documento é um **Playbook**, um guia passo a passo que define as ações exatas a serem tomadas quando um incidente de segurança específico ocorre. O objetivo é garantir uma resposta rápida, consistente e eficaz. Usaremos como base o framework do **NIST (National Institute of Standards and Technology)**, um padrão global em cibersegurança._
---

## 1. Fase de Preparação
*Esta fase ocorre ANTES do incidente. Nossas ferramentas e conhecimentos devem estar prontos.*

- **Ferramentas Necessárias:** Acesso ao SIEM (Simulado pelo `log_analyzer.py`), sistema de IAM, firewalls, EDR.
- **Fontes de Dados:** Logs de autenticação (Simulado pelo `auth_logs.csv`).

## 2. Fase de Detecção e Análise
*O alerta foi gerado. O objetivo agora é validar e entender o escopo do ataque.*

| Passo | Ação | Ferramenta/Comando Simulado |
| :--- | :--- | :--- |
| **D-1** | **Recebimento do Alerta:** O script `log_analyzer.py` dispara um alerta. | `python log_analyzer.py` |
| **D-2** | **Validação:** É um alarme falso? Contatar o usuário, se possível. | Análise manual dos logs. |
| **D-3** | **Análise de Escopo:** Investigar o IP de origem. Este IP está atacando outras contas? | `grep "IP_DO_ATACANTE" auth_logs.csv` |
| **D-4** | **Determinar o Impacto:** A conta-alvo foi comprometida? Qual o nível de privilégio? | Verificar grupos de permissão. |
| **D-5** | **Documentação Inicial:** Iniciar o registro do incidente. | Criar um "Relatório de Incidente". |

## 3. Fase de Contenção
*O objetivo é impedir que o ataque continue e limitar o dano.*

| Prioridade | Ação | Ferramenta/Comando Simulado |
| :--- | :--- | :--- |
| **C-1 (Alta)** | **Bloquear o IP de Origem:** Adicionar o IP do atacante à *blocklist* do firewall. | `firewall-cmd --add-rich-rule='...reject'` |
| **C-2 (Alta)** | **Desabilitar a Conta-Alvo:** Desabilitar temporariamente a conta sob ataque. | `Disable-ADAccount -Identity "username"` |

## 4. Fase de Erradicação e Recuperação
*O objetivo é remover a causa raiz e restaurar os sistemas de forma segura.*

| Passo | Ação |
| :--- | :--- |
| **ER-1** | **Resetar a Senha:** Forçar a redefinição de senha da conta-alvo. |
| **ER-2** | **Análise de Causa Raiz:** Por que o ataque foi possível? Senha fraca? Falta de MFA? |
| **ER-3** | **Restauração do Serviço:** Reabilitar a conta do usuário. |

## 5. Fase Pós-Incidente (Lições Aprendidas)
*O objetivo é melhorar para que isso não aconteça novamente.*

- **Reunião de Lições Aprendidas:** O que funcionou no nosso playbook? O que não funcionou?
- **Relatório Final do Incidente:** Finalizar a documentação.
- **Ações de Melhoria:** Implementar política de *lockout*, forçar uso de MFA, etc.

---
