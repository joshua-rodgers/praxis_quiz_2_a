

---

## Question 1

**Question:**  
Writers and graphic artists are working to develop illustrations for a children’s book. Which of the following aspects of the creative process has been most significantly enhanced by the availability of software?

**Options:**  
A. Determining the layout, size, and number of illustrations  
B. Designing sketches to illustrate the author’s concepts  
C. Selecting sketches to recommend for each illustration  
D. Sharing illustrations among all the artists and writers to obtain feedback  

**Correct Answer:** D  

**Explanation:**  
Even if the writers and graphic artists are nearby, the processes of sharing the illustrations and obtaining feedback have been made easier through a variety of software applications. Without software, the illustrations would have to be physically shipped to the various team members. Options A, B, and C could be done with the aid of software; however, the judgments needed for layout, sketch design, and selection are typically not done by software.  

---

## Question 2

**Question:**  
Consider the following pseudocode procedure, which is intended to return the index of the least element in an array of integers `data[0..n-1]` of length `n`. If the least element in the array `data` occurs at multiple positions, the lowest index is returned.

```java
// precondition: n > 0
public int positionOfMinimum (int[] data, int n)
    int startingPosition ← 0
    int bestGuessSoFar ← startingPosition
    for (int i ← startingPosition + 1; i < n; i ← i + 1)
        if (data[i] < data[bestGuessSoFar])
            bestGuessSoFar ← i
        end if
    end for
    return bestGuessSoFar
end positionOfMinimum
```

Sometimes, it is necessary to search only part of an array. Of the following, which describes the most general solution for updating `positionOfMinimum` so that only the part of the array that begins at a specified index is searched?

**Options:**  
A. Make `startingPosition` a parameter of the method and remove the line that declares `startingPosition` and initializes it to 0.  
B. Change the `for` loop to a `while` loop that only executes while the code is searching the correct part of the array.  
C. Add a second `if` statement to the method that checks that the index found is in the correct part of the array.  
D. Change the initial value of `startingPosition` to the value of the index in the array where the search should begin.  

**Correct Answer:** A  

**Explanation:**  
The procedure `positionOfMinimum` searches through array `data` beginning at the first element and continuing until the last element. The procedure initializes a local variable named `startingPosition` to 0. If `startingPosition` is instead initialized with the parameter, it could be given different values in different calls. Abstraction is a way of generalizing. A procedure that always searches from a fixed position is less general than one that can begin at any specified position.  

---

## Question 3

**Question:**  
Consider the following pseudocode segment.

```java
int[] c ← {7, 6, 8, 10}
int[] d ← {8, 6, 7, 5}
mystery(c, d, 4)
```

```java
procedure mystery(A, B, n)
    for (k ← 0; k < n; k ← k + 1)
        if (A[i] > B[k])
            A[i] ← B[k]
        else
            i ← i + 1
        end if
    end for
end mystery
```

What is the value of `c` after the code segment above is run?

**Options:**  
A. {7, 6, 5, 10}  
B. {7, 6, 7, 5}  
C. {7, 6, 7, 10}  
D. The code causes an array index out-of-bounds error.  

**Correct Answer:** A  

**Explanation:**  
In the procedure, `i` and `k` are index variables for arrays `A` and `B`, respectively. During the iterations, `i` increments only when `A[i]` is not greater than `B[k]`. Through the given loop logic, the array `c` becomes `{7, 6, 5, 10}` at the end.  

---

## Question 4

**Question:**  
Match each characteristic with the appropriate type of data compression.

| Characteristic | Lossy Compression | Lossless Compression |
|----------------|-------------------|----------------------|
| Allows perfect reconstruction of the original data from the compressed data |   |   |
| Generally achieves a greater compression ratio |   |   |
| Is more appropriate for streaming music and video |   |   |

**Correct Answers:** B, C, E  

**Explanation:**  
- Allows perfect reconstruction → **Lossless compression**  
- Generally achieves greater compression ratio → **Lossy compression**  
- More appropriate for streaming → **Lossy compression**  
Lossless compression enables exact data recovery, while lossy compression reduces file size at the cost of minor, often imperceptible data loss, making it ideal for streaming.  

---

## Question 5

**Question:**  
Match each acronym with its correct description.

| Acronym | Description |
|----------|--------------|
| CPU | A component that executes program instructions |
| LCD | A technology used in flat-screen displays |
| RAM | A memory device for temporary storage of data and programs |
| ROM | A storage device for data and start-up instructions for a computer |
| USB | A connector and protocol used for communication and power supply |

**Correct Answer Order:** B, E, C, D, A  

**Explanation:**  
- **CPU (Central Processing Unit):** Executes program instructions.  
- **LCD (Liquid Crystal Display):** Used in flat-screen display technology.  
- **RAM (Random Access Memory):** Temporarily stores data and programs for quick access.  
- **ROM (Read-Only Memory):** Stores start-up instructions and is not altered on restart.  
- **USB (Universal Serial Bus):** Provides both power and data communication through standardized connectors.  



---

## Question 6

**Question:**  
Which of the following software license agreements allows users to use, modify, and sell or give away source code without the payment of royalties to the original developer?

**Options:**  
A. Creative Commons Attribution-NoDerivs license  
B. End-user license  
C. Open-source license  
D. Proprietary license  

**Correct Answer:** C  

**Explanation:**  
Open-source licenses allow software to be freely used, modified, and shared, including being sold or used for commercial purposes.  


---

## Question 7

**Question:**  
Geofencing is the use of geolocation data to trigger an action when a mobile device crosses a virtual boundary, called a geofence. A student wants to create a smartphone application that uses geofencing to help new students move from one location in a school to another. Which of the following features of the application might require a heuristic solution?

**Options:**  
A. The application detects when a student leaves a classroom.  
B. The application finds the best path from one classroom to the next.  
C. The application requires login information consisting of a student ID and password.  
D. The application retrieves a student’s schedule and sends schedule information to the smartphone.  

**Correct Answer:** B  

**Explanation:**  
A heuristic approach to problem solving finds a solution within a reasonable time frame that is good enough, though not guaranteed to be optimal. Finding the best path may be complex or time-consuming, making a heuristic method appropriate.  


---

## Question 8

**Question:**  
A programmer has written a procedure `wa(x, y, w)` to calculate the weighted average of two values `x` and `y`. The given weight `w` is applied to the greater of `x` and `y`, and the remaining weight `1 - w` is applied to the smaller of `x` and `y`.

An application calls the procedure on a pair of values `a` and `b` and then on a different pair of values `c` and `d`. Both calls use the same weight `w`. The final step is to call `wa` on the results of the previous two calls, again using the same weight `w`.

Which of the following correctly uses `wa` to calculate the desired result?

**Options:**  
A. `wa(wa(a, b), wa(c, d), w)`  
B. `wa(wa(a, b, w), wa(c, d, w))`  
C. `wa(wa(a, b, w), wa(c, d, w), w)`  
D. `wa(wa(a, b, w) + wa(c, d, w))`  

**Correct Answer:** C  

**Explanation:**  
The first argument in the outer `wa` procedure is `wa(a, b, w)`, and the second argument is `wa(c, d, w)`. The third argument in the outer `wa` procedure is `w`, the same weight used in the earlier calls. Thus, the correct call is `wa(wa(a, b, w), wa(c, d, w), w)`.  


---

## Question 9

**Question:**  
A computer simulation of operations at a car wash with several wash stations is run several times. In each run, only the number of available wash stations is changed. Which of the following changes is most likely to occur between runs of the simulation?

**Options:**  
A. A change in the average wait time per customer to enter a wash station  
B. A change in the amount charged per car wash  
C. A change in the amount of water used per car wash  
D. A change in the average length of time needed to wash a car once the car enters the wash station  

**Correct Answer:** A  

**Explanation:**  
Changing the number of available wash stations directly impacts the wait time per customer. It does not affect the price, water used per wash, or wash duration once inside the station.  


---

## Question 10

**Question:**  
Which of the following network devices is responsible for finding and changing the paths of data packets as needed?

**Options:**  
A. Network firewall  
B. Network interface card  
C. Network repeater  
D. Network router  

**Correct Answer:** D  

**Explanation:**  
Routers determine and adjust the paths that packets take across a network. Firewalls filter packets based on rules, NICs handle communication between a computer and the network, and repeaters simply amplify signals.  




---

## Question 10

**Question:**  
Which of the following network devices is responsible for finding and changing the paths of data packets as needed?

**Options:**  
A. Network firewall  
B. Network interface card  
C. Network repeater  
D. Network router  

**Correct Answer:** D  

**Explanation:**  
Routers direct packets through the network by determining and updating their paths. Firewalls use rules to allow or deny packets, NICs exchange data along fixed paths, and repeaters amplify signals without changing paths.  


---

## Question 11

