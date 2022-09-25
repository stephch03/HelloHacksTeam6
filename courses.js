import data from "./data.json" assert {type: 'json'};

let courses = data;

export function createCourse(input) {
    const courseExists = courses.find((course) => {
        return course.courseName === input.courseName;
    });
    const newCourse = {
        courseName: input.courseName
    }
    console.log(input.courseName)
    courses.push(newCourse);
    return courses;

}
export function createModule(input) {
    const moduleExists = courses.find((module) => {
        return module.moduleName === input.moduleName
    });
    const newModule = {
        moduleName: input.moduleName,
        completed: Boolean(input.completed)
       
    }
    courses.push(newModule)
    return courses;

}

