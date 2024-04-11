<template>
    <Report>
        <template v-slot:title>
            <h4>新增商品</h4>
        </template>
        <template v-slot:content>
            <form ref="form" @submit.prevent="submit">
                <section class="row">
                    <div class="col-12 mb-3">
                        <input type="text" class="form-control" name="name" placeholder="名稱" autocomplete="off"
                            required />
                    </div>
                    <div class="col-sm-12 col-md-6 mb-3">
                        <div class="row">
                            <div class="col-12 mb-3">
                                <input type="number" class="form-control" name="price" placeholder="單價" required />
                            </div>
                            <div class="col-12 mb-3">
                                <input type="number" class="form-control" name="stock" placeholder="庫存量" required />
                            </div>
                            <div class="col-12 mb-3">
                                <input type="number" class="form-control" name="discount" placeholder="折扣" required />
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-6 mb-3">
                        <div class="upload-wrape">
                            <img :src="uploadBg" class="upload-img">
                            <input ref="fileInput" type="file" class="form-control upload" @change="changeImg"
                                accept="image/*">
                        </div>
                    </div>
                </section>
                <DefultButton type="submit" class="btn btn-defult col-12 mb-3">確認</DefultButton>
            </form>
        </template>
    </Report>
</template>
<script>
import uploadBg from '@/assets/upload_bg.png'
import Report from '@/components/Report'
import DefultButton from '@/components/Button/DefultButton.vue';
import axios from "axios";
export default {
    components: {
        Report,
        DefultButton
    },
    data() {
        return {
            uploadBg
        }
    },
    methods: {
        submit() {
            const formData = new FormData(this.$refs.form)
            if (this.$refs.fileInput.files.length) {
                formData.append('image', this.$refs.fileInput.files[0].name)
                formData.append('file', this.$refs.fileInput.files[0])
            } else {
                formData.append('image', '')
            }

            axios({
                method: 'POST',
                url: 'http://127.0.0.1:8000/CRUD/Product',
                data: formData
            })
                .then((response) => {
                    if (response.data.success) alert('新增成功')
                    else alert(response.data.error) })
                .catch((error) => { console.log(error) })
        },
        changeImg(event) {
            const file = event.target.files[0]
            const reader = new FileReader()
            reader.readAsDataURL(file)
            reader.onload = (e) => {
                this.uploadBg = e.target.result
            }
        }
    }
}
</script>
<style scoped>
form {
    min-width: 250px;
    max-width: 400px;
}
.upload-wrape {
    position: relative;
    width: 100%;
    aspect-ratio: 5/4;
    border: 1px black solid;
}
.upload-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    object-position: center;
    background-color: lightgray;
}
.upload {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
}
</style>