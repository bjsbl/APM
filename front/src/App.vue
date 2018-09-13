<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
<style>
  a:focus,
  a:active {
    outline: none;
  }

  a,
  a:focus,
  a:hover {
    cursor: pointer;
    color: inherit;
    text-decoration: none;
  }
</style>