**Question:**  
Which of the following are impacts of computing?  

**Select all that apply.**

**Options:**  
A. Computing has enabled the creation of interactive art forms.  
B. Computers analyze images produced by medical imaging devices.  
C. Computers enable people who speak different languages to communicate.  

**Correct Answers:** A, B, C  

**Explanation:**  
Computers impact diverse fields: enabling interactive art via sensors and interfaces, performing original analysis of medical images, and facilitating translation across languages for communication.  


---

## Question 12

**Question:**  
Place the following in order from lowest level of abstraction to highest level of abstraction:

**Items:**  
- Field  
- Record  
- Table  
- Database  

**Correct Answer:** A (Field), C (Record), D (Table), B (Database)  

**Explanation:**  
The order from lowest to highest abstraction is **field → record → table → database**. Fields contain single data points; records group related fields; tables store multiple records; and databases contain multiple tables.  


---

## Question 13

**Question:**  
Consider the following pseudocode procedure, intended to return true if a positive integer greater than 1 is prime and false otherwise.

```java
boolean isPrime (int n)
    if (n < 2)
        return false
    end if
    int k ← 2
    /* missing code */
end isPrime
```

Which of the following can replace `/* missing code */` so that `isPrime` works as intended?

**Options:**  
A. Returns too early after first iteration  
B. Returns true when n is 2 and for all n > 2  
C. Correct loop checking all divisors from 2 to n−1  
D. Uses count variable but fails to increment k  

**Correct Answer:** C  

**Explanation:**  
Option C correctly checks divisibility for all numbers from 2 to n−1. If any divisor divides evenly, it returns false; otherwise, after the loop ends, it returns true. The other options fail due to early returns or infinite loops.  


---

## Question 14

**Question:**  
Which of the following is the decimal representation of the sum of binary numbers 1011 and 1011?

**Options:**  
A. 22  
B. 31  
C. 44  
D. 2022  

**Correct Answer:** A  

**Explanation:**  
Binary 1011 equals decimal 11. Adding 11 + 11 gives 22. Alternatively, 1011 + 1011 = 10110 (binary), which equals 22 in decimal.  


---

## Question 15

**Question:**  
Two people with access to the same bank account make simultaneous withdrawals at different branches. Both see a balance of $400; one withdraws $200 and the other $250. Both transactions succeed, and the account becomes overdrawn. Which of the following best describes the error in the bank software?

**Options:**  
A. Failed user authentication  
B. Allowed multiple tasks to run concurrently  
C. Allowed two processes to access shared data simultaneously  
D. Used virtual instead of physical memory  

**Correct Answer:** C  

**Explanation:**  
The error occurred because two processes accessed and modified shared data (the account balance) concurrently without proper synchronization. This is a classic race condition in shared data access.  




---

## Question 16

**Question:**  
Which of the following is most likely to be permitted as fair use?

**Options:**  
A. A small-business owner uses copyrighted music in an advertisement on social media.  
B. A student uses an image from a Web site for a research project without citing the source.  
C. A teacher digitizes a computer science textbook and posts it online.  
D. A teacher shows a two-minute video clip of a movie illustrating a concept just discussed.  

**Correct Answer:** D  

**Explanation:**  
Fair use allows limited noncommercial use of copyrighted material for educational purposes without significantly affecting market value. Showing a short, relevant video clip for teaching is consistent with fair use.  


---

## Question 17

**Question:**  
A teacher wants to arrange 32 students in groups of 4. Each student ranks the others in order of preference. All possible groupings are considered to find the one that maximizes overall satisfaction. There are approximately 5.9×10¹⁹ possible groupings. Which of the following best describes the computational limitations of this problem?

**Options:**  
A. Finding the best possible solution is impossible, since there are too many possibilities.  
B. Finding an optimal solution is impossible, since no exact algorithm exists.  
C. Finding an optimal solution is difficult, since the data cannot easily be stored digitally.  
D. Finding an acceptable solution using a heuristic approach is possible, but it may differ from the best possible solution.  

**Correct Answer:** D  

**Explanation:**  
The vast number of combinations makes a brute-force solution computationally infeasible. A heuristic can produce a reasonable solution quickly, though it may not be optimal.  


---

## Question 18

**Question:**  
A refrigerator sensor monitors temperature and humidity. The climate is “comfortable” if the temperature is between 62°F and 75°F inclusive, and the humidity is between 30% and 50% inclusive.

Which of the following conditional expressions correctly implements this logic?

**Options:**  
A. `(temperature ≥ 62 and temperature ≤ 75) and (humidity ≥ 30 and humidity ≤ 50)`  
B. `(temperature ≥ 62 or temperature ≤ 75) and (humidity ≥ 30 or humidity ≤ 50)`  
C. `(temperature ≥ 62 and temperature ≤ 75) or (humidity ≥ 30 and humidity ≤ 50)`  
D. `(temperature ≥ 62 or temperature ≤ 75) or (humidity ≥ 30 or humidity ≤ 50)`  

**Correct Answer:** A  

**Explanation:**  
Both conditions must be satisfied for comfort, so the `and` operator is required between each range check.  


---

## Question 19

**Question:**  
A simulation models city traffic over a 24-hour period. A variable represents the time (in hours) between cars entering a street. Which of the following best describes how values should be assigned to this variable for realistic simulation?

**Options:**  
A. Values that decrease linearly during the simulation  
B. Values that increase exponentially during the simulation  
C. Values that oscillate during the simulation above and below a specified mean  
D. Values randomly generated between 1 and 23, inclusive  

**Correct Answer:** C  

**Explanation:**  
Traffic fluctuates with time of day—busy during daylight hours and light at night—so the interval between cars should oscillate above and below an average, reflecting daily cycles.  


---

## Question 20

**Question:**  
Which of the following best describes how network load and latency change as more devices are connected to a home Internet network?

**Options:**  
A. Both network load and latency decrease.  
B. Network load decreases and latency increases.  
C. Network load increases and latency decreases.  
D. Both network load and latency increase.  

**Correct Answer:** D  

**Explanation:**  
As more devices connect, total data traffic (load) increases. More simultaneous transmissions cause delays, increasing latency.  




---

## Question 21

**Question:**  
Which of the following are examples of a digital divide?

**Select all that apply.**

**Options:**  
A. An older couple cannot post messages on a social network without help from their grandchildren.  
B. A student cannot view a homework video because they lack high-speed Internet.  
C. A family’s broadband slows down when multiple members use it simultaneously.  

**Correct Answers:** A, B  

**Explanation:**  
(A) represents a generational digital divide, and (B) represents a socioeconomic or geographic divide due to unequal Internet access. (C) is not an example of a digital divide since it reflects temporary bandwidth limitations, not inequity in access.  


---

## Question 22

**Question:**  
Match each device to its correct classification.

| Device | Classification |
|---------|----------------|
| Joystick | Input device |
| Speaker | Output device |
| CPU | Processing device |
| ROM | Storage device |

**Correct Answer Order:** B, D, A, C  

**Explanation:**  
- **Joystick:** An input device that allows user interaction.  
- **Speaker:** An output device for sound.  
- **CPU:** A processing unit that executes instructions.  
- **ROM:** A storage medium that contains essential system instructions.  


---

## Question 23

**Question:**  
A programmer is writing a program to display even numbers 2 through 10 using these pseudocode statements:

| # | Pseudocode |
|---|-------------|
| 1 | `print(n)` |
| 2 | `while (n ≤ 10)` |
| 3 | `n ← n + 2` |
| 4 | `end while` |
| 5 | `int n ← 2` |

Which order of statements correctly produces the intended result?

**Options:**  
A. 2, 5, 1, 3, 4  
B. 2, 5, 3, 4, 1  
C. 5, 2, 1, 3, 4  
D. 5, 2, 3, 1, 4  

**Correct Answer:** C  

**Explanation:**  
The variable must first be initialized (`int n ← 2`), then the while loop (`while n ≤ 10`) begins. Inside the loop, `n` is printed, incremented by 2, and the loop ends properly with `end while`.  


---

## Question 24

**Question:**  
For the encoding scheme shown in the table, what is the decimal result of adding 5 and 6?

**Correct Answer:** −5  

**Explanation:**  
Binary 5 = `0101` and binary 6 = `0110`. Adding these gives `1011`. In the encoding scheme used, `1011` corresponds to **−5**.  


---

## Question 25

**Question:**  
Which of the following would best be classified as an input device?

**Options:**  
A. Keyboard  
B. Monitor  
C. Speakers  
D. Printer  

**Correct Answer:** A  

**Explanation:**  
An input device sends data to a computer for processing. A keyboard captures typed input. Monitors, printers, and speakers are output devices.  


---

## Question 26

**Question:**  
A bank customer receives an e-mail warning of suspicious activity and is asked to click a link to verify their identity. The e-mail looks legitimate but links to a malicious website. Which of the following best describes the scam?

