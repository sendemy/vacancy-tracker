<script setup lang="ts">
import { type InterfaceResponse } from '@/types/types'
import Modal from './Modal.vue'

// const user: Ref<InterfaceUser | null> = ref(null)

const { user } = defineProps(['user'])

const emit = defineEmits(['sendUserData'])

function getUserData(userData: InterfaceResponse) {
	emit('sendUserData', userData)
}
</script>

<template>
	<header>
		<div class="logo-container">
			<svg
				width="32"
				height="37"
				viewBox="0 0 32 37"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<ellipse cx="16" cy="20.0362" rx="16" ry="16.4638" fill="#03071E" />
				<line
					x1="1.5"
					y1="-1.5"
					x2="29.9174"
					y2="-1.5"
					transform="matrix(0.330232 0.9439 -0.937729 0.347367 9.5 1)"
					stroke="#FDC500"
					stroke-width="3"
					stroke-linecap="round"
				/>
				<line
					x1="1.5"
					y1="-1.5"
					x2="23.4202"
					y2="-1.5"
					transform="matrix(-0.415885 0.909417 -0.900042 -0.435804 22.8643 9.23187)"
					stroke="#FDC500"
					stroke-width="3"
					stroke-linecap="round"
				/>
				<mask
					id="mask0_207_31"
					style="mask-type: alpha"
					maskUnits="userSpaceOnUse"
					x="0"
					y="3"
					width="32"
					height="34"
				>
					<ellipse cx="16" cy="20.0362" rx="16" ry="16.4638" fill="#03071E" />
				</mask>
				<g mask="url(#mask0_207_31)">
					<line
						x1="1.5"
						y1="-1.5"
						x2="29.293"
						y2="-1.5"
						transform="matrix(0.900042 0.435804 -0.415885 0.909417 -2.5 25.6956)"
						stroke="#FDC500"
						stroke-width="3"
						stroke-linecap="round"
					/>
				</g>
			</svg>
		</div>
		<div class="links-container">
			<div>vacancies</div>
			<div>analytics</div>
		</div>
		<div class="profile-container">
			<div v-if="user" class="profile-title">{{ user.given_name }}</div>
			<span v-if="user" class="profile-img">
				<img :src="user.picture" alt="User Picture" width="32" height="32" />
			</span>
			<div class="hover" v-else>
				<Modal @sendUserData="getUserData" />
			</div>
		</div>
	</header>
</template>

<style lang="scss" scoped>
header {
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: space-between;
	font-size: 1.2rem;
	border-bottom: 0.15rem solid #03071e;
	max-height: 4rem;
	// padding: 0.2rem 0;
}

.logo-container {
	align-items: center;
	// margin-left: 10%;
	margin-left: 0.5rem;
}

.links-container {
	display: flex;
	align-items: center;
	flex-shrink: 0;
	flex-direction: row;
	gap: 1.25rem;

	&:hover {
		cursor: pointer;
	}

	div {
		transition: 0.4s all ease-out;

		&:hover {
			color: #3d0066;
		}
	}
}

.profile-container {
	display: flex;
	flex-direction: row;
	height: 2rem;
	transition: 0.4s all ease-out;

	&:hover {
		color: #3d0066;
	}

	// margin-right: 10%;
	margin-right: 0.5rem;
}

.profile-title {
	margin-right: 0.5rem;
	line-height: 2rem;
}
.profile-img {
	& > img {
		display: block;
		border-radius: 1000rem;
	}
}

.hover {
	cursor: pointer;
}
</style>
