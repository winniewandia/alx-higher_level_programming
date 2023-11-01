$(document).ready(function () {
  $('#btn_translate').click(function () {
    translate();
  });
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });
});
function translate () {
  const langCode = $('#language_code').val();
  $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (data, status) {
    $('#hello').text(data.hello);
  });
}
