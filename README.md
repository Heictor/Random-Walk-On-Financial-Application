## Random-Walk-On-Financial-Application
This tool was built aiming to produce a close simulation to the cryptocurrency dinamic behavior.
The first step is to analyse the mathematical equation, the compound interest formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_phv&space;\huge&space;FV&space;=&space;PV&space;\times&space;\left&space;{(1&plus;i\right&space;)^{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;\huge&space;FV&space;=&space;PV&space;\times&space;\left&space;{(1&plus;i\right&space;)^{n}}" title="\huge FV = PV \times \left {(1+i\right )^{n}}" /></a>.

Here we have the Future Value (FV), the Present Value (PV), the Interest Rate (i), and the Number of Periods (n).
When this equation is applied with constant values, the graphic result is shown on the the following image:
![alt text](https://github.com/Heictor/Random-Walk-On-Financial-Application/blob/master/SimpleApplication_1.png)

However, this method is quite far from the real phenomenon, and limited to few number of paralel possibilites.
Using 3D vizualization, it is possible to study a larger number of possible monetary applications, each one with different, but still constant, values for Interest Rate.

![alt text](https://github.com/Heictor/Random-Walk-On-Financial-Application/blob/master/Figure_1.png)

Although, this method continues too much theorical, the next step is to use a random generator function to attribute a new value to Interest Rate at each interval of time, be it month, week, or day. Choosing smaller intervals between each changing of value will result in a more efficienty and "realistic" approach, but it will cost more from the hardware.
So now the script is able to create a tridimensional visualization of the cryptocurrency behavior, as shown on the following image:

![alt text](https://github.com/Heictor/Random-Walk-On-Financial-Application/blob/master/3D_i_n_FV.png)

It is important to remember that when we run this code, we are able to use interactive option to move the plot around as well as needed to better understand what it is supposed to show. But considering that this kind of interactivity does not have support at every platform, this Python script also produces 2 more bidimensional plots, the analysis of Interest Rate along with Future Value:

![alt text](https://github.com/Heictor/Random-Walk-On-Financial-Application/blob/master/i_FV.png)

The second 2D plot shows the variation of Future Value along with the Number of Periods (Months):
![alt text](https://github.com/Heictor/Random-Walk-On-Financial-Application/blob/master/n_FV.png)
