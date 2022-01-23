<template>
  <div>
    <h3>
      <label for="victimas">Regiones:</label>
    </h3>
    <select id="victimas">
      <option v-for="region in regions" :key="region.id"> region.name </option>
    </select>
    <button>Descargar Region</button>
  </div>
</template>

<script>
export default {
    name: 'PxRegiones',
    props: {
        assets:{
            type: Array,
            default: () => []
        }
    }
}
</script>

<style scoped>

</style>