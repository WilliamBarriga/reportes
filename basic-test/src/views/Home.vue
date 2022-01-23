<template>
  <div>
    <px-regiones :regions="regions"></px-regiones>
  </div>
</template>

<script>
import PxRegiones from '@/components/PxRegiones'
import api from '@/api'

export default {
  name: 'Home',

  components:{PxRegiones},

  data () {
    return{
      regions: []
    }
  },

  created () {
    api.getRegions()
      .then(regions => (this.regions = regions))
  }

}
</script>
