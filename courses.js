import data from "./data.json" assert {type: 'json'};

let courses = data;

export function createCourse(input) {
    const courseExists = courses.find((course) => {
        return course.courseName === input.courseName;
    });
    const newCourse = input.courseName

    courses.push(newCourse);
    return courses;
}

export function createPeople(input) {
    const idExists = people.find((person) => {
        return person.name === input.name;
    }); // We check if a user already exists with the same name; because we determined the name to be the id, we do not want to create an entry with a duplicate id.
    if (idExists) {
        return people; // You could return an error here instead; this would be a design choice!
    }
    const newPerson = {
        name: input.name,
        // Ternary expression syntax: "?" means "if", ":" means "else"
        interests: input.interests ? input.interests.split(",") : [],
        subscribed: Boolean(input.subscribed),
        demographics: {
            country: input.country,
            age: Number(input.age)
        }
    };
    people.push(newPerson);
    return people;
}

export function readPeople(input) {
    let result = people;
    if (input.name) {
        result = result.filter((person) => {
            return person.name === input.name;
        });
    }
    if (input.country) {
        result = result.filter((person) => {
            return person.demographics.country === input.country;
        });
    }
    return result;
}

export function updatePeople(input) {
    const index = people.findIndex((person) => {
        return person.name === input.name;
    });
    if (index === -1) {
        return people;
    }
    const person = people[index];

    person.subscribed = Boolean(input.subscribed);
    if (input.interests) {
        const interestsArray = input.interests.split(",");
        person.interests = person.interests.concat(interestsArray);
    }
    if (input.age) {
        person.demographics.age = Number(input.age);
    }

    people[index] = person;
    return people;
}

export function deletePeople(input) {
    people = people.filter((person) => {
        return person.name !== input.name;
    });
    return people;
}