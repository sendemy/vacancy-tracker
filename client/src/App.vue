<script setup lang="ts">
import { ref, watch, type Ref } from 'vue'
import './assets/main.css'
import Chart from './components/Chart.vue'
import InputForm from './components/InputForm.vue'
import NavBar from './components/NavBar.vue'
import Vacancy from './components/Vacancy.vue'
import { createUser, getUserBySub, getUserVacancies } from './requests'
import type { InterfaceUser, InterfaceVacancy } from './types/types'

const vacanciesList: Ref<InterfaceVacancy[]> = ref([])
const user: Ref<InterfaceUser | null | any> = ref(null)

function getVacancyData(vacancy: InterfaceVacancy) {
	vacanciesList.value.push(vacancy)
}

async function getUserData(userData: InterfaceUser) {
	user.value = userData

	const isCreated = await getUserBySub(userData.sub)
	console.log(isCreated)

	if (!isCreated.sub) {
		createUser({
			name: userData.given_name,
			email: userData.email,
			sub: userData.sub,
			image: userData.picture,
		})
	} else {
		user.value = await getUserBySub(isCreated.sub)
		// vacanciesList.value = await getUserVacancies(user.value.id)
	}
}

function getStatusChange(
	id: string,
	status: 'waiting' | 'accepted' | 'rejected'
) {
	// const obj = vacanciesList.value.find((v: InterfaceVacancy) => v.id === id)

	// if (obj) {
	// 	obj.status = status
	// }

	vacanciesList.value.find((v: InterfaceVacancy) => v.id === id)!.status =
		status

	console.log(vacanciesList.value)
}

watch([vacanciesList], () => {
	console.log('vacancies change in APP.VUE')
})

watch([user], async () => {
	vacanciesList.value = await getUserVacancies(user.value.id)
})
</script>

<template>
	<NavBar :user="user" @sendUserData="getUserData" />
	<main>
		<div class="flex-1">
			<div class="form-container">
				<InputForm :user="user" @sendVacancyData="getVacancyData" />
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
