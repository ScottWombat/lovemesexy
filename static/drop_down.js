$(document).ready(function() {
    $(".languages").click(function(){
        $(".languages ul").show();
      })
   $(".languages ul").mouseleave(function(){
     $(".languages ul").hide(); 
   });
    
   $(".languages li a").click(function(){
        $(".languages li a").removeClass('sel');
        $(this).addClass('sel');
        var selectedValue = $(this).text();
        var showLang = selectedValue;
        $('.languages .current').html(showLang);
        $('.languages .current').attr("title", selectedValue);
        $('.languages .hover').html(selectedValue);
      })
      
      
});