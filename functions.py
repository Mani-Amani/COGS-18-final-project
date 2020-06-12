from numpy import random
def create_accel_lst():
    #function creates a random list so we can test it
    lst=[]
    choice=[]
    for i in range(0,100):
        lst.append(random.choice(range(0,100)))
    return(lst)
def calibration_for_xy(lst,avg_noise=0):
    #lst= Type: List our raw data that has been created in create_accel_lst, 
    #avg_noise: Type: Int used to be decreased from the raw data
    #function calibrates the data by using a low pass filter to cancel out noise 
    for i in range(0,len(lst)):
        lst[i]=lst[i]-avg_noise
    return(lst)
def calibration_for_z(lst,avg_noise=0):
    #lst= Type: List our raw data that has been created in create_accel_lst, 
    #avg_noise: Type: Int used to be decreased from the raw data
    #funtcion calculates data by using a low pass filter with addition of subtracting gravitational accelaration
    gravitation_accel=9.81
    #gravitation_accel Int used to decrease from the z-axis data
    for i in range(0,len(lst)):
        #performing the calibration
        lst[i]=lst[i]-avg_noise-gravitation_accel
    return(lst)
def integration_for_distance(lst):
    #Intergration of accelaration using a trazpezodial integration, we acquire speed and distance through this function
    item=0
    #Item Int used as a counter for the while
    distance_total=0
    #distance_total Int used to store the distances after integration
    distance_temp=0
    #distance_temp Int used as a temporary integer to save short time integration numbers
    while (item<len(lst)):
        #used to integrate the first two intevral times so we can get the speed for the interval
        speed_n1= (lst[item]+((lst[item]-lst[item+1])/2))*0.1
        #used to integrate the second two intevral times so we can get the speed for the interval
        speed_n2= ((lst[item+2]+((lst[item+2]-lst[item+3])/2))*0.1)
        #integration of speed gives us displacement
        distance_temp=(speed_n1+((speed_n1-speed_n2)/2))*0.2
        #adding up displacement
        distance_total=distance_total+distance_temp
        #adding our counter to reach the next items
        item=item+4
    return(distance_total)
class Navigator ():
    #navigator class which is our robot that navigates
  
    def calculate_distance(self,accelx,accely,accelz,avg_noise=0):
        #calibrating and calculating the distance in each angle
        accelx=calibration_for_xy(accelx,avg_noise)
        accely=calibration_for_xy(accely,avg_noise)
        accelz=calibration_for_z(accelz,avg_noise)
        #running the integration function for distance
        distancex=integration_for_distance(accelx)
        distancey=integration_for_distance(accely)
        distancez=integration_for_distance(accelz)
        #calculating the distance in 3d
        distance=((distancex**2)+(distancey**2)+(distancez**2)**0.5)
        return (distance)
        