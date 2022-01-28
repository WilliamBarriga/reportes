<template>
  <div>
    <scale-loader :loading="isLoading" :color="'#666'" :size="100" class="flex justify-center"></scale-loader>
    <div v-if="!isLoading">
        <div class="flex w-5/12 justify-center items-center py-4 mb-4 mx-2 bg-gray-600">
          <h2 class="text-xl font-semibold">Cambiar el tipo de reporte:</h2>
          <button  @click="changeReport()" class=" bg-pink-600 rounded-lg h-10 px-3 mx-3 w-40 text-white font-semibold">{{ reportName }}</button>
      </div>
      <px-regiones v-if="reportType" :regions="regions"></px-regiones>
      <px-departments v-else :regions="regions"></px-departments>
    </div>
  </div>
</template>

<script>
import PxRegiones from '@/components/PxRegiones'
import PxDepartments from '@/components/PxDepartments'
import api from '@/api'

export default {
  name: 'Home',

  components:{PxRegiones, PxDepartments},

  data () {
    return{
      isLoading: false,
      regions: [],
      reportType: false,
      reportName: 'Departamentos'
    }
  },

  created () {
    this.getData()
  },

  watch:{
    reportType () {
      this.getData(this.reportType);
      if (this.reportType) {
        this.reportName = 'Regiones'
      } else {
        this.reportName = 'Departamentos'
      }
    }
  },
  
  methods:{

    getData: function (report){
      this.isLoading = true
      if (report) {
        console.log('region')
        api.getRegions()
        .then(regions => (this.regions = regions))
        .catch(error => console.log('error: ' + error))
        .finally(() => this.isLoading = false)
      } else{
        console.log('department')
        api.getDepartments()
        .then(regions => (this.regions = regions))
        .catch(error => console.log('error: ' + error))
        .finally(() => this.isLoading = false)
      }
    },
    changeReport: function(){
      this.reportType = !this.reportType
    }
  },

  

}
</script>
