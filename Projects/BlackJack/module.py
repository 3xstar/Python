from random import *
import user_utils as utils

def show_card(cards):
    for card in cards:
        print(card)


def take_card(deck):
    return choice(deck)


def generate_card():
    deck = []
    suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Ace", "Queen", "King"]
    for rank in ranks:
        for suit in suits:
            card = rank, suit
            deck.append(card)
    for i in deck:
        card1 = randint(0, len(deck) - 1)
        card2 = randint(0, len(deck) - 1)
        deck[card1], deck[card2] = deck[card2], deck[card1]
    return deck


def _count_score(cards):
    score = 0
    if len(cards) > 1:
        for card in cards:
            if card[0] == "Jack" or card[0] == "King" or card[0] == "Queen":
                score += 10
            elif card[0] == "Ace":
                score += 11
            else:
                score += card[0]
    return score


def finish_game(player_cards, diller_cards, bet):
    player_win = False
    player_score = _count_score(player_cards)
    diller_score = _count_score(diller_cards)
    print("Карты игрока: ")
    show_card(player_cards)
    print("Карты диллера: ")
    show_card(diller_cards)

    if player_score > 21 and diller_score > 21:
        if player_score > diller_score:
            print("Вы проиграли")
            player_win = False
        else:
            print("Вы выиграли")
            player_win = True
    elif player_score > 21 > diller_score:
        print("Вы проиграли")
        player_win = False
    elif diller_score > 21 > player_score:
        print("Вы выиграли")
        player_win = True
    elif player_score <= 21 and diller_score <= 21:
        if player_score > diller_score:
            print("Вы выиграли")
            player_win = True
        elif player_score < diller_score:
            print("Вы проиграли")
            player_win = False
        elif player_score == diller_score:
            print("Ничья")
            return bet

    bet = _results(player_win, bet)
    return bet


def diller_take_cards(deck):
    diller_cards = [take_card(deck), take_card(deck)]
    while True:
        diller_score = _count_score(diller_cards)
        if diller_score <= 17:
            diller_cards.append(take_card(deck))
        else:
            break
        return diller_cards

def _results(player_win, bet):
    if player_win:
        bet *= 2
    else:
        bet = 0
    return bet


def game(deck, player_cards, diller_cards, bet):
    while True:
        print("1. Взять карту")
        print("2. Посмотреть карты")
        print("3. Закончить игру")

        action = utils.input_int("Введите номер действия: ")

        if action == 1:
            print("Вы взяли карту: ")
            card = take_card(deck)
            player_cards.append(card)
            print(card)

        elif action == 2:
            print("Ваши карты: ")
            show_card(player_cards)
        elif action == 3:
            print("Результаты")
            bet = finish_game(player_cards, diller_cards, bet)
            break
        input()
    return bet

def make_bet(cash):
    if cash > 0:
        while True:
            bet = utils.input_int("Введите вашу ставку: ")
            if bet <= cash:
                break
            else:
                print("У вас нет столько денег")
    else:
        print("У вас нет денег")
        bet = 0
    return bet