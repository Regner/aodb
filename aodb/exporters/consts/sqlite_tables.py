

TN_FarmableItems = 'farmableitem'
TN_StackableItems = 'stackableitem'
TN_ConsumableItems = 'consumableitem'
TN_EquipmentItems = 'equipmentitem'
TN_Weapons = 'weapon'
TN_Mounts = 'mount'
TN_FurnitureItems = 'furnitureitem'
TN_JournalItems = 'journalitem'

create_farmable_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_FarmableItems} (
        uniquename STRING PRIMARY KEY,
        tier INTEGER,
        craftfamegainfactor FLOAT,
        placecost INTEGER,
        placefame INTEGER,
        pickupable BOOLEAN,
        destroyable BOOLEAN,
        unlockedtoplace BOOLEAN,
        maxstacksize INTEGER,
        shopcategory STRING,
        shopsubcategory1 STRING,
        kind STRING,
        weight FLOAT,
        unlockedtocraft BOOLEAN,
        uiatlas STRING,
        animationid STRING,
        activefarmfocuscost INTEGER,
        activefarmmaxcycles INTEGER,
        activefarmactiondurationseconds INTEGER,
        activefarmcyclelengthseconds INTEGER,
        activefarmbonus FLOAT,
        prefabname STRING,
        prefabscale FLOAT,
        resourcevalue INTEGER,
        showinmarketplace BOOLEAN,
        tile STRING
    )
'''

create_stackable_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_StackableItems} (
        uniquename STRING PRIMARY KEY,
        nutrition INTEGER,
        foodcategory STRING,
        shopcategory STRING,
        shopsubcategory1 STRING,
        resourcetype STRING,
        tier INTEGER,
        weight FLOAT,
        maxstacksize INTEGER,
        uiatlas STRING,
        uisprite STRING,
        unlockedtocraft BOOLEAN,
        craftfamegainfactor INTEGER,
        enchantmentlevel INTEGER,
        descriptionlocatag STRING,
        descvariable0 STRING,
        descvariable1 STRING,
        itemvalue INTEGER,
        salvageable BOOLEAN,
        showinmarketplace BOOLEAN
    )
'''

create_consumeable_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_ConsumableItems} (
        uniquename STRING PRIMARY KEY,
        uisprite STRING,
        abilitypower INTEGER,
        slottype STRING,
        consumespell STRING,
        shopcategory STRING,
        shopsubcategory1 STRING,
        tier INTEGER,
        weight FLOAT,
        maxstacksize INTEGER,
        uiatlas STRING,
        unlockedtocraft BOOLEAN,
        unlockedtoequip BOOLEAN,
        nutrition INTEGER
    )
'''

create_equipment_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_EquipmentItems} (
        uniquename STRING PRIMARY KEY,
        uisprite STRING,
        maxqualitylevel INTEGER,
        abilitypower INTEGER,
        slottype STRING,
        itempowerprogressiontype STRING,
        shopcategory STRING,
        shopsubcategory1 STRING,
        skincount INTEGER,
        tier INTEGER,
        weight FLOAT,
        activespellslots INTEGER,
        passivespellslots INTEGER,
        physicalarmor INTEGER,
        magicresistance INTEGER,
        uiatlas STRING,
        durability INTEGER,
        durabilityloss_attack FLOAT,
        durabilityloss_spelluse INTEGER,
        durabilityloss_receivedattack INTEGER,
        durabilityloss_receivedspell INTEGER,
        offhandanimationtype STRING,
        unlockedtocraft BOOLEAN,
        unlockedtoequip BOOLEAN,
        hitpointsmax INTEGER,
        hitpointsregenerationbonus FLOAT,
        energymax INTEGER,
        energyregenerationbonus FLOAT,
        crowdcontrolresistance INTEGER,
        itempower INTEGER,
        physicalattackdamagebonus FLOAT,
        magicattackdamagebonus FLOAT,
        physicalspelldamagebonus FLOAT,
        magicspelldamagebonus FLOAT,
        healbonus FLOAT,
        bonusccdurationvsplayers FLOAT,
        bonusccdurationvsmobs FLOAT,
        threatbonus FLOAT,
        magiccooldownreduction FLOAT,
        bonusdefensevsplayers FLOAT,
        bonusdefensevsmobs FLOAT,
        magiccasttimereduction FLOAT,
        attackspeedbonus FLOAT,
        movespeedbonus FLOAT,
        showinmarketplace BOOLEAN,
        facestate STRING,
        movespeed INTEGER,
        maxload INTEGER,
        beardstate STRING,
        mesh STRING
    )
'''

