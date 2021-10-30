'''
Adapted from code by NeuralNine 
(https://www.youtube.com/watch?v=pYasYyjByKI)
'''

import hashlib
from datetime import datetime
import random


class SimpleCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "\n".join(transaction_list) + \
            "\n" + previous_block_hash + '\n' + str(datetime.today())
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


'''
    Helper functions for the data
'''


def generateRandomTransactionList(names, number_of_transactions, transaction_range):
    transaction_list = []
    for i in range(number_of_transactions):
        first_name = names[random.randint(0, len(names)-1)]
        copy_of_names = names.copy()
        copy_of_names.remove(first_name)
        second_name = copy_of_names[random.randint(0, len(copy_of_names)-1)]
        transaction = first_name + " sends " + \
            str(random.randint(transaction_range[0], transaction_range[1]) + round(
                random.random(), 2)) + " SimpleCoin to " + second_name
        transaction_list.append(transaction)

    return transaction_list


def generateBlockchain(transaction_list):
    blockchain_elements = []
    transactions = []
    for i in range(len(transaction_list)-1):
        if i == 0:
            transactions.append(transaction_list[0])
            transactions.append(transaction_list[1])
            block = SimpleCoinBlock("Initial Hash", transactions)
            blockchain_elements.append(block)
        else:
            transactions.append(transaction_list[i+1])
            block = SimpleCoinBlock(
                blockchain_elements[i-1].block_hash, transactions)
            blockchain_elements.append(block)

    return blockchain_elements


'''
    Example implementation
'''

names = ['Thor', 'Odysseus',
         'Tolkien', 'Atreides', 'Roskolnikov', 'Asimov', 'Einstein', 'Newton', 'Turing', 'Zimmer']
transaction_range = [1, 50]

transactions = generateRandomTransactionList(
    names, random.randint(1, 15), transaction_range)
blockchain = generateBlockchain(transactions)

for index in range(len(blockchain)):
    print("\tBlock Data " + str(index) + "\n" + blockchain[index].block_data)
    print("\tBlock Hash " + str(index) + "\n" + blockchain[index].block_hash)