**Options:**  
A. Spam  
B. Hacking  
C. Phishing  
D. Robocalls  

**Correct Answer:** C  

**Explanation:**  
Phishing involves tricking users into entering personal information, such as usernames or passwords, on fraudulent websites that mimic legitimate ones.  


---

## Question 27

**Question:**  
Two algorithms, `f` and `g`, calculate Fibonacci numbers differently. Algorithm 1 is iterative, and Algorithm 2 is recursive.

Which of the following best describes their running times in terms of *n*?

| Algorithm 1 | Algorithm 2 |
|--------------|--------------|
| A. Linear | Linear |
| B. Linear | Exponential |
| C. Quadratic | Linear |
| D. Quadratic | Exponential |

**Correct Answer:** B  

**Explanation:**  
The iterative algorithm runs in linear time (*O(n)*), while the recursive one makes repeated overlapping calls, resulting in exponential growth (*O(2ⁿ)*).  


---

## Question 28

**Question:**  
Which of the following features would be most beneficial for Deaf users accessing a website?

**Options:**  
A. Captions for video media  
B. Limited use of color contrast and sound to convey meaning  
C. Alternate text for images  
D. An advanced speech synthesizer  

**Correct Answer:** A  

**Explanation:**  
Captions or subtitles allow Deaf users to follow along with video content. While alt text and screen readers help the visually impaired, captions specifically enhance accessibility for Deaf individuals.  


---

## Question 29

**Question:**  
The following pseudocode simulates rolling a fair six-sided die multiple times and returns the number of pairs of consecutive identical rolls. Which code segment correctly replaces `/* missing code block */` so the function works as intended?

**Options:**  
A.
```java
int roll = RANDOM(1, 6)
if (roll == temp)
    numTwoInARow = numTwoInARow + 1
    temp = roll
end if
```
B.
```java
int roll = RANDOM(1, 6)
if (roll == temp)
    numTwoInARow = numTwoInARow + 1
end if
temp = roll
```
C.
```java
if (temp == RANDOM(1, 6))
    numTwoInARow = numTwoInARow + 1
end if
```

**Correct Answer:** B  

**Explanation:**  
Each iteration must update `temp` to store the current roll and compare it to the next roll. Option B correctly performs both steps in the right order, ensuring accurate consecutive roll counting.  


---

## Question 30

**Question:**  
How long would it take to transfer 30 gigabytes of data over a 480-megabit-per-second connection?

**Options:**  
A. 50 seconds  
B. 8 minutes  
C. 1 hour  
D. 5 hours  

**Correct Answer:** B  

**Explanation:**  
Using dimensional analysis:
\[
30 \text{ GB} × \frac{2^{30} \text{ bytes}}{1 \text{ GB}} × \frac{8 \text{ bits}}{1 \text{ byte}} × \frac{1 \text{ Mbit}}{2^{20} \text{ bits}} × \frac{1 \text{ s}}{480 \text{ Mbit/s}}
\]
This simplifies to approximately 512 seconds, or about **8.5 minutes**, making **8 minutes** the closest answer.  




---

## Question 31

**Question:**  
A robot starts at point **P** facing east in a 3×4 grid and must move to point **Q**, ending up facing north. Each move awards a different number of points depending on the type of move:

| Procedure | Description | Points |
|------------|--------------|---------|
| `forward()` | Move forward one square | 1 |
| `forward_right()` | Move forward and turn 90° right | 2 |
| `forward_left()` | Move forward and turn 90° left | 3 |

If moving off the grid earns no points, which sequence moves the robot from P to Q and earns the most points?

**Options:**  
A. `forward(), forward(), forward_left(), forward(), forward()`  
B. `forward(), forward_left(), forward_right(), forward_left(), forward()`  
C. `forward_left(), forward_left(), forward_right(), forward_right(), forward(), forward(), forward()`  
D. `forward_left(), forward_right(), forward(), forward(), forward_left(), forward_left(), forward_right()`  

**Correct Answer:** B  

**Explanation:**  
Option (B) correctly moves the robot from **P** → **A** → **B** → **F** → **G** → **Q**, earning a total of 10 points (1 + 3 + 2 + 3 + 1). It ends facing north, as required.  


---

## Question 32

**Question:**  
Consider the pseudocode procedure:

```java
int power(int x, int y)
    int answer ← 1
    for (int count ← 0; count < y; count ← count + 1)
        answer ← answer * x
    end for
    return answer
end power
```

Under which condition does this procedure fail to produce the correct result?

**Options:**  
A. x < 0, y > 0  
B. x = 0, y ≥ 2  
C. x > 0, y = 0  
D. x ≥ 2, y < 0  

**Correct Answer:** D  

**Explanation:**  
The for loop only executes for positive values of *y*. When *y* is negative, the loop never runs, returning 1 instead of the correct fractional result.  


---

## Question 33

**Question:**  
Although self-driving cars have imperfect records, their potential benefits may outweigh the costs. Which of the following best explains why research to improve them is worthwhile?

**Options:**  
A. Computers do not get distracted, so collisions due to distracted driving are reduced.  
B. Pedestrians will learn to avoid self-driving cars.  
C. Employees can live farther from work, increasing productivity.  
D. Eventually, all software bugs will be fixed.  

**Correct Answer:** A  

**Explanation:**  
Self-driving cars reduce accidents caused by human error, such as distraction, fatigue, or delayed reaction time. This advantage justifies continued research and development.  


---

## Question 34

**Question:**  
Consider this binary search pseudocode:

```java
int binarySearch(int[] arr, int length, int target)
    int lo ← 0
    int hi ← length - 1
    while (lo ≤ hi)
        int mid ← lo + (hi - lo) / 2
        if (arr[mid] > target)
            hi ← mid - 1
        else
            if (arr[mid] < target)
                lo ← mid + 1
            else
                return mid
            end if
        end if
    end while
    return -1
end binarySearch
```

Given:  
`arr = {-3, -2, 1, 2, 3, 4, 5, 6, 7, 9}`, `length = 10`, `target = 4`  

**Options:**  
A. -1, 5 comparisons  
B. -1, 8 comparisons  
C. 5, 5 comparisons  
D. 5, 8 comparisons  

**Correct Answer:** D  

**Explanation:**  
The function returns index 5 (where value = 4). During the three loops, lines 4, 6, and 9 are executed eight times in total.  


---

## Question 35

**Question:**  
Consider the procedure header:

```java
int average(int a, int b, int c)
```

Which of the following is a valid call to `average`?

**Options:**  
A. `average(3, 4)`  
B. `average("2", 3, 4)`  
C. `average(2.5, 5, 6)`  
D. `average(average(1, 2, 3), 4, 5)`  

**Correct Answer:** D  

**Explanation:**  
The nested call is valid because all parameters of `average` must be integers. The inner call returns an integer value that can be used as an argument in the outer call.  




---

## Question 36

**Question:**  
Using 8-bit ASCII, the 2-character string message "Hi" is encoded as `01001000 01101001`. If each 8-bit binary code of the message is encrypted using the 8-bit key `11010011` and an XOR operation, which of the following represents the encrypted message?

**Options:**  
A. `00011011 00111100`  
B. `00100001 10111010`  
C. `10011011 10111010`  
D. `11011011 11111011`  

**Correct Answer:** C  

**Explanation:**  
XORing each byte of the message with the key results in:  
- `01001000 XOR 11010011 = 10011011`  
- `01101001 XOR 11010011 = 10111010`  
Thus, the encrypted message is `10011011 10111010`.  


---

## Question 37

**Question:**  
ASCII is a 7-bit encoding system. The table shows several characters and their decimal values:

| Character | Decimal |
|------------|----------|
| 7 | 55 |
| = | 61 |
| A | 65 |
| Z | 90 |

For which of the following ASCII characters does the associated binary representation contain the greatest number of 0s?

**Options:**  
A. 7  
B. =  
C. A  
D. Z  

**Correct Answer:** C  

**Explanation:**  
Binary(55) = `0110111`, Binary(61) = `0111101`, Binary(65) = `1000001`, Binary(90) = `1011010`.  
Character **A** (`1000001`) contains **five 0s**, more than any other option.  


---

## Question 38

**Question:**  
Consider the following pseudocode line with mismatched parentheses:

```java
int x ← (r + 4 * (t - 3) / 2
```

Which of the following best describes the error that would result?

**Options:**  
A. The compilation step would fail because of improper syntax.  
B. The code would compile but produce an incorrect value for x.  
C. The code would compile but cause a run-time error due to division by zero.  
D. The code would compile but cause a rounding error.  

**Correct Answer:** A  

**Explanation:**  
Most compilers detect unmatched parentheses during the **syntax-checking (compile)** phase. The code fails compilation before execution begins.  


---

## Question 39

