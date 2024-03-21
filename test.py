# import pandas as pd
# import os
# os.chdir('C:\\Users\\JLUIJBE99\\Downloads')


# def create_experiment_lists(df, total_lists=4):
#     lists = {i: pd.DataFrame() for i in range(1, total_lists + 1)}
#     target_words = df['target'].unique()

#     for target in target_words:
#         target_rows = df[df['target'] == target]
        
#         # Shuffle rows to randomize the order of conditions for each target
#         target_rows = target_rows.sample(frac=1).reset_index(drop=True)

#         for i, row in target_rows.iterrows():
#             list_number = (i % total_lists) + 1  # Determine which list to add the row to
#             lists[list_number] = lists[list_number]._append(row)

#     return lists

# df = pd.read_csv('list (1).csv')
# # Apply the function to your DataFrame
# experiment_lists = create_experiment_lists(df)

# # Save each list to a separate CSV file
# for list_number, list_df in experiment_lists.items():
#     list_df.to_csv(f"newlist{list_number}.csv", index=False)

# print("CSV files created for each list.")



# import pandas as pd
# # Expanded list of words and their conditions


# def create_structured_data(group_id, words_data):
#     structured_data = []
#     for words in words_data:
#         correct_word, *primes, target = words
#         # Add related TL-internal and TL-final conditions
#         structured_data.append({"group": group_id, "condition": "related-TL-internal", "prime": primes[0], "target": target, "expected": "F", "primetype": "related"})
#         structured_data.append({"group": group_id, "condition": "related-TL-final", "prime": primes[1], "target": target, "expected": "F", "primetype": "related"})
#         # Add unrelated TL-internal and TL-final conditions
#         structured_data.append({"group": group_id, "condition": "unrelated-TL-internal", "prime": primes[2], "target": target, "expected": "F", "primetype": "unrelated"})
#         structured_data.append({"group": group_id, "condition": "unrelated-TL-final", "prime": primes[3], "target": target, "expected": "F", "primetype": "unrelated"})
#         group_id += 1  # Increment group_id for the next set
#     return structured_data
# # Create structured data for all words
# structured_data_all = create_structured_data(45, words_data)

# # Convert to DataFrame
# df_all = pd.DataFrame(structured_data_all)
# print(df_all)
# # Display the first few rows of the DataFrame to ensure it's correctly structured
# import os
# cwd = os.getcwd()
# print(cwd)
# df_all.to_csv('list_new.csv')



# import pandas as pd

# import os
# os.chdir('C:\\Users\\JLUIJBE99\\Downloads')


# # Load the lists from CSV files
# list1 = pd.read_csv('newlist1.csv')
# list4 = pd.read_csv('newlist4.csv')
# # Assuming you have list2 and list3 as well, load them similarly
# list2 = pd.read_csv('newlist2.csv')
# list3 = pd.read_csv('newlist3.csv')

# # Combine all lists into a single DataFrame for analysis
# all_lists = pd.concat([list1, list2, list3, list4], ignore_index=True)

# # Check if each target appears in each condition across the lists
# targets = all_lists['target'].unique()
# conditions = all_lists['condition'].unique()

# # Initialize a dictionary to keep track of condition coverage for each target
# coverage_check = {target: set() for target in targets}

# # Populate the dictionary with conditions each target appears in across all lists
# for _, row in all_lists.iterrows():
#     coverage_check[row['target']].add(row['condition'])

# # Check for any targets that do not have all four conditions covered
# incomplete_coverage = {target: conditions for target, conditions in coverage_check.items() if len(conditions) < 4}

# if incomplete_coverage:
#     print("Incomplete condition coverage for the following targets:")
#     for target, conditions in incomplete_coverage.items():
#         print(f"Target: {target}, Conditions: {list(conditions)}")
# else:
#     print("All targets have complete condition coverage across the lists.")

# # Check for any repetition of target words in the same condition within each list
# repetition_check = []

