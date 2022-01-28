<template>
  <div class="flex">
    <div class="bg-sky-50 w-5/12 mx-2 px-5 py-5">
      <h2 class="text-4xl text-center">Reporte victimas Regiones</h2>
      <div class="flex my-10 justify-end">
        <label for="victimas" class="text-xl mr-2">Regiones:</label>
        <select
          id="victimas"
          @change="onchange()"
          v-model="regionName"
          class="w-2/4 ml-2"
        >
          <option v-for="region in regions" :key="region.id" :value="region.id">
            {{ region.option }}
          </option>
        </select>
      </div>
      <div class="flex mt-5 pt-28">
        <button
          @click="changeProcess()"
          class="text-2xl text-white font-semibold bg-blue-700 py-2 px-2 w-screen flex items-center justify-center"
        >
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/135px-Flag_of_Colombia.svg.png"
            alt="book"
            class="mx-2"
            width="50"
          />
          <p v-if="downloadProcess" class="mx-2">Descargar region</p>
          <bar-loader v-else></bar-loader>
        </button>
      </div>
    </div>
    <div id="regionimg" class="h-96 flex justify-center w-7/12 mx-2">
      <img
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/135px-Flag_of_Colombia.svg.png"
        alt="imagen colombia"
      />
    </div>
  </div>
</template>

<script>
import api from "@/api";
export default {
  name: "PxRegiones",
  props: {
    regions: {
      type: Array,
      default: () => [],
    },
  },

  data() {
    return {
      regionName: 0,
      downloadProcess: true,
    };
  },
  methods: {
    onchange: function () {
      let regionName = this.regionName;
      let option = this.regions[regionName].img;
      document.getElementById("regionimg").innerHTML = option;
    },
    changeProcess: async function () {
      this.downloadProcess = !this.downloadProcess;
      await api.downloadReport(
        this.regionName,
        this.regions[this.regionName].option,
        "region"
      );
      this.downloadProcess = !this.downloadProcess;
    },
  },
};
</script>

<style scoped></style>
