const renderGraph=()=>{
    const ctx = document.getElementById('dashboard');
    new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    }
  });
}

window.onload=(event)=>{
    renderGraph()
  }