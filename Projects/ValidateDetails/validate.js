function validateform(){
    let x=document.forms["myForm"]["fname"].value;
    let y=document.forms["myForm"]["pass"].value;
    
    if(x==""&&y==""){
        alert("Email and Password is compulsary");
        return false;
    }
    
    if(x==""){
        alert("Email is necessary");
        return false;
    }
    
    if(y==""){
        alert("Password is necessary");
        return false;
    }

    alert("Logged in Succesfully");

}