**Question:**  
An IPv4 address has the form `nnn.nnn.nnn.nnn`, where each `nnn` is an 8-bit integer. An IPv6 address has the form `HHHH:HHHH:HHHH:HHHH:HHHH:HHHH:HHHH:HHHH`, where each `H` is a hexadecimal digit. Which statement correctly describes the relationship between the number of possible IPv4 and IPv6 addresses?

**Options:**  
A. 4× as many IPv6 addresses as IPv4 addresses  
B. 2⁴× as many IPv6 addresses as IPv4 addresses  
C. 2⁹⁶× as many IPv6 addresses as IPv4 addresses  
D. 2¹²⁸× as many IPv6 addresses as IPv4 addresses  

**Correct Answer:** D  

**Explanation:**  
IPv4 addresses have 32 bits (4×8), while IPv6 addresses have 128 bits. The number of possible combinations is 2¹²⁸ for IPv6 and 2³² for IPv4, meaning there are **2⁹⁶ times more IPv6 addresses** than IPv4.  


---

## Question 40

**Question:**  
Which of the following best describes a situation in which a heuristic should be used to find a solution?

**Options:**  
A. An accountant calculating taxes for clients  
B. A researcher combining results from different groups  
C. A nurse determining correct medication dosage  
D. A family planning a cross-country road trip while avoiding traffic congestion  

**Correct Answer:** D  

**Explanation:**  
Heuristics are useful when exact optimization is impractical due to the problem’s complexity. Planning an optimal route that minimizes congestion involves too many possibilities for an exact solution.  


---

## Question 41

**Question:**  
A software engineer is developing a simulation of customers and cashiers in a store for the purpose of understanding customer wait times. The following information is stored for each customer:

- Arrival time: the time at which the customer joins a line for a cashier  
- Service time: the time it takes a cashier to complete the customer’s order  

Which of the following is the most appropriate abstract data type to store customer objects in this simulation?

**Options:**  
A. Customer objects should be placed in a queue data structure in the order of their arrival time.  
B. Customer objects should be pushed onto a stack data structure in the order of their arrival time.  
C. Customer objects should be put into a dictionary using the customer’s arrival time as the key.  
D. Customer objects should be put into a dictionary using the customer’s service time as the key.  

**Correct Answer:** A  

**Explanation:**  
A queue follows a first-in, first-out (FIFO) structure, matching the real-world order in which customers are served at a cashier line.  
 

---

## Question 42

**Question:**  
Which of the following is a primary difference between encoding and encryption?

**Options:**  
A. Encoding involves binary digits and encryption does not.  
B. Encoding transforms data and encryption does not.  
C. Encryption is used in online transactions and encoding is not.  
D. Encryption is used to restrict access and encoding is not.  

**Correct Answer:** D  

**Explanation:**  
Both encoding and encryption transform data, but encryption is specifically designed to **restrict access** and maintain confidentiality, while encoding simply changes data into another form for transmission or storage.  


---

## Question 43

**Question:**  
Which **three** of the following are factors that contribute to the digital divide?

**Options:**  
A. Different physical access to computers and networks  
B. Different levels of information literacy  
C. Different accessibility needs when working with digital technologies  
D. Different manufacturers of physical digital devices  

**Correct Answers:** A, B, C  

**Explanation:**  
The digital divide refers to inequalities in access, literacy, and usability regarding technology. Physical access, digital literacy, and accessibility differences all contribute to this gap. Manufacturer variation does not.  


---

## Question 44

**Question:**  
Consider the following pseudocode segment, intended to initialize integer arrays `x[0..4]` and `y[0..4]` to the values below.

| k | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| x[k] | 7 | 12 | 17 | 22 | 27 |
| y[k] | 10 | 15 | 20 | 25 | 30 |

```java
int x[0..4]
int y[0..4]
/* missing code */
for (int i ← 1; i < 6; i ← i + 1)
    x[i - 1] ← a * i + b
    y[i - 1] ← x[i - 1] + c
end for
```

Which of the following could replace `/* missing code */` so that the pseudocode works as intended?

**Options:**  
A. a = 3, b = 2, c = 5  
B. a = 3, b = 4, c = 3  
C. a = 5, b = 3, c = 5  
D. a = 5, b = 2, c = 3  

**Correct Answer:** D  

**Explanation:**  
When `i = 1`, `x[0] = 5 * 1 + 2 = 7`; when `i = 2`, `x[1] = 5 * 2 + 2 = 12`. These match the table values. `y[0] = x[0] + 3 = 10`, confirming `c = 3`.  


---

## Question 45

**Question:**  
Consider the pseudocode segment below, where `condA` and `condB` are Boolean variables.

```java
if (condA and condB)
    print "Red"
else
    if ((not condA) or condB)
        print "Blue"
    else
        print "Green"
    end if
end if
```

What is printed as a result of executing this pseudocode when `condA` is **true** and `condB` is **false**?

**Options:**  
A. Red  
B. Blue  
C. Green  
D. Nothing is printed  

**Correct Answer:** C  

**Explanation:**  
When `condA` is true and `condB` is false, the first condition `(condA and condB)` is false. The next condition `((not condA) or condB)` is also false, so the program prints **Green**.  




---

## Question 46

**Question:**  
Which of the following is an example of the Internet of Things (IoT)?

**Options:**  
A. A driver uses a remote car starter to warm up the car when it is cold outside.  
B. A coffeemaker in the kitchen turns on when an alarm clock uses the Internet to send it a message.  
C. A computer automatically runs a daily scan to look for viruses.  
D. A customer receives an automatically generated e-mail via the Internet for a special discount at a local shop.  

**Correct Answer:** B  

**Explanation:**  
The Internet of Things (IoT) connects devices that normally lack Internet capability, allowing them to interact autonomously. The coffeemaker turning on via a signal from an alarm clock demonstrates IoT functionality.  


---

## Question 47

**Question:**  
Which of the following best describes the average running time of a linear search algorithm and a binary search algorithm on a sorted array of integers, in terms of the array’s length?

| Search Type | Average Running Time |
|--------------|----------------------|
| Linear Search | ? |
| Binary Search | ? |

**Options:**  
A. Logarithmic, Logarithmic  
B. Logarithmic, Linear  
C. Linear, Logarithmic  
D. Linear, Linear  

**Correct Answer:** C  

**Explanation:**  
A **linear search** must examine elements sequentially, resulting in linear time complexity \(O(n)\). A **binary search** halves the search space at each step, yielding logarithmic time complexity \(O(\log n)\).  


---

## Question 48

**Question:**  
Integrated development environments (IDEs) contain programming tools to help developers create software. Which of the following describes an IDE feature and its intended purpose?

**Options:**  
A. Code completion: Suggests subsequent text based on current text  
B. Compiler: Maintains a logical ordering of source-code files  
C. Debugger: Generates API documentation in HTML format  
D. Interpreter: Optimizes code to minimize the program’s running time  

**Correct Answer:** A  

**Explanation:**  
Code completion predicts the rest of a variable, method, or class name based on partial input, reducing typing errors and development time. Other options describe unrelated behaviors.  


---

## Question 49

**Question:**  
Consider the following class and line of code:

```java
public class Fraction {
    public int numerator;
    public int denominator;
    public Fraction(int num, int den) {
        // implementation not shown
    }
}

Fraction f = new Fraction(7, 12);
```

Match each code element to its concept.

| Concept | Code Element |
|----------|---------------|
| Argument | 12 |
| Object Type | First occurrence of `Fraction` |
| Constructor | Second occurrence of `Fraction` |
| Object Name | `f` |
| Keyword | `new` |

**Correct Answer:** A, B, C, D, E  

**Explanation:**  
This example demonstrates object-oriented terminology: defining an **object type** (`Fraction`), using the **constructor** (`new Fraction`), assigning to an **object name** (`f`), and initializing with **arguments** (7, 12).  


---

## Question 50

**Question:**  
Which of the following best describes the main purpose of encoding?

**Options:**  
A. To format data for efficient storage and transmission  
B. To maintain data confidentiality  
C. To minimize data size  
D. To slow down the transfer of data between computers  

**Correct Answer:** A  

**Explanation:**  
Encoding converts data into a standardized form suitable for storage, transmission, or processing. Encryption, by contrast, ensures confidentiality; compression minimizes data size.  




---

## Question 51

**Question:**  
What is the maximum number of distinct symbols that could appear in the hexadecimal representation of a positive integer?

**Options:**  
A. 8  
B. 10  
C. 15  
D. 16  

**Correct Answer:** D  

**Explanation:**  
The hexadecimal system uses sixteen symbols: 0–9 and A–F (representing 10–15). Thus, the maximum number of distinct symbols that can appear is 16.  


---

## Question 52

**Question:**  
The following figure shows the contents of integer array `arr[0..9]` of length 10.

