# Stage 1: Build
FROM node:22.2.0-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

# Stage 2: Production
FROM node:22.2.0-alpine

WORKDIR /app

# Copia apenas o necessário para produção
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package.json ./
COPY --from=builder /app/package-lock.json ./

# Instala apenas as dependências de produção
RUN npm install --omit=dev --ignore-scripts

# Instala pacotes do sistema
RUN apk add --no-cache \
    graphicsmagick \
    ghostscript \
    vips-dev

ENV NODE_ENV=production
ENV OPENSSL_CONF='/etc/ssl/'
ENV NODE_OPTIONS=--max_old_space_size=4096

EXPOSE 3000

CMD ["node", "dist/server.js"]

