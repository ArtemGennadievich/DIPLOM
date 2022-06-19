var $popUp = $('#popup');
  var $popOverlay = $('.pop-overlay');
  var $popWindow = $('#popup-window');
  var $popClose = $('.popup-window .btn-close');
  var $popClose2 = $('input_submit_close');

  $popUp.on('click', function(){
    $popOverlay.fadeIn();
    $popWindow.fadeIn();
  });

  $popClose.on('click', function(){
    $popOverlay.fadeOut();
    $popWindow.fadeOut();
  });
    $popClose2.on('click', function(){
    $popOverlay.fadeOut();
    $popWindow.fadeOut();
  });

  $(function(){
    $(document).on('click', function(event) {
      if ($(event.target).closest($popUp).length) return;
      if ($(event.target).closest($popWindow).length) return;
      $popOverlay.fadeOut();
      $popWindow.fadeOut();
      event.stopPropagation();
    });
  });
