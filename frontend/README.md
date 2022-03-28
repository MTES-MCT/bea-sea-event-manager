# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Launch unit tests
```
npm run test:unit
```

### Deploy with docker
```
docker build -t sea-event-manager .
docker run -it -p 8080:8080 --rm --name dockerize-sea-event-manager-app-1 sea-event-manager
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
