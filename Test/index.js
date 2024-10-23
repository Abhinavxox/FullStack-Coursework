class Car {
  constructor(name, type) {
    this.name = name;
    this.type = type;
  }

  start() {
    console.log(`car name is ${this.name}`);
  }
}

const myCar = new Car("Toyota", "Corolla");
myCar.start();
