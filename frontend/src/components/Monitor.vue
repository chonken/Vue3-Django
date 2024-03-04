<template>
    <div class="mx-5 pt-3">
        <div class="monitor">
            <div class="screen">
                <slot name="screen"></slot>
            </div>
            <div class="model">
                <slot name="model"></slot>
            </div>
        </div>
    </div>
</template>
<script>
export default {

}
</script>
<style scoped>
.monitor {
    position: relative;
    margin-top: 1.5rem;
    aspect-ratio: 16/9;
    max-width: 100%;
    max-height: calc(100vh - 5rem - 15px);
    min-width: 675px;
    box-shadow: 20px 20px 30px 0 rgba(0, 0, 0, 0.4);
    border-radius: 0.25rem 0.25rem 0 0;
}
.monitor .screen {
    width: 100%;
    height: 100%;
    padding: 0.5rem;
    overflow-x: auto;
    background-color: var(--monitor-content-color);
    border: 0.3rem solid var(--monitor-border-color);
    border-bottom: none;
    border-radius: 0.5rem 0.5rem 0 0;
}
.model {
    position: absolute;
    top: 100%;
    left: 0;
    padding: 2px 0;
    width: 100%;
    min-height: 15px;
    color: white;
    text-align: center;
    background-color: var(--monitor-title-color);
    box-shadow: 20px 20px 30px 0 rgba(0, 0, 0, 0.4);
    border-radius: 0 0 0.25rem 0.25rem;
}
.model > * {
    margin: 0;
    vertical-align: middle;
}
</style>