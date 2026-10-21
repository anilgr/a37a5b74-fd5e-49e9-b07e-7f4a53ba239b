import json

replacements = {
    "SNAKES {ಹಾವುಗಳು}": {
        "members": ["BOA {ಕೆರೆಹಾವು}", "MAMBA {ನಾಗರಹಾವು}", "PYTHON {ಹೆಬ್ಬಾವು}", "VIPER {ಮಂಡಲದ ಹಾವು}"]
    },
    "GRAINS {ಧಾನ್ಯಗಳು}": {
        "members": ["BARLEY {ಜೋಳ}", "OAT {ರಾಗಿ}", "RYE {ನವಣೆ}", "SPELT {ಸಜ್ಜೆ}"]
    },
    "HATS {ಟೋಪಿಗಳು}": {
        "members": ["BERET {ಗಾಂಧಿ ಟೋಪಿ}", "BOWLER {ಮಂಕಿ ಕ್ಯಾಪ್}", "FEDORA {ರೈತನ ಟೋಪಿ}", "FEZ {ಮೈಸೂರು ಪೇಟ}"]
    },
    "COCKTAILS {ಕಾಕ್‌ಟೇಲ್‌ಗಳು}": {
        "group": "LOCAL DRINKS {ಸ್ಥಳೀಯ ಪಾನೀಯಗಳು}",
        "members": ["COSMOPOLITAN {ಕಷಾಯ}", "HURRICANE {ಮಜ್ಜಿಗೆ}", "MANHATTAN {ಪಾನಕ}", "SCREWDRIVER {ಬಾದಾಮಿ ಹಾಲು}"]
    },
    "LONG SANDWICHES {ಉದ್ದನೆಯ ಸ್ಯಾಂಡ್‌ವಿಚ್‌ಗಳು}": {
        "group": "LOCAL SNACKS {ಸ್ಥಳೀಯ ತಿಂಡಿಗಳು}",
        "members": ["HERO {ಮಸಾಲೆ ದೋಸೆ}", "HOAGIE {ರೊಟ್ಟಿ}", "GRINDER {ಚಪಾತಿ}", "SUB {ಪಡ್ಡು}"]
    },
    "B.L.T. INGREDIENTS {ಬಿಎಲ್‌ಟಿ ಸ್ಯಾಂಡ್‌ವಿಚ್ ಪದಾರ್ಥಗಳು}": {
        "group": "UPPITTU INGREDIENTS {ಉಪ್ಪಿಟ್ಟು ಪದಾರ್ಥಗಳು}",
        "members": ["BREAD {ರವೆ}", "BACON {ಒಗ್ಗರಣೆ}", "LETTUCE {ಈರುಳ್ಳಿ}", "TOMATO {ಟೊಮೆಟೊ}"]
    },
    "DATING APPS {ಡೇಟಿಂಗ್ ಆ್ಯಪ್‌ಗಳು}": {
        "group": "MATRIMONIAL SITES {ಮ್ಯಾಟ್ರಿಮೋನಿ ತಾಣಗಳು}",
        "members": ["BUMBLE {ಶಾಧಿ}", "HINGE {ಭಾರತ್ ಮ್ಯಾಟ್ರಿಮೋನಿ}", "MATCH {ಜೀವನಸಾಥಿ}", "TINDER {ಕನ್ನಡ ಮ್ಯಾಟ್ರಿಮೋನಿ}"]
    },
    "DANCES {ಪಾಶ್ಚಿಮಾತ್ಯ ನೃತ್ಯಗಳು}": {
        "group": "FOLK DANCES {ಜಾನಪದ ನೃತ್ಯಗಳು}",
        "members": ["HUSTLE {ಹುಲಿ ಕುಣಿತ}", "SALSA {ಯಕ್ಷಗಾನ}", "SWING {ಡೊಳ್ಳು ಕುಣಿತ}", "TANGO {ಕಂಸಾಳೆ}"]
    },
    "KINDS OF DANCE {ನೃತ್ಯದ ವಿಧಗಳು}": {
        "group": "CLASSICAL DANCES {ಶಾಸ್ತ್ರೀಯ ನೃತ್ಯಗಳು}",
        "members": ["MODERN {ಭರತನಾಟ್ಯ}", "SALSA {ಕುಚಿಪುಡಿ}", "SWING {ಕಥಕ್}", "TAP {ಮೋಹಿನಿಯಾಟ್ಟಂ}"]
    },
    "SODA FOUNTAIN ORDERS {ಜ್ಯೂಸ್ ಸೆಂಟರ್ ಪಾನೀಯಗಳು}": {
        "members": ["FLOAT {ಲಸ್ಸಿ}", "MALT {ಮಿಲ್ಕ್ ಶೇಕ್}", "SHAKE {ಫಲೂಡ}", "SUNDAE {ಮಸ್ತಾನಿ}"]
    },
    "ICE CREAM TREATS {ಐಸ್‌ಕ್ರೀಮ್ ತಿನಿಸುಗಳು}": {
        "members": ["FLOAT {ಲಸ್ಸಿ}", "SHAKE {ಮಿಲ್ಕ್ ಶೇಕ್}", "SPLIT {ಫಲೂಡ}", "SUNDAE {ಮಸ್ತಾನಿ}"]
    },
    "REALITY SHOWS {ರಿಯಾಲಿಟಿ ಶೋಗಳು}": {
        "members": ["ALONE {ಬಿಗ್ ಬಾಸ್}", "CATFISH {ಮಜಾ ಟಾಕೀಸ್}", "CHOPPED {ವೀಕೆಂಡ್ ವಿತ್ ರಮೇಶ್}", "SURVIVOR {ಸರಿಗಮಪ}"]
    },
    "BAKED GOODS {ಬೇಕರಿ ತಿಂಡಿಗಳು}": {
        "members": ["BUN {ಬೆಣ್ಣೆ ಬಿಸ್ಕತ್ತು}", "DANISH {ದಿಲ್ ಪಸಂದ್}", "MUFFIN {ಕಾಂಗೋ ಬಾರ್}", "TURNOVER {ಪಫ್ಸ್}"]
    },
    "OFF-WHITE SHADES {ಬಿಳಿಯ ಛಾಯೆಗಳು}": {
        "members": ["CREAM {ಹಾಲಿನ ಬಣ್ಣ}", "EGGSHELL {ಮೊಟ್ಟೆಯ ಸಿಪ್ಪೆ ಬಣ್ಣ}", "IVORY {ದಂತದ ಬಣ್ಣ}", "VANILLA {ಬೆಣ್ಣೆ ಬಣ್ಣ}"]
    },
    "TYPES OF PAINT {ಬಣ್ಣದ ಪ್ರಕಾರಗಳು}": {
        "members": ["ACRYLIC {ಅಕ್ರಿಲಿಕ್}", "OIL {ತೈಲವರ್ಣ}", "TEMPERA {ರಂಗೋಲಿ}", "WATERCOLOR {ಜಲವರ್ಣ}"]
    },
    "CLASSIC ARCADE GAMES {ಹಳೆಯ ವಿಡಿಯೋ ಗೇಮ್‌ಗಳು}": {
        "group": "TRADITIONAL GAMES {ದೇಸೀ ಆಟಗಳು}",
        "members": ["ASTEROIDS {ಲಗೋರಿ}", "BREAKOUT {ಬುಗರಿ}", "FROGGER {ಗೋಲಿ}", "PONG {ಗಿಲ್ಲಿದಾಂಡು}"]
    },
    "SNEAKER BRANDS {ಶೂ ಬ್ರಾಂಡ್‌ಗಳು}": {
        "members": ["CONVERSE {ಬಾಟಾ}", "JORDAN {ಪ್ಯಾರಾಗಾನ್}", "PUMA {ಲಖಾನಿ}", "VANS {ವಿ.ಕೆ.ಸಿ}"]
    },
    "LUXURIOUS FABRICS {ಐಷಾರಾಮಿ ಬಟ್ಟೆಗಳು}": {
        "group": "TRADITIONAL SAREES {ಸಾಂಪ್ರದಾಯಿಕ ಸೀರೆಗಳು}",
        "members": ["CHIFFON {ಮೈಸೂರ್ ಸಿಲ್ಕ್}", "SATIN {ಇಳಕಲ್}", "SILK {ಕಾಂಚೀವರಂ}", "VELVET {ಬನಾರಸ್}"]
    },
    "KINDS OF SALADS {ಸಲಾಡ್ ವಿಧಗಳು}": {
        "group": "KINDS OF KOSAMBARI {ಕೋಸಂಬರಿ ವಿಧಗಳು}",
        "members": ["CAESAR {ಕಡಲೆಬೇಳೆ}", "GREEK {ಹೆಸರುಬೇಳೆ}", "GREEN {ಸೌತೆಕಾಯಿ}", "WEDGE {ಕ್ಯಾರೆಟ್}"]
    },
    "THINGS SEEN AT A CASINO {ಕ್ಯಾಸಿನೊದಲ್ಲಿ}": {
        "group": "VILLAGE FAIR GAMES {ಜಾತ್ರೆಯ ಆಟಗಳು}",
        "members": ["CARDS {ಇಸ್ಪೀಟ್}", "CHIPS {ಚೌಕಾಬಾರ}", "DICE {ದಾಳ}", "SLOTS {ಗಿರಗಿಟ್ಲೆ}"]
    },
    "SUNDAE TOPPINGS {ಐಸ್‌ಕ್ರೀಮ್ ಮೇಲಿನ ವಸ್ತುಗಳು}": {
        "group": "DRY FRUITS {ಒಣಹಣ್ಣುಗಳು}",
        "members": ["CHERRY {ಗೋಡಂಬಿ}", "FUDGE {ಒಣದ್ರಾಕ್ಷಿ}", "NUTS {ಬಾದಾಮಿ}", "SPRINKLES {ಪಿಸ್ತಾ}"]
    },
    "NEWSPAPER NAMES {ದಿನಪತ್ರಿಕೆಗಳ ಹೆಸರುಗಳು}": {
        "group": "KANNADA NEWSPAPERS {ಕನ್ನಡ ದಿನಪತ್ರಿಕೆಗಳು}",
        "members": ["CHRONICLE {ಪ್ರಜಾವಾಣಿ}", "HERALD {ವಿಜಯವಾಣಿ}", "REGISTER {ಉದಯವಾಣಿ}", "SUN {ಕನ್ನಡಪ್ರಭ}"]
    },
    "ECCLESIASTICAL TITLES {ಚರ್ಚ್‌ನ ಹುದ್ದೆಗಳು}": {
        "group": "TEMPLE ROLES {ದೇವಸ್ಥಾನದ ಹುದ್ದೆಗಳು}",
        "members": ["BISHOP {ಮುಖ್ಯ ಅರ್ಚಕ}", "CARDINAL {ಪುರೋಹಿತ}", "PASTOR {ಪೂಜಾರಿ}", "PRIOR {ಧರ್ಮದರ್ಶಿ}"]
    },
    "CARD GAMES {ಇಸ್ಪೀಟ್ ಆಟಗಳು}": {
        "members": ["BRIDGE {ರಮ್ಮಿ}", "GIN {ಮಂಗನಾಟ}", "SPIT {ಜೋಕರ್}", "WAR {ಬ್ಲಫ್}"]
    },
    "SAUCES IN CHINESE CUISINE {ಚೈನೀಸ್ ಸಾಸ್‌ಗಳು}": {
        "group": "CHUTNEYS {ಚಟ್ನಿಗಳು}",
        "members": ["OYSTER {ಕಾಯಿ ಚಟ್ನಿ}", "PLUM {ಪುದೀನಾ ಚಟ್ನಿ}", "SOY {ಶೇಂಗಾ ಚಟ್ನಿ}", "XO {ಟೊಮೆಟೊ ಚಟ್ನಿ}"]
    },
    "KINDS OF CRACKERS {ಬಿಸ್ಕತ್ತುಗಳ ವಿಧಗಳು}": {
        "members": ["ANIMAL {ಮಾರಿಗೋಲ್ಡ್}", "GOLDFISH {ಪಾರ್ಲೆ-ಜಿ}", "OYSTER {ಗುಡ್-ಡೇ}", "RITZ {ಬೌರ್ಬನ್}"]
    },
    "CHEESES, FAMILIARLY {ಚೀಸ್ ವಿಧಗಳು}": {
        "group": "DAIRY PRODUCTS {ಹಾಲಿನ ಉತ್ಪನ್ನಗಳು}",
        "members": ["AMERICAN {ಮೊಸರು}", "BLUE {ಮಜ್ಜಿಗೆ}", "JACK {ಬೆಣ್ಣೆ}", "SWISS {ತುಪ್ಪ}"]
    },
    "DOG BREEDS, INFORMALLY {ನಾಯಿ ತಳಿಗಳು}": {
        "group": "INDIAN DOG BREEDS {ಭಾರತೀಯ ನಾಯಿ ತಳಿಗಳು}",
        "members": ["BOSTON {ಮುಧೋಳ}", "GOLDEN {ರಾಜಪಾಳ್ಯಂ}", "LAB {ಕನ್ನಿ}", "PIT {ಚಿಪ್ಪಿಪಾರೈ}"]
    },
    "FAMOUS POEMS {ಪ್ರಸಿದ್ಧ ಕವನಗಳು}": {
        "group": "KANNADA POEMS {ಕನ್ನಡದ ಪ್ರಸಿದ್ಧ ಕವನಗಳು}",
        "members": ["DADDY {ಮಂಕುತಿಮ್ಮನ ಕಗ್ಗ}", "HARLEM {ಕುರುಡು ಕಾಂಚಾಣ}", "HOWL {ಬೊಮ್ಮನಹಳ್ಳಿಯ ಕಿಂದರಿಜೋಗಿ}", "IF {ಪುಷ್ಪಗಿರಿ}"]
    },
    "ITALIAN DISHES {ಇಟಾಲಿಯನ್ ತಿನಿಸುಗಳು}": {
        "group": "KARNATAKA DISHES {ಕರ್ನಾಟಕದ ತಿನಿಸುಗಳು}",
        "members": ["BOLOGNESE {ಬಿಸಿಬೇಳೆ ಬಾತ್}", "CARBONARA {ವಾಂಗಿಬಾತ್}", "PESTO {ಪುಳಿಯೋಗರೆ}", "SCAMPI {ಚಿತ್ರಾನ್ನ}"]
    },
    "CANDY BARS": {
        "group": "LOCAL SWEETS {ಸ್ಥಳೀಯ ಸಿಹಿತಿಂಡಿಗಳು}",
        "members": ["BOUNTY {ಕಡಲೆಕಾಯಿ ಮಿಠಾಯಿ}", "CRUNCH {ಎಳ್ಳುಂಡೆ}", "HEATH {ಕೊಬ್ಬರಿ ಮಿಠಾಯಿ}", "MILKY WAY {ಬರ್ಫಿ}"]
    },
    "CANDY STORE TREATS {ಮಿಠಾಯಿ ಅಂಗಡಿಯ ತಿನಿಸುಗಳು}": {
        "group": "LOCAL SWEETS {ಸ್ಥಳೀಯ ಸಿಹಿತಿಂಡಿಗಳು}",
        "members": ["CHOCOLATE {ಕಡಲೆ ಮಿಠಾಯಿ}", "GUM {ಬತ್ತಾಸು}", "LICORICE {ಕೊಬ್ಬರಿ ಮಿಠಾಯಿ}", "LOLLIPOP {ಬಾಂಬೆ ಮಿಠಾಯಿ}"]
    },
    "MOJITO INGREDIENTS {ಮೊಜಿತೊ ಪದಾರ್ಥಗಳು}": {
        "group": "PANAKA INGREDIENTS {ಪಾನಕದ ಪದಾರ್ಥಗಳು}",
        "members": ["LIME {ನಿಂಬೆ}", "MINT {ಬೆಲ್ಲ}", "RUM {ನೀರು}", "SODA {ಏಲಕ್ಕಿ}"]
    },
    "SPORTS VENUES {ಆಟದ ಮೈದಾನಗಳು}": {
        "members": ["COURT {ಕೋರ್ಟ್}", "DIAMOND {ಪಿಚ್}", "FIELD {ಫೀಲ್ಡ್}", "RINK {ಅಖಾಡ}"]
    },
    "SPORTS VENUES {ಕ್ರೀಡಾ ಸ್ಥಳಗಳು}": {
        "members": ["ARENA {ಕ್ರೀಡಾಂಗಣ}", "BOWL {ಮೈದಾನ}", "DOME {ಸ್ಟೇಡಿಯಂ}", "FIELD {ಪಿಚ್}"]
    },
    "TRACK AND FIELD EQUIPMENT {ಅಥ್ಲೆಟಿಕ್ಸ್ ಉಪಕರಣಗಳು}": {
        "group": "TRADITIONAL SPORTS {ದೇಸೀ ಕ್ರೀಡೆಗಳು}",
        "members": ["BATON {ಖೋ-ಖೋ}", "HAMMER {ಕಬಡ್ಡಿ}", "HURDLE {ಕುಸ್ತಿ}", "POLE {ಮಲ್ಲಕಂಬ}"]
    }
}

with open('kannada_connections.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for day in data:
    for group in day['answers']:
        gname = group['group']
        if gname in replacements:
            rep = replacements[gname]
            if "group" in rep:
                group['group'] = rep["group"]
            group['members'] = rep["members"]

with open('kannada_connections.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Done adapting.")
