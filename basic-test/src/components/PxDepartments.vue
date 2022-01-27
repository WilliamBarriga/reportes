<template>
    <div class="flex">
        <div class="bg-blue-100 w-5/12 mx-2 px-5 py-5">
            <h2 class="text-4xl text-center">Reporte victimas Sub-Regiones</h2>
            <label for="victimas" class="text-xl">Departamentos: </label>
            <div class="flex">
                <select id="victimas" @change="onchange()" v-model="regionName">
                <option v-for="region in regions" :key="region.id" :value="region.id">
                    {{ region.option }}
                </option>
                </select>
            </div>
            <div class="flex mt-5">
                <button @click="changeProcess()" class="text-2xl text-white font-semibold bg-blue-700 py-2 px-2 w-screen flex items-center justify-center">
                    <img src="https://www.flaticon.es/svg/vstatic/svg/3914/3914759.svg?token=exp=1643295656~hmac=7b57471d2a2c3a2779bf991f20b937a1" alt="book" width="50" class="mx-2">
                    <p v-if="downloadProcess" class="mx-2"> Generar Reporte de Departamento </p>
                    <bar-loader v-else></bar-loader>
                </button>
            </div>
        </div>
        <div id="regionimg" class="bg-gray-600 flex justify-center w-7/12 mx-2">
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
  name: "PxDepartments",
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
        "department"
      );
      this.downloadProcess = !this.downloadProcess;
    },
  },
};
</script>

<style scoped>

</style>