<template>
    <div class="container">
        <div class="row mt-4">
            <div class="col=md-12">
                <h1>Results</h1>
            </div>
        </div>
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            <div class="col" v-for="image in result.getAllImages" :key="image.id">
                <div class="card shadow-sm">
                    <img :src="image.image" class="img-fluid" />
                    <div class="card-body">
                        <p class="card-text">ELO:{{ image.elo }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </template>

  <script setup>
    import { useQuery } from '@vue/apollo-composable'
    import { gql } from 'graphql-tag'

    const GET_RESULTS = gql`
      query getAllImages {
          getAllImages {
            id
            image
            upvotes
            downvotes
            elo
        }
      }
    `;

    const { result } = useQuery(GET_RESULTS)
</script>