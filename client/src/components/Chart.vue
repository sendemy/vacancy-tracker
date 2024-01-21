<script setup lang="ts">
import { PieChart } from 'echarts/charts'
import {
	LegendComponent,
	TitleComponent,
	TooltipComponent,
} from 'echarts/components'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { provide, ref, watch } from 'vue'
import VChart, { THEME_KEY } from 'vue-echarts'

const { vacanciesList } = defineProps(['vacanciesList'])

// if (vacanciesList) {
// 	console.log('got the thing')
// 	console.log(vacanciesList)
// }

// const chartData = ref([
// 	{ value: 0, name: 'Accepted' },
// 	{ value: 0, name: 'Rejected' },
// 	{ value: 0, name: 'Waiting' },
// ])

watch([vacanciesList], () => {
	console.log('vacanciesList CHANGED')
	// console.log(vacanciesList)
	const tempData = [
		{ value: 0, name: 'Accepted' },
		{ value: 0, name: 'Rejected' },
		{ value: 0, name: 'Waiting' },
	]

	for (const vacancy of vacanciesList) {
		// switch (vacancy.status) {
		// 	case 'accepted':
		// 		tempData[0].value++
		// 		console.log(vacancy)
		// 	case 'rejected':
		// 		tempData[1].value++
		// 		console.log(vacancy)
		// 	case 'waiting':
		// 		tempData[2].value++
		// 		console.log(vacancy)
		// }
		if (vacancy.status === 'accepted') {
			tempData[0].value++
			console.log(vacancy)
		} else if (vacancy.status === 'rejected') {
			tempData[1].value++
			console.log(vacancy)
		} else if (vacancy.status === 'waiting') {
			tempData[2].value++
			console.log(vacancy)
		}
	}

	console.log('Temp data: ', tempData)

	option.value.series[0].data = tempData
})

use([
	CanvasRenderer,
	PieChart,
	TitleComponent,
	TooltipComponent,
	LegendComponent,
])

provide(THEME_KEY, 'light')

const option = ref({
	title: {
		text: 'Vacancies',
		left: 'center',
	},
	tooltip: {
		trigger: 'item',
		formatter: '{a} <br/>{b} : {c} ({d}%)',
	},
	legend: {
		orient: 'vertical',
		left: 'left',
		data: ['Accepted', 'Rejected', 'Waiting'],
	},
	series: [
		{
			name: 'Vacancies',
			type: 'pie',
			radius: '55%',
			center: ['50%', '60%'],
			data: [
				{ value: 0, name: 'Accepted' },
				{ value: 0, name: 'Rejected' },
				{ value: 0, name: 'Waiting' },
			],
			emphasis: {
				itemStyle: {
					shadowBlur: 10,
					shadowOffsetX: 0,
					shadowColor: 'rgba(0, 0, 0, 0.5)',
				},
			},
		},
	],
})
</script>

<template>
	<v-chart class="chart" :option="option" autoresize />
</template>

<style scoped lang="scss">
.chart {
	height: 50%;
}
</style>
