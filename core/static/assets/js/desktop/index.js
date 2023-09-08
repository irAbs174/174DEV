/* function ready 
index.js for desktop VS-Tech
developer : ABS174
see more : https://vs-web.space
*/
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