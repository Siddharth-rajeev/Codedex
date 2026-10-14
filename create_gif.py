import imageio.v2 as iio

filenames = ['team-pic1.png', 'team-pic2.png']
images = []

for filename in filenames:
    img = iio.imread(filename)
    images.append(img)

# Use mimsave (or mimwrite) to write multiple frames into an animated GIF
iio.mimwrite('team.gif', images, duration=500, loop=0)
print("GIF created successfully!")