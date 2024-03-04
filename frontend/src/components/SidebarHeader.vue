<template>
    <div class="sidebar-header">
        <a href="#">
            <slot></slot>
        </a>
    </div>
</template>

<script>
export default {
}
</script>

<style>
.sidebar-header {
    padding: 1rem;
    font-size: 1.5rem;
    text-align: center;
}
.sidebar-header > * {
    color: var(--text-dark);
    text-decoration: none;
}
</style>