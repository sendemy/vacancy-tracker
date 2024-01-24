<script setup lang="ts">
import { type InterfaceResponse } from '@/types/types'
import { ref, type Ref } from 'vue'
import { decodeCredential } from 'vue3-google-login'

const emit = defineEmits(['sendUserData'])
const showModal: Ref<boolean> = ref(false)

function callback(response: InterfaceResponse) {
	if (response.credential) {
		toggleModal()
	}
	emit('sendUserData', decodeCredential(response.credential))
}

function toggleModal() {
	showModal.value = !showModal.value
}
</script>

<template>
	<div v-if="showModal" class="modal-container">
		<div>
			<h2>Sign up with:</h2>
			<div>
				<GoogleLogin :callback="callback" />
			</div>
			<button @click="toggleModal()">Close</button>
		</div>
	</div>
	<div @click="toggleModal()">Sing up</div>
</template>

<style scoped lang="scss">
.modal-container {
	position: absolute;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);
	background-color: rgb(145, 145, 224);
	padding: 2rem;
	border-radius: 0.25rem;
}
</style>
