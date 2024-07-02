import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import { createApp, provide, h } from 'vue'
import { DefaultApolloClient } from '@vue/apollo-composable'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import createUploadLink from 'apollo-upload-client/createUploadLink.mjs'

const uploadLink = createUploadLink({
    uri: 'http://localhost:3000/graphql', // Replace with your GraphQL endpoint
  });

// Cache implementation
const cache = new InMemoryCache()

// Create the apollo client
const apolloClient = new ApolloClient({
  link: uploadLink,
  cache,
})

const app = createApp({
    setup() {
        provide(DefaultApolloClient, apolloClient)
    },
    render: () => h(App),
})

app.use(createPinia())
app.use(router)

app.mount('#app')
