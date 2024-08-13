def deposit_money():
    account_id = int(input())
    deposit_money = int(input())

    for i in range(len(account_list)):
        if account_id == account_list[i]:
            account_list[i].balance -= deposit_money
            print("입금완료")
            return
    print("유효하지 않는 ID입니다.")