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
        $('.languages .current .lang').html(showLang);
        $('.languages .current').attr("title", selectedValue);
        $('.languages .hover').html(selectedValue);
        $('.img_id').attr('src','https://s3-us-west-2.amazonaws.com/s.cdpn.io/19554/flag-icon-us.gif');
      }) 
      
      
});