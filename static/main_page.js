let xhr = new XMLHttpRequest()

xhr.onload = () => {
  let wins = 0, loses = 0;
  console.log(xhr.response.type())
  for (let i in xhr.response) {
    if (i.win == 'win') {
      wins++;
    } else {
      loses++;
    }
  }
  console.log(loses);
  var options = {
    plotOptions: {
      pie: {
        customScale: 0.7
      }
    },
    series: [wins, loses],
      chart: {
      type: 'donut',
    },
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom',
        }
      }
    }]
  };
  
  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();
}

xhr.open('GET', '/get_articles')
xhr.setRequestHeader('Content-Type', 'application/json')
xhr.send();
