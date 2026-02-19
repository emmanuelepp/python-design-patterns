from abc import ABC, abstractmethod


class ICarBuilder(ABC):
    @abstractmethod
    def build_body_style(self, body_style: str):
        pass

    @abstractmethod
    def build_engine(self, engine: str):
        pass

    @abstractmethod
    def build_fuel_type(self, fuel_type: str):
        pass

    @abstractmethod
    def build_make(self, make: str):
        pass

    @abstractmethod
    def build_tires_type(self, tires_type: str):
        pass

    @abstractmethod
    def get_car(self):
        pass


class CarBuilder(ICarBuilder):
    def __init__(self):
        self.car = Car()

    def build_body_style(self, body_style: str):
        self.car.body_style = body_style

    def build_engine(self, engine: str):
        self.car.engine = engine

    def build_fuel_type(self, fuel_type: str):
        self.car.fuel_type = fuel_type

    def build_make(self, make: str):
        self.car.make = make

    def build_tires_type(self, tires_type: str):
        self.car.tires_type = tires_type

    def get_car(self):
        return self.car


class CarDirector:
    def __init__(self, car_builder):
        self.car_builder = car_builder

    def build_car(self):
        self.car_builder.build_body_style("SUV")
        self.car_builder.build_engine("V8")
        self.car_builder.build_fuel_type("Petrol")
        self.car_builder.build_make("Ford")
        self.car_builder.build_tires_type("All-terrain")


class Car:
    def display_car_info(self):
        print("Car Information:")
        print(f"Body Style: {self.body_style}")
        print(f"Engine: {self.engine}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Make: {self.make}")
        print(f"Tires Type: {self.tires_type}")


if __name__ == "__main__":
    car_builder = CarBuilder()
    director = CarDirector(car_builder)
    director.build_car()
    car = car_builder.get_car()
    car.display_car_info()
