<template>
    <div class="backplane">
        <div class="rank" ref="rank">
            <div class="title">
                <slot></slot>
            </div>
            <div :style="{ transform: `translateX(-${translate}px)` }" class="itemplane" ref="plane">
                <RankingItem v-for="(item, index) in member" :key="index" :url="item.url">
                    <template v-slot:title>{{ item.title }}</template>

                    <template v-slot:content>{{ item.content }}</template>
                </RankingItem>
            </div>
            <div @click="showMore" class="more">></div>
        </div>
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
            const rankWidth = this.$refs.rank.clientWidth
            const planeWidth = this.$refs.plane.clientWidth
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
}
</script>

<style scoped>
.backplane {
    width: 100%;
    padding: 10px 0;
    background-color: var(--rankarea-color);
}
.itemplane {
    display: inline-block;
    text-wrap: nowrap;
    transition: transform 0.5s ease-in-out;
}
.rank {
    position: relative;
    margin-top: 30px;
    padding-top: 20px;
    padding-bottom: 10px;
    width: 100%;
    border-top: 5px solid lightgray;
    border-bottom: 1px solid lightgrey;
    background-color: #f8f8f8;
}
.title {
    position: absolute;
    bottom: 100%;
    left: 25px;
    padding: 0 8px;
    font-size: 1.5rem;
    line-height: 0.5;
    background-color: var(--rankarea-color);
    z-index: 1;
}
.more {
    position: absolute;
    bottom: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 50px;
    font-size: 1.5rem;
    color: white;
    background-color: gray;
    cursor: pointer;
    opacity: 0.1;
}
.more:hover {
    opacity: 0.5;
}
</style>