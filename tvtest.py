from tv import tv

tv1 = tv()

a = tv1.getChannel()
b = tv1.getVolume()
c = tv1.setChannel(30)
d = tv1.setVolume(10)
e = tv1.channelUp()
f = tv1.channelDown()
g = tv1.volumeUp()
h = tv1.volumeDown()
i = tv1.getPower()
m = int(input("The TV is off, enter 1 to turn the tv on! "))
j = tv1.setPower(m)


if j == 1:
    print("The TV is on!")
    print("Default channel: ", a)
    print("Deafault Volume:", b)
    print("New Channel:", c)
    print("New Volume: ", d)
    print("Channel Up: ", e)
    print("Channel Down: ", f)
    print("Volume up: ", g)
    print("Volume Down: ", h)


k = int(input("Enter 0 to turn the TV off! "))

if k == 0:
    print("The TV is off!!")
