<script setup>
import { useQuery } from '@vue/apollo-composable'
import { gql } from 'graphql-tag'

const { result } = useQuery(gql`
      query compareImages {
        compareImages {
            id
            image
            upvotes
            downvotes
            elo
          }
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
          <div class="card-body text-center">
            <div class="row">
              <div class="col-md-12">
                <img :src="result.compareImages[0].image" class="img-fluid" />
              </div>
            </div>
            <div class="row">
              <div class="col-md-4">
                <p>Upvotes: {{ result.compareImages[0].upvotes }}</p>
              </div>
              <div class="col-md-4">
                <p>Downvotes: {{ result.compareImages[0].downvotes }}</p>
              </div>
              <div class="col-md-4">
                <p>Elo: {{ result.compareImages[0].elo }}</p>
              </div>
            </div>
          </div>
         </div>
      </div>
      <div class="col-md-6">
        <div class="card mt-4">
          <div class="card-body text-center">
            <div class="row">
              <div class="col-md-12">
                <img :src="result.compareImages[1].image" class="img-fluid" />
              </div>
            </div>
            <div class="row">
              <div class="col-md-4">
                <p>Upvotes: {{ result.compareImages[1].upvotes }}</p>
              </div>
              <div class="col-md-4">
                <p>Downvotes: {{ result.compareImages[1].downvotes }}</p>
              </div>
              <div class="col-md-4">
                <p>Elo: {{ result.compareImages[1].elo }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
