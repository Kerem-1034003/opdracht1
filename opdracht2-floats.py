# Ethernet capacity
ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print (maximum_capacity)

# Print capacity used on the ethernet
download_speed_avarage = 96.25
usage = ethernet_speed_mbps / download_speed_avarage
print(usage)

# Speed of light in m/s 
speed_of_light = 299_792_458

# Distance Rotterdam / New York in km
distance_Rotterdam_NewYork = 5_862.03
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) /speed_of_light
print(time_to_reach_NYC)

# welke datatype is het?
type(time_to_reach_NYC)