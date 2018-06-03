function updateFooterYear(year) {
  const footer = document.querySelector("#footer-copyright");
  footer.innerHTML = `©University of Liverpool HackSoc ${year}. All rights reserved.`;
}

const currYear = (new Date()).getFullYear();
updateFooterYear(currYear);