# for list_df in [list1, list2, list3, list4]:
#     duplicated = list_df[list_df.duplicated(subset=['target', 'condition'], keep=False)]
#     if not duplicated.empty:
#         repetition_check.append(duplicated)

# if repetition_check:
#     print("\nRepetitions found in the lists:")
#     for df in repetition_check:
#         print(df)
# else:
#     print("\nNo repetitions found within the lists.")

import random

words_data = [
    ("never", "neevr", "nemer", "nevre", "nevem", "ALWAYS"),
    ("fruit", "friut", "freit", "fruti", "fruil", "APPLE"),
    ("march", "macrh", "manch", "marhc", "maroh", "APRIL"),
    ("Uncle", "unlce", "unvle", "uncel", "uncte", "AUNT"),
    ("roast", "raost", "roant", "roats", "roask", "BEEF"),
    ("above", "abvoe", "alove", "aboev", "abovs", "BELOW"),
    ("robin", "roibn", "rofin", "robni", "roban", "BIRD"),
    ("flesh", "felsh", "flosh", "flehs", "flest", "BLOOD"),
    ("skirt", "skrit", "skart", "skitr", "skist", "BLOUSE"),
    ("study", "sutdy", "stady", "stuyd", "stuky", "BOOKS"),
    ("house", "huose", "houge", "houes", "houne", "BRICK"),
    ("carry", "crary", "cargy", "caryr", "carsy", "BRING"),
    ("hills", "hlils", "holls", "hilsl", "hille", "BUMPS"),
    ("bread", "braed", "breid", "breda", "breal", "BUTTER"),
    ("jails", "jials", "jaips", "jaisl", "jaits", "CELLS"),
    ("fraud", "fruad", "frald", "fradu", "fraod", "CHEAT"),
    ("miner", "mienr", "miver", "minre", "minen", "COAL"),
    ("judge", "jugde", "judpe", "judeg", "judpe", "COURT"),
    ("river", "rievr", "ruver", "rivre", "rives", "CREEK"),
    ("thief", "tihef", "thirf", "thife", "thiaf", "CROOK"),
    ("faces", "faecs", "fapes", "facse", "facen", "CROWD"),
    ("fatal", "faatl", "fatil", "fatla", "fatak", "DEATH"),
    ("angel", "agnel", "antel", "angle", "angol", "DEVIL"),
    ("clean", "claen", "chean", "clena", "cleam", "DIRTY"),
    ("nurse", "nusre", "nunse", "nures", "nurss", "DOCTOR"),
    ("awake", "awkae", "awane", "awaek", "awaks", "DREAM"),
    ("lifts", "litfs", "lirts", "lifst", "lifte", "DROPS"),
    ("sober", "soebr", "siber", "sobre", "sobir", "DRUNK"),
    ("bacon", "baocn", "bamon", "bacno", "bacos", "EGGS"),
    ("knife", "kinfe", "knike", "knief", "knike", "FORK"),
    ("empty", "emtpy", "empky", "empyt", "empky", "FULL"),
    ("plays", "palys", "pluys", "plasy", "plags", "GAMES"),
    ("sells", "slels", "salls", "selsl", "selks", "GOODS"),
    ("coast", "caost", "coost", "coats", "coant", "GUARD"),
    ("curly", "culry", "cusly", "curyl", "curky", "HAIR"),
    ("glove", "golve", "glone", "gloev", "glovs", "HAND"),
    ("loves", "loevs", "lovos", "lovse", "lovis", "HATES"),
    ("spice", "sipce", "skice", "spiec", "spime", "HERBS"),
    ("mount", "muont", "moult", "moutn", "mounk", "HORSE"),
    ("camel", "caeml", "cawel", "camle", "camek", "HUMP"),
    ("pearl", "paerl", "peirl", "pealr", "peard", "JEWEL"),
    ("royal", "roayl", "ropal", "royla", "royat", "KINGS"),
    ("early", "ealry", "eanly", "earyl", "earty", "LATE"),
    ("sneer", "sener", "skeer", "snere", "sneor", "LAUGH"),
    ("teach", "taech", "toach", "teahc", "teash", "LEARN"),
    ("heavy", "hevay", "heamy", "heayv", "heamy", "LIGHT"),
    ("tiger", "tiegr", "tiper", "tigre", "tigem", "LION"),
    ("short", "shrot", "shart", "shotr", "shork", "LONG"),
    ("tight", "tihgt", "teght", "tigth", "tigkt", "LOOSE"),
    ("maybe", "mabye", "marbe", "mayeb", "maybs", "MIGHT"),
    ("major", "maojr", "majar", "majro", "majos", "MINOR"),
    ("coins", "cions", "clins", "coisn", "coirs", "MONEY"),
    ("teeth", "teteh", "telth", "teeht", "teesh", "MOUTH"),
    ("usher", "uhser", "uther", "ushre", "ushen", "MOVIE"),
    ("bathe", "bahte", "buth", "bateh", "batke", "NAKED"),
    ("scarf", "scraf", "scerf", "scafr", "scanf", "NECK"),
    ("green", "geren", "grenn", "grene", "greem", "OLIVE"),
    ("spray", "spary", "sproy", "sprya", "sprey", "PAINT"),
    ("whole", "whloe", "wiole", "whoel", "whols", "PART"),
    ("paper", "paepr", "puper", "papre", "papec", "PENCIL"),
    ("pilot", "pliot", "pidot", "pilto", "pilok", "PLANE"),
    ("board", "baord", "boird", "boadr", "boart", "PLANK"),
    ("ideas", "idaes", "idoas", "idesa", "idean", "PLANS"),
    ("peach", "paech", "peash", "peahc", "peash", "PLUM"),
    ("songs", "snogs", "sengs", "sonsg", "sonps", "POEMS"),
    ("lakes", "laeks", "lokes", "lakse", "lakem", "PONDS"),
    ("lower", "loewr", "liwer", "lowre", "lowem", "RAISE"),
    ("shave", "shvae", "shawe", "shaev", "shane", "RAZOR"),
    ("coral", "coarl", "cural", "corla", "corak", "REEFS"),
    ("monks", "mokns", "manks", "monsk", "monke", "ROBES"),
    ("slide", "silde", "slike", "slied", "slidd", "RULER"),
    ("bolts", "botls", "bolps", "bolst", "boltn", "SCREW"),
    ("plant", "palnt", "plint", "platn", "plamt", "SEED"),
    ("point", "piont", "poilt", "poitn", "poind", "SHARP"),
    ("barns", "banrs", "balns", "barsn", "barrs", "SHEDS"),
    ("metal", "meatl", "megal", "metla", "metak", "SHINY"),
    ("pants", "patns", "palts", "panst", "pante", "SHIRT"),
    ("music", "muisc", "muric", "musci", "musoc", "SING"),
    ("cloud", "cluod", "choud", "clodu", "cloul", "SKIES"),
    ("large", "lagre", "lange", "lareg", "largs", "SMALL"),
    ("rough", "ruogh", "roegh", "rouhg", "rougl", "SMOOTH"),
    ("sleet", "selet", "sliet", "slete", "sleed", "SNOW"),
    ("shoes", "sheos", "spoes", "shose", "shoen", "SOCKS"),
    ("couch", "cuoch", "cooch", "couhc", "courh", "SOFA"),
    ("lemon", "leomn", "leron", "lemno", "lemin", "SOUR"),
    ("north", "notrh", "norgh", "norht", "norlh", "SOUTH"),
    ("round", "ruond", "roond", "roudn", "rount", "SQUARE"),
    ("meats", "maets", "miats", "meast", "meaks", "STEAK"),
    ("rigid", "riigd", "rogid", "rigdi", "rigil", "STIFF"),
    ("stick", "sitck", "steck", "stikc", "stisk", "STONE"),
    ("bible", "bilbe", "beble", "bibel", "bibke", "STORY"),
    ("broom", "borom", "braom", "bromo", "broam", "SWEEP"),
    ("salty", "satly", "safty", "salyt", "salky", "SWEET"),
    ("chair", "chiar", "chuir", "chari", "chaim", "TABLE"),
    ("heads", "haeds", "hends", "heasd", "heaks", "TAILS"),
    ("given", "gievn", "gilen", "givne", "givem", "TAKEN"),
    ("fairy", "fiary", "faimy", "faiyr", "faisy", "TALES"),
    ("speak", "spaek", "spesk", "speka", "speaf", "TALK"),
    ("tells", "tlels", "tulls", "telsl", "telle", "TALKS"),
    ("onion", "oinon", "omion", "onino", "oniom", "TEARS"),
    ("fleas", "flaes", "fluas", "flesa", "fleis", "TICKS"),
    ("clock", "colck", "cleck", "clokc", "cloct", "TIME"),
    ("train", "trian", "traln", "trani", "trais", "TRACK"),
    ("magic", "maigc", "magoc", "magci", "maguc", "TRICK"),
    ("stems", "setms", "stefs", "stesm", "stemm", "TWIGS"),
    ("angry", "anrgy", "angdy", "angyr", "angny", "UPSET"),
    ("coats", "caots", "clats", "coast", "coaks", "VESTS"),
    ("sleep", "selep", "slemp", "slepe", "sleip", "WAKES"),
    ("polka", "pokla", "ponka", "polak", "polke", "WALTZ"),
    ("needs", "nedes", "neeks", "neesd", "neeks", "WANTS"),
    ("ocean", "ocena", "oceln", "ocena", "oceam", "WAVES"),
    ("grass", "garss", "gnass", "grasn", "grasm", "WEEDS"),
    ("wagon", "waogn", "wafon", "wagno", "wagos", "WHEEL"),
    ("black", "balck", "bleck", "blakc", "blask", "WHITE"),
    ("corks", "croks", "corms", "corsk", "corls", "WINES"),
    ("girls", "gilrs", "girns", "girsl", "girks", "WOMEN"),
    ("sheep", "sehep", "shoep", "shepe", "sheey", "WOOL"),
    ("globe", "golbe", "glibe", "gloeb", "gloke", "WORLD"),
    ("value", "vaule", "vanue", "valeu", "valce", "WORTH"),
    ("child", "chlid", "chuld", "chidl", "chilk", "YOUNG")
]

