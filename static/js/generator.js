//OBJECT CLASSES

function StateContext(){
    this.state = null;
    this.stateDict = {};
}

StateContext.prototype = {

    addState : function(identifier, state){
        if(this.stateDict[identifier] != undefined){
            console.log("There is already a state defined with the identifier: "+identifier);
            return false;
        }
        this.stateDict[identifier] = state;
        return true;
    }

    getState : function(identifier){
        if(this.stateDict[identifier] != undefined){
            console.log("State not found: "+identifier);
            return null;
        }
        return this.stateDict[identifier];
    }
}
