import data from "./data.json" assert {type: 'json'};

let course = data;

export function createCourse(input) {
    const newCourse = input.courseName;
    course.push(newCourse);
    return course;
}





