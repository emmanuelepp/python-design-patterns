from patterns.creational.builder import CarBuilder, CarDirector


def test_director_builds_expected_car():
    builder = CarBuilder()
    director = CarDirector(builder)

    director.build_car()
    car = builder.get_car()

    assert car.body_style == "SUV"
    assert car.engine == "V8"
    assert car.fuel_type == "Petrol"
    assert car.make == "Ford"
    assert car.tires_type == "All-terrain"
