<script setup lang="ts">
import { createVacancy } from '@/requests'
import type { InterfaceVacancy } from '@/types/types'
import { ref, toRefs, watch, type Ref } from 'vue'

const vacancyId: Ref<string | null> = ref(null)

const props = defineProps(['user'])

const { user } = toRefs(props)

const emit = defineEmits(['sendVacancyData'])

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

watch([vacancyId, user], () => {
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

			emit('sendVacancyData', vacancy)

			if (vacancyId && user) {
				console.log('in the scope', user.value)
				createVacancy({
					text: vacancy.description,
					user_id: 4,
				})
			}
		})
		.catch((error) => {
			console.log(error)
		})
})

function createUser(e: Event) {
	e.preventDefault()

	const target = e.target as HTMLFormElement
	const inputElement1 = target[0] as HTMLInputElement
	const inputElement2 = target[1] as HTMLInputElement

	let text = ''
	let user_id = 0

	if (inputElement1 && inputElement2) {
		text = inputElement1.value
		user_id = parseInt(inputElement2.value)
		inputElement1.value = ''
		inputElement2.value = ''
	}

	fetch('http://127.0.0.1:5000/create-vacancy', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({
			text: text,
			user_id: user_id,
		}),
	})
}
</script>

<template>
	<div>
		<form @submit="(e) => handleSubmit(e)">
			<label for="vacancyId">Enter a vacancy URL</label>
			<input type="text" name="vacancyId" />
			<button type="submit">Submit</button>
		</form>
		<form @submit="(e) => createUser(e)">
			<input type="text" />
			<input type="text" />
			<button type="submit">Submit</button>
		</form>
	</div>
</template>

<style scoped lang="scss">
div {
	border: 2px solid black;
	display: flex;
	padding: 1rem;
	background-color: aquamarine;
	border-radius: 0.5rem;
}

form {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	gap: 1rem;
}

button {
	width: fit-content;
}
</style>
