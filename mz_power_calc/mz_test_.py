# -*- coding: cp949 -*-
#�����̳� ������ �ִ� ���
def count_single_word(s):
    single_word_cnt = 0
    for word in s:
        if word >= '��' and word <= '��':
            single_word_cnt += 1
        if word >= '��' and word <= '��':
            single_word_cnt += 1
    return single_word_cnt

#��,��,�а��� ����
def count_z_b (s):
    z_cnt, b_cnt = 0,0
    for word in s:
        if word == "��":
            z_cnt += 1
        elif word == "��":
            b_cnt += 1
            
    return [z_cnt, b_cnt]

#��,��,�� ������ ���� mz�� ��ȯ
def mz_point_count (cnt_list):
    z_cnt,b_cnt = cnt_list
    mz_power_z = [50,70,10,50,60,70,80,100]
    if b_cnt:
        return 100
    elif z_cnt:
        return mz_power_z[z_cnt]
    else:
        return 0

sentence = "�ȳ� ������ ���� ��"
print(count_z_b(sentence))
print(mz_point_count(count_z_b(sentence)),"%")
print("����, ���� ���� :",count_single_word(sentence))



