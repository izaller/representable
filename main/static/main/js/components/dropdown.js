function toggleAngle(e) {
  var collapsible = e.parentNode.getElementsByClassName('collapse')[0].id;
  $('#' + collapsible).collapse('toggle');
  if (e.innerHTML.includes("fa-angle-down")) {
    e.getElementsByClassName("dropdown-toggle-angle")[0].innerHTML = e.getElementsByClassName("dropdown-toggle-angle")[0].innerHTML.replace("fa-angle-down", "fa-angle-up");
  } else {
    e.getElementsByClassName("dropdown-toggle-angle")[0].innerHTML = e.getElementsByClassName("dropdown-toggle-angle")[0].innerHTML.replace("fa-angle-up", "fa-angle-down");
  }
}
