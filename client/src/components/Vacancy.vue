<script setup lang="ts">
import { ref } from 'vue'

const { vacancy } = defineProps(['vacancy'])
const emit = defineEmits(['handleStatusChange'])

const bgColor = ref('')

// function handleStatusChange(value: 'bg-red' | 'bg-green' | null) {
// 	if (value) {
// 		bgColor.value = value
// 	}
// }
</script>

<template>
	<div class="vacancy-container" :class="bgColor">
		<div class="vacancy-name">{{ vacancy.name }}</div>
		<div class="vacancy-salary-container" v-if="vacancy.salary">
			<span v-if="vacancy.salary.from && vacancy.salary.to">
				{{ vacancy.salary.from }} - {{ vacancy.salary.to }}
				{{ vacancy.salary.currency }}
			</span>
			<span v-else-if="vacancy.salary.from">
				От {{ vacancy.salary.from }} {{ vacancy.salary.currency }}
			</span>
			<span v-else-if="vacancy.salary.to">
				До {{ vacancy.salary.to }} {{ vacancy.salary.currency }}
			</span>
		</div>
		<div class="vacancy-salary-container" v-else>Зарплата не указана</div>
		<div class="vacancy-date-added">
			Добавлено: {{ vacancy.added_at.toLocaleString() }}
		</div>
		<div class="vacancy-buttons-container">
			<button @click="emit('handleStatusChange', vacancy.id, 'accepted')">
				Accepted
			</button>
			<button @click="emit('handleStatusChange', vacancy.id, 'rejected')">
				Rejected
			</button>
			<button @click="emit('handleStatusChange', vacancy.id, 'waiting')">
				Waiting
			</button>
		</div>
	</div>
</template>

<style scoped lang="scss">
.bg-red {
	background-color: red;
}
.bg-green {
	background-color: green;
}
</style>
