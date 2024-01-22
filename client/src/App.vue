<script setup lang="ts">
import { ref, type Ref } from 'vue'
import './assets/main.css'
import Vacancy from './components/Vacancy.vue'

import Chart from './components/Chart.vue'
import InputForm from './components/InputForm.vue'
import NavBar from './components/NavBar.vue'
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
	<NavBar />
	<main>
		<div class="flex-1">
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
		</div>
		<div class="flex-2">
			<div class="charts-container">
				<Chart :vacanciesList="vacanciesList" />
			</div>
		</div>
	</main>
</template>

<style scoped lang="scss">
main {
	display: flex;
	flex-direction: row;
}

.flex-1 {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	text-align: center;
	flex: 0;
}

.flex-2 {
	display: flex;
	flex: 1;
}

.form-container {
	flex: 0;
}

.vacancies-container {
	flex: 1;
}

.charts-container {
	width: 100%;
	height: 100%;
}
</style>
