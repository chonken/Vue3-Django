<template>
    <aside>
        <SidebarHeader>回首頁</SidebarHeader>
        <SidebarBody :sidebarTitle="sidebarTitle" :defaultId="defaultId" @active="(id) => this.$emit('active', id)">
        </SidebarBody>
        <SidebarFooter />
    </aside>
</template>

<script>
import SidebarHeader from './SidebarHeader.vue'
import SidebarBody from './SidebarBody.vue'
import SidebarFooter from './SidebarFooter.vue'
export default {
    components: {
        SidebarHeader,
        SidebarBody,
        SidebarFooter,
    },
    props: {
        sidebarTitle: {
            type: Object,
            default: () => ({}),
        },
        defaultId: {
            default: () => ""
        },
    },
}
</script>

<style>
aside {
    display: flex;
    flex-direction: column;
    position: fixed;
    padding: 1rem 0 1em 1rem;
    height: 100vh;
}
</style>