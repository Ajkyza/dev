/ Import the HTMX library
import htmx from 'htmx';

// Initialize the HTMX library
htmx.config.adapter = 'turbolinks';

// Create a component that uses HTMX
const MyComponent = Vue.component('my-component', {
    template: `
        <button @click="loadData()">Charger des données</button>

        <div v-if="data">
            <p>{{ data }}</p>
        </div>
    `,

    data() {
        return {
            data: null,
        };
    },

    methods: {
        loadData() {
            this.data = 'Hello, world!';
        },
    },
});

// Mount the component
const app = new Vue({
    el: '#app',
    components: {
        MyComponent,
    },
});
