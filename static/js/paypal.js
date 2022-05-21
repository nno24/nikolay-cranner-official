//Paypal API integration ------------------------------------
const payPalButtons = paypal.Buttons({

    style: {
      color: "gold",
      shape: "rect",
      layout: "vertical"
    },
  
  //On Initializastion 
  onInit: (data, actions) => {
    try {
      let grand_total = document.getElementById('grand-total').textContent;
      let user_id = document.getElementById('user_id').textContent;
      let order_id = document.getElementById('order_id').textContent;
      let order_items = document.getElementById('order_items').textContent;
    
      document.getElementById('id_order_id').setAttribute('value', order_id );
      document.getElementById('id_order_items').setAttribute('value', order_items );
      document.getElementById('id_user_id').setAttribute('value', user_id );
      document.getElementById('id_grand_total').setAttribute('value', grand_total );
      actions.enable();
      console.log("updated form fields, and enabled paypal buttons");
    }
  
    catch (error) {
      console.log("No items in bag: " + error);
      console.log("Disabling paypal payment button");
      actions.disable();
    }
  
    finally {
      console.log("No action needed")
    }
  
  },
  
  // Set up the transaction -- making sure to get user_id and grand_total again, in case it was not set before
  //createOrder method was called -- this was an issue earlier.
  createOrder: function(data, actions) {
    const createOrderPayload = {
        purchase_units: [{
        reference_id: document.getElementById('user_id').textContent,
        amount: {
           
            value: document.getElementById('grand-total').textContent
        },
      }]
    }
    console.log('The order payload is: ' + JSON.stringify(createOrderPayload, null, 4));
    return actions.order.create(createOrderPayload);
  },
  //If order is cancelled
  onCancel: (data) => {
    alert('Payment Cancelled');
  },
  // Finalize the transaction
  onApprove: (data, actions) => {
      const captureOrderHandler = (details) => {
          const payerName = details.payer.name.given_name;
          console.log('Transaction completed for: ' + payerName);
          console.log('The details: ' + JSON.stringify(details, null, 4));
          let transaction_date = document.getElementById('transaction_date').textContent;
          let transaction_time = document.getElementById('transaction_time').textContent;
          document.getElementById('id_transaction_date').setAttribute('value', transaction_date );
          document.getElementById('id_transaction_time').setAttribute('value', transaction_time );              
          document.getElementById('order-form').submit();
      };
      return actions.order.capture().then(captureOrderHandler);
  
    },
  
    // handle unrecoverable errors
    onError: (err) => {
        console.error('An error prevented the buyer from checking out with PayPal');
        location.href = '/store/payment_failed/'
    }
    });
  
    //Render the paypal button
    payPalButtons
      .render("#paypal-button-container")
      .catch((err) => {
        console.error('PayPal Buttons failed to render');
      });