<template>
  <div>
    <form @submit.prevent="submitForm">
      <label>
        Enter URL:
        <input type="text" v-model="inputURL" />
      </label>
      <button type="submit">Submit</button>
    </form>
    <div v-if="responseURL">
      API Response URL: {{ responseURL }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { onMounted, ref } from 'vue';

export default {
  setup() {
    const inputURL = ref('');
    const responseURL = ref('');

    const submitForm = async () => {
      try {
        const response = await axios.post('127.0.0.1:8000/create', { url: inputURL.value });
        responseURL.value = 'http://127.0.0.1:8000/' + response.data.url_key;
      } catch (error) {
        console.error(error);
      }
    }

    onMounted(() => {
      // any lifecycle hooks or setup logic goes here
    })

    return { inputURL, responseURL, submitForm }
  }
}
</script>
