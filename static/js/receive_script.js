//Question Object

edisco_receiveArray = [];

function QuestionReceive(question_id, question_text, question_type, question_body){
    this.question_id = question_id;
    this.question_text = question_text;
    this.question_type = question_type;
    this.question_body = question_body;
    this.receive_link = null;
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

    addToTest: function(){

    },
};

$(document).ready(function(){
    
});
