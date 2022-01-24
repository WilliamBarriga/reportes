<template>
  <div>
    <h3>
      <label for="victimas">Regiones:</label>
    </h3>
    <select id="victimas" @change="onchange()" v-model="regionName">
      <option v-for="region in regions" :key="region.id" :value="region.id"> {{ region.option }} </option>
    </select>
    <button @click="changeProcess()">
            <span v-if="downloadProcess">
            Descargar region
            </span>
            <bar-loader v-else></bar-loader>
        </button>
    <span id="regionimg">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/135px-Flag_of_Colombia.svg.png" alt="imagen colombia">
    </span>
  </div>
</template>

<script>
import api from '@/api'
export default {
    name: 'PxRegiones',
    props: {
        regions:{
            type: Array,
            default: () => []
        }
    },
    
    data (){
      return{
        regionName: 0,
        downloadProcess: true
      }
    },
    methods:{
      onchange: function () {
          let regionName = this.regionName
          let option = this.regions[regionName].img;
          document.getElementById('regionimg').innerHTML=option;
        },
      changeProcess: async function () {
            this.downloadProcess = !this.downloadProcess
            await api.downloadReport(this.regionName, this.regions[this.regionName].option, 'region')
            this.downloadProcess = !this.downloadProcess
        }

      }
    }
</script>

<style scoped>

</style>