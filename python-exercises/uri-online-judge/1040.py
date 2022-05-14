# results = input().split(" ")

# N1, N2, N3, N4 = results

# N1 = float(N1)
# N2 = float(N2)
# N3 = float(N3)
# N4 = float(N4)

N1 = 2.0
N2 = 6.5
N3 = 4.0
N4 = 9.0


average = (N1 * 0.2) + (N2 * 0.3) + (N3 * 0.4) + (N4 * 0.1)

print("Media: {:.1f}".format(average))

if average >= 7.0:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado")
elif (average >= 5) and (average < 7):
    print("Aluno em exame.")
    exam_result = input()
    exam_score = float(exam_result)
    print("Nota do exame: {:.1f}".format(exam_score))

    final_result = (average + exam_score)/2

    if final_result >= 5:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(final_result))
    
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(final_result))