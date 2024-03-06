<template>
    <button>
        <slot></slot>
    </button>
</template>
<script>
export default {
}
</script>
<style scoped>
button {
    color: var(--text-light);
    background: linear-gradient(15deg, var(--report-title-color-1), var(--report-title-color-2));
    border: 0;
}
button:hover {
    color: var(--text-light);
    box-shadow: 0 14px 26px -12px rgba(123, 128, 154, 0.4), 0 4px 23px 0 rgba(123, 128, 154, 0.15), 0 8px 10px -5px rgba(123, 128, 154, 0.2);
}
button:active {
    transform: scale(0.95);
    box-shadow: none !important;
}
button:focus {
    box-shadow: none;
}
button:focus:hover {
    box-shadow: 0 14px 26px -12px rgba(123, 128, 154, 0.4), 0 4px 23px 0 rgba(123, 128, 154, 0.15), 0 8px 10px -5px rgba(123, 128, 154, 0.2);
}
</style>