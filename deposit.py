from account_list import account_list

def deposit_money():
    account_id = input("계좌ID: ")
    deposit_money = int(input("입금액: "))

    for i in range(len(account_list)):
        if account_id == account_list[i]:
            account_list[i].balance -= deposit_money
            print("입금완료")
            return
    print("유효하지 않는 ID입니다.")