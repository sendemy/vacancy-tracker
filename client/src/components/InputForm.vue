<script setup lang="ts">
import type { InterfaceVacancy } from '@/types/types'
import { ref, watch, type Ref } from 'vue'

const vacancyId: Ref<string | null> = ref('')

const emit = defineEmits(['sendVacancy'])

function getVacancyId(url: string) {
	const pattern = /vacancy\/(\d+)/
	const match = url.match(pattern)
	if (match) {
		return match[1]
	} else {
		return null
	}
}

function handleSubmit(e: Event) {
	e.preventDefault()

	const target = e.target as HTMLFormElement
	const inputElement = target[0] as HTMLInputElement

	if (inputElement) {
		vacancyId.value = getVacancyId(inputElement.value)
		inputElement.value = ''
	}
}

watch([vacancyId], () => {
	fetch(`https://api.hh.ru/vacancies/${vacancyId.value}`)
		.then((response) => {
			if (response.ok) {
				return response.json()
			}
			throw new Error('Incorrect URL.')
		})
		.then((data: InterfaceVacancy) => {
			const vacancy = data
			vacancy.added_at = new Date()
			vacancy.status = 'waiting'

			emit('sendVacancy', vacancy)
		})
		.catch((error) => {
			console.log(error)
		})
})
</script>

<template>
	<form @submit="(e) => handleSubmit(e)">
		<label>
			Enter a vacancy URL
			<input type="text" name="vacancyIdInpuy" />
		</label>
		<button type="submit">Submit</button>
	</form>
</template>
