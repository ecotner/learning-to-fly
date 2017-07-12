"""
Practice integration program

author: Eric Cotner

Simple numerical integrator using Simpson's rectangle algorithm. There is
much room for improvement, like using different timestep and
"endcap" geometries.
"""

step=0.000001                    #timestep
x=1                             #lower limit of integration
ans=0                           #initializes result to zero
while (ans<1):              #sets upper limit of integration
    ans=ans+(1/x)*step          #function to be integrated
    x=x+step                    #increments dependent variable
print(x)                      #prints answer