<script setup>

</script>
<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Image Mash</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
            <RouterLink class="nav-link" to="/">Home</RouterLink>
        </li>
        <li class="nav-item">
            <RouterLink class="nav-link" to="/results">Results</RouterLink>
        </li>
        <li class="nav-item">
            <RouterLink class="nav-link" to="/upload">Upload Image</RouterLink>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>