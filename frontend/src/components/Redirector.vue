<template>
    <div>
        <div v-if="error.status" class="alert alert-danger">
            <h4>{{ error.status }}: {{ error.message }}</h4>
            <p>{{ error.body }}</p>
        </div>
    </div>
</template>

<script>
export default {
    props: ['urlKey'],
    data() {
        return {
            apiUrl: this.$apiUrl,
            error: {
                status: null,
                message: null,
                body: null,
            },
        };
    },
    methods: {
        async fetchData() {
            try {
                const response = await fetch(`${this.apiUrl}/${this.urlKey}`);
                const data = await response.json();
                if (data.target_url && response.ok) {
                    window.location = data.target_url
                } else {
                    this.error = {
                        status: response.status,
                        message: response.statusText,
                        body: data,
                    }
                }
            } catch (err) {
                console.log(err);
                this.error = {
                    status: 'Error',
                    message: err.message,
                    body: null,
                };
            }
        }
    },
    mounted() {
        this.fetchData();
    },
};
</script>
