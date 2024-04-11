<template>
    <Monitor>
        <template v-slot:screen>
            <NavbarSlide :items="['客戶', '商品', '門市']" :defaultItem="defaultItem" @change="changeTable">
                <template v-slot:brand>
                    <div class="brand">
                        <i class="fa-solid fa-gear"></i>
                        <h4>編輯資料</h4>
                    </div>
                </template>
            </NavbarSlide>
            <form ref="form" @submit.prevent="submit">
                <table v-show="table === '客戶'" class="table table-striped table-hover text-center">
                    <thead>
                        <tr>
                            <th scope="col">名稱</th>
                            <th scope="col" class="col-3">電話</th>
                            <th scope="col" class="col-4">地址</th>
                            <th scope="col">行政區</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in customerData" :key="item.id" class="align-middle">
                            <td>
                                <input type="text" class="form-control" :name="'customer&' + item.id + '&name'"
                                    :placeholder="item.name" />
                            </td>
                            <td>
                                <input type="number" class="form-control" :name="'customer&' + item.id + '&phone'"
                                    :placeholder="item.phone" />
                            </td>
                            <td>
                                <input type="text" class="form-control" :name="'customer&' + item.id + '&address'"
                                    :placeholder="item.address" />
                            </td>
                            <td>
                                <input type="text" class="form-control" :name="'customer&' + item.id + '&district'"
                                    :placeholder="item.district" />
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table v-show="table === '商品'" class="table table-striped table-hover text-center">
                    <thead>
                        <tr>
                            <th scope="col">名稱</th>
                            <th scope="col">單價</th>
                            <th scope="col">庫存量</th>
                            <th scope="col">折扣</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in productData" :key="item.id" class="align-middle">
                            <td>
                                <input type="text" class="form-control" :name="'product&' + item.id + '&name'"
                                    :placeholder="item.name" />
                            </td>
                            <td>
                                <input type="number" class="form-control" :name="'product&' + item.id + '&price'"
                                    :placeholder="item.price" />
                            </td>
                            <td>
                                <input type="number" class="form-control" :name="'product&' + item.id + '&stock'"
                                    :placeholder="item.stock" />
                            </td>
                            <td>
                                <input type="number" class="form-control" :name="'product&' + item.id + '&discount'"
                                    :placeholder="item.discount" step="0.001" />
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table v-show="table === '門市'" class="table table-striped table-hover text-center">
                    <thead>
                        <tr>
                            <th scope="col">名稱</th>
                            <th scope="col">營業人統編</th>
                            <th scope="col" class="col-6">地址</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in storeData" :key="item.id" class="align-middle">
                            <td>
                                <input type="text" class="form-control" :name="'store&' + item.id + '&name'"
                                    :placeholder="item.name" />
                            </td>
                            <td>
                                <input type="number" class="form-control" :name="'store&' + item.id + '&tax_id'"
                                    :placeholder="item.tax_id" />
                            </td>
                            <td>
                                <input type="text" class="form-control" :name="'store&' + item.id + '&address'"
                                    :placeholder="item.address" />
                            </td>
                        </tr>
                    </tbody>
                </table>

                <div class="w-100 text-center">
                    <DefultButton type="submit" class="btn btn-defult mb-3">確認</DefultButton>
                </div>
            </form>
        </template>
    </Monitor>
