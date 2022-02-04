<template>
  <header class="w-screen shadow">
    <nav
      class="items-center justify-between bg-blue-700 p-6 text-white font-semibold text-center"
    >
      <div class="flex justify-between">
        <div class="flex items-center mr-6 space-x-6">
          <px-icon />
          <p class="text-xl tracking-tight">
            Equipo de Gestión de Conocimiento de la Consejería Presidencial para
            la Estabilización y la Consolidación
          </p>
        </div>
        <div class="flex items-center justify-around mr-10 space-x-4">
          <a href="/" class="hover:text-pink-600">Victimas</a>
          <a href="/arn" class="hover:text-pink-600">ARN</a>
          <a href="/art" class="hover:text-pink-600">ART</a>
          <a href="/dri" class="hover:text-pink-600">DRI</a>
          <a href="/other" class="hover:text-pink-600">Otro</a>
        </div>
      </div>
    </nav>
  </header>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import PxIcon from "./PxIcon.vue";

@Component({
  components: {
    PxIcon,
  },
})
export default class PxHeader extends Vue {}
</script>
