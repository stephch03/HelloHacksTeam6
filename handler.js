import {
    createCourse
  } from "./video.js";
  
  const showResult = document.getElementById("result");
  const createCourseForm = document.getElementById("createCourseForm");

  createCourseForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const formProps = Object.fromEntries(formData);
    const result = createCourse(formProps);
    showResult.innerHTML = JSON.stringify(result, null, 2);
  });
  
  