standard_nonwords = [
    "merse", "glest", "plust", "drost", "frent", "bandom", "nolk", "chenk", "garrel", "noast", "plare", "frope", "cottle",
    "plick", "lurge", "cleed", "grire", "vener", "jore", "quast", "shir", "codel", "nurch", "crich", "reast", "drave", "merve",
    "poose", "chade", "norke", "roste", "pruch", "trisp", "yinch", "brape", "proth", "leath", "glink", "vind", "gress", "tream",
    "tault", "gripa", "gifle", "plich", "falet", "emple", "trime", "peash", "gouch", "reasy", "telk", "cromp", "heast", "arone",
    "kelsh", "bramp", "fint", "ferch", "cheab", "sholl", "shoon", "hald", "nelect", "mact", "shrum", "rooze", "blass", "benim",
    "heech", "naipt", "untle", "grulp", "calt", "hurky", "bline", "pewor", "hote", "gleek", "hoid", "thark", "wesp", "blipe",
    "bero", "sloat", "teason", "fotion", "appit", "drick", "trusk", "wadge", "frink", "souch", "thrag", "fing", "yownd", "dake",
    "dage", "halst", "crame", "grosp", "sooch", "jaste", "brich", "vaste", "chork", "guilm", "nulk", "cremit", "polt", "treda",
    "blatt", "flish", "parm", "gour", "bosh", "zourk", "kremp", "woney", "qualt"
]


