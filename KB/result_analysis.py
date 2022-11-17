
open_path = "../data/OCR/gt_test.txt"



open_path = "result\TPS-ResNet-BiLSTM-CTC-Seed1111_best_accuracy.pth"

with open(open_path+"/log_evaluation_answer.txt", "r", encoding="utf-8") as f:
    line = None

    count = 0
    numeric_count = 0
    while line!= "":
        count += 1
        line = f.readline().strip()
        data = line.split("*")

        if len(data) != 2:
            continue

        gt = data[0]
        pred = data[1]

        print(gt, pred)



print("전체 데이터 길이 : ", count)