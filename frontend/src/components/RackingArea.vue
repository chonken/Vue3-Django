<template>
    <div class="backplane">
        <div class="title">
            <slot></slot>
        </div>
        <div class="rank" ref="rankWidth">
            <div :style="{ transform: `translateX(-${translate}px)` }" class="itemplane" ref="planeWidth">
                <RankingItem v-for="(item, index) in member" :key="index" :url="item.url">
                    <template v-slot:title>{{ item.title }}</template>

                    <template v-slot:content>{{ item.content }}</template>
                </RankingItem>
            </div>
        </div>
        <div @click="showMore" class="more">></div>
    </div>
</template>

<script>
import RankingItem from './RankingItem.vue';
export default {
    components: {
        RankingItem,
    },
    props: {
        member: {
            type: Object,
            default: () => { }
        },
    },
    data() {
        return {
            translate: 0,
        }
    },
    methods: {
        /**
         * 
         */
        showMore() {
            const rankWidth = this.$refs.rankWidth.clientWidth
            const planeWidth = this.$refs.planeWidth.clientWidth
            const remainingLength = planeWidth - this.translate - rankWidth
            
            console.log(planeWidth, this.translate, rankWidth, remainingLength)
            if (remainingLength === 0) {
                this.translate = 0
            }
            else if (remainingLength > rankWidth) {
                this.translate += rankWidth
            } else {
                this.translate += remainingLength
            }
        },
    },
    mounted() {
    }
}
</script>

<style scoped>
.backplane {
    position: relative;
    flex-direction: row;
    display: flex;
    width: 100%;
    margin-bottom: 30px;
    padding: 0;
    background-color: white;
}
.itemplane {
    display: inline-block;
    text-wrap: nowrap;
    transition: transform 0.5s ease-in-out;
}
.rank {
    margin-top: 30px;
    padding-top: 20px;
    padding-bottom: 10px;
    width: 100%;
    border-top: 5px solid lightgray;
    border-bottom: 1px solid lightgrey;
    overflow-x: hidden;
}
.title {
    position: absolute;
    left: 25px;
    padding: 0 8px;
    font-size: 2rem;
    background-color: white;
    z-index: 1;
}
.more {
    position: absolute;
    bottom: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: calc(100% - 35px);
    width: 50px;
    font-size: 1.5rem;
    color: white;
    background-image: linear-gradient(to right, rgba(0, 0, 0, 0.15) 0%, rgba(0, 0, 0, 0.85) 30%, rgba(0, 0, 0, 1));
    cursor: pointer;
}
</style>