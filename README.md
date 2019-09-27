## Random-Walk-On-Financial-Application
This tool was built aiming to produce a close simulation to the cryptocurrency dinamic behavior.
The first step is to analyse the mathematical equation, the compound interest formula:
![equation](http://www.sciweavers.org/tex2img.php?eq=FV%20%3D%20PV%20%20\times%20%20%20\big(1\big%20%2B%20i\big)^{\eta}%20&bc=White&fc=Black&im=png&fs=12&ff=mathdesign&edit=0).

Here we have the Future Value (FV), the Present Value (PV), the Interest Rate (i), and the Number of Periods (n).
When this equation is applied with constant values, the graphic result is shown on the the following image:
![alt text](https://github.com/Heictor/Random-Walk-On-Financial-Application/blob/master/SimpleApplication_1.png)
However, this method is quite far from the real phenomenon, and limited to few number of paralel possibilites.
Using 3D vizualization, it is possible to study a larger number of possible monetary applications, each one with different, but still constant, values for Interest Rate.
![alt text](https://github.com/Heictor/Random-Walk-On-Financial-Application/blob/master/Figure_1.png)

Although, this method continues too much theorical, the next step is to use a random generator function to attribute a new value to Interest Rate at each interval of time, be it month, week, or day. Choosing smaller intervals between each changing of value will result in a more efficienty and "realistic" approach, but it will cost more from the hardware.
