$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (data, status) {
      $('#hello').text(data.hello);
    });
  });
});
