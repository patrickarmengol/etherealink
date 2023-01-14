<template>
    <div class="d-flex flex-column align-items-center justify-content-center vh-100 bg-dark">
        <div class="d-flex justify-content-center">
            <Header class="p-2 text-center" />
        </div>
        <router-view class="text-white" />
    </div>
</template>
  
  
  


<script>
import Header from './components/Header.vue';

export default {
    name: 'App',
    components: {
        Header
    }
}
</script>