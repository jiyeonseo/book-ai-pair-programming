/* eslint-disable no-console */
const name = 'John Doe';
const age = 30;

if (name === 'John Doe') {
  console.log('Welcome, John Doe!');
}

console.log('This is a log message');

const greeting = `Hello, ${name}! You are ${age} years old`;

if (age > 18) {
  console.log(greeting);
}
