/* function ready 
index.js for desktop VS-Tech
developer : ABS174
see more : https://vs-web.space
*/
$(document).ready(function() {
    $.ajax({
        url : '/desk/set_language',
        type : 'POST',
        data : {
            'hi': 'success',
        },
        success: function(response) {
            if (response.success === false) {
              Swal.fire({
                icon: "error",
                title: response.status,
                showConfirmButton: false,
                timer: 3000,
              });
            } else {
              Swal.fire({
                icon: "success",
                title: response.status,
                showConfirmButton: false,
                timer: 2000,
              });
              // -> if success !!!
            }
          },
          error: function(xhr, status, error) {
            console.log(status);
            Swal.fire({
              icon: "error",
              title: status,
              showConfirmButton: false,
              timer: 3000,
            });
          }
    });//End ajax
});//end ready