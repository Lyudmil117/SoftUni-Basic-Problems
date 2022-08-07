width = int(input())
length = int(input())
hight = int(input())
volume_free_space = width * length * hight
volume_boxes = 0
free_space = 0
num_boxes = 0

boxes = input()
while num_boxes <= volume_free_space:
    if boxes == "Done":
        print(f"{volume_free_space - num_boxes} Cubic meters left.")
        break

    boxes = int(boxes)
    volume_boxes = boxes
    num_boxes = num_boxes + boxes
    free_space = abs(volume_free_space - num_boxes)

    if volume_free_space < num_boxes:
        if free_space < volume_free_space:
            print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break

    boxes = input()





