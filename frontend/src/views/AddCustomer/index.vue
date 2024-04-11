<template>
    <Report>
        <template v-slot:title>
            <h4>新建客戶</h4>
        </template>
        <template v-slot:content>
            <form ref="form" @submit.prevent="submit">
                <section class="row">
                    <div class="col-sm-12 col-md-6 mb-3">
                        <input type="text" class="form-control" name="name" placeholder="名稱" autocomplete="off"
                            required />
                    </div>
                    <div class="col-sm-12 col-md-6 mb-3">
                        <input type="number" class="form-control" name="phone" placeholder="電話" autocomplete="off"
                            required />
                    </div>
                    <div class="col-sm-12 col-md-6 mb-3">
                        <input type="text" class="form-control" name="district" placeholder="行政區" required />
                    </div>
                    <div class="col-sm-12 col-md-6 mb-3">
                        <input type="text" class="form-control" name="id" placeholder="會員識別證" autocomplete="off"
                            required />
                    </div>
                    <div class="col-md-12 mb-3 ">
                        <input type="text" class="form-control" name="address" placeholder="地址" autocomplete="off"
                            required />
                    </div>
                </section>
                <DefultButton type="submit" class="btn btn-defult col-12 mb-3">確認</DefultButton>
            </form>
        </template>
    </Report>
</template>
<script>
import Report from '@/components/Report'
import DefultButton from '@/components/Button/DefultButton.vue';
import axios from "axios";
export default {
    components: {
        Report,
        DefultButton,
    },
    methods: {
        submit() {
            const formData = new FormData(this.$refs.form)

            axios({
                method: 'POST',
                url: 'http://127.0.0.1:8000/CRUD/Customer',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: formData
            })
                .then((response) => {
                    if (response.data.success) alert('新增成功')
                    else alert(response.data.error) })
                .catch((error) => { console.log(error) })
        }
    }
}
</script>
<style scoped>
form {
    min-width: 250px;
    max-width: 400px;
}
</style>