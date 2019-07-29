access_key = "";
secret_access_key = "";
region_name = "";
get_category_func_name = "";
post_register_func_name = "";

AWS.config.update({
  accessKeyId : access_key,
  secretAccessKey : secret_access_key
});
AWS.config.region = region_name;

window.onload = () => {
  // let xhr = new XMLHttpRequest();
  // xhr.open("", "");
  // xhr.setRequestHeader("x-api-key", "");
  // xhr.send();
  // xhr.onreadystatechange = () => {
  //   if(xhr.readyState === 4){
  //     console.log(xhr.responseText)
  //   }
  // }
  // AWS.config.update({
  //   accessKeyId : "",
  //   secretAccessKey : ""
  // });
  // AWS.config.region = 'region_name';
  // let lambda = new AWS.Lambda();
  // lambda.invoke(null, (err, data) => {
  //   if(err)
  //     console.log(err, err,stack);
  //   else
  //     console.log(data);
  // })

  let lambda = new AWS.Lambda();
  let params = {
    FunctionName : get_category_func_name,
    Payload : null
  };

  lambda.invoke(params, function(err, data) {
    if (err) {
      console.log(err, err.stack);
    }else {
      if(data["FunctionError"] != null){
        console.log("No data");
      }else{
        console.log("Success");
      }
    }
  });
};

// $(document).ready(() => {
//   'use strict';
//   let gateWayURL = '';
//   let APIKey = '';
//   $.ajax({
//     url: gateWayURL,
//     type: 'GET',
//     headers: {
//       'x-api-key': APIKey
//     }
//   }).done((result) => {
//     console.log(result)
//   })
// });

function sendCardInfo(){
  let cat1 = document.getElementById("input-cat1").value;
  let cat2 = document.getElementById("input-cat2").value;
  let quest = document.getElementById("edit-question").value;
  let ans = document.getElementById("edit-answer").value;
  if(cat1.replace(/\s/g, "") === "" || cat2.replace(/\s/g, "") === "" ||
      quest.replace(/\s/g, "") === "" || ans.replace(/\s/g, "") === ""){
    alert("Caution: There is information that has not been entered.")
    return false;
  }
  const sendObject = {
  };

  let lambda = new AWS.Lambda();
  let params = {
    FunctionName : post_register_func_name,
    Payload : JSON.stringify(sendObject)
  };

  lambda.invoke(params, function(err, data) {
    if (err) {
      console.log(err, err.stack);
    }else {
      if(data["FunctionError"] != null){
        console.log(data);
      }else{
        console.log("Success");
      }
    }
  });
}
