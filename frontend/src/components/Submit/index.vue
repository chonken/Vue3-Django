<template>
    <DefultButton type="submit" class="btn btn-defult col-12 mb-3" @submit="this.$emit('res', res)">確認</DefultButton>
</template>
<script>
import DefultButton from '@/components/Button/DefultButton.vue';
import axios from 'axios';
export default {
    props: {
        method: {
            type: String,
            default: () => 'GET'
        },
        url: {
            type: String,
            default: () => ''
        },
        formData: {
            type: FormData,
            default: () => { new FormData() }
        },
    },
    components: {
        DefultButton
    },
    data() {
        return {
            res: false
        }
    },
    methods: {
        submit() {
            console.log(1)
            let resText = '成功'
            if (this.method === 'POST')
                resText = '新增成功'

            axios({
                method: this.method,
                url: 'http://127.0.0.1:8000/' + this.url,
                // headers: {
                //     'Content-Type': 'application/json'
                // },
                data: this.formData
            })
                .then((response) => {
                    if (response.data.success) {
                        this.res = true
                        alert(resText)
                    }
                    else {
                        this.res = false
                        alert(response.data.error)
                    }
                })
                .catch((error) => { console.log(error) })
        }
    }
}
</script>
<style scoped></style>