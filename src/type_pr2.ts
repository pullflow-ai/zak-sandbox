interface User {
    name: string;
    age: number;
}

function createUser(name: string, age: number): User {
    return { name, age };
}

class Calculator {
    add(a: number, b: number): number {
        return a + b;
    }
}

function sayHello(name: string): string {
    return `Hello, ${name}!`;
}

const user: User = createUser("Alice", 30);
console.log(sayHello(user.name));

const calc = new Calculator();
console.log(`2 + 3 = ${calc.add(2, 3)}`);

export { User, createUser, Calculator, sayHello };