`50 21 94 35 12 88 5 101 47 59`

Consider the following pseudocode segment that sorts the array `arr`.

```java
for (int j ← 1; j < 10; j ← j + 1)
    int val ← arr[j]
    int k ← j - 1
    while ((k ≥ 0) and (arr[k] > val))
        arr[k + 1] ← arr[k]
        k ← k - 1
    end while
    arr[k + 1] ← val
end for
```

Which of the following shows the contents of `arr` after 3 iterations of the outer `for` loop?

**Options:**  
A. 5 12 21 35 47 50 59 88 94 101  
B. 5 12 21 94 35 50 88 101 47 59  
C. 12 21 35 50 94 88 5 101 47 59  
D. 21 35 50 94 12 88 5 101 47 59  

**Correct Answer:** D  

**Explanation:**  
After three passes of insertion sort, the first four elements are sorted. The sequence becomes `21 35 50 94 ...`, confirming that option D is correct.  


---

## Question 53

**Question:**  
Which of the following is the best reason to use named constants instead of hard-coded values in a program?

**Options:**  
A. To make the program easier for clients to use  
B. To make the program easier for programmers to maintain  
C. To make the program execute in less time  
D. To make the program use less memory  

**Correct Answer:** B  

**Explanation:**  
Named constants improve readability and maintainability. Changing a constant’s value only requires a single edit, whereas hard-coded values require changes throughout the code. Execution time and memory usage are unaffected.  


---

## Question 54

**Question:**  
An e-commerce site asks users to input a shipping address including street, city, state/territory abbreviation, and ZIP code. Users select the state/territory code from a pull-down menu containing all legal codes. What additional validation must be performed on the state/territory code?

**Options:**  
A. Validate that the state/territory code matches the ZIP code to form a valid pair.  
B. Validate that the state/territory code matches a database of shipping costs.  
C. Validate that the code contains only legal characters.  
D. No additional validation is needed.  

**Correct Answer:** A  

**Explanation:**  
Although the pull-down menu ensures only legal codes are used, consistency between the ZIP code and state/territory must still be verified to ensure valid address data.  


---

## Question 55

**Question:**  
Match the four Internet technology descriptions with the corresponding acronyms.

| Acronym | Description |
|----------|--------------|
| DNS | The service that maps domain names to IP addresses |
| HTML | A markup language for creating Web pages |
| HTTP | The protocol used for transferring Web pages |
| TCP | The protocol that governs packet transmission on the Internet |

**Correct Answer:** C, A, B, D  

**Explanation:**  
- **DNS (Domain Name System):** Maps domain names to IP addresses.  
- **HTML (Hypertext Markup Language):** Defines the structure of web pages.  
- **HTTP (Hypertext Transfer Protocol):** Governs transfer of web pages.  
- **TCP (Transmission Control Protocol):** Manages reliable packet transmission.  


---

## Question 56

**Question:**  
When the following pseudocode is executed, the program outputs a negative number:

```java
int totPopulation = populationX + populationY
print("Total population = ")
print(totPopulation)
```

The output is:
```
Total population = -1614967296
```

Which of the following best explains this unexpected negative value?

**Options:**  
A. The use of intermediate variables introduces errors.  
B. The variable names are too long.  
C. A round-off error occurred.  
D. The sum of the two populations exceeds the largest value that can be stored in an int.  

**Correct Answer:** D  

**Explanation:**  
This is an **integer overflow** issue. In two’s complement representation, exceeding the maximum positive int causes the leftmost bit to flip to 1, yielding a negative result. This occurs when the total exceeds 2³¹−1.  


---

## Question 57

**Question:**  
The following pseudocode segment is intended to count all even numbers in the array `numbers`, but it contains an error.

```java
// precondition: numbers is an array of integers.
int count ← 0
for (int i ← 0; i ≤ numbers.length; i ← i + 1)
    if ((numbers[i] % 2) == 0)
        count ← count + 1
    end if
end for
```

Which of the following best describes the error in the code segment?

**Options:**  
A. Arithmetic precision error  
B. Array index out-of-bounds error  
C. Infinite loop error  
D. Stack overflow error  

**Correct Answer:** B  

**Explanation:**  
Since array indices range from 0 to `numbers.length − 1`, the loop condition `i ≤ numbers.length` causes an **array index out-of-bounds** error during the final iteration when `i = numbers.length`.  


---

## Question 58

**Question:**  
A major technology company has collected large amounts of user data. Which of the following uses of this data would be the most ethical?

**Options:**  
A. Selling the user data as is to another company  
B. Requesting that users specifically opt in to sharing data with another company  
C. Removing personally identifiable information before sharing the data  
D. Including a clause allowing data sale in the terms of service  

**Correct Answer:** B  

**Explanation:**  
According to the Web Analyst’s Code of Ethics, users must retain control over their data. Requesting explicit **opt-in consent** ensures transparency and user autonomy. Simply anonymizing data or burying consent in legal text violates ethical data-use standards.  


---

## Question 59

**Question:**  
Which of the following best describes an essential characteristic that distinguishes a recursive algorithm from a nonrecursive one?

**Options:**  
A. Having a single parameter  
B. Using an accumulator to store intermediate results  
C. Making progress toward a solution by solving a smaller version of the problem  
D. Returning a fixed value in the base case  

**Correct Answer:** C  

**Explanation:**  
Recursion involves calling the same function on smaller inputs until a base case is reached. Progress toward the base case is what prevents infinite recursion. Nonrecursive (iterative) solutions typically use loops instead.  


---

## Question 60

**Question:**  
Consider the incomplete procedure below, which is intended to return the index of the smallest element in the integer array `data`.

```java
int positionOfSmallestValue (int[] data, int length)
    int guess ← 0
    for (int i ← 1; i < length; i ← i + 1)
        /* missing code */
    end for
    return guess
end positionOfSmallestValue
```

Which code segment should replace `/* missing code */` so that the procedure works as intended?

**Options:**  
A.
```java
if (data[i] < guess)
    guess ← data[i]
end if
```
B.
```java
if (data[i] < guess)
    data[i] ← guess
end if
```
C.
```java
if (data[i] < data[guess])
    i ← guess
end if
```
D.
```java
if (data[i] < data[guess])
    guess ← i
end if
```

**Correct Answer:** D  

**Explanation:**  
The algorithm compares the current element with the smallest known element. When a smaller value is found, the index `i` replaces `guess`. At the end, `guess` holds the index of the smallest element.  




---

## Question 61

**Question:**  
Taking massive open online courses (MOOCs) is one example of using the Internet for education. MOOCs allow students from all parts of the world to take a course simultaneously. Some MOOCs are managed by private organizations and others by colleges and universities. Which of the following statements is true about the positive and negative impacts of online learning using MOOCs?

**Options:**  
A. MOOCs allow virtually unlimited enrollment, but face-to-face communication is limited.  
B. MOOCs are free and accredited but provide only certificates of completion.  
C. MOOCs have high course-completion rates, but the number of available courses is limited.  
D. MOOCs provide one-on-one access to instructors, but access to course materials is only available while the course is in session.  

**Correct Answer:** A  

**Explanation:**  
MOOCs can enroll thousands of students globally, providing broad access to education. However, this scalability limits interpersonal and face-to-face communication. Emotional and tonal nuances are often lost in digital formats.  
 

---

## Question 62

**Question:**  
An algorithm was written for drawing the part of a line segment that lies within a given drawing window. The algorithm uses simple tests to determine if a line segment lies entirely inside or outside the window. It only finds intersections with the border when both tests fail. This approach represents which of the following problem-solving strategies?

**Options:**  
A. Building a solution by combining small pieces of the solution one at a time and in sequence  
B. Expressing a large problem in terms of smaller, similarly structured problems  
C. Guessing a solution, refining it iteratively  
D. Solving easy cases first and hard cases only when necessary  

**Correct Answer:** D  

**Explanation:**  
The algorithm first handles simple cases—lines fully inside or outside the window—before performing complex computations for partial intersections. This exemplifies **“solving easy cases first”** to reduce unnecessary computation.  


---

## Question 63

**Question:**  
Consider a `Fraction` class:

```java
public class Fraction {
    public int numerator;
    public int denominator;
    public Fraction(int n, int d) { /* implementation not shown */ }
    public normalize() { /* implementation not shown */ }
}
```

The `normalize()` method reduces the fraction to lowest terms. For instance, if `numerator = 12` and `denominator = 15`, calling `normalize()` updates them to 4 and 5.  

Given:  
```java
Fraction f = new Fraction(12, 15);
```
Which code segment correctly prints `4/5`?

**Options:**  
A.
```java
f.normalize();
print f.numerator;
print "/";
print f.denominator;
```
B.
```java
f.normalize(numerator, denominator);
print f;
```
C.
```java
print f.normalize(numerator);
print "/";
print f.normalize(denominator);
```
D.
```java
f.normalize();
print numerator;
print "/";
print denominator;
```

