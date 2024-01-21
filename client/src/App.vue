<script setup lang="ts">
import { ref, type Ref } from 'vue'
import './assets/main.css'
import Vacancy from './components/Vacancy.vue'

import Chart from './components/Chart.vue'
import InputForm from './components/InputForm.vue'
import type { InterfaceVacancy } from './types/types'

const vacanciesList: Ref<InterfaceVacancy[]> = ref([])

function getVacancy(vacancy: InterfaceVacancy) {
	vacanciesList.value.push(vacancy)
}

function getStatusChange(
	id: string,
	status: 'waiting' | 'accepted' | 'rejected'
) {
	const obj = vacanciesList.value.find((v: InterfaceVacancy) => v.id === id)

	if (obj) {
		obj.status = status
	}

	console.log(vacanciesList.value)
}
</script>

<template>
	<main>
		<div class="form-container">
			<InputForm @sendVacancy="getVacancy" />
		</div>
		<div class="vacancies-container">
			<h1>Vacancies</h1>
			<div class="vacancies-wrapper">
				<Vacancy
					v-for="(vacancy, index) in vacanciesList"
					@handleStatusChange="getStatusChange"
					:key="index"
					:vacancy="vacancy"
				/>
			</div>
		</div>
		<div class="charts-container">
			<Chart :vacanciesList="vacanciesList" />
		</div>
	</main>
</template>

<style scoped lang="scss">
main {
	display: grid;
	grid-gap: 1rem;
	grid-template-columns: 1fr 1fr;
	grid-template-rows: 20vh 80vh;
	grid-template-areas:
		'form charts'
		'vacancies charts';
}

.form-container {
	grid-area: form;
}

.vacancies-container {
	grid-area: vacancies;
}

.charts-container {
	grid-area: charts;
}
.vacancy-wrapper {
	margin-top: 0.6rem;
}
</style>
