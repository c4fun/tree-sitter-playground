// Variables and Data Types
let message = 'Hello, JavaScript!';
const PI = 3.14;
var dynamicType = true;
dynamicType = 'Changed type';

// Functions
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrow Function
const add = (a, b) => a + b;

// Control Structures
if (message === 'Hello, JavaScript!') {
    console.log('Conditionals are working!');
} else {
    console.error('Oops!');
}

// Loop
for (let i = 0; i < 5; i++) {
    console.log(`Loop iteration: ${i}`);
}

// Objects and Arrays
const person = {
    name: 'John',
    age: 30
};

const hobbies = ['Reading', 'Gaming', 'Coding'];

// Destructuring
const { name, age } = person;
console.log(name, age);

// Asynchronous Operations
function fetchData() {
    return new Promise((resolve) => setTimeout(() => resolve('Data fetched!'), 1000));
}

async function asyncCall() {
    console.log('Calling fetchData...');
    const result = await fetchData();
    console.log(result);
}

asyncCall();

// Modules (This would typically be in separate files)
// export function exportedFunction() {
//     return 'Exported!';
// }
// Import syntax would typically be: import { exportedFunction } from './module';

// Basic DOM Manipulation
document.addEventListener('DOMContentLoaded', () => {
    const heading = document.createElement('h1');
    heading.textContent = 'JavaScript Features';
    document.body.appendChild(heading);
});

// Error Handling
try {
    nonExistentFunction();
} catch (error) {
    console.error('Caught an error:', error.message);
}

console.log(greet('JavaScript Learner'));