create_weapons = f'''
    CREATE TABLE IF NOT EXISTS {TN_Weapons} (
        uniquename STRING PRIMARY KEY,
        mesh STRING,
        uisprite STRING,
        maxqualitylevel INTEGER,
        abilitypower INTEGER,
        slottype STRING,
        shopcategory STRING,
        shopsubcategory1 STRING,
        attacktype STRING,
        attackdamage INTEGER,
        attackspeed FLOAT,
        attackrange INTEGER,
        twohanded BOOLEAN,
        tier INTEGER,
        weight FLOAT,
        activespellslots INTEGER,
        passivespellslots INTEGER,
        uiatlas STRING,
        durability INTEGER,
        durabilityloss_attack INTEGER,
        durabilityloss_spelluse INTEGER,
        durabilityloss_receivedattack INTEGER,
        durabilityloss_receivedspell INTEGER,
        mainhandanimationtype STRING,
        unlockedtocraft BOOLEAN,
        unlockedtoequip BOOLEAN,
        itempower INTEGER,
        unequipincombat BOOLEAN,
        attackbuildingdamage FLOAT,
        physicalspelldamagebonus INTEGER,
        magicspelldamagebonus INTEGER,
        fxbonename STRING,
        fxboneoffset STRING,
        hitpointsmax INTEGER,
        hitpointsregenerationbonus FLOAT,
        itempowerprogressiontype STRING,
        focusfireprotectionpeneration FLOAT,
        showinmarketplace BOOLEAN,
        attackdamagetimefactor FLOAT
    )
'''

create_mounts = f'''
    CREATE TABLE IF NOT EXISTS {TN_Mounts} (
        uniquename STRING PRIMARY KEY,
        maxqualitylevel INTEGER,
        itempower INTEGER,
        abilitypower INTEGER,
        slottype STRING,
        shopcategory STRING,
        shopsubcategory1 STRING,
        mountedbuff STRING,
        halfmountedbuff STRING,
        tier INTEGER,
        weight FLOAT,
        activespellslots INTEGER,
        passivespellslots INTEGER,
        uiatlas STRING,
        durability INTEGER,
        durabilityloss_attack INTEGER,
        durabilityloss_spelluse INTEGER,
        durabilityloss_receivedattack INTEGER,
        durabilityloss_receivedspell INTEGER,
        durabilityloss_receivedattack_mounted INTEGER,
        durabilityloss_receivedspell_mounted INTEGER,
        durabilityloss_mounting INTEGER,
        unlockedtocraft BOOLEAN,
        unlockedtoequip BOOLEAN,
        mounttime INTEGER,
        dismounttime INTEGER,
        mounthitpointsmax INTEGER,
        mounthitpointsregeneration FLOAT,
        prefabname STRING,
        prefabscaling FLOAT,
        despawneffect STRING,
        despawneffectscaling INTEGER,
        remountdistance INTEGER,
        halfmountrange INTEGER,
        forceddismountcooldown INTEGER,
        forceddismountspellcooldown INTEGER,
        fulldismountcooldown INTEGER,
        remounttime FLOAT,
        showinmarketplace BOOLEAN,
        uisprite STRING,
        enchantmentlevel INTEGER
    )
'''

create_furniture_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_FurnitureItems} (
        uniquename STRING PRIMARY KEY,
        shopcategory STRING,
        shopsubcategory1 STRING,
        tier INTEGER,
        durability INTEGER,
        durabilitylossperdayfactor FLOAT,
        weight FLOAT,
        unlockedtocraft BOOLEAN,
        placeableindoors BOOLEAN,
        placeableoutdoors BOOLEAN,
        placeableindungeons BOOLEAN,
        uiatlas STRING,
        accessrightspreset STRING,
        customizewithguildlogo BOOLEAN,
        residencyslots INTEGER,
        labourerfurnituretype STRING,
        labourersaffected STRING,
        labourerhappiness INTEGER,
        labourersperfurnitureitem INTEGER,
        uisprite STRING,
        enchantmentlevel INTEGER,
        tile STRING,
        showinmarketplace BOOLEAN,
        durabilitylossperusefactor INTEGER
    )
'''

create_journal_items = f'''
    CREATE TABLE IF NOT EXISTS {TN_JournalItems} (
        uniquename STRING PRIMARY KEY,
        tier INTEGER,
        maxfame INTEGER,
        baselootamount INTEGER,
        shopcategory STRING,
        shopsubcategory1 STRING,
        weight FLOAT,
        unlockedtocraft BOOLEAN,
        uiatlas STRING,
        craftfamegainfactor INTEGER,
        uisprite STRING
    )
'''

CREATE_TABLES = {
    TN_FarmableItems: create_farmable_items,
    TN_StackableItems: create_stackable_items,
    TN_ConsumableItems: create_consumeable_items,
    TN_EquipmentItems: create_equipment_items,
    TN_Weapons: create_weapons,
    TN_Mounts: create_mounts,
    TN_FurnitureItems: create_furniture_items,
    TN_JournalItems: create_journal_items,
}
