<template>
  <div class="flex font-semibold">
    <div class="bg-sky-100 w-5/12 mx-2 px-5 py-5">
      <h2 class="text-4xl text-center text-blue-800">
        Reporte victimas sub regiones
      </h2>
      <div class="flex my-10 justify-end items-center">
        <label for="victimas" class="text-xl mr-2 text-blue-800"
          >Regiones:</label
        >
        <select
          id="victimas"
          @change="onchange()"
          v-model="regionName"
          class="py-2 w-2/4 ml-2 bg-white border-2 border-solid border-pink-500 bg-clip-padding bg-no-repeat transition ease-in-out rounded focus:border-blue-700 focus:outline-none cursor-pointer"
        >
          <option
            v-for="region in regionList"
            :key="region.id"
            :value="region.id"
          >
            {{ region.option }}
          </option>
        </select>
      </div>
      <div class="flex mt-5 pt-28">
        <button
          @click="changeProcess()"
          class="text-2xl text-white font-semibold bg-blue-700 py-2 px-2 w-screen flex items-center justify-center hover:bg-blue-800 rounded"
        >
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/135px-Flag_of_Colombia.svg.png"
            alt="book"
            class="mx-2"
            width="50"
          />
          <p v-if="downloadProcess" class="mx-2">
            Generar Reporte de Sub Regiones
          </p>
          <px-loader v-else />
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

<script lang="ts">
import api from "@/api";
import PxLoader from "@/components/PxLoader.vue";
import { Component, Prop, Vue } from "vue-property-decorator";

@Component({
  components: {
    PxLoader,
  },
})
export default class PxRegiones extends Vue {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  @Prop({ default: () => [], type: Array }) readonly regionList!: any;

  regionName = 0;
  downloadProcess = true;

  public onchange(): void {
    let regionName = this.regionName;
    let option = this.regionList[regionName].img;
    document.getElementById("regionimg").innerHTML = option;
  }

  public async changeProcess(): Promise<void> {
    this.downloadProcess = !this.downloadProcess;
    await api.downloadReport(
      this.regionName,
      this.regionList[this.regionName].option,
      "region"
    );
    this.downloadProcess = !this.downloadProcess;
  }
}
</script>
