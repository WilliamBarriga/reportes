<template>
  <div>
    <scale-loader :loading="isLoading" :color="'#666'" :size="100"></scale-loader>
    <div v-if="!isLoading">
      <button  @click="changeReport()">Cambiar Reporte de Victimas</button>
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
      reportType: false
    }
  },

  created () {
    this.getData()
  },

  watch:{
    reportType () {
      this.getData(this.reportType)
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
