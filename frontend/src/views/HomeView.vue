<script setup>
import { useQuery } from '@vue/apollo-composable'
import { gql } from 'graphql-tag'

const { result } = useQuery(gql`
      query randomImages {
        randomImages
      }
    `);
</script>

<template>
  <div class="container">
    <div class="row mt-4">
      <div class="col=md-12">
        <h1>Pick an image</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <div class="card mt-4">
          <div class="card-body">
            <img :src="result.randomImages[0]" class="img-fluid" />
          </div>
         </div>
      </div>
      <div class="col-md-6">
        <div class="card mt-4">
          <div class="card-body">
            <img :src="result.randomImages[1]" class="img-fluid" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
