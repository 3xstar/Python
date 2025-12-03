import user_utils as utils
import module

deck = module.generate_card()
player_cards = [module.take_card(deck), module.take_card(deck)]
diller_cards = module.diller_take_cards(deck)
player_cash = 1000
player_bet = 0
print("Добро пожаловать в казино!")
while True:
    print("Ваш баланс: ",player_cash)
    print("1. Сделать ставку")
    print("2. Сыграть")
    print("3. Забрать деньги и уйти")

    action = utils.input_int("Введите номер действия: ")
    if action == 1:
        player_bet = module.make_bet(player_cash)
    elif action == 2:
        if player_bet > 0:
            player_cash -= player_bet
            player_bet = module.game(deck, player_cards, diller_cards, player_bet)
            player_cash += player_bet
            player_bet = 0
        else:
            print("Вы не сделали ставку")
    elif action == 3:
        break
    else:
        print("Неверная команда")

print("Спасибо за игру :з")
print("Ваш баланс: ", player_cash)