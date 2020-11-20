import random
import requests
import time
import numpy as np
import matplotlib.pyplot as plt


def createRandomPlaces(n):
    places = []
    for x in range(n):
        place = {"name": "Random " + str(x), "latitude": str(random.randrange(-90, 90)),
                 "longitude": str(random.randrange(-180, 180))}
        places.append(place)
    return places


def connect():
    y_data = []
    x_data = []
    for i in range(2, 1000, 1):
        times = []
        for j in range(3):
            trip = {"requestType": "trip", "requestVersion": 4, "options": {"earthRadius": "3959.0",
                                                                            "title": "testTrip",
                                                                            "response": "3.0"},
                    "places": createRandomPlaces(i)}

            start = time.time()
            url = "http://localhost:3000//api/trip"
            requests.post(url, json=trip)
            times.append(time.time() - start)
        times = np.array(times)
        y_data.append(np.mean(times))
        x_data.append(i)
    produceGraph(x_data, y_data)


def produceGraph(x_data, y_data):
    x_data = np.array(x_data)
    y_data = np.array(y_data)
    log_y_data = np.log(y_data)
    curve_fit = np.polyfit(x_data, log_y_data, 1)
    print(curve_fit)
    y = np.exp(-6.47506004e+00) * np.exp(5.48265808e-04 * x_data)  # Values Dependent On Hardware!
    fig = plt.figure()
    plt.yscale("log")
    plt.plot(x_data, y_data, "o")
    plt.plot(x_data, y, label="test")
    plt.xlabel('Number Of Places', fontsize=12)
    plt.ylabel('Running Time', fontsize=12)
    fig.savefig('test.jpg')
    plt.show()


def main():
    connect()


if __name__ == "__main__":
    main()
