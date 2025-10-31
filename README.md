# 🧠 Node.js + TypeScript + Docker + Deploy ECR + ECS

Este projeto é uma API básica construída com **Node.js** e **TypeScript**, estruturada para rodar em **ambiente de produção com Docker**. Ele inclui suporte a builds, desenvolvimento com hot-reload, e um ambiente leve baseado no `node:alpine`.

> Deploy container da aplicação para o ECR e dispara a atualização da nova imagem para o serviço do Cluster

Variáveis e Segredos que devem ser criados no github (settings)

> vars

```bash
AWS_REGION="us-east-1"
ECR_REPOSITORY=""
ECS_CLUSTER=""
ECS_TASK_DEFINITION=""
ECS_SERVICE=""
```

---

> secrets

```bash
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_ACCOUNT_ID=""
```

## 🚀 Tecnologias

- [Node.js 22](https://nodejs.org/)
- [TypeScript](https://www.typescriptlang.org/)
- [Express.js](https://expressjs.com/)
- [Docker](https://www.docker.com/)
- [ts-node-dev](https://github.com/wclr/ts-node-dev)

---

## 📁 Estrutura do Projeto

```bash
.
├── src/
│   └── main.ts         # Arquivo principal da API
├── dist/               # Código transpilado para produção
├── package.json        # Scripts e dependências
├── tsconfig.json       # Configuração do TypeScript
├── Dockerfile          # Configuração do ambiente Docker
├── .gitignore
└── README.md
```

## ⚙️ Scripts

> inicia a API com hot-reload para desenvolvimento

```bash
npm run dev
```

> compila o projeto TypeScript para JavaScript (gera o dist)

```bash
npm run build
```

> roda o projeto já compilado (node dist/main.js)

```bash
npm start
```

## 🐳 Docker

🔨 Build da imagem

```bash
docker build -t minha-api .
```

▶️ Rodar o container

```bash
docker run -p 3025:3025 minha-api
```
