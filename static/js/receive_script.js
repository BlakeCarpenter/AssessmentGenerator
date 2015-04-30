//Question Object

edisco_receiveArray = [];

function QuestionReceive(question_id, question_text, question_type, question_body, link){
    this.question_id = question_id;
    this.question_text = question_text;
    this.question_type = question_type;
    this.question_body = question_body;
    this.receive_link = link;
}

QuestionReceive.prototype = {
    getQuestionText: function(){
        return this.question_text;
    },

    getQuestionType: function(){
        return this.question_type;
    },

    getQuestionBody: function(){
        return this.question_body;
    },

    setReceive: function(link){
        this.receive_link = link;
    },

    /*addToTest: function(destination_block){
      switch(question_type){
      case M:

      default:
      }
      },*/
};

$(document).ready(function(){
    edisco_test_send_array = [];

    $.each(edisco_receiveArray, function(i,v){
        v.receive_link.click(function(){
            var string = "";
            switch($(this).data("q_object").question_type){
                case 'M':
                    string += "<li class=\"gui_question\"><p>"+$(this).data("q_object").question_text+"</p><ol class=\"answer-list\">";
                    $.each($(this).data("q_object").question_body.choices,function(i,v){
                        if(v.correct) string += "<li class=\"answer-correct\">";
                        else string += "<li>";
                        string += v.choice + "</li>";
                    });
                    string += "</ul></li>";
                    break;
                default:
                    console.log("There was an error with the question type.");
                    break;
            }
            edisco_test_send_array.push($(this).data("q_object").question_id);
            $(".test_gui_block").append(string);
        });
    });
});
