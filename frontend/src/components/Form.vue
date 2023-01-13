<template>
    <div class="text-white">
        <form class="form-group mt-5" @submit.prevent="submitForm">
            <label class="form-control-label">Target URL:</label>
            <input class="form-control" type="text" v-model="formData.target_url" required />
            <br />
            <label class="form-control-label">Number of clicks (optional):</label>
            <input class="form-control" type="number" v-model="formData.num_clicks_left" />
            <br />
            <label class="form-control-label">Expiry date (optional):</label>
            <input class="form-control" type="datetime-local" v-model="formData.expiry_date" />
            <br />
            <label class="form-control-label">Custom URL key (optional):</label>
            <input class="form-control" type="text" v-model="formData.custom_url_key" />
            <br />
            <button class="btn btn-primary" type="submit">Submit</button>
        </form>
        <div v-if="url_key && admin_key" class="mt-5">
            <div class="d-flex">
                <input class="form-control mr-2" type="text" :value="baseUrl + '/' + url_key" readonly>
                <button @click="copyUrl" class="btn btn-primary">📋</button>
            </div>
            <div class="d-flex mt-2">
                <input class="form-control mr-2" type="text" :value="baseUrl + '/admin/' + admin_key" readonly>
                <button @click="copyAdminUrl" class="btn btn-primary">📋</button>
            </div>
        </div>
        <div v-if="error" class="alert alert-danger mt-5">
            <p>Error {{ error.status }}: {{ error.message }}</p>
        </div>
    </div>

</template>

<script>
export default {
    data() {
        return {
            baseUrl: this.$baseUrl,
            apiUrl: this.$apiUrl,
            formData: {
                target_url: null,
                num_clicks_left: null,
                expiry_date: null,
                custom_url_key: null
            },
            url_key: "",
            admin_key: "",
            error: null
        };
    },
    methods: {
        async submitForm() {
            this.error = null;
            this.url_key = "";
            this.admin_key = "";
            try {
                const response = await fetch(`${this.apiUrl}/create`, {
                    method: "POST",
                    body: JSON.stringify(this.formData),
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                const data = await response.json();
                if (!response.ok) {
                    this.error = {
                        status: response.status,
                        message: `${response.statusText}. ${JSON.stringify(data, null, '\t')}`
                    }
                } else {
                    this.url_key = data.url_key;
                    this.admin_key = data.admin_key;
                }
            } catch (err) {
                this.error = { status: err.status, message: err.message }
                console.error(err);
            }
        },
        async copyUrl() {
            try {
                await navigator.clipboard.writeText(this.baseUrl + '/' + this.url_key);
                console.log("URL copied to clipboard");
            } catch (err) {
                console.error("Failed to copy text: ", err);
            }
        },
        async copyAdminUrl() {
            try {
                await navigator.clipboard.writeText(this.baseUrl + '/admin/' + this.admin_key);
                console.log("Admin URL copied to clipboard");
            } catch (err) {
                console.error("Failed to copy text: ", err);
            }
        }
    }
};
</script>
