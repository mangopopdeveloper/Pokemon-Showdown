# Python 3.8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from Pokemon_Attacker import atk_pokemon

browser = webdriver.Safari()

# Pokemon 1 Information
pokemon1_name = 'Luxray'
pokemon1_hp = '252'
pokemon1_atk = '0'
pokemon1_def = '0'
pokemon1_spa = '0'
pokemon1_spd = '252'
pokemon1_spe = '0'
pokemon1_nature = 'Adamant'
pokemon1_ability = 'Intimidate'
pokemon1_item = 'Sitrus Berry'

# Global Variables
pokemon_level = '50'
pokemon1_ev = [pokemon1_hp, pokemon1_atk, pokemon1_def, pokemon1_spa, pokemon1_spd, pokemon1_spe]

pokemon1_evpathlist = [
    '//*[@id="p1"]/div[3]/table/tbody/tr[1]/td[3]/input',
    '//*[@id="p1"]/div[3]/table/tbody/tr[2]/td[3]/input',
    '//*[@id="p1"]/div[3]/table/tbody/tr[3]/td[3]/input',
    '//*[@id="p1"]/div[3]/table/tbody/tr[4]/td[3]/input',
    '//*[@id="p1"]/div[3]/table/tbody/tr[5]/td[3]/input',
    '//*[@id="p1"]/div[3]/table/tbody/tr[7]/td[3]/input']

pokemon2_evpathlist = [
    '//*[@id="p2"]/div[3]/table/tbody/tr[1]/td[3]/input',
    '//*[@id="p2"]/div[3]/table/tbody/tr[2]/td[3]/input',
    '//*[@id="p2"]/div[3]/table/tbody/tr[3]/td[3]/input',
    '//*[@id="p2"]/div[3]/table/tbody/tr[4]/td[3]/input',
    '//*[@id="p2"]/div[3]/table/tbody/tr[5]/td[3]/input',
    '//*[@id="p2"]/div[3]/table/tbody/tr[7]/td[3]/input']

pokemon2_atklist = [
    's2id_autogen19',
    's2id_autogen21',
    's2id_autogen23',
    's2id_autogen25']

pokemon2_atkpath = [
    '/html/body/div[1]/div[2]/div[2]/div[2]/label',
    '/html/body/div[1]/div[2]/div[2]/div[3]/label',
    '/html/body/div[1]/div[2]/div[2]/div[4]/label',
    '/html/body/div[1]/div[2]/div[2]/div[5]/label']

# Open Browser
browser.get('https://calc.pokemonshowdown.com')
browser.maximize_window()


def defpokemon(pokemon_name):
    # Select Doubles
    pokemon_element = browser.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/fieldset/div[1]/label[2]')
    pokemon_element.click()

    # Select Pokemon
    pokemon_element = browser.find_element_by_id('s2id_autogen28')
    pokemon_element.click()
    pokemon_element.send_keys(pokemon_name)

    # Select First Set
    pokemon_element = browser.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[2]/div')
    pokemon_element.click()

    # Select Level
    pokemon_element = browser.find_element_by_id('levelL1')
    pokemon_element.clear()
    pokemon_element.click()
    pokemon_element.send_keys(pokemon_level)

    # Select EV
    for i in range(len(pokemon1_ev)):
        pokemon_element = browser.find_element_by_xpath(pokemon1_evpathlist[i])
        pokemon_element.clear()
        pokemon_element.click()
        pokemon_element.send_keys(pokemon1_ev[i])

    # Select Nature
    nature = browser.find_element_by_id('natureL1')
    for option in nature.find_elements_by_tag_name('option'):
        if pokemon1_nature in option.text:
            option.click()
            break

    # Select Ability
    ability = browser.find_element_by_id('abilityL1')
    for option in ability.find_elements_by_tag_name('option'):
        if option.text == pokemon1_ability:
            option.click()
            break

    # Select Item
    item = browser.find_element_by_id('itemL1')
    for option in item.find_elements_by_tag_name('option'):
        if option.text == pokemon1_item:
            option.click()
            break

    # Select Moves


def atkpokemon(pokemon):
    # Select Pokemon
    pokemon_element = browser.find_element_by_id('s2id_autogen31')
    pokemon_element.click()
    pokemon_element.send_keys(pokemon["name"])

    # Select First Set
    pokemon_element = browser.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[2]/div')
    pokemon_element.click()

    # Select Level
    pokemon_element = browser.find_element_by_id('levelR1')
    pokemon_element.clear()
    pokemon_element.click()
    pokemon_element.send_keys(pokemon_level)

    # Select EV
    for i in range(len(pokemon["ev"])):
        pokemon_element = browser.find_element_by_xpath(pokemon2_evpathlist[i])
        pokemon_element.clear()
        pokemon_element.click()
        pokemon_element.send_keys(pokemon["ev"][i])

    # Intimidate
    if pokemon1_ability == "Intimidate":
        boost = browser.find_element_by_xpath('//*[@id="p2"]/div[3]/table/tbody/tr[2]/td[6]/select')
        for option in boost.find_elements_by_tag_name('option'):
            if "-1" in option.text:
                option.click()
                break

    # Select Nature
    nature = browser.find_element_by_id('natureR1')
    for option in nature.find_elements_by_tag_name('option'):
        if pokemon["nature"] in option.text:
            option.click()
            break

    # Select Ability
    ability = browser.find_element_by_id('abilityR1')
    for option in ability.find_elements_by_tag_name('option'):
        if option.text == pokemon["ability"]:
            option.click()
            break

    # Select Item
    item = browser.find_element_by_id('itemR1')
    for option in item.find_elements_by_tag_name('option'):
        if option.text == pokemon["item"]:
            option.click()
            break

    # # Select Moves
    # pokemon_element = browser.find_element_by_id('s2id_autogen19')
    # pokemon_element.click()
    # pokemon_element.send_keys(pokemon["attack"])
    # pokemon_element.send_keys(Keys.RETURN)

    # Select Moves
    for i, move in enumerate(pokemon["attack"]):
        pokemon_element = browser.find_element_by_id(pokemon2_atklist[i])
        pokemon_element.click()
        pokemon_element.send_keys(pokemon["attack"][i])
        pokemon_element.send_keys(Keys.RETURN)

        browser.find_element_by_xpath(pokemon2_atkpath[i]).click()
        pokemon_element = browser.find_element_by_xpath('//span[@id="mainResult"]')
        print(pokemon_element.text)
        print("\n")

    # Gather Damage Information
    # pokemon_element = browser.find_element_by_id('resultDamageR1')
    # pokemon_element = browser.find_element_by_id('resultMoveR1')
    # pokemon_element.click()
    # browser.find_element_by_css_selector("input[id='resultMoveR1'][type='radio']").click()
    # browser.find_element_by_css_selector("#resultMoveR1").click()
    # browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/label').click()
    # pokemon_element = browser.find_element_by_xpath('//span[@id="mainResult"]')
    # return (pokemon_element.text)

    # pokemon_element = browser.find_element_by_xpath('//span[@id="resultDamageR1"]')
    # return (pokemon_element.text)


defpokemon(pokemon1_name)

for pokemon in atk_pokemon:
    atkpokemon(pokemon)
    # damage = atkpokemon(pokemon)
    # print(damage)
    # print("\n")

# time.sleep(5)

browser.close()
