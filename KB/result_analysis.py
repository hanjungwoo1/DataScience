
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

        gt = data[0].strip()
        pred = data[1].strip()

        print(gt, pred)

        if len(gt) != len(pred):
            numeric_count += 1


print("글자수 틀린 데이터 길이 : ", numeric_count)
print("글자수 일치율 : ", numeric_count / count * 100)
print("전체 데이터 길이 : ", count)
