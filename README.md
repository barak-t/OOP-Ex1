## :wavy_dash: OOP-Ex1 :wavy_dash:
### Offline Elevator Algorithm

<br />

#### :green_circle: Base On:
- Elevator System Design: https://www.youtube.com/watch?v=siqiJAJWUVg&ab_channel=ThinkSoftware
- Elevator algorithm: https://en.wikipedia.org/wiki/Elevator_algorithm#Description
- https://www.javatpoint.com/os-scan-and-c-scan-algorithm

<br />

#### :green_circle: The Problem:
We would like that our algorithm allocate the elevators to reaching the best time for every passenger.
In order to get this results we have to took under consideration all its technical details, 
and the elevator position as a dependency our calls.
It's not easy to know where each elevator locates every time (because its offline algorithm) and this is our challenge.

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

#### :green_circle: Diagram:

#### :green_circle: Results:

Building | call | average waiting time per call | uncompleted calls | 
-------- | ---- | ----------------------------- |------------------ |
   B1    |  a   |            112.92             |      0            |
   B2    |  a   |            46.2               |       0           |
   B3    |  a   |            37.37              |          0        |
   B3    |  b   |            527.23             |          171      |
   B3    |  c   |            578.23             |          103      |
   B3    |  d   |            550.4              |         56        |
   B4    |  a   |            26.11              |         0         |
   B4    |  b   |            182.6              |       10          |
   B4    |  c   |            184                |         3         |
   B4    |  d   |            183.53             |        1          |
   B5    |  a   |            20.85              |         0         |
   B5    |  b   |            40.51              |          0        |
   B5    |  c   |            44.91              |         8         |
   B5    |  d   |            39.75              |          0        |
