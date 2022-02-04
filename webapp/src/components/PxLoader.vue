<template>
  <div class="space-x-1 flex">
    <div class="h-5 w-5 animate-bounce bg-pink-600 rounded-full"></div>
    <div class="h-5 w-5 animate-bounce bg-pink-600 rounded-full"></div>
    <div class="h-5 w-5 animate-bounce bg-pink-600 rounded-full"></div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

@Component
export default class PxLoader extends Vue {}
</script>
