

function addCourse(event) {
    console.log('hi')
    event.preventDefault();
    const fileSystem = require("browserify-fs")
    
  
    //const data = new FormData(event.target);
    const data = {
        "Name": "Mini Corp.",
        "Order_count": 83,
        "Address": "Little Havana"
       }

    const value = Object.fromEntries(data.entries());
    const strin = JSON.stringify(value)
    console.log(strin)

    fileSystem.writeFile("./data.json", strin, err=>{
        if(err){
          console.log("Error writing file" ,err)
        } else {
          console.log('JSON data is written to the file successfully')
        }
       })
    }



  
  const form = document.querySelector('form');
  form.addEventListener('submit', addCourse);