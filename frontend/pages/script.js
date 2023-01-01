import Vue from "vue";
import { getDataFromAPI } from "~/services/ApiService"

export default Vue.extend({
    name: 'IndexPage',
    components: { },
    data: () => ({
        currentMetric: {},
        useHistory: false,
        checking: false,
        useAutomaticUpdate: true,
        interval: 5,    // default time of 5 seconds
        intervalId: null,
        history: []
    }),
    computed: {
        temperature() {
            return this.currentMetric.temperature;
        },
        humidity() {
            return this.currentMetric.humidity;
        },
        lastCheck() {
            return this.currentMetric.datetime;
        },
        temperatureHistory() {
            return this.history.map(e => e.temperature);
        },
        isUpdating() {
            return this.checking && this.useAutomaticUpdate
        }
    },
    watch: {
        useHistory(value) {
            if(!value) {
                this.history = [];
            }
        },
        async interval(value) {
            clearInterval(this.intervalId);
            this.intervalId = await this.createInterval();
        }
    },
    async mounted() {
        try {
            await this.loadData();
            this.intervalId = await this.createInterval();
        } catch (error) {
            console.log(error);
        }
    },
    methods: {
        // Creates the automatic update interval
        // Converts the interval from ms to seconds (*1000)
        async createInterval() {
            if(this.interval > 0) {
                return setInterval(async () => {
                    if(this.useAutomaticUpdate) {
                        await this.loadData();
                    }
                }, this.interval * 1000)    
            }
        },

        // Loads data from API
        async loadData() {
            this.checking = true;
            const result = await getDataFromAPI();

            const time = new Date(result.date);

            this.currentMetric = {
                temperature: result.temperature,
                humidity: result.humidity,
                datetime: time
            };

            // Adds to history
            if(this.useHistory) {
                this.history.push(this.currentMetric);
            }
            
            this.checking = false;
        }
    }
})