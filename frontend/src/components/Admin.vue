<template>
    <div>
        <div v-if="error.status" class="alert alert-danger">
            <h4>Error {{ error.status }}: {{ error.message }}</h4>
            <p>{{ error.body }}</p>
        </div>
        <transition name="fade">
            <div class="alert alert-success" v-if="success">
                Changes saved successfully!
            </div>
        </transition>
        <transition name="fade">
            <div class="alert alert-success" v-if="dsuccess">
                Link deleted successfully!
            </div>
        </transition>

        <form @submit.prevent="submitForm" class="form-group">
            <div class="form-group">
                <label class="form-control-label">Target URL:</label>
                <input class="form-control" type="text" :value="data.target_url" readonly />
            </div>
            <div class="form-group">
                <label class="form-control-label">Short URL</label>
                <input class="form-control" type="text" :value="this.baseUrl + '/' + data.url_key" readonly />
            </div>
            <div class="form-group">
                <label class="form-control-label">Expiry:</label>
                <input class="form-control" type="datetime-local" v-model="data.expiry" @change="onChangeExpiry" />
                <button class="btn btn-secondary" v-bind:disabled="!data.expiry"
                    @click.prevent="data.expiry = null; onChangeExpiry()">Clear</button>
            </div>
            <div class="form-group">
                <label class="form-control-label">Clicks Left:</label>
                <input class="form-control" type="number" v-model="data.clicks_left" @change="onChangeClicksLeft" />
                <button class="btn btn-secondary" v-bind:disabled="!data.clicks_left"
                    @click.prevent="data.clicks_left = null; onChangeClicksLeft()">Clear</button>
            </div>
            <div class="form-group">
                <button class="btn btn-primary" type="submit" :disabled="!isChanged">Submit Changes</button>
                <button class="btn btn-danger" @click.prevent="deleteLink">Delete Link</button>
            </div>
        </form>
    </div>
</template>
  

<script>
export default {
    props: ['adminKey'],
    data() {
        return {
            baseUrl: this.$baseUrl,
            apiUrl: this.$apiUrl,
            data: {
                target_url: null,
                url_key: null,
                expiry: null,
                clicks_left: null,
            },
            error: {
                status: null,
                message: null,
                body: null,
            },
            isChanged: false,
            success: false,
            dsuccess: false,
        };
    },
    methods: {
        async fetchData() {
            try {
                const response = await fetch(`${this.apiUrl}/admin/${this.adminKey}`);
                const res_data = await response.json();
                if (response.ok) {
                    this.data = res_data;
                } else {
                    this.error = {
                        status: response.status,
                        message: response.statusText,
                        body: res_data,
                    };
                }
            } catch (err) {
                console.error(err);
                this.error = {
                    status: 'Error',
                    message: err.message,
                    body: null,
                };
            }
        },
        onChangeExpiry() {
            this.isChanged = true;
        },
        onChangeClicksLeft() {
            this.isChanged = true;
        },
        async submitForm() {
            try {
                const payload = {
                    expiry: this.data.expiry,
                    clicks_left: this.data.clicks_left
                };
                const response = await fetch(`${this.apiUrl}/admin/${this.adminKey}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                if (!response.ok) {
                    const res_data = await response.json();
                    this.error = {
                        status: response.status,
                        message: response.statusText,
                        body: res_data,
                    };
                } else {
                    this.isChanged = false;
                    this.error = {
                        status: null,
                        message: null,
                        body: null,
                    }
                    this.success = true;
                    setTimeout(() => { this.success = false }, 3000);
                }
            } catch (err) {
                console.log(err);
                this.error = {
                    status: 'Error',
                    message: err.message,
                    body: null,
                };
            }
        },
        async deleteLink() {
            try {
                const response = await fetch(`${this.apiUrl}/admin/${this.adminKey}`, {
                    method: 'DELETE',
                });
                if (!response.ok) {
                    this.error = {
                        status: response.status,
                        message: response.statusText,
                        body: res_data,
                    };
                } else {
                    this.dsuccess = true;
                    setTimeout(() => { this.dsuccess = false }, 3000);
                }
            } catch (err) {
                console.error(err);
                this.error = {
                    status: 'Error',
                    message: err.message,
                    body: null,
                };
            }
        },
    },
    mounted() {
        this.fetchData();
    },
};
</script>


<style>
.fade-enter-active,
.fade-leave-active {
    transition: opacity .5s;
}

.fade-enter,
.fade-leave-to

/* .fade-leave-active below version 2.1.8 */
    {
    opacity: 0;
}
</style>