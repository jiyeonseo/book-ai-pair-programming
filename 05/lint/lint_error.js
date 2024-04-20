/* eslint-disable no-console */
var name = 'John Doe';
var age = 30;
var unusedVariable = 'This is not used anywhere';

if (name == 'John Doe') {
  console.log('Welcome, John Doe!');
}

console.log('This is a log message');

var greeting = `Hello, ${name}! You are ${age} years old`;

if (age > 18) {
  console.log(greeting);
}
