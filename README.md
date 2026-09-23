# Historical Fundamentus

Aplicação que coleta indicadores fundamentalistas de ações no Fundamentus e os
armazena em um banco PostgreSQL.

## Configuração

1. Instale as dependências:

```bash
uv sync
```

1. Copie `.env.example` para `.env` e preencha as variáveis de conexão:

```bash
cp .env.example .env
```

1. Garanta que o PostgreSQL esteja disponível e que as tabelas esperadas pelo
projeto existam no schema `tickers`.

## Execução

Execute o fluxo de coleta e persistência com:

```bash
uv run python -c "from src.controller.orchestrator import Orchestrator; Orchestrator().perform_workflow()"
```

O processo busca os dados atuais, cadastra novos tickers e atualiza os
indicadores existentes.
