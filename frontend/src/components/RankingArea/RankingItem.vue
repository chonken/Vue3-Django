<template>
    <div class="inline-block">
        <div class="item">
            <div class="pic"></div>
            <span class="title">
                <slot name="title"></slot>
            </span>
            <span class="content">
                <slot name="content"></slot>
            </span>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        url: {
            type: String,
            default: () => "",
        }
    }
}
</script>

<style scoped>
.inline-block{
    display: inline-block;
}
.item {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 10px;
}
.pic {
    height: 120px;
    width: 150px;
    min-width: 150px;
    border: 1.5px solid black;
}
.title {
    max-width: 150px;
    font-size: 1.25rem;
    text-wrap: nowrap;
    overflow-x: hidden;
    text-overflow: ellipsis;
}
.content {
    max-width: 150px;
    text-wrap: nowrap;
    overflow-x: hidden;
    text-overflow: ellipsis;
}
</style>