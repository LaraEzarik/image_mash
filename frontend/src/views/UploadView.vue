<template>
  <div class="container">
    <div class="card mt-4">
      <div class="card-body">
        <h5 class="card-title">Upload a photo</h5>
        <div class="input-group mb-3">
          <input @change="handleFileUpload" type="file" class="form-control" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1">
        </div>
        <button @click="uploadFile" class="btn btn-primary">Upload</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMutation } from '@vue/apollo-composable'
import { gql } from 'graphql-tag'

// Corrected mutation to match the server's expected input and output
const UPLOAD_FILE = gql`
mutation UploadImage($file: Upload!) {
  upload(image: $file)
}
`;

const selectedFile = ref(null)

// Corrected to match the mutation variable
const { mutate } = useMutation(UPLOAD_FILE)

function handleFileUpload(event) {
  selectedFile.value = event.target.files[0]
}

function uploadFile() {
  if (!selectedFile.value) return;

  // Corrected variable name to match the GraphQL mutation definition
  mutate({file: selectedFile.value }).then(({data}) => {
    console.log(data);
  }).catch((e) => {
    console.error(e);
  });
}
</script>
