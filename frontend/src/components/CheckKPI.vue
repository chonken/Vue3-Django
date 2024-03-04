<template>
    <Monitor>
        <template v-slot:screen>
            <RackingArea :member="popular">總銷售量</RackingArea>
            <RackingArea :member="totalSales">總銷售額</RackingArea>
        </template>
    </Monitor>
</template>
<script>
import Monitor from './Monitor.vue';
import NavbarSlide from './NavbarSlide.vue';
import DefultButton from './DefultButton.vue';
import RackingArea from './RackingArea.vue';
import axios from 'axios';
export default {
    components: {
        Monitor,
        NavbarSlide,
        DefultButton,
        RackingArea,
    },
    data() {
        return {
            popular: {},
            totalSales: {},
        }
    },
    methods: {
        submit() {

        },

        /**
         * axios({ ``method``: 'GET', ``url``: '...Customer', })
         * 
         * (``response``) => this.customerData
         */
        async getPopular() {
            try {
                const response = await axios({
                    method: 'GET',
                    url: 'http://127.0.0.1:8000/CheckKPI/Popular',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                })
                if (response.data.success) {
                    let data = []
                    response.data.data.forEach(item => {
                        data.push({ title: item['product__name'], content: item['sales_quantity'], url: "" })
                    });
                    this.popular = data
                } else {
                    console.log(response)
                }
            } catch (error) {
                console.error(error)
            }
        },
        /**
         * axios({ ``method``: 'GET', ``url``: '...Store', })
         * 
         * (``response``) => this.storeData
         */
        async getTotalSales() {
            try {
                const response = await axios({
                    method: 'GET',
                    url: 'http://127.0.0.1:8000/CheckKPI/TotalSales',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                })
                if (response.data.success) {
                    let data = []
                    response.data.data.forEach(item => {
                        data.push({ title: item['product__name'], content: "$: " + item['total_sales'], url: "" })
                    });
                    this.totalSales = data
                } else {
                    console.log(response)
                }
            } catch (error) {
                console.error(error)
            }
        },
    },
    created() {
        this.getPopular();
        this.getTotalSales();
    }
}
</script>
<style scoped>

</style>