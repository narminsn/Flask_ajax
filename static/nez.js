var l=[]
data_list=[]

var countt=0
function create_card(img,title,cast,genre,countt){
    return "<div class=\"col-md-4\"><div class=\"card\" style=\"width: 330px;\"><img class=\"card-img-top\" alt=\""+ countt+"\" src=\""+ img +"\" alt=\"Card image cap\"><div class=\"card-body\"><h5 class=\"card-title\">"+title+"</h5><p class=\"card-text\"><strong class=\"card_strong\">Cast:</strong> <span class=\"card_span\" > "+ cast +"</span> <br> <strong class=\"card_strong\"> Genre:</strong> <span class=\"card_span\"> "+ genre +" </span> </p></div></div></div>";  
}
function create_div(img,title,genres,about){
    return "<div class=\"col-md-12\"><div class=\"col-md-6 img\" style=\"width: 400px;margin-top: 83px;\"> <img src=\""+ img +"\" alt=\"\"></div><div class=\"col-md-6 text\" style=\"margin-top: 83px !important; color: #0c0c0c;\"><p><h1>"+ title +"<h4>("+ genres +")</h4></h1><strong>"+ about +"</strong></p></div></div>"
}
for(var i=0;i<3;i++){
    var random_num=Math.ceil( Math.random() * (11 +1) -1);
    l.push(random_num)
}
// console.log(l)
$(document).ready(function(){
        $.ajax({
                    url: "https://fake.munisisazade.com/v1/5cd96f70fd1d61e440b4d2fa",
                    method: "GET",
                    contentType: "application/json",
                    success: function(data){
                      data_list=data
                      
                    console.log(data_list)
                       
                    },
                    error: function(xhr, err, msg){
                        console.log(xhr, err, msg);
                    }

                
               });
            
           
            
});
  