</template>
<script>
import Monitor from '@/components/Monitor';
import NavbarSlide from '@/components/Navbar';
import DefultButton from '@/components/Button/DefultButton.vue';
import axios from 'axios';
export default {
    components: {
        Monitor,
        NavbarSlide,
        DefultButton,
    },
    data() {
        const defaultItem = '客戶'
        return {
            customerData: {},
            storeData: {},
            productData: {},
            table: defaultItem,
            defaultItem,
        }
    },
    methods: {
        submit() {
            // bug 中文輸入時會，其他資料可能會消失，待修復
            const formData = new FormData(this.$refs.form)

            let customerObj = {};
            let storeObj = {};
            let productObj = {};
            // model-id-field = value => model{ id: { field: value, }, }
            formData.forEach(function (value, key) {
                if (value !== "") {
                    const k = key.split("&")
                    switch (k[0]) {
                        case "customer":
                            if (!customerObj[k[1]])
                                customerObj[k[1]] = {}
                            customerObj[k[1]][k[2]] = value
                            break;
                        case "store":
                            if (!storeObj[k[1]])
                                storeObj[k[1]] = {}
                            storeObj[k[1]][k[2]] = value
                            break;
                        case "product":
                            if (!productObj[k[1]])
                                productObj[k[1]] = {}
                            productObj[k[1]][k[2]] = value
                            break;
                    }
                }
            });

            // model{ id: { field: value, }, } => model[ { id:'*', field: value, }, ]
            let customerList = []
            let storeList = []
            let productList = []
            for (let key in customerObj) {
                customerObj[key].id = key
                customerList.push(customerObj[key])
            }
            for (let key in storeObj) {
                storeObj[key].id = key
                storeList.push(storeObj[key])
            }
            for (let key in productObj) {
                productObj[key].id = key
                productList.push(productObj[key])
            }
            if (customerList.length > 0) {
                this.setCustomerData(customerList)
                this.getCustomerData()
            }
            if (storeList.length > 0) {
                this.setStoreData(storeList)
                this.getStoreData()
            }
            if (productList.length > 0) {
                this.setProductData(productList)
                this.getProductData()
            }

            document.querySelectorAll('input').forEach((input) => { input.value = '' })
        },
        changeTable(item) {
            this.table = item
        },

        /**
         * axios({ ``method``: 'GET', ``url``: '...Customer', })
         * 
         * (``response``) => this.customerData
         */
        async getCustomerData() {
            try {
                const response = await axios({
                    method: 'GET',
                    url: 'http://127.0.0.1:8000/CRUD/Customer',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                })
                if (response.data.success) {
                    this.customerData = response.data.data
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
        async getStoreData() {
            try {
                const response = await axios({
                    method: 'GET',
                    url: 'http://127.0.0.1:8000/CRUD/Store',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                })
                if (response.data.success) {
                    this.storeData = response.data.data
                } else {
                    console.log(response)
                }
            } catch (error) {
                console.error(error)
            }
        },
        /**
         * axios({ ``method``: 'GET', ``url``: '...Product', })
         * 
         * (``response``) => this.productData
         */
        async getProductData() {
            try {
                const response = await axios({
                    method: 'GET',
                    url: 'http://127.0.0.1:8000/CRUD/Product',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                })
                if (response.data.success) {
                    this.productData = response.data.data
                } else {
                    console.log(response)
                }
            } catch (error) {
                console.error(error)
            }
        },
        /**
         * axios({ ``method``: 'PUT', ``url``: '...Customer', })
         * 
         * 
         */
        async setCustomerData(data) {
            try {
                const response = await axios({
                    method: 'PUT',
                    url: 'http://127.0.0.1:8000/CRUD/Customer',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: data,
                })
                if (response.data.success) {
                    this.customerData = response.data.data
                } else {
                    console.log(response)
                }
            } catch (error) {
                console.error(error)
            }
        },
        /**
         * axios({ ``method``: 'PUT', ``url``: '...Store', })
         * 
         * 
         */
        async setStoreData(data) {
            try {
                const response = await axios({
                    method: 'PUT',
                    url: 'http://127.0.0.1:8000/CRUD/Store',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: data
                })
                if (response.data.success) {
                    this.storeData = response.data.data
                } else {
                    console.log(response)
                }
            } catch (error) {
                console.error(error)
            }
        },
        /**
         * axios({ ``method``: 'PUT', ``url``: '...Product', })
         * 
         * 
         */
        async setProductData(data) {
            try {
                const response = await axios({
                    method: 'PUT',
                    url: 'http://127.0.0.1:8000/CRUD/Product',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: data
                })
                if (response.data.success) {
                    this.productData = response.data.data
                } else {
                    console.log(response)
                }
            } catch (error) {
                console.error(error)
            }
        },
    },
    created() {
        this.getCustomerData();
        this.getStoreData();
        this.getProductData();
    }
}
</script>
<style scoped>
.brand {
    padding: 25px 30px 0 30px;
}
.brand i {
    font-size: 2rem;
}
.brand > * {
    display: inline-block;
    margin: 0;
}
.item {
    position: relative;
    font-size: 0;
}
.item > button {
    position: relative;
    margin: 0;
    padding: 0rem 1rem;
    font-size: 1rem;
    color: var(--text-gray);
    background-color: transparent;
    border: none;
    transition: all 0.5s;
}
form {
    min-width: 640px;
}
input {
    background-color: transparent;
}
</style>