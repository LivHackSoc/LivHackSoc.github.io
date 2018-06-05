// Get the current year
const currYear = (new Date()).getFullYear();

// Apply the year to the div
const updateFooterYear = (year) => {
  document.getElementById('year').innerHTML = year;
}

updateFooterYear(currYear);
