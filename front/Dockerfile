FROM node:14

WORKDIR /app/front

COPY package*.json ./
RUN npm install -g @angular/cli

COPY . .

EXPOSE 4200 49153

CMD ng serve --host 0.0.0.0 --port 4200