**Correct Answer:** A  

**Explanation:**  
After `f.normalize()` simplifies the fraction, printing `f.numerator` and `f.denominator` accesses the correct instance variables (4 and 5). Accessing undeclared variables (as in D) would result in errors.  


---

## Question 64

**Question:**  
The Caesar cipher encrypts words by shifting each letter a fixed number of positions in the alphabet. For example, with a shift of 2, “zoo” becomes “bqq.” Which classroom activity best demonstrates this cipher’s vulnerability?

**Options:**  
A. Analyzing the frequency of letters in the encrypted text  
B. Using a program to encrypt words  
C. Using public and private key encryption  
D. Viewing program code for Caesar cipher encoding and decoding  

**Correct Answer:** A  

**Explanation:**  
Frequency analysis reveals how easily Caesar ciphers can be broken, showing letter patterns unique to natural language. This hands-on approach helps students recognize why more advanced ciphers are needed.  


---

## Question 65

**Question:**  
Arrange the following numbers from least to greatest:

- 71 (base 10)  
- 1000110 (base 2)  
- 48 (base 16)  
- 73 (base 10)

**Correct Answer:** 1000110 (base 2), 71 (base 10), 48 (base 16), 73 (base 10)  

**Explanation:**  
Convert all numbers to base 10:  
- 1000110₂ = 64 + 4 + 2 = 70  
- 48₁₆ = 4×16 + 8 = 72  
Thus, the order from least to greatest is: **70, 71, 72, 73.**  




---

## Question 66

**Question:**  
Consider the following pseudocode procedure.

```java
// precondition: n ≥ 0
int f(int n)
    if (n == 0)
        return 0
    end if
    if (n > 0)
        return n + f(n - 1)
    end if
end f
```

Which of the following procedures is equivalent to `f`?

**Options:**  
A. Infinite loop with both `i` and `n` incremented  
B. Adds 1 repeatedly to `x`  
C. Uses loop to sum values from n down to 0  
D. Adds `x` to `n` repeatedly but never updates `x`  

**Correct Answer:** C  

**Explanation:**  
The recursive procedure computes the sum of integers from 0 to *n*. Option (C) correctly uses a `for` loop to add all integers from `n` to 0 to `x`, producing the same result as the recursive sum.  


---

## Question 67

**Question:**  
The pseudocode procedure `assignGrade` is intended to return a letter grade (A–F) based on the following table:

| Score Range | Letter Grade |
|--------------|--------------|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 69 or less | F |

Which of the following pseudocode procedures correctly implements the `assignGrade` procedure?

**Options:**  
A. Sequential if statements overwriting result  
B. Ordered conditional returns  
C. Nested ifs with unreachable code  

**Correct Answer:** B  

**Explanation:**  
Option (B) uses an ordered sequence of comparisons and immediate returns. Once a condition is met, the function exits, ensuring correctness. Options (A) and (C) produce incorrect or unreachable behavior.  


---

## Question 68

**Question:**  
Which of the following is the best way to obtain end-user feedback during web development?

**Options:**  
A. A/B testing  
B. Managerial code reviews  
C. Scrum stand-up meetings  
D. Unit testing  

**Correct Answer:** A  

**Explanation:**  
A/B testing randomly presents users with one of two page versions differing in one feature, allowing data collection on user engagement and effectiveness. It’s a direct, data-driven method of user feedback.  


---

## Question 69

**Question:**  
Which statement best describes a difference between code written in a high-level programming language and code written in a low-level programming language?

**Options:**  
A. High-level code uses more abstractions  
B. High-level code is harder to maintain  
C. High-level code is more optimized for hardware  
D. High-level code is less portable  

**Correct Answer:** A  

**Explanation:**  
High-level languages provide abstraction from hardware through constructs like variables and control flow, improving readability and portability. Low-level languages, like assembly, require manual hardware control.  


---

## Question 70

**Question:**  
To teach Java List objects, students are assigned to simulate a five-card-draw poker game. Which of the following pieces of student feedback are examples of obstacles to equal access?

**Select all that apply.**

**Options:**  
A. I’ve never played cards, so I had to learn how a deck works.  
B. I struggled with avoiding duplicates.  
C. I couldn’t figure out how to initialize the List.  
D. I didn’t know poker rules, so I had to research them.  

**Correct Answers:** A, D  

**Explanation:**  
Both (A) and (D) involve lack of prior cultural or domain exposure rather than programming skill, representing **non-technical barriers** to equitable participation.  


---

## Question 71

**Question:**  
Each employee’s ID number is stored in 32 bits. Which of the following statements about these IDs is true?

**Options:**  
A. Writing the greatest possible ID in hexadecimal requires 8 digits.  
B. Writing it in hexadecimal requires 16 digits.  
C. Writing it in decimal requires 5 digits.  
D. Writing it in decimal requires 8 digits.  

**Correct Answer:** A  

**Explanation:**  
A 32-bit number represents 4,294,967,296 possible values. Each hexadecimal digit represents 4 bits, so 8 hex digits are required to express the full range.  


---

## Question 72

**Question:**  
A drawing program uses `setPosition(x, y)` and `drawTo(x, y)` to make a pattern on a 5×5 grid. Which pseudocode completes the pattern correctly?

**Options:**  
A. x loops increasing, y loops decreasing by 2  
B. x loops decreasing by 2, y decreasing by 1  
C. y outer loop, x increases by 2  
D. y decreases by 2, x decreases by 1  

**Correct Answer:** D  

**Explanation:**  
Option (D) correctly iterates downward in both axes, alternating between horizontal and diagonal line segments to recreate the pattern shown in grid R.  


---

## Question 73

**Question:**  
Which of the following data types is the best choice for storing a worker’s hourly wage and computing total weekly earnings?

**Options:**  
A. float  
B. int  
C. String  
D. boolean  

**Correct Answer:** A  

**Explanation:**  
Floating-point variables store both integer and fractional values, making them ideal for representing currency calculations with decimals.  


---

## Question 74

**Question:**  
Students download population data for analysis. Which file format is best suited for programmatic analysis?

**Options:**  
A. CSV  
B. JPEG  
C. HTML  
D. PDF  

**Correct Answer:** A  

**Explanation:**  
CSV (comma-separated values) is a structured, plain-text format compatible with spreadsheets and databases, ideal for importing and analyzing data computationally.  


---

## Question 75

**Question:**  
A program executes instructions using a fetch-decode-execute cycle. The program counter holds the memory address of the next instruction. Which order correctly performs the cycle?

**Options:**  
A. Fetch → Execute → Increment  
B. Fetch → Increment → Execute  
C. Increment → Execute → Fetch  
D. Execute → Increment → Fetch  

**Correct Answer:** B  

**Explanation:**  
After fetching and decoding an instruction, the **program counter** increments to the next instruction before execution. This order ensures sequential flow unless altered by control instructions.  


---

## Question 76

**Question:**
Which of the following is an example of single sign-on (SSO)?

**Options:**
A. Accessing a travel Web site after completing user authentication on a social media Web site
B. Entering a user ID and password to access a banking Web site
C. Entering an access token sent to a smartphone after entering a user ID and password on an e-mail Web site
D. Using a Web browser to store login and password information for various Web sites

**Correct Answer:** A

**Explanation:**
Single sign-on (SSO) allows users to authenticate once and gain access to multiple applications without needing to re-enter credentials. A social sign-on, such as using your Facebook or Google login to access a third-party travel site, is a specific example of SSO.


---

## Question 77

**Question:**
Consider the following recursive procedure.

```java
int mystery (int num)
    if (num ≤ 1)
        return 1
    end if
    return num * mystery(num - 1)
end mystery
```

Which of the following procedures are equivalent to `mystery`?
*(Select all that apply.)*

**Options:**
A. `enigma` – accumulator initialized to 0
B. `puzzle` – accumulator initialized to 1, multiplies 1 through `num`
C. `riddle` – accumulator initialized to 1, multiplies each integer from 1 to `num`

**Correct Answers:** B, C

**Explanation:**
The recursive method `mystery` computes the **factorial** of `num`. Both `puzzle` and `riddle` correctly initialize the accumulator to 1 and multiply through the full range of values, returning the same product as `mystery`. Option (A) initializes `result` to 0, producing an incorrect result.


---

## Question 78

**Question:**
Consider the following two code segments:

**Code segment A**

```java
class A {
    String message = "code segment A";
    String display() {
        return "Test message " + message;
    }
}

class Test {
    A temp = new A();
    void show() {
        print(temp.display());
    }
}
```

**Code segment B**

```java
void display(String m) {
    print("Test message " + m);
}
String message = "code segment B";
display(message);
```

Which of the following best describes the type of programming languages used in code segments A and B?

