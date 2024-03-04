<template>
    <nav class="navbar">
        <slot name="brand"></slot>
        <div id="nav-item" class="item">
            <button v-for="(item, i) in items" :key="i" type="button" class="btn"
                :class="item === activeItem ? 'active disabled' : ''" @click="this.$emit('change', item)">
                {{ item }}
            </button>
            <div id="activeNav"></div>
        </div>
        <slot name="dropDown"></slot>
    </nav>
</template>
<script>
export default {
    props: {
        items: {
            type: Object,
            default: () => ({}),
        },
        defaultItem: {
            default: () => "",
        },
    },
    data() {
        return {
            activeItem: this.defaultItem
        }
    },
    mounted() {
        navEvent()
    }
}
function navEvent() {
    const navItem = document.querySelector('#nav-item')
    const item = navItem.querySelectorAll('button')
    const activeNav = navItem.querySelector('#activeNav')
    const activated = navItem.querySelector('.active')

    // 導覽底線預設
    if (activated) {
        activeNav.style.width = activated.offsetWidth + 'px'
        activeNav.style.left = activated.offsetLeft + 'px'
    }
    activeNav.style.transition = 'all 0.5s'

    item.forEach(child => {
        child.addEventListener('click', (e) => {
            const activeItem = navItem.querySelector('.active')
            if (activeItem !== e.target) {
                // classList
                if (activeItem)
                    activeItem.classList.remove('active', 'disabled')
                e.target.classList.add('active', 'disabled')

                // 導覽底線切換
                activeNav.style.width = e.target.offsetWidth + 'px'
                activeNav.style.left = e.target.offsetLeft + 'px'
            }
        });
    });
}
</script>
<style scoped>
.navbar {
    justify-content: flex-start;
    align-items: flex-end;
    margin-bottom: 15px;
}

.item {
    position: relative;
    font-size: 0;
}
.item > button {
    position: relative;
    margin: 0;
    padding: 0rem 1rem;
    font-size: 1rem;
    color: var(--text-gray);
    background-color: transparent;
    border: none;
    transition: all 0.5s;
}
#activeNav {
    position: absolute;
    top: 100%;
    left: 0;
    width: 0;
    height: 1px;
    background-color: black;
}
</style>