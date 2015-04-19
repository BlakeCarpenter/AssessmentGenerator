$(document).ready(function(){

    //Object Classes
    function QuestionContext(){
        var state;
    }

    function MultipleChoiceState(){
        var numQuestions = 4;

        this.setup = function(){
            $("#question_instructions").html("Enter the question in the question block, and up to six selections in the fields below. Indicate with the selector which answer is correct.");
            var build = "<form id=\"quest_form\"><table class=\"question-form multiple-choice-form\">";
            for(var i=1;i<=numQuestions;i++){
                build += "<tr><td><label for=\"mcChoice"+i+"\">Choice "+i+"</label></td><td><input id=\"mcChoice"+i+"\" type=\"text\"></td><td><input type=\"radio\" name=\"correct_answer\" value=\""+i+"\"></tr>";
            }
            build += "</table></form>";
            build += "<div><td><input type=\"checkbox\" name=\"order\" value=\"order\">Order Dependant</input></td><td><input type=\"checkbox\" name=\"all\" value=\"all\">All of the Above</input></td></div>";
            build += "<button id=\"addField\">Add a Choice</button>";
            build += "<button id=\"question_submit\">Add Question</button>";
            $("#question_form").html(build);

            //Add action listener to new button
            $("#addField").click(function(){
                edisco_context.state.addField();
            });
            $("#question_submit").click(function(){
                edisco_context.state.addQuestion();
            });
        }

        this.addField = function(){
            if(numQuestions<6){
                numQuestions++;
                $("#question_form table").append("<tr><td><label for=\"mcChoice"+numQuestions+"\">Choice "+numQuestions+"</label></td><td><input id=\"mcChoice"+numQuestions+"\" type=\"text\"></td><td><input type=\"radio\" name=\"correct\" value=\""+numQuestions+"\"></tr>");
            }
            else alert("You can only have six choices for a multiple choice question.");
        }

        this.addQuestion = function(){
            if($("#mcChoice"+$("input[name='correct_answer']:checked").val()).val() == ""){
                alert("The choice marked correct is blank.");
            }
            else if($("#question_form input[name='correct_answer']:checked").length == 0){
                alert("No correct answer has been chosen.");
            }
            else{
                var ret = new Object();
                ret.choices = [];
                ret.order = false;
                ret.all = false;
                ret.num = 0;
                for(var i = 0; i < numQuestions; i++){
                    if($("#question_form input[type='text']")[i].value != "") ret.choices.push({choice : $("#question_form input[type='text']")[i].value, correct: parseInt($("input[name='correct_answer']:checked").val())-1 == i});
                }
                if($("input[name='order']")[0].checked) ret.order = true;
                if($("input[name='all']")[0].checked) ret.all = true;
                ret.num = ret.choices.length;

                //build submit object
                var submission = new Object();
                submission.type = $("#question_type").val();
                submission.text = $("#question_body").val();
                submission.body = JSON.stringify(ret);
                alert(JSON.stringify(submission));
                $.get("/gen/add_question/", submission);

                return ret;
            }
        }
    }

    //Action Listeners
    $("#question_type").change(function(){
        var x = $("#question_type").val();
        switch(x){
            case 'M':
                edisco_context.state = stateDict.M;
                break;
            case 'X':
                //edisco_context.state = stateDict.X;
                break;
            default:
                break;
        }
        edisco_context.state.setup();
    });

    //Data
    stateDict = {M : new MultipleChoiceState(),
        X : undefined,
    };

    edisco_context = new QuestionContext();
});
