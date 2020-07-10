import time
#输入
num1 = str(input('请输入第一个大数'))
num2 = str(input('请输入第二个大数'))
#测试
# num1 = "2649821731631836529481632803462831616487712734074314936141303241873417434716340124362304724324324324324323412121323164329751831"
# num2 = "1045091731748365195814509145981509438583247509149821493213241431431319999999999999999999999999999999999999999999999999341344779"
startTime = time.time()
n1 = list(num1)
n2 = list(num2)
def mul(n1,n2):
    n1 = list(map(int, n1))
    n2 = list(map(int, n2))
    n1.reverse()
    n2.reverse()
    n3=[]
    # print(n1,n2)
    for i0 in range(len(n1)+len(n2)):
        n3.append(0)
    for i1 in range(len(n1)):
        for i2 in range(len(n2)):
            n3[i1+i2] += n1[i1]*n2[i2]
    for i3 in range(len(n3)):
        if(n3[i3]>9):
            n3[i3+1] += n3[i3]//10
            n3[i3] = n3[i3] % 10
    n3.reverse()
    # print(n3)
    result_num = ''.join(str(i) for i in n3)
    return result_num

print('输出结果',mul(n1,n2))
print('耗时{0}ms'.format(time.time() - startTime))


