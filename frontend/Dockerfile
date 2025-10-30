FROM node:20-alpine as build

WORKDIR /app

RUN apk add --no-cache git python3 make

COPY package*.json nginx.conf yarn.lock ./

RUN corepack enable

RUN yarn install

COPY . .
RUN yarn build

FROM nginx:stable-alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3001

CMD [ "nginx", "-g", "daemon off;" ]