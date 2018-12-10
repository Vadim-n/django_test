<template>
    <div>
        {{ msg }}
        <router-link to="/">Hello</router-link>
    </div>
</template>

<script>
export default {
    name: 'Test',
    data() {
        return {
            msg: 'This is a test page'
        }
    }
}
</script>
