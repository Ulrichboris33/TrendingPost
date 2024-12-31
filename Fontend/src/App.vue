<template>
  <div id="app">
    <PopularTopics />
  </div>
</template>

<script>
import PopularTopics from "./components/PopularTopics.vue";

export default {
  components: {
    PopularTopics,
  },
};
</script>

<style>
body {
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
  color: #333;
}

h1, h2, p {
  margin: 0;
  padding: 0;
}

a {
  text-decoration: none;
  color: inherit;
}

</style>
