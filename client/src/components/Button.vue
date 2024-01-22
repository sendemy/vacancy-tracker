<script setup lang="ts">
const { type, text, theme } = defineProps(['type', 'text', 'theme'])
</script>

<template>
	<button v-if="theme === 'light'" :type="type">{{ text }}</button>
	<button v-else-if="theme === 'dark'" :type="type">{{ text }}</button>
</template>
