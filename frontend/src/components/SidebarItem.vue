<template>
    <div class="item" :class="{ active: isActive }" @click="this.$emit('active')">
        <slot></slot>
    </div>
</template>

<script>
export default {
    props: {
        isActive: {
            type: Boolean,
            default: false,
        },
    },
};
</script>

<style scoped>
.item {
    padding: 1rem 2rem;
    user-select: none;
    transition: all 0.5s;
}
.item:hover {
    color: var(--text-light);
    transform: scale(1.15);
    cursor: pointer;
    background-color: var(--secondary-color);
}
.item:active {
    color: var(--text-light);
    transform: scale(1);
    background-color: var(--secondary-color);
    transition-duration: 0.1s;
}
.active {
    color: var(--text-light);
    transform: scale(1.15);
    background-color: var(--secondary-color);
}
</style>