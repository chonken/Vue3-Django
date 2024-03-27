<template>
    <Monitor>
        <template v-slot:screen>
            <div class="hidden-wrap">
                <RackingArea :member="popular">總銷售量</RackingArea>
                <RackingArea :member="totalSales">總銷售額</RackingArea>
            </div>
        </template>
    </Monitor>
</template>
<script>
import Monitor from '@/components/Monitor/Monitor.vue';
import NavbarSlide from '@/components/Navbar/NavbarSlide.vue';
import DefultButton from '@/components/Button/DefultButton.vue';
import RackingArea from '@/components/RankingArea/RackingArea.vue';
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
         * (``response``) => this.popular
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
                        const content = "銷量: " + item['sales_quantity']
                        data.push({ title: item['product__name'], content, url: 'http://127.0.0.1:8000/product/' + item['product__image'] })
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
         * (``response``) => this.totalSales
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
                        const content = "銷售額: $" + item['total_sales']
                        data.push({ title: item['product__name'], content, url: 'http://127.0.0.1:8000/product/' + item['product__image'] })
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
.hidden-wrap {
    height: 100%;
    overflow-x: hidden;
}
</style>