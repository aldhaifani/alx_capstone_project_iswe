/*-------
  main 
-------*/

const dash_cash_chart = document.getElementById('dash_cash_chart');

new Chart(dash_cash_chart, {
	type: 'line',
	data: {
		labels: [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
		datasets: [
			{
				label: "Cash in bank in 1000's (k)",
				data: [200, 370, 560, 700, 890, 773],
				fill: true,
				backgroundColor: 'rgba(255, 255, 255, 0.3)',
				borderColor: 'rgb(255, 255, 255)',
				tension: 0.3,
			},
		],
	},
	options: {
		responsive: false,
	},
});

const dash_liability_chart = document.getElementById('dash_liability_chart');

new Chart(dash_liability_chart, {
	type: 'pie',
	data: {
		labels: ['Current', 'Non-Current'],
		datasets: [
			{
				label: '$ in M',
				data: [current_liability_value, non_current_liability_value],
				backgroundColor: ['#A7ED36', '#ED8936'],
				hoverOffset: 5,
			},
		],
	},
	options: {
		responsive: false,
	},
});
