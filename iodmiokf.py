import urllib.request, json, mouse

id_conv = {
"ENCHANTED_RAW_CHICKEN": "Enchanted Raw Chicken",
"INK_SACK:3": "Cocoa Beans",
"BROWN_MUSHROOM": "Brown Mushroom",
"ENCHANTED_WATER_LILY": "Enchanted Lily Pad",
"INK_SACK:4": "Lapis Lazuli",
"TARANTULA_WEB": "Tarantula Web",
"CARROT_ITEM": "Carrot",
"ENCHANTED_POTATO": "Enchanted Potato",
"LOG:1": "Spruce Log",
"ENCHANTED_SLIME_BALL": "Enchanted Slime Ball",
"ENCHANTED_GOLDEN_CARROT": "Enchanted Golden Carrot",
"LOG:3": "Jungle Log",
"LOG:2": "Birch Log",
"ENCHANTED_RABBIT_HIDE": "Enchanted Rabbit Hide",
"ENCHANTED_GLOWSTONE_DUST": "Enchanted Glowstone Dust",
"ENCHANTED_INK_SACK": "Enchanted Ink Sack",
"ENCHANTED_CACTUS": "Enchanted Cactus",
"ENCHANTED_SUGAR_CANE": "Enchanted Sugar Cane",
"ENCHANTED_BIRCH_LOG": "Enchanted Birch Log",
"ENCHANTED_GUNPOWDER": "Enchanted Gunpowder",
"ENCHANTED_MELON": "Enchanted Melon",
"ENCHANTED_COOKED_SALMON": "Enchanted Cooked Salmon",
"ENCHANTED_SUGAR": "Enchanted Sugar",
"LOG": "Oak Log",
"CACTUS": "Cactus",
"ENCHANTED_BLAZE_ROD": "Enchanted Blaze Rod",
"GHAST_TEAR": "Ghast Tear",
"ENCHANTED_CAKE": "Enchanted Cake",
"PUMPKIN": "Pumpkin",
"ENCHANTED_ENDER_PEARL": "Enchanted Ender Pearl",
"PURPLE_CANDY": "Purple Candy",
"WHEAT": "Wheat",
"ENCHANTED_FERMENTED_SPIDER_EYE": "Enchanted Fermented Spider Eye",
"ENCHANTED_GOLD_BLOCK": "Enchanted Gold Block",
"ENCHANTED_RAW_SALMON": "Enchanted Raw Salmon",
"ENCHANTED_JUNGLE_LOG": "Enchanted Jungle Log",
"ENCHANTED_FLINT": "Enchanted Flint",
"ENCHANTED_GLISTERING_MELON": "Enchanted Glistering Melon",
"IRON_INGOT": "Iron Ingot",
"PRISMARINE_SHARD": "Prismarine Shard",
"ENCHANTED_EMERALD": "Enchanted Emerald",
"ENCHANTED_SPIDER_EYE": "Enchanted Spider Eye",
"ENCHANTED_EMERALD_BLOCK": "Enchanted Emerald Block",
"RED_MUSHROOM": "Red Mushroom",
"MUTTON": "Mutton",
"ENCHANTED_MELON_BLOCK": "Enchanted Melon Block",
"ENCHANTED_CLAY_BALL": "Enchanted Clay Ball",
"DIAMOND": "Diamond",
"COBBLESTONE": "Cobblestone",
"SPIDER_EYE": "Spider Eye",
"RAW_FISH": "Raw Fish",
"ENCHANTED_PUFFERFISH": "Enchanted Pufferfish",
"GLOWSTONE_DUST": "Glowstone Dust",
"GOLD_INGOT": "Gold Ingot",
"REVENANT_VISCERA": "Revenant Viscera",
"TARANTULA_SILK": "Tarantula Silk",
"POTATO_ITEM": "Potato",
"ENCHANTED_MUTTON": "Enchanted Mutton",
"ENCHANTED_HUGE_MUSHROOM_1": "Enchanted Brown Mushroom Block",
"SUPER_COMPACTOR_3000": "Super Compactor 3000",
"ENCHANTED_IRON": "Enchanted Iron",
"SUPER_EGG": "Super Egg",
"STOCK_OF_STONKS": "Stock Of Stonks",
"ENCHANTED_COBBLESTONE": "Enchanted Cobblestone",
"ENCHANTED_BONE": "Enchanted Bone",
"ENCHANTED_PAPER": "Enchanted Paper",
"ENCHANTED_HUGE_MUSHROOM_2": "Enchanted Red Mushroom Block",
"PORK": "Pork",
"ENCHANTED_DIAMOND_BLOCK": "Enchanted Diamond Block",
"EMERALD": "Emerald",
"ENCHANTED_RABBIT_FOOT": "Enchanted Rabbit Foot",
"PRISMARINE_CRYSTALS": "Prismarine Crystals",
"HOT_POTATO_BOOK": "Hot Potato Book",
"ENCHANTED_ICE": "Enchanted Ice",
"ICE": "Ice",
"CLAY_BALL": "Clay Ball",
"HUGE_MUSHROOM_1": "Brown Mushroom Block",
"HUGE_MUSHROOM_2": "Red Mushroom Block",
"LOG_2:1": "Dark Oak Log",
"GREEN_GIFT": "Green Gift",
"ENCHANTED_SNOW_BLOCK": "Enchanted Snow Block",
"GOLDEN_TOOTH": "Golden Tooth",
"STRING": "String",
"PACKED_ICE": "Packed Ice",
"WATER_LILY": "Lily Pad",
"RABBIT_FOOT": "Rabbit Foot",
"LOG_2": "Acacia Log",
"REDSTONE": "Redstone",
"ENCHANTED_OBSIDIAN": "Enchanted Obsidian",
"ENCHANTED_COAL": "Enchanted Coal",
"COAL": "Coal",
"ENCHANTED_QUARTZ": "Enchanted Quartz",
"ENDER_PEARL": "Ender Pearl",
"ENCHANTED_COAL_BLOCK": "Enchanted Coal Block",
"ENCHANTED_CACTUS_GREEN": "Enchanted Cactus Green",
"ENCHANTED_PRISMARINE_CRYSTALS": "Enchanted Prismarine Crystals",
"ENCHANTED_CARROT_STICK": "Enchanted Carrot On A Stick",
"ENCHANTED_CARROT_ON_A_STICK": "Enchanted Carrot On A Stick",
"ENCHANTED_ENDSTONE": "Enchanted Endstone",
"ENCHANTED_LAPIS_LAZULI_BLOCK": "Enchanted Lapis Lazuli Block",
"ENCHANTED_COOKIE": "Enchanted Cookie",
"ENCHANTED_STRING": "Enchanted String",
"SLIME_BALL": "Slime Ball",
"ENDER_STONE": "End Stone",
"ENCHANTED_RAW_FISH": "Enchanted Raw Fish",
"ENCHANTED_ACACIA_LOG": "Enchanted Acacia Log",
"SNOW_BALL": "Snow Ball",
"ENCHANTED_EGG": "Enchanted Egg",
"QUARTZ": "Quartz",
"RAW_BEEF": "Raw Beef",
"ENCHANTED_EYE_OF_ENDER": "Enchanted Eye Of Ender",
"SAND": "Sand",
"RAW_CHICKEN": "Raw Chicken",
"MAGMA_CREAM": "Magma Cream",
"SUGAR_CANE": "Sugar Cane",
"ENCHANTED_LAPIS_LAZULI": "Enchanted Lapis Lazuli",
"ENCHANTED_GHAST_TEAR": "Enchanted Ghast Tear",
"ENCHANTED_COCOA": "Enchanted Cocoa",
"RED_GIFT": "Red Gift",
"ENCHANTED_RAW_BEEF": "Enchanted Raw Beef",
"SEEDS": "Seeds",
"ENCHANTED_LEATHER": "Enchanted Leather",
"ENCHANTED_SPONGE": "Enchanted Sponge",
"ENCHANTED_FEATHER": "Enchanted Feather",
"ENCHANTED_SLIME_BLOCK": "Enchanted Slime Block",
"ENCHANTED_OAK_LOG": "Enchanted Oak Log",
"RABBIT_HIDE": "Rabbit Hide",
"WHITE_GIFT": "White Gift",
"INK_SACK": "Ink Sack",
"FLINT": "Flint",
"ENCHANTED_SPRUCE_LOG": "Enchanted Spruce Log",
"WOLF_TOOTH": "Wolf Tooth",
"ENCHANTED_ROTTEN_FLESH": "Enchanted Rotten Flesh",
"ENCHANTED_GRILLED_PORK": "Enchanted Grilled Pork",
"SULPHUR": "Gunpowder",
"NETHER_STALK": "Nether Wart",
"RABBIT": "Rabbit",
"ENCHANTED_NETHER_STALK": "Enchanted Nether Wart",
"ENCHANTED_REDSTONE_BLOCK": "Enchanted Redstone Block",
"ENCHANTED_QUARTZ_BLOCK": "Enchanted Quartz Block",
"ENCHANTED_CARROT": "Enchanted Carrot",
"ENCHANTED_PUMPKIN": "Enchanted Pumpkin",
"GREEN_CANDY": "Green Candy",
"ENCHANTED_REDSTONE": "Enchanted Redstone",
"ROTTEN_FLESH": "Rotten Flesh",
"ENCHANTED_COOKED_FISH": "Enchanted Cooked Fish",
"OBSIDIAN": "Obsidian",
"ENCHANTED_MAGMA_CREAM": "Enchanted Magma Cream",
"GRAVEL": "Gravel",
"MELON": "Melon",
"ENCHANTED_PACKED_ICE": "Enchanted Packed Ice",
"RAW_FISH:3": "Pufferfish",
"ENCHANTED_PRISMARINE_SHARD": "Enchanted Prismarine Shard",
"ENCHANTED_IRON_BLOCK": "Enchanted Iron Block",
"LEATHER": "Leather",
"ENCHANTED_COOKED_MUTTON": "Enchanted Cooked Mutton",
"BONE": "Bone",
"RAW_FISH:1": "Salmon",
"REVENANT_FLESH": "Revenant Flesh",
"ENCHANTED_PORK": "Enchanted Pork",
"ENCHANTED_GLOWSTONE": "Enchanted Glowstone",
"ENCHANTED_RABBIT": "Enchanted Rabbit",
"ENCHANTED_BREAD": "Enchanted Bread",
"FEATHER": "Feather",
"ENCHANTED_CHARCOAL": "Enchanted Charcoal",
"ENCHANTED_BLAZE_POWDER": "Enchanted Blaze Powder",
"NETHERRACK": "Netherrack",
"SUMMONING_EYE": "Summoning Eye",
"SPONGE": "Sponge",
"BLAZE_ROD": "Blaze Rod",
"ENCHANTED_DARK_OAK_LOG": "Enchanted Dark Oak Log",
"SNOW_BLOCK": "Snow Block",
"ENCHANTED_BAKED_POTATO": "Enchanted Baked Potato",
"COMPACTOR": "Compactor",
"ENCHANTED_DIAMOND": "Enchanted Diamond",
"ENCHANTED_GOLD": "Enchanted Gold",
"WISE_FRAGMENT": "Wise Dragon Fragment",
"PROTECTOR_FRAGMENT": "Protector Dragon Fragment",
"STRONG_FRAGMENT": "Strong Dragon Fragment",
"YOUNG_FRAGMENT": "Young Dragon Fragment",
"UNSTABLE_FRAGMENT": "Unstable Dragon Fragment",
"SUPERIOR_FRAGMENT": "Superior Dragon Fragment",
"OLD_FRAGMENT": "Old Dragon Fragment",
"ENCHANTED_FIREWORK_ROCKET": "Enchanted Firework",
"ENCHANTED_LAVA_BUCKET": "Enchanted Lava Bucket",
"CATALYST": "Catalyst",
"ENCHANTED_REDSTONE_LAMP": "Enchanted Redstone Lamp",
"ENCHANTED_HAY_BLOCK": "Enchanted Hay Bale",
"HAY_BLOCK": "Hay Bale",
"ENCHANTED_SEEDS": "Enchanted Seeds",
"ENCHANTED_SAND": "Enchanted Sand",
"ENCHANTED_RED_MUSHROOM": "Enchanted Red Mushroom",
"ENCHANTED_BROWN_MUSHROOM": "Enchanted Brown Mushroom",
"ENCHANTED_WET_SPONGE": "Enchanted Wet Sponge",
"HAMSTER_WHEEL": "Hamster Wheel",
"FOUL_FLESH": "Foul Flesh",
"RECOMBOBULATOR_3000": "Recombobulator 3000",
"HOLY_FRAGMENT": "Holy Dragon Fragment",
"FUMING_POTATO_BOOK": "Fuming Potato Book",
"CARROT_BAIT": "Carrot Bait",
"MINNOW_BAIT": "Minnow Bait",
"FISH_BAIT": "Fish Bait",
"LIGHT_BAIT": "Light Bait",
"DARK_BAIT": "Dark Bait",
"SPOOKY_BAIT": "Spooky Bait",
"SPIKED_BAIT": "Spiked Bait",
"BLESSED_BAIT": "Blessed Bait",
"ICE_BAIT": "Ice Bait",
"WHALE_BAIT": "Whale Bait",
"ENCHANTED_CLOWNFISH": "Enchanted Clownfish",
"RAW_FISH:2": "Clownfish",
"ENCHANTED_BONE_BLOCK": "Enchanted Bone Block",
"BOOSTER_COOKIE": "Booster Cookie",
"TIGER_SHARK_TOOTH": "Tiger Shark Tooth",
"BLUE_SHARK_TOOTH": "Blue Shark Tooth",
"NURSE_SHARK_TOOTH": "Nurse Shark Tooth",
"GREAT_WHITE_SHARK_TOOTH": "Great White Shark Tooth",
"SHARK_FIN": "Shark Fin",
"ENCHANTED_SHARK_FIN": "Enchanted Shark Fin",
"BAZAAR_COOKIE": "Bazaar Cookie",
"GRIFFIN_FEATHER": "Griffin Feather",
"DAEDALUS_STICK": "Daedalus Stick",
"ANCIENT_CLAW": "Ancient Claw",
"ENCHANTED_ANCIENT_CLAW": "Enchanted Ancient Claw",
"REFINED_MINERAL": "Refined Mineral",
"SHARK_BAIT": "Shark Bait",
"HYPER_CATALYST": "Hyper Catalyst",
"JACOBS_TICKET": "Jacob's Ticket",
"SPOOKY_SHARD": "Spooky Shard",
"ECTOPLASM": "Ectoplasm"
}
#ppi = profit per item
#ep = estimated profit
constants = (5760,1620)

