# Arquitetura do Fluxo de Resposta a Incidentes

Este diagrama ilustra o ciclo de vida de um incidente de segurança no projeto Optimus Security, desde a detecção inicial até a melhoria contínua.

```mermaid
graph TD
    subgraph "Fase 2: Detecção"
        A[Logs de Autenticação] --> B{log_analyzer.py};
        B --> C((🚨 Alerta Gerado));
    end

    subgraph "Fase 3: Resposta"
        C --> D{PRIO-001: Playbook};
        D --> E[Ações de Contenção: Bloquear IP];
        D --> F[Ações de Erradicação: Resetar Senha];
    end

    subgraph "Fase 5: Pós-Incidente"
        F --> G[Preencher Relatório de Incidente];
        G --> H{Reunião de Lições Aprendidas};
    end

    subgraph "Fase 4: Melhoria Contínua"
        H --> I[Ações de Melhoria: Implementar MFA];
        I --> A;
    end

    style B fill:#222,stroke:#3f3,stroke-width:2px
    style C fill:#f00,stroke:#fff,stroke-width:2px,color:#fff

