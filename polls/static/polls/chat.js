function handleEnterKey(event) {
    if (event.keyCode === 13) {
      // Enter key was pressed
      console.log("Enter key pressed in textarea");
      // Add your code here to handle the Enter key press
    }
  }
  
  var textarea = document.getElementById("my-textarea");
  textarea.addEventListener("keydown", handleEnterKey);