def load_json():
    with open('clicks.json') as clicks:
        return json.load(clicks)

def take_average_ep(elem):
    return elem['AverageEP']

def get_data():
    #gets data
    with urllib.request.urlopen('https://api.hypixel.net/skyblock/bazaar') as url:
        data = json.loads(url.read().decode())
    return data

def data_trim(data):
    #trims data
    data_t = {}
    for item in data['products']:
        if len(data['products'][item]['buy_summary']) > 0 and len(data['products'][item]['sell_summary']) > 0:
            buyPrice = data['products'][item]['sell_summary'][0]['pricePerUnit']
            buyMovingWeek = data['products'][item]['quick_status']['buyMovingWeek']
            sellPrice = data['products'][item]['buy_summary'][0]['pricePerUnit']
            sellMovingWeek = data['products'][item]['quick_status']['sellMovingWeek']
            data_t[item] = [buyPrice, buyMovingWeek, sellPrice, sellMovingWeek]
    return data_t

def proessess_data(data):
    #processes the data
    data_p = {}
    for item in data:
        buy_in = data[item][0]
        sell_in = data[item][2]
        PPI = data[item][2] - data[item][0]
        PPI *= 1-0.0125
        buyIMF = data[item][1]
        sellIMF = data[item][3]
        buyEP = PPI * buyIMF
        sellEP = PPI * sellIMF
        averageEP = buyEP + sellEP / 2
        if item in id_conv.keys():
            data_p[id_conv[item]] = {'PPI' : PPI, 'BuyEP' : buyEP, 'SellEP' : sellEP, 'AverageEP' : averageEP, 'BuyIn' : buy_in, 'SellIn' : sell_in}
        else:
            data_p[item] = {'PPI' : PPI, 'BuyEP' : buyEP, 'SellEP' : sellEP, 'AverageEP' : averageEP, 'BuyIn' : buy_in, 'SellIn' : sell_in}
    return data_p

