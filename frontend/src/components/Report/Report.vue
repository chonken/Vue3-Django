<template>
    <div class="mx-3 mx-xl-5 pt-3 text-center">
        <div class="report text-start">
            <div class="clip">
                <slot name="title"></slot>
            </div>
            <div class="paper">
                <slot name="content"></slot>
            </div>
        </div>
    </div>
</template>
<script>
export default {

}
</script>
<style>
.report {
    display: inline-block;
    position: relative;
    border-radius: 0.75rem;
    margin-top: 3rem;
    margin-bottom: 3rem;
    padding: 0 1rem 1rem 1rem;
    vertical-align: bottom;
    box-shadow: 0 20px 30px 0 rgba(0, 0, 0, 0.1);
    background-color: var(--report-content-color);
}
.report .clip {
    position: relative;
    top: -1.5rem;
    left: 5%;
    width: 90%;
    padding: 1rem;
    color: white;
    background: linear-gradient(15deg, var(--report-title-color-1), var(--report-title-color-2));
    border-radius: 1rem;
    text-align: center;
}
.report .clip > * {
    margin: 0;
}
.report .paper {
    display: inline-block;
    padding: 1rem;
    vertical-align: bottom;
    border: 3.5px dashed lightgray;
    border-radius: 1rem;
    overflow-x: auto;
}
</style>