| Code Segment A  | Code Segment B |
| --------------- | -------------- |
| Object-oriented | Procedural     |

**Correct Answer:** B

**Explanation:**
Code segment A defines classes and methods—characteristic of **object-oriented programming (OOP)**—where data and behavior are encapsulated. Code segment B uses standalone procedures without object encapsulation, making it **procedural programming**.


---

## Question 79

**Question:**
The data in the following spreadsheet are the responses to one question of a survey that asked,
“*How many siblings do you have?*” The survey was given to five small groups A–E.

|   | A            | B | C    | D    | E |
| - | ------------ | - | ---- | ---- | - |
| 1 | 2            | 3 | 2    | none | 2 |
| 2 | only child   | ? | four | 3    | 2 |
| 3 | fewer than 3 | 1 | 3    | 2    | 6 |

In order to calculate the average number of siblings, some of the data must be modified, while other cells must be removed. Which of the following cells must be **removed**?
*(Select all that apply.)*

**Options:**
A. A2
B. A3
C. B2
D. C2
E. D1

**Correct Answers:** B, C

**Explanation:**
Cells A3 (“fewer than 3”) and B2 (“?”) cannot be converted into numeric values, so they must be removed. The remaining cells can be converted to numeric equivalents for averaging.


# Praxis Computer Science (5652) Practice Test — Extracted MCQs and Explanations

---

## Question 80

**Question:**  
Which of the following is the most effective way to prevent a successful cyberattack of a computer system?

**Options:**  
A. Disable the use of e-mail on the computer system  
B. Disconnect the computer system from the Internet  
C. Make sure all security software is up-to-date  
D. Use a strong password  

**Correct Answer:** B  

**Explanation:**  
Cyberattacks are launched from one or more computers against another computer or a network through the Internet. The most effective way to prevent a successful cyberattack is to **disconnect the computer system from the Internet** entirely. While using updated security software and strong passwords are important preventive measures, only full disconnection ensures complete protection from remote attacks.  



# Praxis Computer Science (5652) Practice Test — Extracted MCQs and Explanations

---

## Question 81

**Question:**  
Which of the following pseudocode segments implements the flowchart shown below?

```java
int n ← 10
int s ← 0
```
*(The block of code repeatedly adds `n` to `s` and decrements `n` until `n = 0`.)*

**Options:**  
A.  
```java
if (n == 0)
    s ← s + n
    n ← n - 1
end if
```
B.  
```java
if (n > 0)
    s ← s + n
    n ← n - 1
end if
```
C.  
```java
while (n == 0)
    s ← s + n
    n ← n - 1
end while
```
D.  
```java
while (n > 0)
    s ← s + n
    n ← n - 1
end while
```

**Correct Answer:** D  

**Explanation:**  
The block of two statements (`s ← s + n` and `n ← n - 1`) must execute **repeatedly** for all positive values of `n`. A `while` loop with condition `n > 0` ensures the body executes until `n` becomes 0, matching the described behavior.  

---

## Question 82

**Question:**  
Consider an integer array `A` of length `n`, where indices start at 0 and all elements are positive. For which of the following code segments is the value of `sum` at completion **less than** the sum of all elements in array `A`?

**Options:**  
A.  
```java
int sum = A[0]
for (int j = 1; j < n; j = j + 1)
    sum = sum + A[j]
end for
```
B.  
```java
int sum = 0
for (int j = 0; j < n; j = j + 1)
    sum = sum + A[j]
end for
```
C.  
```java
int sum = 0
int j = n
do
    j = j - 1
    sum = sum + A[j]
while (j ≥ 1)
```
D.  
```java
int sum = 0
int j = 1
while (j < n)
    sum = sum + A[j]
    j = j + 1
end while
```

**Correct Answer:** D  

**Explanation:**  
This loop begins summing at index 1 rather than 0, skipping `A[0]`. As a result, the computed `sum` excludes one element, making it less than the total of all array elements.  


---

## Question 83

**Question:**  
Match the following data descriptions to their most appropriate data types:

| Data Description | Data Type |
|------------------|------------|
| A dollar amount | Floating-point |
| The state of a check box | Boolean |
| A year | Integer |
| A name | String |

**Correct Match:** A dollar amount → Floating-point, Check box → Boolean, Year → Integer, Name → String  

**Explanation:**  
- A **dollar amount** may include decimals, so it uses a floating-point type.  
- A **check box** has two states (true/false), making it Boolean.  
- A **year** is an integer value.  
- A **name** is a sequence of characters, hence a String.  


---

## Question 84

**Question:**  
A homeowner wants to determine how changes in temperature affect humidity. Temperature and humidity readings are collected hourly for 48 hours and entered into a spreadsheet. Which of the following visualizations is most appropriate?

**Options:**  
A. Two histograms — one for temperature, one for humidity  
B. Two pie charts — one for temperature, one for humidity  
C. A scatterplot using temperature as the independent variable and humidity as the dependent variable  
D. Two time-series plots — one for temperature, one for humidity  

**Correct Answer:** C  

**Explanation:**  
A scatterplot best shows **how one variable changes in relation to another**. Here, temperature serves as the **independent variable**, and humidity as the **dependent variable**, making a scatterplot the correct visualization.  


---

## Question 85

**Question:**  
Which of the following is an **advantage of cloud-based storage**?

**Options:**  
A. It gives users access to files from any Internet-connected device.  
B. It gives users the greatest control over their files.  
C. It gives users the most secure way to store files.  
D. It gives users the quickest way to access files.  

**Correct Answer:** A  

**Explanation:**  
Cloud storage enables **remote file access** from any Internet-enabled device, supporting collaboration and mobility. However, it trades off physical control and is typically slower and less secure than local storage.  




# Praxis Computer Science (5652) Practice Test — Extracted MCQs and Explanations

---

## Question 86

**Question:**  
A traveler is keeping a digital photo journal. When the journal is ready, it will be posted on an Internet Web site that offers controlled access. Which of the following presents the greatest risk to the traveler’s privacy?

**Options:**  
A. Posting the journal using HTTP  
B. Posting the journal using HTTPS  
C. Posting the journal using public Wi-Fi and HTTP  
D. Posting the journal using public Wi-Fi and HTTPS  

**Correct Answer:** C  

**Explanation:**  
Public Wi-Fi combined with unencrypted HTTP exposes the data being transmitted, allowing attackers to intercept private information. HTTPS encrypts the data, protecting it during transmission, but HTTP does not. Therefore, using **public Wi-Fi with HTTP** poses the greatest risk to privacy.  


---

## Question 87

**Question:**  
A student wants to write an expression that will generate a random integer between 5 and 10, inclusive. The expression should take on the values 5, 6, 7, 8, 9, or 10 with approximately equal likelihood. The student writes the expression below:

```java
round(random() * 5) + 5
```

The expression fails to generate a random integer with the desired properties. Which of the following describes how the integers generated by the expression differ from the intended result?

**Options:**  
A. The expression generates noninteger numbers (for example, 5.5).  
B. The expression generates integer numbers outside the desired range (for example, 11).  
C. The expression fails to generate all integers in the desired range (for example, 7 is never generated).  
D. The expression generates all integers in the desired range, but the values are not all approximately equally likely.  

**Correct Answer:** D  

**Explanation:**  
The use of `round(random() * 5)` causes some output values to occur with different probabilities because of how rounding divides the range of possible numbers. As a result, 6–9 are twice as likely as 5 or 10. All integers from 5–10 appear, but they are **not equally likely**.  


---

## Question 88

**Question:**  
Consider a program written in an object-oriented programming language. Which of the following statements are true if class **B** is a child class of parent class **A**?  
*(Select all that apply.)*

**Options:**  
A. Public methods in A are accessible in B and can be overloaded by other methods in B.  
B. Public methods in A are accessible in B and can be overridden by other methods in B.  
C. Public methods in B are accessible in A and can be overloaded by other methods in A.  
D. Public methods in B are accessible in A and can be overridden by other methods in A.  

**Correct Answers:** A, B  

**Explanation:**  
Public methods in a **parent class** are accessible to its **child class**.  
- **Overloading** occurs when methods have the same name but different parameters.  
- **Overriding** occurs when a child class defines a new version of a parent method with the same signature.  
Options (C) and (D) are incorrect because parent classes cannot access child class methods.  


---

## Question 89

**Question:**  
Which of the following is a factor that affects the size of a digital audio file?

**Options:**  
A. Bit rate  
B. Intensity  
C. Tone  
D. Volume  

**Correct Answer:** A  

**Explanation:**  
The **bit rate**—the number of bits processed per second—directly determines the data density and, therefore, the file size. A higher bit rate produces larger files and higher audio quality. The other options (intensity, tone, volume) are perceptual qualities, not encoding parameters.  


---

## Question 90

