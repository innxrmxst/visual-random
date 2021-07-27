import matplotlib.pyplot as plt
from logic import RandomWalk
# import uuid

rw = RandomWalk(50000)
rw = RandomWalk()
rw.cords_gen()

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(30,30))
point_numbers = range(rw.dot_ammount)

ax.scatter(0,0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)

ax.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues ,edgecolors='none')
ax.plot(rw.x_values, rw.y_values, linewidth=0.4, c=(0, 0.12, 1))

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.tick_params(axis='both', which='major' ,labelsize=14)

def create_image():
    # img_name = str(uuid.uuid4())
    # plt.savefig(f'{img_name}.png', bbox_inches='tight')
    plt.show()
    exit()

create_image()

