$.each(edisco_receiveArray, function(i,v){
    v.receive_link.click(function(){
        var string = "";
        switch($(this).data("q_object").question_type){
            case 'M':
                string += "<div class=\"gui_question\"><p>"+$(this).data("q_object").question_text+"</p><ol class=\"answer-list\">";
                $.each($(this).data("q_object").question_body.choices,function(i,v){
                    if(v.correct) string += "<li class=\"answer-correct\">";
                    else string += "<li>";
                    string += v.choice + "</li>";
                });
                string += "</ul></div>";
                break;
            default:
                console.log("There was an error with the question type.");
                break;
        }
        //$(".test_gui_block").append($(this).data("q_object").question_text);
        $(".test_gui_block").append(string);
    });
});
