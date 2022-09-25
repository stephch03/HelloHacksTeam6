import data from "./data.json" assert {type: 'json'};
let people = data;

export function createPeople(input) {
  const linkExists = people.find((video) => {
    return video.link === input.link;
  }); 
  if (idExists) {
    return console.log("Welcome"); 
  }
  const newVideo = {
    link: input.link,
    title: input.title;
    ,
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