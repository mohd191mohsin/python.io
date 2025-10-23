
  fetch('../sidebar.html')
    .then(response => response.text())
    .then(data => {
      document.getElementById('sidebar-placeholder').innerHTML = data;
    })
    .catch(err => console.error('Error loading sidebar:', err));