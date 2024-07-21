# Flatmate-Bill
## Description
This script calculates the monthly flat bill for two individuals based on the number of days they spent in the flat. It utilizes object-oriented programming principles by defining two classes: Flatmate and Bill.
## Features 
- Asks user to enter the bill amount and takes the period for that bill.
- It asks to enter both flatmates name along with the days they spent during that particular period.
- Calculates both persons bill seperately and generates the pdf for visual representation.
## Prerequisites
- python 3.x
- `fpdf` module, to generate pdf
## Installation
Make sure you have `fpdf` module, to install the module
```cmd
pip install fpdf
```
1. Clone the repository
```cmd
git clone https://github.com/Spandana-M-Patil/Flatmate-Bill.git
```
2. Go to the directory
```cmd
cd Flatmate-Bill
```
3. Run the main file
```cmd
python main.py
```
## Usage
1. Enter the bill amount for particular month and provide the month and year (period) for the bill amount.
2. Provide both flatmates name.
3. Enter the number of days individulas spent uring that period in the flat.
4. Now the output or the bill should be paid from both individuals is available on output window as also in the pdf format.
5. User can download the generated pdf to share with other flatmate.
## Example
```cmd
Hey user, Enter the bill amount: 12000
What is the bill period ?(E.g : January 2024) June 2024
What is your name? Jack
How many days you spent in the flat during the bill period? 27
What is the name of the other flatmate? David
How many days David spent in the flat during the bill period? 21
Jack pays: 6750.0
David pays: 5250.0
------------ U directed to the pdf that open's in your default pdf opener ------------
```
## Conclusion
This project broden's my understanding of OOPs concets and I had a fun along the way of creating this project. Looking forward to work more on this OOPs concpets like classes. 
