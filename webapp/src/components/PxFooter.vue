<template>
  <div
    class="w-screen shadow text-center bg-blue-700 text-white py-2 font-semibold"
  >
    <div class="flex justify-around underline">
      <a href="/" class="hover:text-pink-600">Home</a>
      <a
        href="https://github.com/WilliamBarriga"
        target="_blank"
        class="hover:text-pink-600"
        >GitHub</a
      >
      <a
        href="https://www.linkedin.com/in/williambarriga/"
        target="_blank"
        class="hover:text-pink-600"
        >LinkedIn</a
      >
      <a
        href="https://platzi.com/p/william-barriga/"
        target="_blank"
        class="hover:text-pink-600"
        >Platzi</a
      >
    </div>
    <div class="flex justify-center">William Barriga - 2021</div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

@Component
export default class PxFooter extends Vue {}
</script>
