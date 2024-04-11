<template>
    <div class="loading">
        <span style="font-size: 125%;">L</span>
        <span>o</span>
        <span>a</span>
        <span>d</span>
        <span>i</span>
        <span>n</span>
        <span>g</span>
        <span>.</span>
        <span>.</span>
        <span>.</span>
    </div>
</template>
<script>
export default {

}
</script>
<style scoped>
@keyframes pulsate {
    0% {
        transform: translateY(0);
    }
    8% {
        transform: translateY(-0.8vw);
    }
    25% {
        transform: translateY(0);
    }
}
.loading {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    font-size: 3vw;
}
.loading span {
    display: inline-block;
    animation: pulsate 2.5s infinite;
    /* 設定動畫，持續時間 2 秒，無限循環 */
}

.loading span:nth-child(1) {
    animation-delay: 0s;
}
.loading span:nth-child(2) {
    animation-delay: 0.2s;
}
.loading span:nth-child(3) {
    animation-delay: 0.4s;
}
.loading span:nth-child(4) {
    animation-delay: 0.6s;
}
.loading span:nth-child(5) {
    animation-delay: .8s;
}
.loading span:nth-child(6) {
    animation-delay: 1s;
}
.loading span:nth-child(7) {
    animation-delay: 1.2s;
}
.loading span:nth-child(8) {
    animation-delay: 1.4s;
}
.loading span:nth-child(9) {
    animation-delay: 1.6s;
}
.loading span:nth-child(10) {
    animation-delay: 1.8s;
}
</style>