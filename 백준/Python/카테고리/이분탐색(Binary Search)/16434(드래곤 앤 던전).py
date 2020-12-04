
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
stages = [list(map(int, input().split())) for i in range(N)]

lo = 0
hi = 9223372036854775800


def fight(ai, hi, hc, H):
    mon_h = hi
    mon_a = ai

    if hc % ai == 0:
        live_count = hc//ai
    else:
        live_count = hc//ai + 1

    if hi % H == 0:
        monster_count = hi//H
    else:
        monster_count = hi//H + 1

    if live_count >= monster_count:
        hc -= (monster_count-1)*ai
        if hc <= 0:
            hc += ai
        return hc
    else:
        return False

    # while True:
    #     # 용사의 공격력 HATK만큼 몬스터의 생명력을 깎습니다.
    #     mon_h -= H
    #     # 몬스터의 생명력이 0 이하이면 전투가 종료되고 용사는 다음 방으로 이동합니다.
    #     if mon_h < 1:
    #         return hc
    #     # 몬스터의 공격력만큼 용사의 생명력 HCurHP를 깎습니다.
    #     hc -= mon_a
    #     # 용사의 생명력이 0 이하이면 전투가 종료되고 용사는 사망합니다.
    #     if hc < 1:
    #         return False
    #     # 다시 1부터 진행합니다.


def portion(ai, hi, hc, H, mid):
    H += ai
    if hc+hi > mid:
        hc = mid
    else:
        hc += hi
    return [H, hc]  # 공격력과 현재 hc 리턴


def go(mid, H):
    hc = mid
    H = H
    for stage in stages:
        # print('stage진행 : 현재 에너지={},현재 공격력={}'.format(hc, H))
        ti, ai, hi = stage
        if ti == 1:
            result = fight(ai, hi, hc, H)
            if not result:
                return False  # 죽었을 경우 false 리턴
            else:
                hc = result  # 살았을 경우 남은 hc 리턴
        else:
            result = portion(ai, hi, hc, H, mid)
            H = result[0]
            hc = result[1]
    # print('현재hp={},현재공격력={}'.format(hc, H))
    return True


while lo+1 < hi:
    mid = (lo+hi)//2
    result = go(mid, H)
    # print('lo={},hi={},mid = {}, result ={}'.format(lo, hi, mid, result))
    if result:
        hi = mid
    else:
        lo = mid

print(hi)
