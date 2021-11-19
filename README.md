## :wavy_dash: OOP-Ex1 :wavy_dash:
### Offline Elevator Algorithm

<br />

#### :green_circle: Base On:
- Elevator System Design: https://www.youtube.com/watch?v=siqiJAJWUVg&ab_channel=ThinkSoftware
- Elevator algorithm: https://en.wikipedia.org/wiki/Elevator_algorithm#Description
- https://www.javatpoint.com/os-scan-and-c-scan-algorithm

<br />
<br />

#### :green_circle: The Problem:
We would like that our algorithm allocate the elevators to reaching the best time for every passenger.
In order to get this results we have to took under consideration all its technical details, 
and the elevator position as a dependency our calls.
It's not easy to know where each elevator locates every time (because its offline algorithm) and this is our challenge.

<br />
<br />

#### :green_circle: Our Algorithm:

Given two files csv & json. <br />
We take the information from these files and start. <br />
We save for each elevator its current time and last location and do the folowing:

1.  Our algorithm go over all the calls.
2.  It's takes every time one call.
3.  It's saves for every elevator it's current floor and it's last location time.
4.  it's Checks the time it will take to drive in each elevator by using the technical details of the elevetor, and its last location time.
5.  Choose the best time elevetor (fom src ---> dest) and allocate this elevator this call.

<br />
<br />

#### :green_circle: Diagram:

#### :green_circle: Results:

Building | call | total waiting time | average waiting time per call | uncompleted calls | certificate | 
-------- | ---- | ------------------ | ----------------------------- |------------------ |------------ |
b1       | 55   | ------------------ | ----------------------------- |------------------ |------------ |
