<template>
    <Monitor>
        <template v-slot:screen>
            <div v-if="isDataExist">
                <NavbarSlide :defaultItem="defaultItem" @change="changeTable">
                    <template v-slot:brand>
                        <div class="brand">
                            <i class="fa-solid fa-gear"></i>
                            <h4>全台PM2.5監測</h4>
                        </div>
                    </template>

                    <template v-slot:dropDown>
                        <div class="dropdown item" id="selectCity">
                            <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                                選擇縣市
                            </button>
                            <ul class="dropdown-menu">
                                <li>
                                    <button class="dropdown-item ">臺北市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">新北市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">基隆市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">桃園市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">新竹縣</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">新竹市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">苗栗國</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">臺中市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">彰化縣</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">南投縣</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">雲林縣</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">嘉義縣</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">嘉義市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">臺南市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">高雄市</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">屏東縣</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">宜蘭縣</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">花蓮縣</button>
                                </li>
                                <li>
                                    <button class="dropdown-item ">臺東縣</button>
                                </li>
                            </ul>
                        </div>
                        <div class="dropdown item" id="selectCity">
                            <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                                選擇縣市
                            </button>
                            <ul class="dropdown-menu">
                                <li>
                                    <button class="dropdown-item ">臺北市</button>
                                </li>
                            </ul>
                        </div>
                    </template>
                </NavbarSlide>
                <table class="table table-striped table-hover text-center">
                    <thead>
                        <tr>
                            <th v-for="(field, i) in fields" :key="i" scope="col">{{ field.info.label }}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, i) in records" :key="i" class="align-middle">
                            <td v-for="(cell, i) in item" :key="i">{{ cell }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <Loading v-else></Loading>
        </template>
    </Monitor>
</template>
<script>
import Monitor from '@/components/Monitor/Monitor.vue';
import NavbarSlide from '@/components/Navbar/NavbarSlide.vue';
import Loading from '@/components/Loading/Loading.vue';
export default {
    components: {
        Monitor,
        NavbarSlide,
        Loading,
    },
    data() {
        return {
            airQuality: undefined,
            fieldsData: ['sitename', 'county', 'monitordate', 'concentration']
        }
    },
    computed: {
        /**
         * 此函數會過濾fieldsData內不存在於原始資料的欄位
         * 
         * 篩選欄位內有與fieldsData有交集的欄位
         * @returns {Array | undefined} 塞選後的資料，原始排序
         */
        fields() {
            if (this.airQuality.fields === undefined)
                return

            return this.airQuality.fields.filter((field) => (this.fieldsData.includes(field.id)))
        },
        /**
         * 篩選key值存在於fieldsData欄位的內容
         * @returns {Array | undefined} 塞選後的資料，根據fieldsData排序
         */
        records() {
            if (this.airQuality.records === undefined)
                return

            let ans = []
            this.airQuality.records.forEach(record => {
                let temp = []
                this.fieldsData.forEach(index => {
                    temp.push(record[index])
                })
                ans.push(temp)
            });
            return ans
        },
        isDataExist() {
            return this.airQuality === undefined ? false : true
        },
    },
    mounted() {
        (async () => {
            const response = await fetch('https://data.moenv.gov.tw/api/v2/aqx_p_322?language=zh&offset=0&api_key=42691430-d2da-4b18-8930-4367d190369d')
            const json = await response.json()
            this.airQuality = json
        })()
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
</style>