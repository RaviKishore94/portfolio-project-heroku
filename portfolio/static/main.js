$('#myModal').on('show.bs.modal', function (event) {
  var image = $(event.relatedTarget)
  var url = image.data('whatever')
  var modal = $(this)
  modal.find('.modal-body #achievementImage').attr("src", url)
})

$(document).ready(function(){
  $("a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top,
      }, 500);
    }
  });
});

!function(t){"use strict";t('a.js-scroll-trigger[href="#"]:not([href*="#"])').click(function(){if(location.pathname.replace(/^\//,"")==this.pathname.replace(/^\//,"")&&location.hostname==this.hostname){var e=t(this.hash);if((e=e.length?e:t("[name="+this.hash.slice(1)+"]")).length)return t("html, body").animate({scrollTop:e.offset().top},1e3,"easeInOutExpo"),!1}}),t(".js-scroll-trigger").click(function(){t(".navbar-collapse").collapse("hide")}),t("body").scrollspy({target:"#SubNav"})}(jQuery);