**Question:**  
Match each **pillar of cybersecurity** with its corresponding example of a violation:

| Violation Example | Pillar Violated |
|--------------------|----------------|
| A hospital posts all patient medical records on its public Web site. | Confidentiality |
| A student uses a bug in a teacher’s grade-book software to change all grades to As. | Integrity |
| Access to a company’s Web site is slowed because of a denial-of-service (DoS) attack. | Availability |
| An employee changes file metadata to claim credit for another’s work. | Nonrepudiation |
| A private investigator uses a copy of a coworker’s fingerprint to gain computer access. | Authentication |

**Correct Answer:** Confidentiality, Integrity, Availability, Nonrepudiation, Authentication  

**Explanation:**  
Each of the five **pillars of cybersecurity** corresponds to a fundamental protection principle:  
- **Confidentiality:** Unauthorized access to sensitive data (e.g., patient records).  
- **Integrity:** Data must remain accurate and unaltered (e.g., grade changes).  
- **Availability:** Services must remain accessible (e.g., DoS attacks).  
- **Nonrepudiation:** Actions must be traceable to their source (e.g., falsified metadata).  
- **Authentication:** Verifying identity (e.g., fake fingerprint use).  




# Praxis Computer Science (5652) Practice Test — Extracted MCQs and Explanations

---

## Question 91

**Question:**  
Consider a plaintext string that consists of uppercase letters. A certain encryption algorithm replaces each letter in the string with a ciphertext letter as follows: the algorithm selects a letter and moves a fixed number of positions forward in the English alphabet. If the end of the alphabet is reached, it wraps around to the beginning.

The line of code implementing this is:

```java
ltr = (((ltr - 'A') + offset) % 26) + 'A';
```

If `offset` = 3 and the plaintext string is "SAY", what is the ciphertext output?

**Options:**  
A. PXV  
B. RZX  
C. TBZ  
D. VDB  

**Correct Answer:** D  

**Explanation:**  
Since V is the third letter after S, D is the third letter after A, and Y wraps around to B, the ciphertext produced is **"VDB"**. The modulo operation correctly wraps alphabet positions from Z to A.  


---

## Question 92

**Question:**  
Consider the following method for a class `Closet`. Assume `Closet` objects contain `Hanger` and `Shoe` objects.

**Method Explanation:**  
```java
void update(int z, String w)
```
- If `w` = "a", adds `z` Hanger objects.  
- If `w` = "r", adds `z` Shoe objects.  
- Otherwise, does nothing.

Given that a `Closet` object `myCloset` has been declared and initialized, which method call correctly adds **10 Shoe objects** to `myCloset`?

**Options:**  
A. `myCloset.update(10, "a")`  
B. `myCloset.update("a", 10)`  
C. `myCloset  update(10, "r")`  
D. `myCloset.update(10, "r")`  

**Correct Answer:** D  

**Explanation:**  
The correct call must invoke the method on the instance `myCloset`, passing `10` as the number of items and "r" to indicate shoes. Therefore, `myCloset.update(10, "r")` is the correct form.  


---

## Question 93

**Question:**  
Consider the following pseudocode procedure, where the index of array `x` starts at 0:

```java
// precondition: 0 ≤ y < z < length of x
int sumItems(int[] x, int y, int z)
    int s = 0
    int i = y
    while (i < z)
        s = s + x[i]
        i = i + 1
    end while
    return s
end sumItems
```

Now consider:

```java
int[] a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int r = sumItems(a, 2, 5) + sumItems(a, 4, 6);
```

What is the value of `r` after execution?

**Options:**  
A. 17  
B. 23  
C. 29  
D. 34  

**Correct Answer:** B  

**Explanation:**  
`sumItems(a, 2, 5)` adds elements 3 + 4 + 5 = 12.  
`sumItems(a, 4, 6)` adds elements 5 + 6 = 11.  
The total `r` = 12 + 11 = **23**. The `while` condition excludes the element at index `z`.  


---

## Question 94

**Question:**  
A city is conducting a census and collects household-level data on income, education, age, and race. Names and addresses are **not** collected to preserve anonymity. Which of the following describes a valid spreadsheet visualization using this data?

**Options:**  
A. Report total number of college graduates living on each street.  
B. Use a filter to convert ages to birth years.  
C. Use a formula to estimate average income per household.  
D. Sort by age to identify the oldest person.  

**Correct Answer:** C  

**Explanation:**  
Because individual names and addresses are not collected, only aggregate statistics like **average income** can be computed. Option (C) is valid, while the others require identifying data that is unavailable.  


---

## Question 95

**Question:**  
Which of the following best describes an appropriate use of a wireless communication technology?

**Options:**  
A. Using Bluetooth on a boat to call rescue vessels  
B. Using cellular communication in a sparsely populated area to connect a mobile device to the Internet  
C. Using satellite communication to connect a wireless keyboard to a nearby computer  
D. Using Wi-Fi to connect a laptop and router within a house  

**Correct Answer:** D  

**Explanation:**  
Wi-Fi is designed for wireless connectivity over a short range, such as within a home network between a laptop and router. Bluetooth is for very short-range communication, and satellite or cellular options are unnecessary or unreliable in these contexts.  




# Praxis Computer Science (5652) Practice Test — Extracted MCQs and Explanations

---

## Question 96

**Question:**  
In the digital world, businesses and individuals often need to decide between local and cloud-based storage options. Each option has trade-offs.

Cloud storage can be a benefit to businesses and individuals because it often has more ____ (i) ____ . Cloud storage can be a risk to businesses and individuals because it often has less ____ (ii) ____ .

**Options:**  
Blank (i):  
A. direct control of storage infrastructure  
B. flexibility to scale up or down  
C. long-term reliance on internal IT capabilities  

Blank (ii):  
D. dependence on Internet connections  
E. direct control of storage infrastructure  
F. flexibility to scale up or down  

**Correct Answers:** (i) B, (ii) E  

**Explanation:**  
Cloud storage provides **greater flexibility to scale up or down** based on demand, reducing the need for local infrastructure. However, users give up **direct control of storage infrastructure** since the cloud provider manages hardware and maintenance.  


---

## Question 97

**Question:**  
A software application that sends encrypted data over the Internet uses a popular pseudorandom number generator. The application uses a seed value of 1024. Which of the following statements about the application must be true?

**Options:**  
A. The length of the key used to encrypt the data is 1024 bits.  
B. The sequence of random numbers generated will repeat every 1024 numbers.  
C. The sequence of random numbers generated by all instances of the application will be the same.  
D. Increasing the seed value from 1024 to 2048 would make the application’s data significantly more resistant to hacking.  

**Correct Answer:** C  

**Explanation:**  
Pseudorandom number generators are **deterministic**. Using the same seed value (1024) ensures that each instance of the application generates the **same sequence of random numbers**. Changing the seed value does not inherently improve encryption security.  


---

## Question 98

**Question:**  
A programmer writes the following method in class `Class1` in an object-oriented language:

```java
public void printResults (String data)
    // implementation not shown
end printResults
```

The programmer attempts to write several overloaded `printResults` methods in class `Class2`, which extends `Class1`. Which of the following methods **overrides** the original method but does **not overload** it?

**Options:**  
A. `public void printResults (int data)`  
B. `public void printResults (String data2)`  
C. `public void printResults (float data)`  
D. `public void printResults (int data, String data2)`  

**Correct Answer:** B  

**Explanation:**  
The method `public void printResults(String data2)` has the **same name and parameter type** as the original, so it overrides the original instead of overloading it. Overloaded methods must differ in parameter types or count.  


---

## Question 99

**Question:**  
Which of the following is an example of crowdsourcing?

**Options:**  
A. A language-learning platform offers a free service to allow anyone to learn a language.  
B. A language-learning platform builds a collection of documents in native languages by soliciting aid from users of its Internet services.  
C. A language-learning platform offers a free language translator that automatically collects user data to improve the translator.  
D. A language-learning platform sells user data for profit to offer other free services.  

**Correct Answer:** B  

**Explanation:**  
Crowdsourcing relies on **distributed collaboration**, where users contribute skills or knowledge to a shared project. Option (B) fits this model, as users collectively translate and contribute documents. The other options involve data collection or monetization, not true crowdsourced collaboration.  


---

## Question 100

**Question:**  
Why might a developer embed a script in HTML code?

**Options:**  
A. Because scripts are needed to control presentation of content styles  
B. Because scripts are needed to protect the copyrights of the page  
C. Because scripts are needed to provide semantic markup of content  
D. Because scripts are needed to support dynamic Web page behavior  

**Correct Answer:** D  

**Explanation:**  
Scripts are used to enable **dynamic Web page behavior**, such as form validation, interactivity, and real-time updates. HTML alone defines structure and content, while CSS controls appearance. Copyright and semantic markup are not managed by scripting.  



