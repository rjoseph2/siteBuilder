(function () {

  $(window).scroll(function () {

    var top = $(document).scrollTop();
    if (top > 50)
      $('#home > .navbar').removeClass('navbar-transparent');
    else
      $('#home > .navbar').addClass('navbar-transparent');
  });
 
  $(window).resize(function () {
    //location.reload()
  });

  /*append the header menu start */
  var mainMenuCall = function () {
    if ($(".menu-item") != undefined && $(".menu-item").html() != undefined 
    && $(".menu-item").html().trim() != "" ) {
      $.ajax({
        url: $(".menu-item").html().trim(),
        success: function (result) {
          $(".menu-item").html(result);
        },
        error : function(result){
          $('.collapse').addClass("hidden");
      $('.collapse').css("display" , 'none')
        }
      });
    }else {
      $('.collapse').addClass("hidden");
      $('.collapse').css("display" , 'none')
    }

  }

  /*append the sub-menu/side menu menu ends */
  var subMenuCall = function () {
    if ($(".menu_place_holder") != undefined  && $(".menu_place_holder").html() != undefined
    && $(".menu_place_holder").html() != "") {
      $.ajax({
        url: $(".menu_place_holder").html().trim(),
        success: function (result) {
          $(".menu_place_holder").replaceWith(result);
          closeNavMenu();
          navarrowClick();
          var contentDiv = $(".content-div");
          contentDiv.removeClass('col-lg-12').addClass('col-lg-9');
          contentDiv.removeClass('col-sm-12').addClass('col-sm-11');
          contentDiv.addClass('offset-lg-3');
          contentDiv.addClass('offset-md-1');
          contentDiv.addClass('offset-sm-1');
          $(".nav-arrow").css("z-index",'1');
          var parentDiv = contentDiv.parent();
          parentDiv.parent().removeClass("container").addClass("container-fluid");
        },
        error: function(results) {
          adjustDisplayContentDiv();
        }
      });
    } else {
      adjustDisplayContentDiv();

    }

  }
  adjustDisplayContentDiv = function(){
    var contentDiv = $(".content-div");
      contentDiv.addClass('col-md-12');
      contentDiv.addClass('col-sm-12');
      contentDiv.css("max-width", "100%")
      contentDiv.css("width", "100%")
      contentDiv.removeClass('col-lg-9').addClass('col-lg-12');
      var parentDiv = contentDiv.parent();
      parentDiv.parent().removeClass("container-fluid").addClass("container");
  }; 

  $(document).ready(function () {
    mainMenuCall();
    subMenuCall();
  })

  $("a[href='#']").click(function (e) {
    e.preventDefault();
  });

  $(".nav-arrow").ready(function () {
    
  });

  $(".nav-arrow").ready(function () {
    closeNavMenu();
    navarrowClick();
  });   
  var closeNavMenu = function(){
    $(".navdiv  a").bind("click", function () {
      var link = $(".navdiv a").attr('href')
      $(".navdiv").fadeOut();
      
    });
  }
  var closeNav = function () {
    $(".navdiv").fadeOut();
  }
  var navarrowClick = function () {
    $(".nav-arrow").bind("click", function () {
      $(".navdiv").fadeIn();
    });
    
  }

})();
