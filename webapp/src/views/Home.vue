<template>
  <div>
    <div v-if="isLoading" class="my-3 py-0 flex justify-center items-center">
      <px-loader />
    </div>
    <div v-else>
      <div class="flex w-5/12 justify-center items-center py-4 mb-4 mx-2">
        <h2 class="text-xl font-semibold">Cambiar el tipo de reporte:</h2>
        <button
          @click="changeReport()"
          class="bg-pink-600 rounded-lg h-10 px-3 mx-3 w-40 text-white font-semibold hover:bg-pink-700 shadow-md"
        >
          {{ reportName }}
        </button>
      </div>
      <px-regiones v-if="reportType" :regionList="regionList"></px-regiones>
      <px-departments v-else :regionList="regionList"></px-departments>
      <px-victimas-footer></px-victimas-footer>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Watch, Vue } from "vue-property-decorator";
import PxRegiones from "@/components/PxRegiones.vue";
import PxDepartments from "@/components/PxDepartments.vue";
import PxVictimasFooter from "@/components/PxVictimasFooter.vue";
import PxLoader from "@/components/PxLoader.vue";
import api from "@/api";

@Component({
  components: {
    PxRegiones,
    PxDepartments,
    PxVictimasFooter,
    PxLoader,
  },
})
export default class Home extends Vue {
  isLoading = false;
  reportType = false;
  regionList: Array<string> = [];
  reportName = "Departamentos";

  created(): void {
    this.getData(this.reportType);
  }

  @Watch("reportType")
  onChangeReport(): void {
    this.getData(this.reportType);
    if (this.reportType) {
      this.reportName = "Sub Regiones";
    } else {
      this.reportName = "Departamentos";
    }
  }

  public changeReport(): void {
    this.reportType = !this.reportType;
  }

  public getData(report: boolean): void {
    this.isLoading = true;
    if (report) {
      console.log("region");
      api
        .getRegions()
        .then((regionList) => (this.regionList = regionList))
        .catch((error) => console.log("error: " + error))
        .finally(() => (this.isLoading = false));
    } else {
      console.log("department");
      api
        .getDepartments()
        .then((regionList) => (this.regionList = regionList))
        .catch((error) => console.log("error: " + error))
        .finally(() => (this.isLoading = false));
    }
  }
}
</script>
