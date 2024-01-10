/* function ready 
index.js for desktop VS-Tech
developer : ABS174
see more : https://vs-web.space
*/
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('newsletter').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the default form submission
    let lang = $(".LANGUAGE_CODE").val();
    let email = $(".email").val();
    $.ajax({
      url : '/desk/newsletter',
      type : 'POST',
      data : {
        'email': email,
        'lang': lang,
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

  });
});

let currentPath = window.location.pathname;
let slug = currentPath.split('/').filter(Boolean).pop();
$(document).ready(function() {
  $.ajax({
    url : '/desk/set_content_index',
    type : 'POST',
    data : {
        'code': 'en',
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
          console.log("NOTING !");
        }
      },
});//End ajax
});//end ready
// => set_en
$(".set_en").click(function() {
  console.log(slug);
  $.ajax({
    url : '/desk/set_language',
    type : 'POST',
    data : {
        'code': 'en',
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
          window.location.href = `/${response.status}`;
        }
      },
});//End ajax
});// end set_en
// => set_fa
$(".set_fa").click(function() {
  $.ajax({
    url : '/desk/set_language',
    type : 'POST',
    data : {
        'code': 'fa',
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
          window.location.href = `/${response.status}`;
        }
      },
});//End ajax
});// end set_fa
// => set_ar
$(".set_ar").click(function() {
  $.ajax({
    url : '/desk/set_language',
    type : 'POST',
    data : {
        'code': 'ar',
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
          window.location.href = `/${response.status}`;
        }
      },
});//End ajax
});// end set_ar