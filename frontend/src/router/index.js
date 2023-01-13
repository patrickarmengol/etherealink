import { createRouter, createWebHistory } from 'vue-router';
import Form from "../components/Form.vue";
import Redirector from "../components/Redirector.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            component: Form
        },
        {
            path: '/:urlKey',
            component: Redirector,
            props: true
        },
    ]
});

export default router;
