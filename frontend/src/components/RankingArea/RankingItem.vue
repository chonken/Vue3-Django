<template>
    <div class="item">
        <div class="wrape" @mouseenter="toggle = true" @mouseleave="toggle = false">
            <div class="pic">
                <img :src="'/product/' + url" @error="notFound">
            </div>
            <div class="title">
                <hr>
                <slot name="title"></slot>
            </div>
            <div class="detail" :style="{ height: toggle ? contentHeight + 'px' : '0px' }">
                <p ref="content" class="content">
                    <slot name="content"></slot>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
import pic from '@/assets/not_found.png'
export default {
    props: {
        url: {
            type: String,
            default: () => "",
        }
    },
    data() {
        return {
            toggle: false,
            contentHeight: 0,
            pic,
        }
    },
    methods: {
        notFound(event) {
            event.target.src = this.pic
        }
    },
    mounted() {
        this.contentHeight = this.$refs.content.clientHeight
    }
}
</script>

<style scoped>
hr {
    margin: 0;
    margin-bottom: 5px;
}
.item {
    display: inline-block;
    max-height: 157.4px;
}
.wrape {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 10px;
    max-width: 150px;
    box-sizing: content-box;
    background-color: white;
    border: 1px darkgray solid;
}
.pic {
    height: 120px;
    width: 150px;
    min-width: 150px;
}
.title {
    padding: 0 0.5rem;
    width: 100%;
    font-size: 1.25rem;
    text-align: center;
    text-wrap: nowrap;
    text-overflow: ellipsis;
    overflow-x: hidden;
}
.content {
    padding: 0 0.5rem;
    margin: 0;
    max-width: 100%;
}
.detail {
    width: 100%;
    overflow: hidden;
    transition: all 0.3s ease-in-out;
}
</style>