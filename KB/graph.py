


x = [1]+ list(range(2000, 50001, 2000))

train_loss = []
valid_loss = []
valid_acc = []

open_path = "saved_models/TPS-ResNet-BiLSTM-CTC-Seed1111/log_train.txt"

with open(open_path, "r") as f:
    line = None

    count = 0
    numeric_count = 0
    while line!= "":
        count += 1
        line = f.readline().strip()

        if count == 1:
            data = line.split(",")

            if len(data) == 3:
                train = data[0].split(":")[1]
                valid = data[1].split(":")[1]
                train_loss.append(float(train))
                valid_loss.append(float(valid))

        if count == 3:
            data = line.split(",")
            if len(data) == 2:

                acc = data[0].split(":")[1]
                valid_acc.append(float(acc))

        if count == 12:
            count = 0


print(x)
print(len(train_loss))
print(len(valid_loss))
print(len(valid_acc))

print(train_loss)
print(valid_loss)
print(valid_acc)



import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
plt.rcParams['figure.figsize'] = (16, 12)
plt.rcParams['font.size'] = 12


fig, ax1 = plt.subplots()
line1 = ax1.plot(x[1:], train_loss[1:], color='green', label="train_loss")
line2 = ax1.plot(x[1:], valid_loss[1:], color='deeppink', label="valid_loss")
ax1.set_xlabel("iterations")

ax2 = ax1.twinx()
line3 = ax2.plot(x[1:], valid_acc[1:], color='purple', label="valid_acc")


lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='center right')
plt.show()