<template>
    <div class="sidebar-body">
        <SidebarItem v-for="(title, i) in sidebarTitle" :key="i" :isActive="activeId === title.id"
            @active="itemClick(title.id)">{{ title.name }}</SidebarItem>
    </div>
</template>

<script>
import SidebarItem from './SidebarItem.vue'
export default {
    components: {
        SidebarItem,
    },
    props: {
        sidebarTitle: {
            type: Object,
            default: () => ({}),
        },
        defaultId: {
            default: () => "",
        },
    },
    data() {
        return {
            activeId: this.defaultId,
        }
    },
    methods: {
        itemClick(id) {
            this.activeId = id
            this.$emit("active", id)
        }
    }
}
</script>

<style scoped>
.sidebar-body {
    height: 100%;
}
</style>