//Initialize mobile menu
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });

  //Initialize modals
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {'dismissible': true, 'opacity': 0.65});
  });


 
 document.addEventListener('DOMContentLoaded' && 'submit', function openModal() {
    var instance = M.Modal.getInstance($('#add-to-basket'));
    instance.open();
});

//Auto fill hidden form for submitting order to database...
document.addEventListener('DOMContentLoaded', function autoFillOrderForm() {
  document.getElementById('id_order_id').setAttribute('value', order_id );
  document.getElementById('id_user_id').setAttribute('value', user_id );
  document.getElementById('id_grand_total').setAttribute('value', grand_total );
  console.log("updating form fields");
});

    

 