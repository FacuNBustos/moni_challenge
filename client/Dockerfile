FROM node:18-alpine

RUN mkdir /client

WORKDIR /client
COPY package.json /client/

RUN npm update
RUN npm install yarn
RUN yarn install

COPY . /client/
RUN yarn build

EXPOSE 3000

CMD ["yarn", "preview"]