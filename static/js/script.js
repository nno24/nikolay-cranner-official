//Initialize mobile menu
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });

  //Initialize modals
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {});
  });

function openModal() {
  var instance = M.Modal.getInstance($('#basket-confirm'));
  instance.open();
}


 