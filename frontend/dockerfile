# Stage 1: Build stage (The Kitchen)
FROM node:18-slim AS builder

WORKDIR /app

# Copy the "shopping list"
COPY package.json ./
# Install the tools
RUN npm install --production

# Stage 2: Final stage (The Dining Room)
FROM node:18-slim

# Install curl so the HEALTHCHECK can work
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Create your non-root user
RUN useradd -m blessing_benedicta_bill
USER blessing_benedicta_bill

WORKDIR /home/blessing_benedicta_bill/app

# Copy only the installed "groceries" and the code
COPY --from=builder /app/node_modules ./node_modules
COPY --chown=blessing_benedicta_bill:blessing_benedicta_bill . .

# The Heartbeat: Check if the Node server is answering on port 3000
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/ || exit 1

EXPOSE 3000

# Start the Node.js proxy server
CMD ["node", "app.js"]
