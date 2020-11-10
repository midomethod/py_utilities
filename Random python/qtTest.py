import quaternion as qt

axis = qt.co2qt((0,0,1))    # Clockwise about the k axis
theta = 45
pt = qt.co2qt((3,5,0))

print(qt.rotateLH(pt,axis,theta))
print(qt.rotateRH(pt,axis,theta))
print(qt.rotate(pt,axis,theta))
