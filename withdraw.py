from account_list import AccountList

def withdraw_money():
    account_id = int(input("계좌ID: "))
    withdraw_money_ = int(input("출금액: "))

    for i in range(len(AccountList.account_list)):
        if account_id == AccountList.account_list[i]:
            if AccountList.account_list[i].balance >= withdraw_money_:
                AccountList.accoutnt_list[i].balance -= withdraw_money_
                print("출금완료")
                return
            else:
                print("잔액부족")
                return
            
    print("유효하지 않는 ID입니다.")
        