def order_list(data):
    ordered_list = []
    for item in data:
        ordered_list.append({'item': item, 'PPI' : data[item]['PPI'], 'BuyEP' : data[item]['BuyEP'], 'SellEP' : data[item]['SellEP'], 'AverageEP' : data[item]['AverageEP'], 'BuyIn' : data[item]['BuyIn'], 'SellIn' : data[item]['SellIn']})
    ordered_list.sort(key=take_average_ep, reverse=True)
    return ordered_list

def get_suggestions(data):
    for x in range(5):
        print(data[x]['item'], ':')
        print('Average Estimated Profit: ',data[x]['AverageEP'])
        print('Profit Per Item: ',data[x]['PPI'])
        print('Buy In: ', data[x]['BuyIn'])
        print('\n')

def suggestions():
    data = order_list(proessess_data(data_trim(get_data())))
    return data


#money
def get_action(orders):
    items = suggestions()
    if len(orders) < 1:
        return 'buy'
    for item in items:
        if item['item'] == orders[0][0] and orders[0][3] == 'buy':
            print(orders[0][2])
            print(item['BuyIn'])
            if orders[0][2] > item['BuyIn']:
                return 'flip'
    for item in items:
        if item['item'] == orders[0][0] and orders[0][3] == 'flip':
            if orders[0][2] > item['SellIn']:
                return 'collect'
    return 'wait'