<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  <Sidebar :sidebarTitle="sidebarTitle" :defaultId="defaultId" @active="changePages"></Sidebar>
  <main>
    <AddCustomer v-if="page === 'addCustomer'"></AddCustomer>
    <AddProduct v-else-if="page === 'addProduct'"></AddProduct>
    <AddBranch v-else-if="page === 'addBranch'"></AddBranch>
    <EditInfo v-else-if="page === 'editInfo'"></EditInfo>
    <CheckKPI v-else-if="page === 'checkKPI'"></CheckKPI>
    <!-- <AirQuality v-else-if="page === 'airQuality'"></AirQuality> -->
  </main>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle'
import '@fortawesome/fontawesome-free/css/all.css'
import Sidebar from './views/Sidebar'
import AddCustomer from './views/AddCustomer'
import AddProduct from './views/AddProduct'
import AddBranch from './views/AddBranch'
import EditInfo from './views/EditInfo'
import CheckKPI from './views/CheckKPI'
// import AirQuality from './views/AirQuality'

export default {
  name: 'App',
  components: {
    Sidebar,
    AddCustomer,
    AddProduct,
    AddBranch,
    EditInfo,
    CheckKPI,
    // AirQuality,
  },
  data() {
    const sidebarTitle = [
      { id: "addCustomer", name: "新建客戶" },
      { id: "addProduct", name: "新增商品" },
      { id: "addBranch", name: "新增分店" },
      { id: "editInfo", name: "編輯資料" },
      { id: "checkKPI", name: "查看績效" },
      // { id: "airQuality", name: "台灣空氣品質" },
    ]
    const defaultId = sidebarTitle[0].id
    const page = defaultId

    return {
      sidebarTitle,
      defaultId,
      page,
    }
  },
  methods: {
    changePages(id) {
      this.page = id
    },
  }
}
</script>

<style>
:root {
  --primary-color: #ecf0f1;
  --secondary-color: #2c3e50;
  --accent-color: #e74c3c;
  --report-title-color-1: #0B5A84;
  --report-title-color-2: #0C6697;
  --report-content-color: #fafafa;
  --monitor-title-color: #0B5A84;
  --monitor-border-color: #808080;
  --monitor-content-color: #fff;
  --rankarea-color: #fff;
  --test: #000;
  /* --body-color: #f0f2f5; */
  /* --content-color: #ffffff; */
  /* --bg-color-dark: #191919; */
  /* --thead-color: #344767; */
  /* --default-color-deg: 195deg; */
  --default-color-start: #747b8a;
  --default-color-end: #495361;
  --btn-color-confirm: #F44335;
  --btn-color-deny: #7b809a;
  --btn-color-goback: #adff2f;
  --btn-color-import: #198754;
  --text-light: #ffffff;
  --text-dark: #000000;
  --text-gray: #67748e;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Microsoft JhengHei', sans-serif;
}

/* 版面設定 */
body {
  background: var(--primary-color);
}
aside {
  width: 300px;
}
main {
  margin-left: 300px;
}
</style>
