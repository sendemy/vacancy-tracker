import type { InterfaceUserDB, InterfaceVacancyDB } from '@/types/types'

const API_URL = 'http://127.0.0.1:5000'

export function getVacancy(id: number) {
	return fetch(`${API_URL}/vacancies/${id}`)
		.then((response) => {
			if (response.ok) {
				return response.json()
			}
			throw new Error('Incorrect URL.')
		})
		.then((data) => {
			return data
		})
		.catch((error) => {
			console.log(error)
		})
}

export function getUser(id: number) {
	return fetch(`${API_URL}/users/${id}`)
		.then((response) => {
			if (response.ok) {
				return response.json()
			}
			throw new Error('Incorrect URL.')
		})
		.then((data) => {
			return data
		})
		.catch((error) => {
			console.log(error)
		})
}

export function getUserBySub(sub: string) {
	return fetch(`${API_URL}/users-sub/${sub}`)
		.then((response) => {
			if (response.ok) {
				return response.json()
			}
			throw new Error('Incorrect URL.')
		})
		.then((data) => {
			return data
		})
		.catch((error) => {
			console.log(error)
		})
}

export function getVacancies() {
	return fetch(`${API_URL}/vacancies`)
		.then((response) => {
			if (response.ok) {
				return response.json()
			}
			throw new Error('Incorrect URL.')
		})
		.then((data) => {
			return data
		})
		.catch((error) => {
			console.log(error)
		})
}

export function getUsers() {
	return fetch(`${API_URL}/users`)
		.then((response) => {
			if (response.ok) {
				return response.json()
			}
			throw new Error('Incorrect URL.')
		})
		.then((data) => {
			return data
		})
		.catch((error) => {
			console.log(error)
		})
}

export function getUserVacancies(id: number) {
	return fetch(`${API_URL}/user-vacancies/${id}`)
		.then((response) => {
			if (response.ok) {
				return response.json()
			}
			throw new Error('Incorrect URL.')
		})
		.then((data) => {
			return data
		})
		.catch((error) => {
			console.log(error)
		})
}

export function createUser(data: InterfaceUserDB) {
	return fetch(`${API_URL}/create-user`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	})
}

export function createVacancy(data: InterfaceVacancyDB) {
	return fetch(`${API_URL}/create-vacancy`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json; charset="utf-8"',
		},
		body: JSON.stringify(data),
	})
}
